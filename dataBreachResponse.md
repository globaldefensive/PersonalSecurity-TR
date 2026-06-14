# 🔓 Veri Sızıntısı Rehberi — Bilgilerim Sızdı, Ne Yapacağım?

> Her yıl milyarlarca hesap bilgisi sızıyor. Sızıntı olduktan sonra ne kadar hızlı hareket ettiğin hasarı belirler.

---

## İçindekiler

1. [Önce: Sızıntı Var mı Kontrol Et](#1-önce-sızıntı-var-mı-kontrol-et)
2. [Haveibeenpwned Çıktısını Anlama](#2-haveibeenpwned-çıktısını-anlama)
3. [Sızıntı Türüne Göre Öncelik Sırası](#3-sızıntı-türüne-göre-öncelik-sırası)
4. [Hesap Bazında Eylem Planı](#4-hesap-bazında-eylem-planı)
5. [Kimlik Hırsızlığı — Nasıl Anlarım, Ne Yaparım?](#5-kimlik-hırsızlığı--nasıl-anlarım-ne-yaparım)
6. [Credential Stuffing Saldırısı Aldın mı?](#6-credential-stuffing-saldırısı-aldın-mı)
7. [Sızıntıdan Sonra Kalıcı Koruma](#7-sızıntıdan-sonra-kalıcı-koruma)

---

## 1. Önce: Sızıntı Var mı Kontrol Et

### Ana Kontrol: HaveIBeenPwned

[haveibeenpwned.com](https://haveibeenpwned.com) — Troy Hunt tarafından yönetilen, güvenilir ve ücretsiz.

**Nasıl kullanılır:**
1. E-posta adresini gir
2. Sonuçları incele
3. Her kullandığın e-posta adresi için ayrı ayrı kontrol et

**Telefon numarası için:**
[haveibeenpwned.com](https://haveibeenpwned.com) artık telefon numaralarını da kontrol ediyor — +90 ile Türkiye formatında gir.

### Şifre Kontrolü

[haveibeenpwned.com/passwords](https://haveibeenpwned.com/passwords) — kullandığın şifrenin daha önce sızdırılıp sızdırılmadığını kontrol eder.

**Nasıl çalışır:** Şifreni doğrudan göndermez — SHA-1 hash'inin ilk 5 karakterini gönderir, geri kalanını lokal olarak karşılaştırır. Güvenli.

**Eğer şifren listede çıkıyorsa:** O şifreyi kullanan her hesabı hemen değiştir.

---

## 2. Haveibeenpwned Çıktısını Anlama

Sızıntı tespit edildiğinde şöyle bir ekran görürsün:

```
Oh no — pwned!
Pwned in 3 data breaches and found no pastes.

LinkedIn — 2021
  Compromised data: Email addresses, Passwords

Dropbox — 2012
  Compromised data: Email addresses, Passwords

Adobe — 2013
  Compromised data: Email addresses, Encrypted passwords, Password hints
```

### Ne Anlama Geliyor?

**"Email addresses, Passwords"** — En kritik. E-posta ve şifren açık metin veya kırılabilir hash olarak sızdı.

**"Encrypted passwords"** — Şifren hash'lenmiş ama kırılmış olabilir, özellikle zayıf şifrelerde.

**"Password hints"** — Şifre ipuçları sızdı. Şifreyi tahmin etmek kolaylaşmıştır.

**"Phone numbers"** — Telefon numaranla SIM swap veya phishing saldırısı yapılabilir.

**"Physical addresses"** — Ev adresi sızdı. Sosyal mühendislik veya fiziksel tehdit potansiyeli.

**"Credit card data"** — Kredi kartı bilgisi sızdı. Bankayı ara, kartı iptal ettir.

### Sızıntı Yaşına Dikkat Et

2012 yılından bir sızıntı güncel şifreni içermiyor olabilir — ama o şifreyi hâlâ başka bir yerde kullanıyorsan sorun devam ediyor.

---

## 3. Sızıntı Türüne Göre Öncelik Sırası

Hepsine aynı anda bakmak yerine kritikten başla:

### 🔴 Acil (Bugün Halledilmeli)

- **Banka ve finans hesapları sızıntısı** → Bankayı ara, şüpheli işlem sor, şifreyi değiştir
- **Ana e-posta sızıntısı** → Şifreyi değiştir, 2FA ekle, aktif oturumları sonlandır
- **Kredi kartı verisi** → Kartı iptal ettir, banka müşteri hizmetlerini ara

### 🟠 Önemli (Bu Hafta İçinde)

- Sosyal medya hesaplarının şifresi
- İş e-postası veya kurumsal hesaplar
- Şifre yöneticisi hesabı

### 🟡 Takipte Tut

- Forum, oyun, e-ticaret hesapları
- Artık kullanmadığın eski servisler

---

## 4. Hesap Bazında Eylem Planı

### E-posta Hesabı Sızdıysa

```
1. Şifreyi değiştir (güçlü, benzersiz)
2. Authenticator 2FA ekle (SMS değil)
3. Aktif oturumları sonlandır (tüm cihazlardan çıkış)
4. Kurtarma bilgilerini kontrol et (kurtarma e-postası, telefon)
5. Bu e-postayla giriş yapılan diğer hesapların şifrelerini de değiştir
```

### Banka / Finans Sızdıysa

```
1. Bankayı ara — "son işlemleri kontrol etmek istiyorum"
2. Şüpheli işlem varsa → kartı dondur / iptal ettir
3. Online bankacılık şifresini değiştir
4. E-bankacılık 2FA'sını kontrol et
5. Kredi raporu çek (Türkiye: KKB — findeks.com)
```

### Sosyal Medya Sızdıysa

```
1. Şifreyi değiştir
2. 2FA ekle
3. Aktif oturumları sonlandır
4. Bağlı üçüncü taraf uygulamaları kontrol et
5. Son paylaşımları/mesajları kontrol et (hesap kullanılmış olabilir)
```

### Şifre Yöneticisi Sızdıysa

Bu en kritik senaryo — tüm şifrelerin potansiyel risk altında.

```
1. Master şifreyi hemen değiştir
2. Tüm cihazlardan çıkış yap
3. 2FA'yı doğrula (zaten aktif olmalıydı)
4. Kritik hesapların şifrelerini yöneticiden bağımsız olarak değiştir
5. Yönetici sağlayıcısının güvenlik bildirimlerini takip et
```

---

## 5. Kimlik Hırsızlığı — Nasıl Anlarım, Ne Yaparım?

### Belirtiler

Kimlik bilgilerin kullanılıyorsa şunlar olabilir:

- Yapmadığın kredi başvurusu onaylandı/reddedildi
- Almadığın paket/sipariş için SMS geldi
- Tanımadığın borç tahsilat araması
- Adına açılmış bilinmeyen banka hesabı
- Vergi dairesi veya SGK'dan beklenmedik bildirim
- E-Devlet'te görünmeyen, sana ait olmayan işlemler

### Türkiye'de Kimlik Hırsızlığı Kontrol Adımları

**E-Devlet üzerinden:**
- e-Devlet → SGK Hizmet Dökümü → adına kayıtlı işyeri var mı?
- e-Devlet → Adres Bilgilerim → adresin değiştirilmiş mi?
- e-Devlet → Nüfus Hizmetleri → kimlik belgesi çıkarılmış mı?

**Findeks (KKB) üzerinden:**
- [findeks.com](https://findeks.com) → kredi notu raporu
- Adına kredi başvurusu yapılmış mı?
- Kayıtlı kredi kartı sayısı beklediğinden fazla mı?

### Kimlik Hırsızlığı Tespit Edilirse

```
1. Nüfus Müdürlüğü → kimlik belgesi değişikliği şüphesini bildir
2. Savcılık → e-Devlet üzerinden suç bildirimi (TCK 136, 142)
3. İlgili banka → sahte başvuruyu iptal ettir
4. Findeks → itiraz süreci başlat
5. Tüm şifreleri ve e-postaları değiştir
```

---

## 6. Credential Stuffing Saldırısı Aldın mı?

**Credential stuffing nedir?** Sızdırılmış şifre listelerinin otomatik araçlarla binlerce siteye denenmesidir.

**Belirtiler:**
- Tanımadığın yerden "Giriş denemesi engellendi" maili
- Hesabında tanımadığın cihaz görünüyor
- Şifreni değiştirmemişken hesabın kilitlendi

**Bu saldırı neden bu kadar etkili?**
Çünkü insanların %60'tan fazlası birden fazla sitede aynı şifreyi kullanıyor. Bir siteden sızan şifre, diğer sitelerde de deneniyor.

**Korunma:**
- Her site için farklı şifre → şifre yöneticisi zorunlu
- 2FA açık olan hesaplara şifre bilinsede girilemez
- Haveibeenpwned "Notify me" özelliğini aktif et — e-posta adresi yeni sızıntıda görünürse bildirim gelir

---

## 7. Sızıntıdan Sonra Kalıcı Koruma

### E-posta Alias Sistemi Kur

Her site için farklı e-posta adresi kullan — böylece hangi siteden sızdığını anlarsın ve sadece o aliası kapatırsın.

Örnek:
- Amazon → `amazon.xyz123@simplelogin.com`
- Forum → `forum.abc456@simplelogin.com`
- Gerçek e-postan hiçbir zaman ifşa olmaz

Servisler: SimpleLogin (açık kaynak), AnonAddy (ücretsiz)

### Sızıntı Bildirimi İçin Kayıt Ol

- **HaveIBeenPwned "Notify Me"** — e-posta adresin yeni sızıntıda görününce bildirim
- **Firefox Monitor** — Firefox hesabıyla aynı hizmeti sunar
- **Google One Dark Web Report** — Google hesabı varsa mevcut

### Şifre Hijyeni

Tek bir sızıntının zincirleme hasara yol açmaması için:

```
✅ Her site için farklı şifre (şifre yöneticisi)
✅ Her kritik hesapta 2FA (authenticator)
✅ Şifre yöneticisinin master şifresi çok güçlü ve benzersiz
✅ 3-6 ayda bir kritik hesapların şifrelerini rotasyona al
✅ Artık kullanmadığın hesapları sil (kapatma değil, silme)
```

### Veri Minimizasyonu

Sızıntı olan verinin zararı vermesi için önce o verinin olması lazım.

- Zorunlu olmadıkça gerçek ad, adres, doğum tarihi verme
- Telefon numarasını sadece gerçekten gerekli servislere ver
- Ödeme bilgisi saklama (tek kullanımlık sanal kart: Papara, Tosla vb.)

---

## Hızlı Referans Tablosu

| Durum | İlk Adım | Kaynak |
|-------|----------|--------|
| Şifre sızdı | Haveibeenpwned kontrol + şifre değiştir | haveibeenpwned.com |
| Kredi kartı sızdı | Bankayı ara, kartı dondur | Bankanın müşteri hizmetleri |
| Kimlik hırsızlığı şüphesi | e-Devlet + Findeks kontrol | findeks.com |
| Hesap ele geçirildi | mailProtect.md → Bölüm 5 veya 155_911.md → Bölüm 2 | Bu repo |
| Siber şikayet | Emniyet Siber Suçlar | siber.pol.tr |

---

> ⚠️ Bu rehber bilgilendirme amaçlıdır. Hukuki veya finansal danışmanlığın yerini tutmaz.
> 📄 MIT License © 2025 globaldefensive
