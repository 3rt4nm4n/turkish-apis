[English Guide](#contributing-guide)

[Türkçe Kılavuz](#katkıda-bulunma-kılavuzu)

## Contributing Guide

- Thank you for contributing to this repository.
- Open a pull request and add your row to **both** the English and Türkçe tables, in Turkish alphabetical order.
- Only APIs and open data sources from companies/institutions based in Türkiye, or made for Türkiye, are accepted.
- Link to the official API documentation. The link must be working.

**API tables:**

```
| [Name of The Site/Company](URL) | DESCRIPTION | Auth | HTTPS |
```

**Open Data Sources table:**

```
| [Name](URL) | Türkçe tanım / English description | [@creator](https://github.com/creator) or institution | Yok / None | Var / Yes |
```

- **Auth:** `None`, `apiKey`, `apiKey + HMAC`, `OAuth`, `Basic`, `Token` or `Unknown`.
- **HTTPS:** `Yes` / `No` in English, `Var` / `Yok` in Türkçe. Write `Unknown` if you are not sure.
- **Not accepted:** services that look up or validate personal or financial data (IBAN, TC Kimlik No, phone or plate owner), unofficial scrapers, leaked data and Kaggle dumps.

-----

## Katkıda Bulunma Kılavuzu

- Katkınız için teşekkürler.
- PR açın ve satırınızı **hem** English **hem** Türkçe tablolarına, Türk alfabesine göre sıralı ekleyin.
- Yalnızca Türkiye merkezli şirket/kurumların ya da Türkiye için yapılmış API'ler ve açık veri kaynakları kabul edilir.
- Resmi API dokümantasyonunun linkini verin. Link çalışıyor olmalıdır.

**API tabloları:**

```
| [Site/Şirket Adı](Link) | TANIM | Auth | HTTPS |
```

**Açık Veri Kaynakları tablosu:**

```
| [Ad](Link) | Türkçe tanım / English description | [@oluşturan](https://github.com/oluşturan) veya kurum | Yok / None | Var / Yes |
```

- **Auth:** `None`, `apiKey`, `apiKey + HMAC`, `OAuth`, `Basic`, `Token` veya `Unknown`.
- **HTTPS:** English tabloda `Yes` / `No`, Türkçe tabloda `Var` / `Yok`. Emin değilseniz `Unknown` yazın.
- **Kabul edilmez:** Kişisel veya finansal veri sorgulayan/doğrulayan servisler (IBAN, TC Kimlik No, telefon veya plaka sahibi), resmi olmayan scraper'lar, sızdırılmış veriler ve Kaggle dump'ları.
