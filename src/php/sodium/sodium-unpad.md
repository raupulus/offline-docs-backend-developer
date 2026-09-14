---
title: sodium_unpad
description: Elimina los datos de relleno
source_url: https://www.php.net/manual/es/function.sodium-unpad.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-unpad.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 77050
---

sodium_unpad

Elimina los datos de relleno

## Descripción

```php
#[\SensitiveParameter] sodium_unpad(string $string, int $block_size): string
```php

Elimina los datos de relleno de una string. Seguro en términos de tiempo.

## Parámetros

`string`  
La string rellena.

`block_size`  
El tamaño del bloque para el relleno.

## Valores devueltos

La string sin relleno.
