# cv_lab2
# Теория
### Template Matching
Сопоставление шаблонов - пошаговое сканирование шаблоном исходного изображения, причем на каждом шаге рассчитывается либо просто измеряется степень соответствия участка изображения существующему шаблону. Когда сканирование заканчивается, на изображении выделяется область, которая соответствует шаблону в большей степени [1].

### SIFT
SIFT является одним из наиболее распространённых алгоритмов для сравнения
изображений. Он инвариантен к поворотам объекта или камеры, изменениям масштаба
изображения или перемещению объекта на сцене.
Принцип работы алгоритма SIFT основан на поиске локальных максимумов в пространстве переменного масштаба [2].

# Описание разработанной системы
Была разработана программа на языке Python, которая реализует поиск двумя способами: template matching и sift.

# Результаты работы программы
#### Пример 1
Исходное изображение  
<img src="data/src1.jpg" width=50% height=50%>   
Шаблон  
<img src="data/temp1.jpg" width=50% height=50%>   
Результаты Template matching  
<img src="template_matching/src1_template_match.jpg" width=50% height=50%>  
Результаты SIFT в виде точек  
<img src="sift_lines/src1_sift_lines.jpg" width=70% height=70%>  
Результаты SIFT в виде прямоугольника  
<img src="sift_rect/src1_sift_lines.jpg" width=70% height=70%>

#### Пример 2
Исходное изображение  
<img src="data/src2.jpg" width=50% height=50%>   
Шаблон  
<img src="data/temp2.jpg" width=50% height=50%>   
Результаты Template matching  
<img src="template_matching/src2_template_match.jpg" width=50% height=50%>  
Результаты SIFT в виде точек  
<img src="sift_lines/src2_sift_lines.jpg" width=70% height=70%>  
Результаты SIFT в виде прямоугольника  
<img src="sift_rect/src2_sift_lines.jpg" width=70% height=70%>

#### Пример 3
Исходное изображение  
<img src="data/src3.jpg" width=50% height=50%>   
Шаблон  
<img src="data/temp3.jpg" width=50% height=50%>   
Результаты Template matching  
<img src="template_matching/src3_template_match.jpg" width=50% height=50%>  
Результаты SIFT в виде точек  
<img src="sift_lines/src3_sift_lines.jpg" width=70% height=70%>  
Результаты SIFT в виде прямоугольника  
<img src="sift_rect/src3_sift_lines.jpg" width=70% height=70%>

#### Пример 4
Исходное изображение  
<img src="data/src4.jpg" width=50% height=50%>   
Шаблон  
<img src="data/temp4.jpg" width=50% height=50%>   
Результаты Template matching  
<img src="template_matching/src4_template_match.jpg" width=50% height=50%>  
Результаты SIFT в виде точек  
<img src="sift_lines/src4_sift_lines.jpg" width=70% height=70%>  
Результаты SIFT в виде прямоугольника  
<img src="sift_rect/src4_sift_lines.jpg" width=70% height=70%>

#### Пример 5
Исходное изображение  
<img src="data/src5.jpg" width=50% height=50%>   
Шаблон  
<img src="data/temp5.jpg" width=50% height=50%>   
Результаты Template matching  
<img src="template_matching/src5_template_match.jpg" width=50% height=50%>  
Результаты SIFT в виде точек  
<img src="sift_lines/src5_sift_lines.jpg" width=70% height=70%>  
Результаты SIFT в виде прямоугольника  
<img src="sift_rect/src5_sift_lines.jpg" width=70% height=70%>

#### Пример 6
Исходное изображение  
<img src="data/src6.jpg" width=50% height=50%>   
Шаблон  
<img src="data/temp6.jpg" width=50% height=50%>   
Результаты Template matching  
Сходства не нашел.  
Результаты SIFT в виде точек  
<img src="sift_lines/src6_sift_lines.jpg" width=70% height=70%>  
Результаты SIFT в виде прямоугольника  
<img src="sift_rect/src6_sift_lines.jpg" width=70% height=70%>

#### Пример 7
Исходное изображение  
<img src="data/src7.jpg" width=50% height=50%>   
Шаблон  
<img src="data/temp7.jpg" width=50% height=50%>   
Результаты Template matching  
<img src="template_matching/src7_template_match.jpg" width=50% height=50%>  
Результаты SIFT в виде точек  
<img src="sift_lines/src7_sift_lines.jpg" width=70% height=70%>  
Результаты SIFT в виде прямоугольника  
<img src="sift_rect/src7_sift_lines.jpg" width=70% height=70%>

#### Пример 8
Исходное изображение  
<img src="data/src8.jpg" width=50% height=50%>   
Шаблон  
<img src="data/temp8.jpg" width=50% height=50%>   
Результаты Template matching  
<img src="template_matching/src8_template_match.jpg" width=50% height=50%>  
Результаты SIFT в виде точек  
<img src="sift_lines/src8_sift_lines.jpg" width=70% height=70%>  
Результаты SIFT в виде прямоугольника  
<img src="sift_rect/src8_sift_lines.jpg" width=70% height=70%>

#### Пример 9
Исходное изображение  
<img src="data/src9.jpg" width=50% height=50%>   
Шаблон  
<img src="data/temp9.jpg" width=50% height=50%>   
Результаты Template matching  
<img src="template_matching/src9_template_match.jpg" width=50% height=50%>  
Результаты SIFT в виде точек  
<img src="sift_lines/src9_sift_lines.jpg" width=70% height=70%>  
Результаты SIFT в виде прямоугольника  
<img src="sift_rect/src9_sift_lines.jpg" width=70% height=70%>

#### Пример 10
Исходное изображение  
<img src="data/src10.jpg" width=50% height=50%>   
Шаблон  
<img src="data/temp10.jpg" width=50% height=50%>   
Результаты Template matching  
<img src="template_matching/src10_template_match.jpg" width=50% height=50%>  
Результаты SIFT в виде точек  
<img src="sift_lines/src10_sift_lines.jpg" width=70% height=70%>  
Результаты SIFT в виде прямоугольника  
<img src="sift_rect/src10_sift_lines.jpg" width=70% height=70%>

# Выводы по работе
В результате работы программы можно сделать вывод, что SIFT лучше работает при изменении ракурса/масштаба/положения искомого объекта. Его недостатком является большие требования к вычислительным ресурсам.

# Использованные источники
[1] https://otus.ru/nest/post/2478/
[2] https://bstudy.net/857771/tehnika/algoritm_sift
