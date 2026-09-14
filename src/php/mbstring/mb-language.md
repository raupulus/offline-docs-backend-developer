---
title: mb_language
description: Define/Recupera el lenguaje actual
source_url: https://www.php.net/manual/es/function.mb-language.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-language.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: false
translation_revision: 92f1b8b17
order: 45260
---

mb_language

Define/Recupera el lenguaje actual

## Descripción

```php
mb_language([string $language]): string
```php

Define/Recupera el lenguaje actual.

## Parámetros

`language`  
Utilizado para codificar los correos electrónicos. Los lenguajes válidos se enumeran en la siguiente tabla. `mb_send_mail` utiliza esta opción para codificar los correos electrónicos.

| Idioma                    | Juego de caracteres | Codificación     | Alias     |
|---------------------------|---------------------|------------------|-----------|
| German/de                 | ISO-8859-15         | Quoted-Printable | Deutsch   |
| English/en                | ISO-8859-1          | Quoted-Printable |           |
| Armenian/hy               | ArmSCII-8           | Quoted-Printable |           |
| Japanese/ja               | ISO-2022-JP         | BASE64           |           |
| Korean/ko                 | ISO-2022-KR         | BASE64           |           |
| neutral                   | UTF-8               | BASE64           |           |
| Russian/ru                | KOI8-R              | Quoted-Printable |           |
| Turkish/tr                | ISO-8859-9          | Quoted-Printable |           |
| Ukrainian/ua              | KOI8-U              | Quoted-Printable |           |
| uni                       | UTF-8               | BASE64           | universal |
| Simplified Chinese/zh-cn  | HZ                  | BASE64           |           |
| Traditional Chinese/zh-tw | BIG-5               | BASE64           |           |

## Valores devueltos

Si `language` es proporcionado y `language` es válido, devuelve `true`. De lo contrario, devuelve `false`. Cuando `language` es omitido o `null`, devuelve el nombre del lenguaje actual, como `string`.

## Historial de cambios

| Versión | Descripción                   |
|---------|-------------------------------|
| 8.0.0   | `language` ahora es nullable. |

## Véase también

`mb_send_mail`
