---
title: sodium_pad
description: Añade datos de relleno
source_url: https://www.php.net/manual/es/function.sodium-pad.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-pad.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 77040
---

sodium_pad

Añade datos de relleno

## Descripción

```php
#[\SensitiveParameter] sodium_pad(string $string, int $block_size): string
```php

Rellena a la derecha una string hasta la longitud deseada. Seguro en términos de tiempo.

## Parámetros

`string`  
La string sin rellenar.

`block_size`  
La string será rellenada hasta que sea un múltiplo par del tamaño del bloque.

## Valores devueltos

La string rellenada.
