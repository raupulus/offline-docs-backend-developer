---
title: Juegos de caracteres soportados
source_url: https://www.php.net/manual/es/mbstring.supported-encodings.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/supported-encodings.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: a0ae28d3b
order: 45660
---

## Juegos de caracteres soportados

Actualmente, los siguientes juegos de caracteres son soportados por `mbstring`. La codificación de caracteres puede ser especificada mediante los parámetros `encoding` en las funciones `mbstring`.

Los siguientes juegos de caracteres son soportados por `mbstring`:

- UCS-4\*

- UCS-4BE

- UCS-4LE\*

- UCS-2

- UCS-2BE

- UCS-2LE

- UTF-32\*

- UTF-32BE\*

- UTF-32LE\*

- UTF-16\*

- UTF-16BE\*

- UTF-16LE\*

- UTF-7

- UTF7-IMAP

- UTF-8\*

- ASCII\*

- EUC-JP\*

- SJIS\*

- eucJP-win\*

- SJIS-win\*

- ISO-2022-JP

- ISO-2022-JP-MS

- CP932

- CP51932

- SJIS-mac (alias: MacJapanese)

- SJIS-Mobile#DOCOMO (alias: SJIS-DOCOMO)

- SJIS-Mobile#KDDI (alias: SJIS-KDDI)

- SJIS-Mobile#SOFTBANK (alias: SJIS-SOFTBANK)

- UTF-8-Mobile#DOCOMO (alias: UTF-8-DOCOMO)

- UTF-8-Mobile#KDDI-A

- UTF-8-Mobile#KDDI-B (alias: UTF-8-KDDI)

- UTF-8-Mobile#SOFTBANK (alias: UTF-8-SOFTBANK)

- ISO-2022-JP-MOBILE#KDDI (alias: ISO-2022-JP-KDDI)

- JIS

- JIS-ms

- CP50220

- CP50220raw

- CP50221

- CP50222

- ISO-8859-1\*

- ISO-8859-2\*

- ISO-8859-3\*

- ISO-8859-4\*

- ISO-8859-5\*

- ISO-8859-6\*

- ISO-8859-7\*

- ISO-8859-8\*

- ISO-8859-9\*

- ISO-8859-10\*

- ISO-8859-13\*

- ISO-8859-14\*

- ISO-8859-15\*

- ISO-8859-16\*

- byte2be

- byte2le

- byte4be

- byte4le

- BASE64

- HTML-ENTITIES (alias: HTML)

- 7bit

- 8bit

- EUC-CN\*

- CP936

- GB18030

- HZ

- EUC-TW\*

- CP950

- BIG-5\*

- EUC-KR\*

- UHC (alias: CP949)

- ISO-2022-KR

- Windows-1251 (alias: CP1251)

- Windows-1252 (alias: CP1252)

- CP866 (alias: IBM866)

- KOI8-R\*

- KOI8-U\*

- ArmSCII-8 (alias: ArmSCII8)

\* : codificaciones también utilizables en expresiones regulares.

Todas las entradas del `php.ini` que aceptan un nombre de codificación pueden también utilizar los valores "`auto`" y "`pass`". Las funciones `mbstring`, que aceptan nombres de juegos de caracteres, pueden también utilizar el valor "`auto`".

Si "`pass`" es utilizada, ninguna conversión se efectúa.

Si "`auto`" es definido, la lista será extendida a la lista de codificaciones definidas por [NLS](#mbstring.configuration). Por ejemplo, si `NLS` vale `Japanese`, los valores serán "`ASCII,JIS,UTF-8,EUC-JP,SJIS`".

Ver también `mb_detect_order`.
