---
title: mcrypt_module_is_block_algorithm
description: Indica si un algoritmo funciona por bloques
source_url: https://www.php.net/manual/es/function.mcrypt-module-is-block-algorithm.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mcrypt-module-is-block-algorithm.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 45970
---

mcrypt_module_is_block_algorithm

Indica si un algoritmo funciona por bloques

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
mcrypt_module_is_block_algorithm(string $algorithm, [string $lib_dir]): bool
```php

Esta función devuelve `true` si `algorithm` es un algoritmo por bloques, o `false` si es un algoritmo por flujo.

## Parámetros

`algorithm`  
El algoritmo a verificar.

`lib_dir`  
El parámetro opcional `lib_dir` puede contener la ruta donde se encuentran los módulos de los algoritmos en el disco del sistema.

## Valores devueltos

Devuelve `true` si el algoritmo especificado es un algoritmo por bloques o `false` si es un algoritmo por flujo.
