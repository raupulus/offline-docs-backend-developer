---
title: imap_8bit
description: Convierte un string de 8 bits en un string codificado en Quoted-Printable
source_url: https://www.php.net/manual/es/function.imap-8bit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-8bit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: e2f50c240
order: 37920
---

imap_8bit

Convierte un string de 8 bits en un string codificado en Quoted-Printable

## Descripción

```php
imap_8bit(string $string): string
```php

Convierte el string de 8 bits en un string codificado en Quoted-Printable (según la [RFC 2045](https://datatracker.ietf.org/doc/html/rfc2045), Sección 6.7).

## Parámetros

`string`  
El string de 8 bits a convertir

## Valores devueltos

Devuelve un string codificado en Quoted-Printable, o `false` si ocurre un error.

## Véase también

`imap_qprint`
