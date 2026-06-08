# 🖥️ Cihaz Sıkılaştırma (Device Hardening) Rehberi

Bu rehber; bilgisayarınızı, telefonunuzu ve tarayıcınızı siber saldırılara karşı sistematik olarak güçlendirmenin yollarını anlatır. E-posta güvenliğinin yanında, saldırı yüzeyini en aza indirmeye odaklanır.

---

## İçindekiler

1. [Tarayıcı Güvenliği](#1-tarayıcı-güvenliği)
2. [VPN ve DNS Şifreleme](#2-vpn-ve-dns-şifreleme)
3. [Cihaz Şifreleme](#3-cihaz-şifreleme)
4. [İşletim Sistemi Sıkılaştırma](#4-işletim-sistemi-sıkılaştırma)
5. [Ağ Güvenliği (Wi-Fi)](#5-ağ-güvenliği-wi-fi)
6. [Mobil Cihaz Güvenliği](#6-mobil-cihaz-güvenliği)
7. [Güvenlik Denetim Çizelgesi](#7-güvenlik-denetim-çizelgesi)

---

## 1. Tarayıcı Güvenliği

Tarayıcı, internetle doğrudan temas ettiğiniz en büyük saldırı yüzeyidir. Doğru ayarlar ve uzantılarla riskin büyük bölümü kapatılabilir.

### Tarayıcı Seçimi

| Tarayıcı | Gizlilik | Güvenlik | Önerilen Kullanım |
|---|---|---|---|
| **Firefox** | Yüksek | Yüksek | Günlük kullanım — en iyi özelleştirme |
| **Brave** | Çok Yüksek | Yüksek | Reklamlara karşı yerleşik koruma isteyenler |
| **Chrome** | Düşük | Yüksek | Google ekosistemi bağımlıları için |
| **Safari** | Orta | Yüksek | macOS / iOS kullanıcıları için |
| **Tor Browser** | Çok Yüksek | Yüksek | Anonimlik gerektiren özel durumlar |

### Zorunlu Tarayıcı Uzantıları

| Uzantı | İşlev | Nerede Bulunur |
|---|---|---|
| **uBlock Origin** | Reklam, tracker ve kötü amaçlı script engelleme | Firefox / Chrome mağazası |
| **Privacy Badger** | Görünmez izleyici tespiti ve engeli | EFF tarafından geliştirildi |
| **HTTPS Everywhere** | HTTP bağlantıları otomatik HTTPS'e yönlendir | Firefox'ta artık yerleşik |
| **Bitwarden** | Şifre yöneticisi tarayıcı entegrasyonu | Her tarayıcı |

### Tarayıcı Ayarları

**Firefox için önerilen ayarlar:**
1. `about:preferences#privacy` → Gelişmiş İzleme Koruması → **Katı** seçin.
2. Çerezler: "Yalnızca üçüncü taraf çerezleri engelle" veya daha kısıtlayıcı.
3. DNS over HTTPS: Ayarlar → Genel → Ağ Ayarları → "DNS over HTTPS'i etkinleştir" → Cloudflare veya NextDNS seçin.
4. `about:config` → `privacy.resistFingerprinting` → `true` (parmak izi koruması).

**Her tarayıcı için genel kurallar:**
- Eklentileri yalnızca resmi mağazadan indirin.
- Kullanmadığınız eklentileri kaldırın (her eklenti bir saldırı yüzeyi).
- Tarayıcıyı güncel tutun; güncellemeler genellikle kritik güvenlik yamaları içerir.
- Tarayıcı otomatik doldurma özelliğini şifre yöneticisi lehine devre dışı bırakın.

---

## 2. VPN ve DNS Şifreleme

### DNS Şifreleme (DoH / DoT)

Her web sitesine girerken bilgisayarınız önce bir DNS sunucusuna "Bu alan adının IP adresi nedir?" diye sorar. Şifresiz DNS sorgularınız internet servis sağlayıcınız (ISS) tarafından görülebilir ve kaydedilebilir.

**DNS over HTTPS (DoH) ile çözüm:**

| Sağlayıcı | Adres | Özellik |
|---|---|---|
| **NextDNS** | nextdns.io | Özelleştirilebilir filtreler, reklam engelleme |
| **Cloudflare 1.1.1.1** | 1.1.1.1 | Hızlı, gizlilik odaklı |
| **Quad9** | 9.9.9.9 | Kötü amaçlı alan engelleme |

**Kurulum (sistem geneli, Windows):**
1. `ncpa.cpl` → Ağ bağdaştırıcısı → Özellikler → TCP/IPv4
2. DNS adresi: `1.1.1.1` ve `1.0.0.1` girin.
3. Daha iyi koruma için NextDNS'i tarayıcı seviyesinde de etkinleştirin.

### VPN

VPN, internet trafiğinizi şifreli bir tünel içinden geçirerek ISS ve ortak Wi-Fi ağlarındaki dinleyicilerden korur.

**VPN ne zaman kullanılmalı:**
- Havalimanı, kafe, otel gibi ortak Wi-Fi ağlarında (kritik)
- ISS'nin trafiğinizi kaydetmemesini istediğinizde
- Coğrafi kısıtlamaları aşmak için

**VPN ne zaman yeterli değil:**
- Hesap güvenliği için VPN tek başına yetersizdir; 2FA olmadan VPN anlamsızdır.
- Ücretsiz VPN'lerin büyük bölümü verilerinizi satar — ücretsiz VPN kullanmayın.

**Önerilen VPN servisleri:**

| Servis | Aylık Ücret | Özellik |
|---|---|---|
| **Mullvad** | ~5 EUR | Hesapsız, log tutmaz, nakit ödeme kabul eder |
| **ProtonVPN** | Ücretsiz plan mevcut | İsviçre merkezli, açık kaynak istemci |
| **IVPN** | ~6 USD | Hesapsız, log tutmaz |

---

## 3. Cihaz Şifreleme

Bilgisayarınız veya telefonunuz çalınırsa, disk şifreleme olmadan verileriniz kolayca okunabilir.

### Windows — BitLocker

1. Başlat → "BitLocker" ara → "BitLocker Sürücü Şifrelemesi'ni Yönet"
2. C: sürücüsü için "BitLocker'ı Aç"
3. Kurtarma anahtarını USB bellekte veya yazdırarak saklayın (buluta kaydetmeyin)
4. "Tüm sürücüyü şifrele" seçeneğini tercih edin.

> ⚠️ Windows Home sürümünde BitLocker yoktur. Alternatif olarak **VeraCrypt** (ücretsiz, açık kaynak) kullanın.

### macOS — FileVault

1. Apple Menüsü → Sistem Tercihleri → Gizlilik ve Güvenlik → FileVault
2. "FileVault'u Aç" → Kurtarma anahtarını güvenli şekilde saklayın.

### Linux — LUKS

Kurulum sırasında "Şifreli kurulum" seçeneğini işaretleyin. Sonradan etkinleştirmek için `cryptsetup` kullanılabilir.

### Android — Cihaz Şifreleme

Modern Android'de (6.0+) şifreleme varsayılan olarak etkindir. Kontrol:
Ayarlar → Güvenlik → Şifreleme ve kimlik bilgileri → Telefonun şifrelenmiş olduğundan emin olun.

### iOS — Otomatik Şifreleme

iOS, güçlü bir parola/PIN belirlendiğinde donanım düzeyinde otomatik şifrelemesi aktif olur. 6 haneli PIN yerine alfanümerik kod tercih edin.

---

## 4. İşletim Sistemi Sıkılaştırma

### Windows

- **Otomatik güncellemeleri açık tutun.** Çoğu saldırı, yaması yayınlanmış ama güncelleme yapılmamış açıklardan yararlanır.
- **Windows Defender'ı devre dışı bırakmayın.** Üçüncü taraf antivirüs yerine Defender + MalwareBytes Free kombinasyonu yeterlidir.
- **UAC'ı (Kullanıcı Hesabı Denetimi) etkin tutun.** "Hiçbir zaman uyarma" seçeneğini seçmeyin.
- **Güvenlik duvarını açık tutun:** Denetim Masası → Windows Defender Güvenlik Duvarı → Açık.
- **Gereksiz servisleri kapatın:** Uzak Masaüstü'nü (RDP) kullanmıyorsanız kapalı tutun.

### macOS

- Sistem Tercihleri → Güvenlik → "Uygulama mağazası ve tanımlı geliştiricilerden" seçin.
- **Gatekeeper'ı devre dışı bırakmayın.**
- Güvenlik Duvarı: Sistem Tercihleri → Güvenlik → Güvenlik Duvarı → Aç.
- **SIP (System Integrity Protection) kapalı bırakmayın.**

### Linux

- Root ile günlük kullanım yapmayın; sudo kullanıcısı olarak çalışın.
- `ufw` (Uncomplicated Firewall) etkinleştirin: `sudo ufw enable`
- Paketleri yalnızca resmi depolardan yükleyin.
- SSH kullanıyorsanız: parola girişini devre dışı bırakıp anahtar tabanlı kimlik doğrulamaya geçin.

---

## 5. Ağ Güvenliği (Wi-Fi)

### Ev Ağı

- **WPA3 şifreleme** kullanın (router ayarlarından). Minimum WPA2-AES.
- WPS'i (Wi-Fi Protected Setup) **kapatın** — kolayca kırılabilir.
- Router admin paneli şifresini değiştirin (varsayılan "admin/admin" bırakmayın).
- Router firmware güncellemelerini takip edin.
- Misafir ağı oluşturun; ev ağınızla misafir cihazlarını ayırın.

### Genel / Ortak Wi-Fi

- Ortak Wi-Fi'de banka ve mail işlemi yapmaktan kaçının.
- Yapacaksanız VPN kullanın.
- "Bu ağa otomatik bağlan" seçeneğini kapatın.
- Telefonunuzun Wi-Fi'ı gerekmediğinde kapalı tutun (MAC adresinizin izlenmesini engeller).

---

## 6. Mobil Cihaz Güvenliği

### Genel Kurallar (Android ve iOS)

- PIN yerine **alfanümerik parola** kullanın.
- Ekran kilidi süresini kısaltın (maksimum 1-2 dakika).
- Uygulamaları yalnızca **resmi mağazalardan** indirin (Google Play / App Store).
- Uygulamalara yalnızca **ihtiyaç duydukları izinleri** verin; bir fener uygulaması mikrofon izni istiyorsa reddedin.
- İşletim sistemi güncellemelerini erteletmeyin.
- Bluetooth'u gerekmediğinde kapalı tutun.

### Android'e Özel

- Google Play Protect'in açık olduğundan emin olun.
- "Bilinmeyen kaynaklardan uygulama yükle" seçeneğini kapalı tutun.
- F-Droid (açık kaynak uygulama mağazası) güvenilir bir alternatiftir.

### iOS'a Özel

- Kilid ekranında Siri'yi devre dışı bırakın (Güvenlik → Siri).
- iCloud yedeklemesi açıksa, iCloud hesabınızı da 2FA ile güvenceye alın.
- "Kısıtlamalar" (Ekran Süresi → İçerik ve Gizlilik Kısıtlamaları) ile kritik ayarlara parola ekleyin.

---

## 7. Güvenlik Denetim Çizelgesi

### Günlük

- [ ] Şüpheli mail veya mesajlara tıklamadan önce göndereni doğrula
- [ ] Yazılımları güncel tut

### Haftalık

- [ ] Mail hesaplarında "Aktif Oturumlar" listesini kontrol et
- [ ] Tarayıcı geçmişini ve çerezleri temizle

### Aylık

- [ ] Şifre yöneticisinde eski veya zayıf şifreleri yenile
- [ ] Router güvenlik ayarlarını gözden geçir
- [ ] Uygulama izinlerini denetle (kullanılmayan uygulamaları kaldır)

### Yıllık

- [ ] Tüm kritik hesaplarda şifre rotasyonu yap
- [ ] Yedek kodlarını fiziksel kopyalarla karşılaştır
- [ ] Cihaz şifrelemenin aktif olduğunu doğrula
- [ ] Veri sızıntısı kontrolü yap: [haveibeenpwned.com](https://haveibeenpwned.com)
