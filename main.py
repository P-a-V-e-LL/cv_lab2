import os
import numpy as np
import cv2
from json.encoder import INFINITY

def template_matching(src_path, template_path):
    source = cv2.imread(src_path, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(template_path, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(source, template, cv2.TM_CCOEFF_NORMED)
    print(result.shape)

    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)
    (startX, startY) = maxLoc

    endX = startX + template.shape[1]
    endY = startY + template.shape[0]

    cv2.rectangle(source, (startX, startY), (endX, endY), (0, 255, 0), 3)
    cv2.imwrite(src_path.replace(".jpg", "").replace("data/", "template_matching/")+"_template_match.jpg", source)
    #cv2.imshow("Output", source)
    #cv2.waitKey(0)

def get_bbox(points):
    min_y = INFINITY
    min_x = INFINITY
    max_x = -1
    max_y = -1
    for x, y in points:
        x = int(x)
        y = int(y)
        min_y = min(y,min_y)
        min_x = min(x,min_x)
        max_y = max(y,max_y)
        max_x = max(x,max_x)
    return ((min_x,min_y), (max_x,max_y))


def sift(src_path, template_path):
    img1 = cv2.imread(src_path,0)
    img2 = cv2.imread(template_path,0)

    sift = cv2.SIFT_create()
    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1,des2,k=2)

    good = []
    good_idx = []
    for m,n in matches:
        if m.distance < 0.7*n.distance:
            good.append(m)
            good_idx.append(matches.index((m,n)))
    #print(good_idx)
    if len(good)>10:
        src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
        dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
        matchesMask = mask.ravel().tolist()
        h,w = img1.shape
        pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
        dst = cv2.perspectiveTransform(pts,M)
        img2 = cv2.polylines(img2,[np.int32(dst)],True,255,3, cv2.LINE_AA)
    else:
        print( "Not enough matches are found - {}".format(len(good)))
        matchesMask = None

    matches_bboxes = [kp1[i].pt for i in good_idx]
    for i in range(len(matches_bboxes)):
        matches_bboxes[i] *= matchesMask[i]

    inline_matches = []
    for i in matches_bboxes:
        if i != ():
            inline_matches.append(i)

    bbox = get_bbox(inline_matches)
    # delete all inline matches
    #for i in range(len(matchesMask)):
    #        matchesMask[i] = 0

    draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                   singlePointColor = None,
                   matchesMask = matchesMask, # draw only inliers
                   flags = 2)
    img3 =  cv2.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)
    cv2.rectangle(img3, bbox[0], bbox[1], (0, 255, 0), 3)
    #cv2.imwrite(src_path.replace(".jpg", "").replace("data/", "sift_rect/")+"_sift_lines.jpg", img3)
    #cv2.imwrite(src_path.replace(".jpg", "").replace("data/", "sift_lines/")+"_sift_lines.jpg", img3)
    cv2.imshow("Output", img3)
    cv2.waitKey(0)

if __name__ == '__main__':
    for i in range(1, 11):
        src = "data/src"+str(i)+".jpg"
        temp = "data/temp"+str(i)+".jpg"
        #template_matching(src, temp)
        sift(src, temp)
