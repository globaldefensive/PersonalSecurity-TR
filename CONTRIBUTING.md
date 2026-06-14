# 🤝 Katkı Rehberi

PersonalSecurity-TR projesine katkıda bulunmak istediğin için teşekkürler!
Bu belge süreci adım adım açıklar.

---

## 🚀 Nasıl Katkıda Bulunurum?

### 1. Fork ve Clone

```bash
# Repoyu fork et (GitHub arayüzünden)
git clone https://github.com/KULLANICI_ADIN/PersonalSecurity-TR.git
cd PersonalSecurity-TR
git remote add upstream https://github.com/globaldefensive/PersonalSecurity-TR.git
```

### 2. Yeni Dal Aç

```bash
git checkout -b feat/yeni-ozellik
# veya
git checkout -b fix/hata-duzeltme
```

### 3. Değişikliklerini Yap

Aşağıdaki standartlara uy (bkz. sonraki bölümler).

### 4. Commit ve Push

```bash
git add .
git commit -m "feat: VPN kurulum rehberi eklendi"
git push origin feat/yeni-ozellik
```

### 5. Pull Request Aç

GitHub'da **Compare & pull request** butonuna tıkla.
PR açıklamasına ne değiştirdiğini ve neden değiştirdiğini yaz.

---

## 📝 Yazım Standartları

### Markdown Dosyaları

- Başlıklar Türkçe olmalı
- Her bölüm emoji ile başlayabilir (okunabilirlik için)
- Teknik terimler ilk kullanımda açıklanmalı
- Kaynak varsa dipnot veya bağlantı ekle
- Satır uzunluğu: 120 karakter altında tut
- Yeni bir dosya eklersen, README.md'deki **İçindekiler** tablosuna ve **Kısa Özet Açıklamaları** bölümüne de ekle
- Başka bir dosyaya atıfta bulunuyorsan göreli link kullan (örn. `[mailProtect.md](mailProtect.md)`)

### Python Dosyaları

- Python 3.10+ uyumlu olmalı
- `secrets` modülü ile kriptografik rastgelelik kullan (`random` değil)
- Her fonksiyon için docstring yaz
- `argparse` ile CLI desteği ekle
- Standart kütüphane dışı bağımlılıkları README'ye yaz

### Commit Mesajı Formatı

```
<tip>: <kısa açıklama>

[opsiyonel gövde]
```

**Tipler:**
| Tip | Anlam |
|-----|-------|
| `feat` | Yeni özellik |
| `fix` | Hata düzeltme |
| `docs` | Sadece belge değişikliği |
| `refactor` | Davranış değiştirmeyen kod yeniden yapılandırma |
| `chore` | Yapılandırma, bağımlılık güncellemesi |

---

## ⚖️ Davranış Kuralları

- Saygılı ve yapıcı ol
- Teknik olmayan eleştirilerden kaçın
- Katkın kabul edilmese de anlayışlı ol — her PR uyumlu olmayabilir

---

## ❓ Soru?

[Issue aç](../../issues) veya mevcut tartışmalara katıl.
