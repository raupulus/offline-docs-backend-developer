---
title: mcrypt_enc_is_block_algorithm
description: Comprueba si el cifrado es por bloques en un algoritmo
source_url: https://www.php.net/manual/es/function.mcrypt-enc-is-block-algorithm.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mcrypt-enc-is-block-algorithm.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 45790
---

mcrypt_enc_is_block_algorithm

Comprueba si el cifrado es por bloques en un algoritmo

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
mcrypt_enc_is_block_algorithm(resource $td): bool
```php

Comprueba si el cifrado es por bloques en un algoritmo.

## Parámetros

`td`  
El recurso de cifrado.

## Valores devueltos

Devuelve `true` si el algoritmo utilizado es un algoritmo por bloques, y `false` si es un algoritmo por flujo.
