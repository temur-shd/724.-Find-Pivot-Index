# 724.-Find-Pivot-Index (Pivot indexi bulma)
Pivot index nedir? diyecek olursak bir dizideki elemanın sağındaki ve solundaki elemanlarının toplamı eşitse o elemana pivot index denir.<br>
Bunu bulmak için önce dizideki elemanları toplamamız gerek, bu arada kaç tane elemanı topladığımızı gösteren sıfırdan başlayan bir değer(running_sum) gerekiyor.Bu değerle birlikte o indexe gelene kadarki anlık toplamı görebiliriz.
dizide index index ilerlerken eğer elemanların toplamı elemanların sayısına eşit ise o index ğivot eleman oluyor. Eğer pivot index yoksa -1 değerini geri döndürmeliyiz <br>
Örneğin [1,7,3,6,5,6] dizisi verildiğinde çıktı 3 olmalı. Çünkü 3'ün sağındaki rakamlar toplamı (7+1+3=11) ve solundaki rakamlar toplamı(5+6=11) eşittir. 
