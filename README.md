# STOP Tabelası Tespiti

OpenCV ile renk tabanlı "STOP" trafik işareti tespiti yapan bir Python uygulaması.

## Ne Yapıyor?

Bir klasördeki fotoğrafları tek tek okuyup, HSV renk uzayında kırmızı renk aralığını
maskeler. Tespit edilen en büyük kırmızı bölgeyi STOP tabelası olarak kabul edip
üzerine yeşil bir kutu çizer, kutunun merkezinin piksel konumunu terminale yazdırır
ve işaretlenmiş görseli `output_images` klasörüne kaydeder.

## Gerekli Kütüphaneler

```bash
pip install opencv-python numpy
```

## Nasıl Çalıştırılır?

1. `images` klasörüne test edilecek fotoğrafları (.jpg / .jpeg / .png) koyun.
2. Aşağıdaki komutla çalıştırın:

```bash
python main.py
```

3. Terminalde her fotoğraf için tespit edilen tabelanın merkez piksel konumu
   (`x`, `y`) yazdırılır.
4. İşaretlenmiş görseller `output_images` klasörüne `detected_<dosya_adı>` olarak kaydedilir.



