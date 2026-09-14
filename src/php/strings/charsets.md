---
title: Juegos de caracteres soportados
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/charsets.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_revision: e5f1a5a29
order: 88570
---

Están soportados los siguientes juegos de caracteres:

| Juego de caracteres | Alias | Descripción |
|----|----|----|
| ISO-8859-1 | ISO8859-1 | Europeo occidental, Latin-1. |
| ISO-8859-5 | ISO8859-5 | Juego de caracteres cirílicos poco usado (Latin/Cyrillic). |
| ISO-8859-15 | ISO8859-15 | Europeo occidental, Latin-9. Añade el signo de euro, y letras del francés y finlandés ausentes en Latin-1 (ISO-8859-1). |
| UTF-8 |  | Unicode de 8 bit multibyte compatible con ASCII. |
| cp866 | ibm866, 866 | Juego de caracteres cirílico específico de DOS. |
| cp1251 | Windows-1251, win-1251, 1251 | Juego de caracteres cirílico específico de Windows. |
| cp1252 | Windows-1252, 1252 | Juego de caracteres específico de Windows para Europa occidental. |
| KOI8-R | koi8-ru, koi8r | Ruso. |
| BIG5 | 950 | Chino tradicional, usado principalmente en Taiwán. |
| GB2312 | 936 | Chino simplificado, juego de caracteres estándar nacional. |
| BIG5-HKSCS |  | Big5 con extensiones de Hong Kong, chino tradicional. |
| Shift_JIS | SJIS, SJIS-win, cp932, 932 | Japonés |
| EUC-JP | EUCJP, eucJP-win | Japonés |
| MacRoman |  | Juego de caracteres que fue utilizado por Mac OS. |
| `''` |  | Un string vacío activa la detección desde la codificación del script (Zend multibyte), [default_charset](#ini.default-charset) y la actual configuración regional (véase `nl_langinfo` y `setlocale`), en este orden. No se recomienda. |

Juegos de caracteres soportados

> [!NOTE]
> No se reconoce cualquier otro juego de caracteres. Será utilizada en su lugar la codificación por defecto y se emitirá una advertencia.
