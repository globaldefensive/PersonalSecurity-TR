#!/usr/bin/env python3
"""
passwordGenerator.py — Güçlü Parola Üretici
Özellikler:
  • Minimum karakter garantisi (büyük, küçük, rakam, sembol)
  • Shannon entropi skoru + güç etiketi
  • Pano (clipboard) kopyalama
  • Özelleştirilebilir uzunluk ve karakter seti
"""

import secrets
import string
import math
import argparse
import sys

try:
    import pyperclip
    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False


# ── Karakter setleri ────────────────────────────────────────────────
LOWERCASE  = string.ascii_lowercase          # a-z
UPPERCASE  = string.ascii_uppercase          # A-Z
DIGITS     = string.digits                   # 0-9
SYMBOLS    = "!@#$%^&*()-_=+[]{}|;:,.<>?"   # özel karakterler
AMBIGUOUS  = "0O1lI"                         # karıştırıcı karakterler


def build_charset(use_upper=True, use_digits=True, use_symbols=True,
                  exclude_ambiguous=False) -> str:
    """Seçilen seçeneklere göre karakter havuzu oluşturur."""
    pool = LOWERCASE
    if use_upper:
        pool += UPPERCASE
    if use_digits:
        pool += DIGITS
    if use_symbols:
        pool += SYMBOLS
    if exclude_ambiguous:
        pool = "".join(c for c in pool if c not in AMBIGUOUS)
    return pool


def generate_password(length: int = 20,
                      use_upper: bool = True,
                      use_digits: bool = True,
                      use_symbols: bool = True,
                      exclude_ambiguous: bool = False) -> str:
    """
    Kriptografik olarak güvenli rastgele parola üretir.
    Her karakter grubundan en az 1 karakter garanti edilir.
    """
    if length < 8:
        raise ValueError("Parola uzunluğu en az 8 olmalıdır.")

    pool = build_charset(use_upper, use_digits, use_symbols, exclude_ambiguous)

    # Minimum garanti listesi
    mandatory = [secrets.choice(LOWERCASE)]
    if use_upper:
        mandatory.append(secrets.choice(UPPERCASE))
    if use_digits:
        mandatory.append(secrets.choice(DIGITS))
    if use_symbols:
        mandatory.append(secrets.choice(SYMBOLS))

    if len(mandatory) > length:
        raise ValueError("Uzunluk, seçilen karakter grubu sayısından az olamaz.")

    # Geri kalan karakterleri rastgele doldur
    remaining = [secrets.choice(pool) for _ in range(length - len(mandatory))]

    # Listeyi karıştır (pozisyon öngörülemez olsun)
    combined = mandatory + remaining
    secrets.SystemRandom().shuffle(combined)

    return "".join(combined)


# ── Entropi ─────────────────────────────────────────────────────────
def entropy_bits(password: str) -> float:
    """
    Shannon entropisi: H = log2(N^L) = L * log2(N)
    N = karakter havuzu boyutu (kullanılan benzersiz karakterlerden tahmini)
    """
    charset_size = 0
    if any(c in LOWERCASE for c in password):
        charset_size += len(LOWERCASE)
    if any(c in UPPERCASE for c in password):
        charset_size += len(UPPERCASE)
    if any(c in DIGITS for c in password):
        charset_size += len(DIGITS)
    if any(c in SYMBOLS for c in password):
        charset_size += len(SYMBOLS)
    if charset_size == 0:
        return 0.0
    return len(password) * math.log2(charset_size)


def strength_label(bits: float) -> tuple[str, str]:
    """Entropi bitine göre güç etiketi ve renk kodu döndürür."""
    if bits < 40:
        return "ÇOK ZAYIF  ✗", "\033[91m"   # kırmızı
    elif bits < 60:
        return "ZAYIF      ✗", "\033[93m"   # sarı
    elif bits < 80:
        return "ORTA       ~", "\033[93m"   # sarı
    elif bits < 100:
        return "GÜÇLÜ      ✓", "\033[92m"   # yeşil
    else:
        return "ÇOK GÜÇLÜ  ✓✓", "\033[92m" # yeşil


# ── Clipboard ───────────────────────────────────────────────────────
def copy_to_clipboard(text: str) -> bool:
    """Parolayı panoya kopyalar. Başarı durumu döner."""
    if not CLIPBOARD_AVAILABLE:
        return False
    try:
        pyperclip.copy(text)
        return True
    except Exception:
        return False


# ── Çıktı ───────────────────────────────────────────────────────────
def print_result(password: str, copy: bool = True):
    RESET  = "\033[0m"
    BOLD   = "\033[1m"
    CYAN   = "\033[96m"

    bits   = entropy_bits(password)
    label, color = strength_label(bits)

    print()
    print(f"  {BOLD}{CYAN}Parola   :{RESET}  {BOLD}{password}{RESET}")
    print(f"  Uzunluk  :  {len(password)} karakter")
    print(f"  Entropi  :  {bits:.1f} bit")
    print(f"  Güç      :  {color}{label}{RESET}")

    if copy:
        ok = copy_to_clipboard(password)
        if ok:
            print(f"  Pano     :  ✓ Kopyalandı")
        elif not CLIPBOARD_AVAILABLE:
            print(f"  Pano     :  pyperclip kurulu değil  →  pip install pyperclip")
    print()


# ── CLI ─────────────────────────────────────────────────────────────
def parse_args():
    p = argparse.ArgumentParser(
        description="Güçlü, entropi skorlu parola üretici",
        formatter_class=argparse.RawTextHelpFormatter
    )
    p.add_argument("-l", "--length",   type=int, default=20,
                   help="Parola uzunluğu (varsayılan: 20)")
    p.add_argument("-n", "--count",    type=int, default=1,
                   help="Üretilecek parola sayısı (varsayılan: 1)")
    p.add_argument("--no-upper",       action="store_true",
                   help="Büyük harf kullanma")
    p.add_argument("--no-digits",      action="store_true",
                   help="Rakam kullanma")
    p.add_argument("--no-symbols",     action="store_true",
                   help="Sembol kullanma")
    p.add_argument("--no-ambiguous",   action="store_true",
                   help="Karıştırıcı karakterleri hariç tut (0,O,1,l,I)")
    p.add_argument("--no-copy",        action="store_true",
                   help="Paroları panoya kopyalama")
    return p.parse_args()


def main():
    args = parse_args()

    print("\n  ╔══════════════════════════════════╗")
    print("  ║   🔐  PAROLA ÜRETİCİ  v1.0       ║")
    print("  ╚══════════════════════════════════╝")

    for i in range(args.count):
        if args.count > 1:
            print(f"  ── Parola {i + 1}/{args.count} " + "─" * 20)
        try:
            pwd = generate_password(
                length=args.length,
                use_upper=not args.no_upper,
                use_digits=not args.no_digits,
                use_symbols=not args.no_symbols,
                exclude_ambiguous=args.no_ambiguous
            )
            # Sadece son parolayı kopyala (çoklu üretimde)
            do_copy = (not args.no_copy) and (i == args.count - 1)
            print_result(pwd, copy=do_copy)
        except ValueError as e:
            print(f"  HATA: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
