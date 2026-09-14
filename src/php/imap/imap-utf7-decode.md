---
title: imap_utf7_decode
description: Decodifica una cadena codificada en UTF-7 modificado
source_url: https://www.php.net/manual/es/function.imap-utf7-decode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-utf7-decode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 4881b14f0
order: 38640
---

imap_utf7_decode

Decodifica una cadena codificada en UTF-7 modificado

## Descripción

```php
imap_utf7_decode(string $string): string
```php

`imap_utf7_decode` decodifica la cadena UTF-7 `string` en ISO-8859-1.

Esta función se utiliza para codificar los nombres de los buzones de correo que contienen caracteres internacionales fuera del espacio ASCII.

## Parámetros

`string`  
La codificación UTF-7 modificada está definida en la [RFC 2060](https://datatracker.ietf.org/doc/html/rfc2060), sección 5.1.3.

## Valores devueltos

Devuelve una `string` codificada en ISO-8859-1 y que contiene la misma secuencia de caracteres que en el parámetro `string`, o `false` si `string` contiene una secuencia UTF-7 modificada inválida o si `string` contiene un carácter que no forma parte del juego de caracteres ISO-8859-1.

## Véase también

`imap_utf7_encode`
