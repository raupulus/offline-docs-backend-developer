---
title: mcrypt_module_get_supported_key_sizes
description: Devuelve un array que contiene los tamaños de claves soportados por el
  algoritmo abierto
source_url: https://www.php.net/manual/es/function.mcrypt-module-get-supported-key-sizes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mcrypt-module-get-supported-key-sizes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 45950
---

mcrypt_module_get_supported_key_sizes

Devuelve un array que contiene los tamaños de claves soportados por el algoritmo abierto

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
mcrypt_module_get_supported_key_sizes(string $algorithm, [string $lib_dir]): array
```php

Devuelve un array que contiene los tamaños de claves soportados por el algoritmo de cifrado `algorithm`. Si devuelve un array vacío, entonces todas las claves entre 1 y `mcrypt_module_get_algo_key_size` son soportadas por el algoritmo.

## Parámetros

`algorithm`  
El algoritmo a utilizar.

`lib_dir`  
El parámetro opcional `lib_dir` puede contener la ruta de acceso del directorio de instalación del módulo, en el sistema.

## Valores devueltos

Devuelve un array que contiene los tamaños de claves soportados por el algoritmo de cifrado `algorithm`. Si devuelve un array vacío, entonces todas las claves entre 1 y `mcrypt_module_get_algo_key_size` son soportadas por el algoritmo.

## Véase también

mcrypt_enc_get_supported_key_sizes
