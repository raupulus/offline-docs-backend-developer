---
title: imap_utf8_to_mutf7
description: Codifica una string UTF-8 en UTF-7 modificado
source_url: https://www.php.net/manual/es/function.imap-utf8-to-mutf7.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-utf8-to-mutf7.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 7f99d5e48
order: 38660
---

imap_utf8_to_mutf7

Codifica una string UTF-8 en UTF-7 modificado

## Descripción

```php
imap_utf8_to_mutf7(string $string): string
```php

Codifica una string UTF-8 en UTF-7 modificado (como se especifica en la RFC 2060, sección 5.1.3).

> [!NOTE]
> Esta función solo está disponible si libcclient exporta utf8_to_mutf7().

## Parámetros

`string`  
Una string codificada en UTF-8.

## Valores devueltos

Devuelve `string` convertida en UTF-7 modificado, o `false` si ocurre un error.

## Véase también

imap_mutf7_to_utf8
