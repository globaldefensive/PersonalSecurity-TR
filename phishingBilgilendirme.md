# 🎣 Sosyal Mühendislik ve Phishing Tanıma Rehberi

Teknik saldırılar çoğunlukla otomatik araçlarla gerçekleşirken, sosyal mühendislik saldırganın **sizi kandırarak** kendi elleriyle kapıyı açtırmasıdır. Güvenlik zincirinin en zayıf halkası her zaman insandır. Bu rehber, bu saldırıları tanıyıp anlık olarak reddetme becerisi kazandırmayı amaçlar.

---

## İçindekiler

1. [Phishing (Oltalama) Saldırıları](#1-phishing-oltalama-saldırıları)
2. [Smishing ve Vishing](#2-smishing-ve-vishing)
3. [Spear Phishing — Hedefli Saldırılar](#3-spear-phishing--hedefli-saldırılar)
4. [Sosyal Medya Dolandırıcılıkları](#4-sosyal-medya-dolandırıcılıkları)
5. [Sahte Teknik Destek (Tech Support Scam)](#5-sahte-teknik-destek-tech-support-scam)
6. [Deepfake ve Yapay Zeka Dolandırıcılıkları](#6-deepfake-ve-yapay-zeka-dolandırıcılıkları)
7. [Kırmızı Bayraklar — Hızlı Tanıma Kılavuzu](#7-kırmızı-bayraklar--hızlı-tanıma-kılavuzu)

---

## 1. Phishing (Oltalama) Saldırıları

Phishing, meşru bir kurumun (banka, Google, kargo şirketi, devlet kurumu) kimliğine bürünerek sizi sahte bir sayfaya yönlendirme ve bilgilerinizi çalma saldırısıdır.

### Tipik Senaryo

1. "Hesabınızda şüpheli işlem tespit edildi, şifrenizi hemen sıfırlayın" içerikli mail gelir.
2. Maildeki link, gerçek sitenin birebir kopyasına benzeyen sahte bir sayfaya yönlendirir.
3. Şifrenizi girdiğinizde saldırgan onu kaydeder, sizi gerçek siteye yönlendirir.
4. Siz "normal giriş yaptım" sanırken şifreniz çalınmıştır.

### Nasıl Tanırsınız?

- **Alan adını kontrol edin:** `google.com` ile `google-security-alert.com` farklı şeylerdir. Köprünün üzerine gelin (tıklamayın), gerçek adresi görün.
- **Aciliyet ve korku:** "24 saat içinde yapmassanız hesabınız kapatılacak" — bu bir baskı taktiğidir.
- **Genel selamlama:** "Sayın kullanıcımız" yerine bankanız adınızı bilir.
- **Dilbilgisi hataları:** Türkçe karakterlerin yanlış kullanımı, garip cümle yapısı.
- **Gönderen adresini kontrol edin:** `noreply@google.com` ile `noreply@g00gle-support.ru` çok farklı.

### Korunma

- Maildeki linkten değil, tarayıcıya **elle yazarak** giriş yapın.
- Bankanız sizi mail ile şifre sıfırlamaya yönlendirmez; böyle bir mail aldığınızda doğrudan müşteri hizmetlerini arayın.
- uBlock Origin ve tarayıcının yerleşik phishing koruması açık olsun.

---

## 2. Smishing ve Vishing

**Smishing (SMS Phishing):** "Kargonuz beklemede, teslim ücreti için tıklayın" gibi SMS mesajları.

**Vishing (Ses Phishing):** Sizi arayan biri "Ben Garanti Bankası güvenlik biriminden arıyorum, kartınızda işlem var, doğrulama yapabilir miyiz?" der.

### Smishing Tanıma

- Kısa linkler (bit.ly, tinyurl.com vb.) içeren SMS'lere şüpheyle yaklaşın.
- Kargo bildirimlerini beklemediğiniz halde gelen "teslimat ücreti" mesajları.
- "Ödülünüzü almak için tıklayın" mesajları.

### Vishing Tanıma

- Gerçek bankanız sizi arayarak **kart numarası, PIN veya SMS kodu** sormaz. Hiçbir zaman.
- "Bu görüşmeyi kaydetmenizi istemiyoruz" derlerse sahte aramadır.
- Arayıcı ısrar ediyorsa, "Sizi geri arayacağım" deyin ve bankanın resmi numarasını arayın (kartonun arkasındaki numara).

### Korunma

- Gelen aramaları doğrulamak için [sorgu.btk.gov.tr](https://sorgu.btk.gov.tr) veya arama sonuçlarını kullanın.
- Kimlik doğrulama amaçlı SMS kodu asla telefonda okunamaz.

---

## 3. Spear Phishing — Hedefli Saldırılar

Spear phishing, sizi tanıyan veya hakkınızda bilgi toplayan biri tarafından özelleştirilen saldırıdır. Adınızı, işyerinizi, arkadaşlarınızı, son alışverişlerinizi kullanır.

### Tipik Senaryo

- LinkedIn'den adınızı, işyerinizi ve yöneticinizi öğrenir.
- Yöneticinizin adından mail atar: "Acil: Şu hesaba ödeme yapılması lazım, ben toplantıdayım."
- E-posta adresi `ali.yilmaz@sirket.com.tr` yerine `ali.yilmaz@sirket-com.tr` gibi ince fark içerir.

### Korunma

- Para veya hassas bilgi içeren talepleri, farklı bir kanaldan (telefon, yüz yüze) doğrulayın.
- Şüpheli mail alındığında BT / güvenlik biriminize bildirin.
- LinkedIn ve sosyal medyada paylaştığınız iş bilgilerini minimize edin.

---

## 4. Sosyal Medya Dolandırıcılıkları

### Sahte Çekiliş ve Ödül

"Apple'dan 1000 iPhone hediye ediyoruz, beğen ve paylaş" tarzı paylaşımlar. Amacı; hesap bilgisi toplamak, zararlı sitelere yönlendirmek veya hesabınızı ele geçirmek.

**Kural:** Gerçek çekilişlerde ödülü almak için asla şifre veya ödeme bilgisi istenmez.

### Sahte "Mavi Tik" Doğrulama

"Hesabınızı doğrulamak için formu doldurun" — sizi sahte bir sayfaya yönlendirir ve hesap bilgilerinizi çalar.

**Kural:** Instagram, Twitter ve benzeri platformlar sizi DM veya mail ile doğrulama formuna yönlendirmez.

### Kripto Dolandırıcılıkları

"1 Bitcoin gönder, 2 Bitcoin geri al" veya "Yatırım platformumuza katıl, %30 günlük kazanç" vaadiyle çalışır.

**Kural:** Kripto para alanında garantili kazanç vaat eden her şey dolandırıcılıktır.

---

## 5. Sahte Teknik Destek (Tech Support Scam)

### Senaryo 1 — Pop-up Uyarısı

Bir web sitesinde "VİRÜS TESPİT EDİLDİ! Microsoft Güvenlik Merkezi'ni arayın: 0850 XXX XX XX" benzeri tam ekran uyarı çıkar. Numarayı ararsanız sizi "uzak masaüstü" bağlantısına ikna ederek cihazınıza sızmaya çalışırlar.

**Kural:** Microsoft, Google veya Apple size asla telefon numarası ile uyarı göndermez. Bu pencereleri kapatın (gerekirse görev yöneticisinden).

### Senaryo 2 — Proaktif Arama

"Microsoft güvenlik birimi" olduklarını söyleyen biri sizi arar, bilgisayarınıza TeamViewer veya AnyDesk kurmanızı ister.

**Kural:** Bu şirketler sizi aramaz. Kapayın.

---

## 6. Deepfake ve Yapay Zeka Dolandırıcılıkları

Yapay zeka ses klonlama ve video deepfake teknolojileri 2024-2025 itibarıyla dolandırıcılık aracı olarak yaygınlaşmaktadır.

### Ses Klonlama Dolandırıcılığı

Birinin ses kaydından (sosyal medya videosu, YouTube) yapay zeka ile ses kopyası oluşturulur. Bu sesle yakını aranır: "Anne, kaza yaptım, acil para lazım."

**Korunma:**
- Acil para talepleri için aile içinde **kod kelime** belirleyin (kimsenin tahmin edemeyeceği, yalnızca aranızdaki kişinin bildiği bir söz).
- Para göndermeden önce farklı bir kanaldan (kısa mesaj, başka numara) doğrulayın.
- Panikle hızlı karar vermeyin; dolandırıcılar her zaman aciliyeti kullanır.

### Video Deepfake

CEO veya tanınan birinin görüntüsü kullanılarak sahte video toplantı düzenlenir, ödeme talimatı verilir.

**Korunma:** Finansal talimatları video görüşmesinden değil, yazılı ve doğrulanmış kanaldan alın. Doğruluğundan emin olmak için farklı bir kanaldan teyit edin.

---

## 7. Kırmızı Bayraklar — Hızlı Tanıma Kılavuzu

Şu işaretlerden herhangi birini gördüğünüzde dur, nefes al, doğrula:

| Kırmızı Bayrak | Ne Anlama Gelir |
|---|---|
| Aşırı aciliyet ("Hemen yapın!") | Düşünmenizi engellemek için baskı |
| Beklenmedik ödül veya kazanç | Gerçek ise zaten gelir, sormaya gerek yok |
| Şifre / SMS kodu / kart bilgisi isteniyor | Hiçbir meşru kurum bunu istemez |
| Farklı kanala geçme isteği ("DM'den yazın") | Kayıt dışı iletişim kurmak istiyor |
| Korkutma ("Hesabınız kapatılacak") | Panikle hareket ettirme taktiği |
| Kötü Türkçe veya garip kelimeler | Otomatik çeviri veya yabancı kaynak |
| Alan adında küçük farklılık | Kimlik sahtekarlığı |
| "Bu konuşmayı kimseye söyleme" | Sosyal mühendisliğin klasik işareti |
| Ödeme için kripto veya hediye kartı talebi | Kesinlikle dolandırıcılık |

**Altın kural:** Gerçek kurumlar sizi asla panikletmez ve farklı ödeme yöntemlerine yönlendirmez. Şüphe duyduğunuzda iletişimi kesin, resmi kanaldan doğrulayın.
