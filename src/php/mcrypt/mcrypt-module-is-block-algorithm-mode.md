---
title: mcrypt_module_is_block_algorithm_mode
description: Indica si un modo funciona por bloques
source_url: https://www.php.net/manual/es/function.mcrypt-module-is-block-algorithm-mode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mcrypt-module-is-block-algorithm-mode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 45960
---

mcrypt_module_is_block_algorithm_mode

Indica si un modo funciona por bloques

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
mcrypt_module_is_block_algorithm_mode(string $mode, [string $lib_dir]): bool
```php

Esta función devuelve `true` si el modo debe ser utilizado con un algoritmo por bloques, de lo contrario, devuelve `false` (i.e. `false` para un flujo, y `true` para cbc, cfb, ofb).

## Parámetros

`mode`  
El modo a verificar.

`lib_dir`  
El argumento opcional `lib_dir` puede contener el directorio donde los módulos de algoritmo se encuentran en el sistema.

## Valores devueltos

Esta función devuelve `true` si el modo debe ser utilizado con un algoritmo por bloques, de lo contrario, devuelve `false` (i.e. `false` para un flujo, y `true` para cbc, cfb, ofb).
