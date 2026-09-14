---
title: imap_utf8
description: Convierte texto en formato MIME a UTF-8
source_url: https://www.php.net/manual/es/function.imap-utf8.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-utf8.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 67acb98da
order: 38670
---

imap_utf8

Convierte texto en formato MIME a UTF-8

## Descripción

```php
imap_utf8(string $mime_encoded_text): string
```php

Convierte el texto `mime_encoded_text` a UTF-8, si el conjunto de caracteres declarado es conocido por libc-client. De lo contrario, el texto proporcionado será decodificado, pero no convertido a UTF-8.

## Parámetros

`mime_encoded_text`  
Un string codificado en MIME. Las especificaciones de MIME y UTF8 están descritas en los [RFC2047](https://datatracker.ietf.org/doc/html/rfc2047) y [RFC2044](https://datatracker.ietf.org/doc/html/rfc2044).

## Valores devueltos

Devuelve el string decodificado y, si es posible, convertido a UTF-8.

## Ejemplos

Uso básico de la función `imap_utf8`

```
<?php
echo imap_utf8("Johannes =?ISO-8859-1?Q?Schl=FCter?=");
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Johannes Schlüter

## Véase también

`imap_mime_header_decode`
