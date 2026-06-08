# 📧 E-Posta Güvenliği ve Mail Çalma Koruması — Kapsamlı Rehber

E-posta adresiniz dijital kimliğinizin kalbidir. Burası ele geçirilirse, buna bağlı tüm banka, sosyal medya, oyun ve iş hesaplarınız domino taşı gibi devrilir.

Bu rehber; basit 2FA kurulumundan, gelişmiş "Ortadaki Saldırgan (AitM)" saldırılarını boşa çıkarmaya kadar katmanlı bir savunma mimarisi sunar.

---

## İçindekiler

1. [Authenticator ile 2FA Kurulumu](#1-authenticator-ile-2fa-kurulumu)
2. [Oturum Çerezleri ve "Beni Hatırla" Tuzağı](#2-oturum-çerezleri-ve-beni-hatırla-tuzağı)
3. [Kurtarma Zinciri ve Döngü Kırma](#3-kurtarma-zinciri-ve-döngü-kırma)
4. [Yedek Kodların Güvenli Saklanması](#4-yedek-kodların-güvenli-saklanması)
5. [Giriş Yapılan Cihazların Denetimi](#5-giriş-yapılan-cihazların-denetimi)
6. [Passkey ve FIDO2 Donanım Anahtarı](#6-passkey-ve-fido2-donanım-anahtarı)
7. [E-posta Takip Piksellerinden Korunma](#7-e-posta-takip-piksellerinden-korunma)
8. [E-posta Alias Servisleri](#8-e-posta-alias-servisleri)
9. [Şifre Yöneticisi Kullanımı](#9-şifre-yöneticisi-kullanımı)
10. [Hızlı Güvenlik Checklist](#10-hızlı-güvenlik-checklist)

---

## 1. Authenticator ile 2FA Kurulumu

İlk ve en kritik adım bir **Authenticator (Doğrulayıcı)** uygulaması yüklemektir. Bu uygulama her 30 saniyede bir değişen, tahmin edilemez 6 haneli kodlar üretir. Saldırganlar şifrenizi ele geçirse bile, telefonunuz fiziksel olarak ellerinde olmadığı sürece hesabınıza giremezler.

**Önerilen uygulamalar (öncelik sırasıyla):**

| Uygulama | Platform | Neden Tercih Edilmeli |
|---|---|---|
| **Aegis Authenticator** | Android | Açık kaynak, yerel şifreli yedek, en güvenli seçenek |
| **Ente Auth** | Android / iOS / Masaüstü | Uçtan uca şifreli bulut yedek, cross-platform |
| **Google Authenticator** | Android / iOS | Yaygın, güvenilir; ancak bulut yedeği Google hesabınıza bağlı |
| **Microsoft Authenticator** | Android / iOS | Microsoft hesapları için ek özellikler |

**Kurulum adımları (Google örneği):**
1. Google Hesabı → Güvenlik → 2 Adımlı Doğrulama
2. "Doğrulayıcı uygulama"yı seçin
3. Ekrandaki QR kodu, uygulamanızla okutun
4. Üretilen 6 haneli kodu girerek eşleştirmeyi doğrulayın
5. Yedek kodlarınızı hemen indirip fiziksel olarak saklayın (Bölüm 4'e bakın)

> ⚠️ **SMS doğrulamasını mutlaka kapatın.** SIM Swapping saldırısında saldırgan operatörü arayarak numaranızı kendi SIM'ine taşıtır ve SMS kodlarını ele geçirir. Authenticator uygulaması bu saldırıyı tamamen etkisiz kılar.

---

## 2. Oturum Çerezleri ve "Beni Hatırla" Tuzağı

Modern saldırganlar artık şifrenizi çalmakla uğraşmaz. Sizi tıklattıkları kötü amaçlı bir link, tarayıcınızdaki **oturum çerezlerini (session cookies)** çalar. Bu çerezler ele geçirilince, saldırgan şifrenizi veya 2FA kodunuzu bilmeden, sanki zaten giriş yapmışsınız gibi hesabınıza girer.

**Korunma yöntemleri:**

- **"Beni Hatırla" seçeneğini işaretlemeyin.** Kritik hesaplarda (banka, ana e-posta) bu seçenek çerezi kalıcı hale getirir, çalındığında saldırgana süresiz erişim verir.
- **Şüpheli link tıklandıktan sonra:** Tarayıcı ayarları → "Tüm çerezleri ve site verilerini temizle" → Bu işlem saldırganın elindeki çerezi anlık olarak geçersiz kılar.
- **Her oturum sonunda çıkış yapın:** Ortak veya başkasına ait cihazlarda mutlaka "Çıkış Yap" butonuna basın.
- **Tarayıcı güvenlik uzantısı kullanın:** uBlock Origin, kötü amaçlı linklerin büyük bölümünü engeller (ayrıntı için DEVICE_HARDENING.md'ye bakın).

---

## 3. Kurtarma Zinciri ve Döngü Kırma

En sık yapılan hata: A mailinin kurtarma adresi B maili, B mailinin kurtarma adresi A maili olarak ayarlanmaktadır. Bu döngüde bir hesap ele geçirilirse diğeri de zincirleme olarak düşer.

**Doğru yapı:**

```
Ana E-posta
  └── Kurtarma: Fiziksel Yedek Kodlar (kağıt)
  └── 2FA: Authenticator uygulaması
  └── Kurtarma e-postası: YOK veya ikincil hesap (hiç bağlantısı olmayan)
```

**Uygulaması:**
1. Ana mail hesabınızın güvenlik ayarlarına girin.
2. Kurtarma e-postası alanını boşaltın veya ana hesabınızla hiçbir ilgisi olmayan başka bir adrese atayın.
3. Kurtarma telefonu olarak SMS yerine Authenticator tercih edin.
4. Yedek kodları mutlaka fiziksel olarak saklayın (Bölüm 4).

---

## 4. Yedek Kodların Güvenli Saklanması

Yedek kodlar, telefonunuz kaybolduğunda veya Authenticator'a erişemediğinizde hesabı kurtaran son kaledir.

**Nerede saklanmamalı:**
- ❌ Telefon fotoğraf galerisinde
- ❌ Bilgisayar masaüstü veya İndirilenler klasöründe
- ❌ Buluta senkronize olan herhangi bir klasörde (Google Drive, iCloud, OneDrive)
- ❌ Ekran görüntüsü olarak herhangi bir cihazda

**Nerede saklanmalı:**
- ✅ Temiz kağıda tükenmez kalemle elle yazılmış, kilitli çekmeced veya cüzdanda
- ✅ Şifreli bir USB belleğe yazdırılıp güvenli yerde saklanmış
- ✅ KeePassXC gibi yerel şifreli kasada (ana şifrenizi unutmamanız koşuluyla)

**Kriz sonrası zorunlu sıfırlama:**
Bir yedek kodu kullanarak hesaba giriş yaptığınızda, işiniz biter bitmez:
1. Güvenlik Ayarları → Yedek Kodlar → "Yeni Kodlar Oluştur" butonuna basın.
2. Yeni kodları yazıp eski kağıdı imha edin.
3. Eski kodlar artık geçersizdir; saldırganın elinde olsalar bile işe yaramazlar.

---

## 5. Giriş Yapılan Cihazların Denetimi

Mail ayarlarında "Güvenlik" veya "Aktif Oturumlar" sekmesinde hangi cihazların hesabınıza bağlı olduğu görülür.

**Denetim yöntemi (haftada bir):**
1. Güvenlik → Cihazlarınız / Aktif Oturumlar bölümünü açın.
2. Tanımadığınız bir şehir, ülke, tarayıcı veya işletim sistemi görürseniz:
   - "Tüm cihazlardan çıkış yap" butonuna basın.
   - Şifrenizi hemen değiştirin.
   - Authenticator kodunuzu doğrulayın, yedek kodlarınızı sıfırlayın.

> 💡 Gmail için: myaccount.google.com → Güvenlik → "Cihazlarınız"
> 💡 Outlook için: account.microsoft.com → Güvenlik → "Son etkinlik"

---

## 6. Passkey ve FIDO2 Donanım Anahtarı

Passkey ve FIDO2 güvenlik anahtarları, kimlik avı (phishing) saldırılarına karşı **neredeyse mutlak** koruma sağlar. Authenticator'ın ötesinde en güçlü 2FA yöntemidir.

**Nasıl çalışır?**
- Şifre yerine kriptografik anahtar çifti (cihazda özel anahtar, sunucuda açık anahtar) kullanılır.
- Sahte bir siteye girsanız bile özel anahtarınız yalnızca gerçek alan adı ile eşleştiğinden kimlik avı mümkün değildir.

**Passkey kurulumu (Google):**
1. myaccount.google.com → Güvenlik → Passkey'ler
2. "Passkey oluştur" → Parmak izi veya PIN ile doğrulayın.
3. Bir sonraki girişte şifre yerine parmak iziniz yeterli.

**FIDO2 Donanım Anahtarı (YubiKey, Google Titan Key):**
- USB veya NFC üzerinden çalışan fiziksel anahtardır.
- Hesabınıza kayıt edin; giriş sırasında anahtarı takıp dokunmanız yeterli.
- En yüksek güvenlik seviyesini gerektiren hesaplarda (ana e-posta, banka) önerilir.
- Fiyat aralığı: 30–80 USD. YubiKey 5 NFC veya Google Titan Key başlangıç için yeterlidir.

---

## 7. E-posta Takip Piksellerinden Korunma

Bir e-postayı açtığınızda, gönderen taraf küçük, görünmez bir piksel resim yükletir. Bu piksel aracılığıyla:
- E-postayı açıp açmadığınızı,
- IP adresinizi (yaklaşık konumunuzu),
- Kullandığınız cihaz ve e-posta uygulamasını

öğrenebilirler. Özellikle phishing saldırılarında hedef tespiti için kullanılır.

**Korunma yöntemleri:**

| Yöntem | Nasıl Yapılır |
|---|---|
| Gmail'de uzak içerikleri engelle | Ayarlar → Genel → "Uzak resimleri her zaman göster" seçeneğini kapatın |
| Outlook'ta engelle | Ayarlar → Posta → Resimler → "Resimleri otomatik indirme" kapatın |
| Apple Mail | Mail Gizliliği Koruması → "Mail Etkinliğimi Gizle" açın (iOS 15+) |
| Tarayıcı tabanlı mail | uBlock Origin ile script engelleyebilirsiniz |

---

## 8. E-posta Alias Servisleri

Gerçek e-posta adresinizi hiçbir zaman doğrudan paylaşmayın. Bunun yerine **alias (takma ad)** servislerini kullanın. Alias, gerçek adresinize yönlendiren tek kullanımlık veya kalıcı takma e-posta adresleridir.

**Avantajları:**
- Bir servisten veri sızıntısı olursa yalnızca o aliası kapatırsınız, gerçek adresiniz güvende kalır.
- Hangi firmadan spam geldiğini tespit edebilirsiniz.
- Gerçek kimliğinizi gizleyebilirsiniz.

**Önerilen servisler:**

| Servis | Ücretsiz Plan | Özellik |
|---|---|---|
| **SimpleLogin** | 15 alias | Açık kaynak, self-host edilebilir |
| **AnonAddy** | Sınırsız alias | Açık kaynak, .anonaddy.com uzantısı |
| **Apple Hide My Email** | iCloud+ abonelerine ücretsiz | iOS/macOS entegrasyonu |
| **Firefox Relay** | 5 alias | Firefox hesabıyla kolayca kurulum |

**Kullanım önerileri:**
- E-ticaret siteleri, forumlar, yarışmalar → Her biri için ayrı alias oluşturun.
- İş ve banka hesapları → Gerçek adresinizi kullanın; bu hesaplarda zaten kimlik doğrulama zorunludur.

---

## 9. Şifre Yöneticisi Kullanımı

Her hesap için farklı, karmaşık şifre kullanmak şarttır; ancak bunları akılda tutmak imkansızdır. Şifre yöneticileri bu sorunu çözer.

**Önerilen şifre yöneticileri:**

| Uygulama | Tür | Platform | Ücret |
|---|---|---|---|
| **Bitwarden** | Açık kaynak, bulut | Her platform | Ücretsiz (Premium $10/yıl) |
| **KeePassXC** | Açık kaynak, yerel | Windows/Linux/macOS | Tamamen ücretsiz |
| **Strongbox** | KeePass uyumlu | iOS/macOS | Ücretli (tek seferlik) |
| **KeePassDX** | KeePass uyumlu | Android | Ücretsiz |

**Başlangıç önerisi:** KeePassXC + veritabanı dosyasını şifreli USB bellekte saklayın. İnternet bağlantısı gerektirmez.

**Ana şifre kuralları:**
- En az 20 karakter, kelime öbeği formatında olabilir: `Mavi-Araba-1987-Pencere!`
- Hiçbir yere yazmayın; sadece ezberleyin.
- Bu şifreyi başka hiçbir yerde kullanmayın.

> 💡 Güçlü rastgele şifre üretmek için bu repodaki `passwordGenerator.py` scriptini kullanın.

---

## 10. Hızlı Güvenlik Checklist

Uzun uzun okumak istemeyenler için e-posta güvenliğinin özeti:

| # | Yapılacak | Öncelik |
|---|---|---|
| 1 | Authenticator uygulaması kur, SMS doğrulamasını kapat | 🔴 Kritik |
| 2 | "Beni Hatırla" seçeneğini kritik hesaplarda kullanma | 🔴 Kritik |
| 3 | Kurtarma e-postası döngüsünü kır | 🔴 Kritik |
| 4 | Yedek kodları kağıda yaz, fiziksel olarak sakla | 🔴 Kritik |
| 5 | Haftada bir "Aktif Oturumlar" listesini kontrol et | 🟠 Önemli |
| 6 | E-posta istemcisinde uzak resim yüklemeyi kapat | 🟠 Önemli |
| 7 | Alias servisi kullanmaya başla (SimpleLogin / AnonAddy) | 🟡 Tavsiye |
| 8 | Şifre yöneticisi kur (Bitwarden veya KeePassXC) | 🟡 Tavsiye |
| 9 | Passkey veya FIDO2 donanım anahtarı ekle | 🟢 İleri Seviye |
| 10 | Ana mail için özel alan adı + ProtonMail / Tutanota | 🟢 İleri Seviye |
