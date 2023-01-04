# 724.-Find-Pivot-Index (Pivot indexi bulma)
Pivot index nedir? diyecek olursak bir dizideki elemanın sağındaki ve solundaki elemanlarının toplamı eşitse o elemana pivot index denir.
Bunu bulmak için önce dizideki elemanları toplamamız gerek, bu arada kaç tane elemanı topladığımızı gösteren sıfırdan başlayan bir değer(running_sum) gerekiyor.
dizide index index ilerlerken eğer elemanların toplamı elemanların sayısına eşit ise o index ğivot eleman oluyor. Eğer pivot index yoksa -1 değerini geri döndürmeliyiz
