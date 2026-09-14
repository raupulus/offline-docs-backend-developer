---
title: imap_qprint
description: Convierte una string con comillas en una string de 8 bits
source_url: https://www.php.net/manual/es/function.imap-qprint.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-qprint.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: e2f50c240
order: 38420
---

imap_qprint

Convierte una string con comillas en una string de 8 bits

## Descripción

```php
imap_qprint(string $string): string
```php

Convierte la string con comillas `string` en una string de 8 bits (según la [RFC2045](https://datatracker.ietf.org/doc/html/rfc2045), sección 6.7).

## Parámetros

`string`  
Una string con comillas

## Valores devueltos

Devuelve una `string` de 8 bits, o `false` si ocurre un error.

## Véase también

`imap_8bit`
