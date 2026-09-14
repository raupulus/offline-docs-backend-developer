---
title: imap_utf7_encode
description: Convierte una cadena ISO-8859-1 en texto UTF-7 modificado
source_url: https://www.php.net/manual/es/function.imap-utf7-encode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-utf7-encode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 4881b14f0
order: 38650
---

imap_utf7_encode

Convierte una cadena ISO-8859-1 en texto UTF-7 modificado

## Descripción

```php
imap_utf7_encode(string $string): string
```php

Convierte una cadena `string` ISO-8859-1 en texto UTF-7 modificado.

Esta función se utiliza para codificar los nombres de las carpetas de correo que contienen caracteres internacionales fuera del espacio ASCII.

## Parámetros

`string`  
Una `string` ISO-8859-1.

## Valores devueltos

Devuelve los datos `string` codificados con la codificación UTF-7 modificada tal como se define en la [RFC 2060](https://datatracker.ietf.org/doc/html/rfc2060), sección 5.1.3.

## Véase también

`imap_utf7_decode`
