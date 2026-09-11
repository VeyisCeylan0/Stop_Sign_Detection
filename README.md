STOP Tabelası Tespiti (Renk Tabanlı)

Yıldız Rover Destek Ekip - Ödev 2 kapsamında hazırlanmış, OpenCV ile renk tabanlı "STOP" trafik işareti tespiti yapan bir Python uygulaması.

Ne Yapıyor?

Bir klasördeki fotoğrafları tek tek okuyup, HSV renk uzayında kırmızı renk aralığını maskeler. Tespit edilen en büyük kırmızı bölgeyi STOP tabelası olarak kabul edip üzerine yeşil bir kutu çizer, kutunun merkezinin piksel konumunu terminale yazdırır ve işaretlenmiş görseli output_images klasörüne kaydeder.

Gerekli Kütüphaneler
bash
pip install opencv-python numpy
Klasör Yapısı
.
├── main.py
├── images/            # Girdi: STOP tabelası fotoğrafları buraya konur
└── output_images/      # Çıktı: işaretlenmiş fotoğraflar buraya kaydedilir (otomatik oluşur)
Nasıl Çalıştırılır?
images klasörüne test edilecek fotoğrafları (.jpg / .jpeg / .png) koyun.
Aşağıdaki komutla çalıştırın:
bash
python main.py
Terminalde her fotoğraf için tespit edilen tabelanın merkez piksel konumu (x, y) yazdırılır.
İşaretlenmiş görseller output_images klasörüne detected_<dosya_adı> olarak kaydedilir.
Yöntem
Görüntü BGR'den HSV renk uzayına çevrilir.
Kırmızı renk HSV'de iki ayrı aralıkta bulunduğundan (0–10 ve 150–180), iki maske oluşturulup birleştirilir.
Küçük kernel ile MORPH_OPEN uygulanarak gürültü temizlenir.
Büyük kernel ile MORPH_CLOSE uygulanarak, tabela üzerindeki beyaz yazının kırmızı alanı bölmesinden kaynaklanan boşluklar kapatılır.
Maskedeki konturlardan en büyük alana sahip olan STOP tabelası adayı olarak seçilir.
Seçilen alanın sınırlayıcı kutusu çizilir, merkezi hesaplanıp işaretlenir.
Sınırlamalar

Algoritma yalnızca renge dayandığı için düşük ışık koşullarında ve tabela üzerindeki yazının kırmızı alanı bölmesi durumunda kısmi/hatalı tespit yapabilmektedir. Detaylı değerlendirme rapor dosyasında (Odev2_Rapor.pdf) bulunmaktadır.
