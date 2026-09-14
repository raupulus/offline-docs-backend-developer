---
title: Juegos de caracteres soportados
source_url: https://www.php.net/manual/es/mbstring.encodings.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/encodings.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_revision: a9ada9d6f
order: 44950
---

## Juegos de caracteres soportados

Nombre en el registro IANA

Juegos de caracteres

Descripción

Notas

ISO-10646-UCS-4

ISO 10646

El juego de caracteres universal (

Universal Character Set

), con 31 bits por caracter, al estándar

UCS-4

por

ISO/IEC 10646

. Está sincronizado con la última versión de Unicode.

Si este nombre es utilizado en la herramienta de conversión, el convertidor intenta reconocer el texto a partir del último BOM (

byte order mark

), para conocer el orden de los bits.

ISO-10646-UCS-4

UCS-4

Ver arriba.

A diferencia de

UCS-4

, las cadenas se suponen estar en formato big endian.

ISO-10646-UCS-4

UCS-4

Ver arriba.

A diferencia de

UCS-2

, las cadenas se suponen estar en formato little endian.

ISO-10646-UCS-2

UCS-2

El juego de caracteres universal (

Universal Character Set

), con 16 bits por caracter, al estándar

UCS-2

por

ISO/IEC 10646

. Está sincronizado con la última versión de Unicode.

Si este nombre es utilizado en la herramienta de conversión, el convertidor intenta reconocer el texto a partir del último BOM (

byte order mark

), para conocer el orden de los bits.

ISO-10646-UCS-2

UCS-2

Ver arriba.

A diferencia de

UCS-4

, las cadenas se suponen estar en formato big endian.

UTF-32

Unicode

Formato de transformación de Unicode, de 32 bits, cuyas cartas corresponden al juego estándar Unicode. Este juego no es idéntico a

UCS-4

porque los caracteres Unicode estaban limitados a valores de 21 bits.

Si este nombre es utilizado en la herramienta de conversión, el convertidor intenta reconocer el texto a partir del último BOM (

byte order mark

), para conocer el orden de los bits.

UTF-32BE

Unicode

Ver arriba.

A diferencia de

UTF-32

, las cadenas se suponen estar en formato big endian.

UTF-32LE

Unicode

Ver arriba.

A diferencia de

UTF-32

, las cadenas se suponen estar en formato little endian.

UTF-16

Unicode

Formato de transformación de Unicode sobre 16 bits. Se debe notar que

UTF-16

ya no es idéntico a

UCS-2

porque un mecanismo fue introducido en Unicode 2.0 y

UTF-16

ahora hace referencia a un codificación de 21 bits.

Si este nombre es utilizado en la herramienta de conversión, el convertidor intenta reconocer el texto a partir del último BOM (

byte order mark

), para conocer el orden de los bits.

UTF-16BE

Unicode

Ver arriba.

A diferencia de

UTF-16

, las cadenas se suponen estar en formato big endian.

UTF-16LE

Unicode

Ver arriba.

A diferencia de

UTF-16

, las cadenas se suponen estar en formato little endian.

UTF-8

Unicode / UCS

Formato de transformación Unicode de 8 bits.

ninguno

UTF-7

Unicode

Un formato compatible con el correo electrónico de Unicode, especificado en

RFC2152

.

ninguno

ninguno

Unicode

Una variante de

UTF-7

que es especialmente utilizada en el

protocolo IMAP

.

ninguno

US-ASCII (recomendado) / iso-ir-6 / ANSI_X3.4-1986 / ISO_646.irv:1991 / ASCII / ISO646-US / us / IBM367 / CP367 / csASCII

ASCII / ISO 646

ASCII,

American Standard Code for Information Interchange

es un formato clásico de 7 bits. También está normalizado internacionalmente, bajo el nombre

ISO 646

.

(ninguno)

EUC-JP (recomendado) / Extended_UNIX_Code_Packed_Format_for_Japanese / csEUCPkdFmtJapanese

Compuesto de US-ASCII / JIS X0201:1997 (hankaku kana) / JIS X0208:1990 / JIS X0212:1990

Como se puede ver, el nombre deriva de la abreviatura de

Extended UNIX Code Packed Format for Japanese

, este juego es esencialmente utilizado en plataformas Unix. El juego original,

Extended UNIX Code

, está diseñado sobre la base de

ISO 2022

.

El juego identificado por

EUC-JP

es diferente de

IBM932 / CP932

, que es utilizado por

OS/2®

y Microsoft® Windows®. Para intercambiar información con estas plataformas, utilice

EUCJP-WIN

.

Shift_JIS (recomendado) / MS_Kanji / csShift_JIS

Compuesto de JIS X0201:1997 / JIS X0208:1997

Shift_JIS

fue desarrollado a principios de los años 80, y, al mismo tiempo, los primeros procesadores de texto estaban en el mercado. Fue hecho para conservar la compatibilidad con el juego

JIS X 0201:1976

. Según la definición de IANA, el juego de caracteres

Shift_JIS

es ligeramente diferente de

IBM932 / CP932

. Sin embargo, los nombres

"SJIS"

y

"Shift_JIS"

son a menudo utilizados erróneamente, para estos juegos.

Para

CP932

, utilice

SJIS-WIN

.

(ninguno)

Compuesto de JIS X0201:1997 / JIS X0208:1997 / IBM extensions / NEC extensions

Aunque este "juego de caracteres" utiliza el mismo juego que

EUC-JP

, en realidad es diferente. Solo tiene algunos caracteres de diferencia.

ninguno

Windows-31J / csWindows31J

Compuesto de JIS X0201:1997 / JIS X0208:1997 / IBM extensions / NEC extensions

Aunque este "juego de caracteres" utiliza el mismo juego que

Shift_JIS

, en realidad es diferente. Solo tiene algunos caracteres de diferencia.

(ninguno)

ISO-2022-JP (recomendado) / csISO2022JP

US-ASCII / JIS X0201:1976 / JIS X0208:1978 / JIS X0208:1983

RFC1468

ninguno

JIS

ISO-8859-1

ISO-8859-2

ISO-8859-3

ISO-8859-4

ISO-8859-5

ISO-8859-6

ISO-8859-7

ISO-8859-8

ISO-8859-9

ISO-8859-10

ISO-8859-13

ISO-8859-14

ISO-8859-15

ISO-8859-16

byte2be

byte2le

byte4be

byte4le

BASE64

HTML-ENTITIES

7bit

8bit

EUC-CN

CP936

HZ

EUC-TW

CP950

BIG-5

EUC-KR

UHC (CP949)

ISO-2022-KR

Windows-1251 (CP1251)

Windows-1252 (CP1252)

CP866 (IBM866)

KOI8-R

KOI8-U
