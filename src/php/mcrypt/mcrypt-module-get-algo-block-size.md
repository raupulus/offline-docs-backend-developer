---
title: mcrypt_module_get_algo_block_size
description: Devuelve el tamaño de bloques de un algoritmo
source_url: https://www.php.net/manual/es/function.mcrypt-module-get-algo-block-size.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mcrypt-module-get-algo-block-size.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 45930
---

mcrypt_module_get_algo_block_size

Devuelve el tamaño de bloques de un algoritmo

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
mcrypt_module_get_algo_block_size(string $algorithm, [string $lib_dir]): int
```php

Devuelve el tamaño de bloques de un algoritmo.

## Parámetros

`algorithm`  
El nombre del algoritmo.

`lib_dir`  
El parámetro opcional `lib_dir` contiene la ruta de acceso hasta el módulo del algoritmo en el sistema.

## Valores devueltos

Devuelve el tamaño de bloques de un algoritmo, en bytes.
