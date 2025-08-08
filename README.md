🐢 Turtle Game
"Turtle Game", Python'un yerleşik turtle modülü kullanılarak geliştirilmiş refleks ve dikkat odaklı eğlenceli bir oyundur. Oyuncu, üçgen şeklindeki karakteri kontrol ederek hareket eden kaplumbağalara çarparak skor kazanmaya çalışır. Ancak dikkat! Süre sınırlı ve canlarınız da sınırlı!

🎮 Oyun Özellikleri
⏱️ 80 saniyelik süre sınırı

❤️ 5 can hakkı

🐢 6 adet rastgele hareket eden hedef kaplumbağa

🎯 Çarpma ile skor kazanma

🎵 Ses efektleri (yeme_sesi.wav, dead_sound.wav)

🎨 Gösterişli grafiksel arayüz (turtle canvas)

⌨️ Klavye kontrolleri ile tam etkileşimli oynanış

📷 Oyun Ekranı
![Oyun Ekranı](Oyun_ekrani.png)

🕹️ Nasıl Oynanır?
Oyunu başlattıktan sonra hedef kaplumbağalara çarparak en yüksek skoru elde etmeye çalışın.

Klavye Kontrolleri
Tuş	İşlev
←	Sola dön
→	Sağa dön
Q	Hızı artır
E	Hızı azalt
SPACE	Dur
ENTER	Oyunu başlat

🧠 Oyun Mantığı
Oyuncu, üçgen şeklindeki karakteri yön tuşlarıyla yönlendirir.

Hedef kaplumbağalar rastgele yönlere doğru sürekli hareket eder.

Oyuncu kaplumbağaya çarptığında:

Skor artar.

Kaplumbağa başka bir konumda tekrar doğar.

Ses efekti çalar.

Oyuncu sınırların dışına çıkarsa:

Can kaybeder.

Başlangıç konumuna döner.

Ses efekti çalar.

Süre bittiğinde veya canlar biterse oyun sona erer.

📁 Proje Dosya Yapısı
bash
Kopyala
Düzenle
TurtleGame/
│
├── turtle_game.py         # Ana oyun dosyası
├── yeme_sesi.wav          # Skor alındığında çalan ses
├── dead_sound.wav         # Kenara çarpıldığında çalan ses
└── README.md              # Bu dosya
Not: Oyun Windows için yazılmıştır ve winsound modülü kullanıldığı için diğer işletim sistemlerinde ses çalışmayabilir.

🔧 Gereksinimler
Python 3.x

turtle modülü (Python ile birlikte gelir)

winsound modülü (yalnızca Windows)

🚀 Başlatmak için
bash
Kopyala
Düzenle
python turtle_game.py
🧑‍💻 Geliştirici Notları
Bu oyun, Python öğrenme sürecinde turtle, random, winsound gibi kütüphaneleri kullanarak eğlenceli bir proje geliştirme fikriyle oluşturulmuştur.

Her türlü katkıya ve geri bildirime açığım! 🙌
