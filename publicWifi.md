# 📶 Ortak Wi-Fi Güvenliği — Kafede, Havalimanında, Otelde Ne Yapmalısın?

> Ortak Wi-Fi'ye bağlandığın an, ağdaki herkesin senin trafiğini görebileceğini varsayarak hareket et.

---

## İçindekiler

1. [Gerçek Risk Ne Kadar Büyük?](#1-gerçek-risk-ne-kadar-büyük)
2. [Saldırı Türleri](#2-saldırı-türleri)
3. [VPN: Temel Savunma Katmanı](#3-vpn-temel-savunma-katmanı)
4. [VPN Yoksa Minimum Önlemler](#4-vpn-yoksa-minimum-önlemler)
5. [Cihaz Ayarları — Bağlanmadan Önce](#5-cihaz-ayarları--bağlanmadan-önce)
6. [Konum Bazında Riskler](#6-konum-bazında-riskler)
7. [Hızlı Kontrol Listesi](#7-hızlı-kontrol-listesi)

---

## 1. Gerçek Risk Ne Kadar Büyük?

**Abartılmış:** "Ortak Wi-Fi'de her şeyini çalarlar" — bu doğru değil.

**Gerçekçi:** Ortak Wi-Fi'de belirli saldırılar mümkün, ama bunların büyük çoğunluğu temel önlemlerle önlenebilir.

**Risk faktörleri:**
- Ne tür veriler gönderiyorsun? (banka işlemi vs YouTube izlemek çok farklı)
- Ağ ne kadar kalabalık? (havalimanı > mahalle kafesi)
- HTTPS kullanan sitelerde misin?
- VPN var mı?

**Gerçek hayatta en çok görülen:** Saldırganlar ortak ağlarda aktif dinleme yerine çoğunlukla sahte ağ kurma ve phishing kombinasyonu kullanır. Çünkü şifreli HTTPS trafiğini dinlemek artık çok zor.

---

## 2. Saldırı Türleri

### Evil Twin (Sahte Erişim Noktası)

En yaygın ve tehlikeli saldırı.

**Nasıl çalışır:**
1. Saldırgan kafenin adıyla aynı veya benzer bir Wi-Fi ağı oluşturur ("Cafe_WiFi" yerine "Cafe-WiFi")
2. Sinyal gücünü artırır, telefon otomatik bağlanır
3. Saldırgan trafiği görebilir, seni sahte giriş sayfalarına yönlendirebilir

**Nasıl anlaşılır:** Bağlandıktan sonra giriş yaptığın sitelerde sertifika uyarısı çıkıyorsa, hemen bağlantıyı kes.

**Korunma:** Ağa bağlanmadan önce kafenin gerçek Wi-Fi adını çalışandan sor. Otomatik bağlanmayı kapat.

---

### Man-in-the-Middle (Ortadaki Adam)

Saldırgan seni ve sunucu arasına girer, trafiği okur/değiştirir.

**Modern gerçek:** HTTPS kullanan sitelerde bu saldırı artık çok zor. Tarayıcı sertifika uyuşmazlığını hemen fark eder.

**Hâlâ risk:** HTTP kullanan siteler (adres çubuğunda "Güvenli değil" uyarısı olanlar) — bunlara ortak ağda kesinlikle şifre girme.

---

### ARP Spoofing

Ağ içinde cihazları aldatarak trafiği saldırganın üzerinden geçirme.

**Korunma:** VPN kullan — trafik şifreli olduğundan ARP spoofing işe yaramaz.

---

### Rogue DHCP

Sahte ağ ayarları dağıtarak DNS sunucunu değiştirme → seni sahte sitelere yönlendirme.

**Belirti:** Gitmediğin sitelere yönlendiriliyorsun.
**Korunma:** VPN veya manuel DNS (1.1.1.1).

---

### Pasif Dinleme (Packet Sniffing)

Ağdaki şifresiz trafiği kaydetme.

**Risk altındakiler:** HTTP siteler, şifrelenmemiş uygulama trafiği, eski protokoller.
**Risk altında olmayanlar:** HTTPS siteler, VPN trafiği, uçtan uca şifreli uygulamalar (Signal, WhatsApp).

---

## 3. VPN: Temel Savunma Katmanı

VPN kullandığında trafiğin şifreli bir tünel içinden geçer — ağdaki kimse ne gönderdiğini göremez.

### Ortak Wi-Fi'de VPN Ne Yapar?

- Evil twin ağına bağlansanız bile içerik şifreli
- ARP spoofing işe yaramaz
- DNS sorgularınız şifreli
- Gerçek IP adresiniz gizli

### VPN Seçimi (Ortak Ağ İçin)

Ücretsiz VPN kullanma — verin trafiğini başka biri okur.

| Servis | Ücret | Neden |
|--------|-------|-------|
| **ProtonVPN** | Ücretsiz plan var | İsviçre, açık kaynak, güvenilir |
| **Mullvad** | ~5 EUR/ay | Log tutmaz, hesap gerektirmez |
| **Windscribe** | 10 GB/ay ücretsiz | Makul ücretsiz seçenek |

### VPN'i Ne Zaman Açmalısın?

Ortak Wi-Fi'ye bağlanmadan **önce** aç. Bağlandıktan sonra açmak kısa bir pencere bırakır.

**Otomatik VPN (Kill Switch):** İyi VPN uygulamalarında "Kill Switch" özelliği vardır — VPN bağlantısı kesilirse internet tamamen kesilir, şifresiz trafik sızmaz. Bu özelliği aç.

---

## 4. VPN Yoksa Minimum Önlemler

VPN yokken şunları yap:

### Sadece HTTPS Siteleri Kullan

Adres çubuğunda kilit simgesi var mı? Yoksa o sitede şifre girme.

Tarayıcı ayarı: Firefox/Chrome → "Her Zaman HTTPS Kullan" modunu aç.

### Hassas İşlemleri Ertele

Ortak Wi-Fi'de yapma:
- ❌ Online bankacılık
- ❌ Kredi kartı ile alışveriş
- ❌ İş e-postası (kurumsal veriler)
- ❌ Şifre değiştirme
- ❌ Yeni hesap açma

Yapabilirsin (dikkatli olmak şartıyla):
- ✅ Haber okuma
- ✅ YouTube / Netflix (önceden giriş yapmışsan)
- ✅ Uçtan uca şifreli mesajlaşma (WhatsApp, Signal)
- ✅ Harita kullanma

### Mobil Veri Tercih Et

Kritik işlem yapman gerekiyorsa Wi-Fi yerine telefon hattını kullan. Mobil veri operatör şifreli, ortak ağ değil.

---

## 5. Cihaz Ayarları — Bağlanmadan Önce

### Otomatik Wi-Fi Bağlantısını Kapat

**Android:** Ayarlar → Wi-Fi → Kayıtlı Ağlar → her ağ için "Otomatik bağlan" kapat  
**iOS:** Ayarlar → Wi-Fi → Her ağın yanındaki (i) → "Otomatik Katıl" kapat

Neden? Telefon tanıdığı ağ adını görünce otomatik bağlanır — sahte ağ gerçek ağ adıyla açılmışsa fark etmezsin.

### Ağları Unut (Güvensiz Ağlar)

Daha önce bağlandığın halka açık ağları sil:
- **Android:** Ayarlar → Wi-Fi → Kayıtlı Ağlar → halka açık ağları sil
- **iOS:** Ayarlar → Wi-Fi → Ağ adına bas → "Bu Ağı Unut"

### Wi-Fi Paylaşımını Kapat

**macOS:** Sistem Tercihleri → Paylaşım → "İnternet Paylaşımı" kapalı olsun  
**Windows:** Ayarlar → Ağ → Gelişmiş → Ağ bulunabilirliğini kapat

### Dosya Paylaşımını Kapat

Ortak ağda dosyalarını başkalarının görmemesi için:
- **Windows:** Ağa bağlanırken "Genel Ağ" seç (ev ağı değil)
- **macOS:** Sistem Tercihleri → Paylaşım → tüm paylaşımları kapat

---

## 6. Konum Bazında Riskler

Her ortak ağ eşit riskli değil:

### 🔴 Yüksek Risk

**Havalimanı:** Çok kalabalık, hedef değeri yüksek kişiler (iş seyahati, diplomatlar), sahte ağ kurulumu kolay. VPN zorunlu.

**Otel lobisi / odası:** Otel ağları çoğunlukla segmentlere ayrılmamış — diğer odaları görebilirsin, onlar da seni. Bazı oteller trafiği kayıt eder.

**Büyük AVM / etkinlik alanları:** Kalabalık = potansiyel saldırgan sayısı yüksek.

### 🟠 Orta Risk

**Kafe / restoran:** Değişken. Küçük mahalle kafesi genellikle düşük risk; turistik alan kafesi daha yüksek.

**Üniversite kampüsleri:** Teknik bilgisi olan kullanıcılar mevcut.

### 🟡 Düşük Risk (Ama Sıfır Değil)

**Kütüphane, belediye noktaları:** Genellikle daha iyi yönetilen ağlar.

---

## 7. Hızlı Kontrol Listesi

Ortak Wi-Fi'ye bağlanmadan önce:

```
□ VPN uygulaması açık ve bağlı
□ Wi-Fi adını çalışandan teyit ettim
□ Otomatik bağlanma kapalı
□ Kill Switch aktif (VPN ayarlarında)
```

Bağlandıktan sonra:

```
□ Ziyaret ettiğim sitelerde HTTPS kilit simgesi var
□ Sertifika uyarısı çıkmıyor
□ Bankacılık / alışveriş işlemi yapmıyorum
```

Bağlantıyı kestikten sonra:

```
□ Bu ağı "unut" (güvensiz ağları kaydetme)
□ VPN hâlâ açık (diğer ağlara geçişte sorun yaratmaz)
```

---

## Sık Sorulan Sorular

**"Kafenin şifreli Wi-Fi'si güvenli mi?"**  
Hayır. WPA2 şifresi ağı dışarıdan korur, ağ içindeki cihazlar hâlâ birbirini görebilir. Şifre, ağ içi güvenliği garantilemez.

**"HTTPS her şeyi çözer mi?"**  
Büyük ölçüde evet — içerik şifreli. Ama hangi siteye gittiğini (domain adı) gizlemez. VPN bunu da gizler.

**"Telefon hotspot açsam güvenli mi?"**  
Evet, kendi hotspot'una bağlanmak ortak Wi-Fi'den çok daha güvenli. Mobil veri varsa tercih et.

**"VPN yavaşlatır mı?"**  
Biraz — genellikle %10-20 hız kaybı. Güvenlik için kabul edilebilir.

---

> ⚠️ Bu rehber bilgilendirme amaçlıdır.
> 📄 MIT License © 2025 globaldefensive
