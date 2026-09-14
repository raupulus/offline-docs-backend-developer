---
title: mcrypt_module_get_algo_key_size
description: Devuelve el tamaño máximo de clave
source_url: https://www.php.net/manual/es/function.mcrypt-module-get-algo-key-size.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mcrypt-module-get-algo-key-size.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 45940
---

mcrypt_module_get_algo_key_size

Devuelve el tamaño máximo de clave

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
mcrypt_module_get_algo_key_size(string $algorithm, [string $lib_dir]): int
```php

Devuelve el tamaño máximo de clave.

## Parámetros

`algorithm`  
El nombre del algoritmo.

`lib_dir`  
El parámetro opcional `lib_dir` contiene la ruta hasta el módulo del algoritmo en el sistema.

## Valores devueltos

Devuelve el tamaño máximo de la clave soportada por el algoritmo `algorithm`.
