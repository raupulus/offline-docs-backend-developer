---
title: imap_mutf7_to_utf8
description: Decodifica una string UTF-7 modificado en UTF-8
source_url: https://www.php.net/manual/es/function.imap-mutf7-to-utf8.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-mutf7-to-utf8.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 7f99d5e48
order: 38370
---

imap_mutf7_to_utf8

Decodifica una string UTF-7 modificado en UTF-8

## Descripción

```php
imap_mutf7_to_utf8(string $string): string
```php

Decodifica una `string` UTF-7 modificado (como se especifica en la RFC 2060, sección 5.1.3) en UTF-8.

> [!NOTE]
> Esta función solo está disponible si libcclient exporta utf8_to_mutf7().

## Parámetros

`string`  
Una `string` codificada en UTF-7 modificado.

## Valores devueltos

Devuelve `string` convertida en UTF-8, o `false` si ocurre un error.

## Véase también

imap_utf8_to_mutf7
