---
title: imap_binary
description: Convierte una string de 8 bits en una string en base64
source_url: https://www.php.net/manual/es/function.imap-binary.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-binary.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: e2f50c240
order: 37960
---

imap_binary

Convierte una string de 8 bits en una string en base64

## Descripción

```php
imap_binary(string $string): string
```php

Convierte la string de 8 bits `string` en una string en base64 (según la [RFC2045](https://datatracker.ietf.org/doc/html/rfc2045), Sección 6.8).

## Parámetros

`string`  
La string de 8 bits

## Valores devueltos

Devuelve la string codificada en base64, o `false` si ocurre un error.

## Véase también

`imap_base64`
