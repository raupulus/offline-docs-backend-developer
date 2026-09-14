---
title: mcrypt_enc_get_block_size
description: Devuelve el tamaño de bloque de un algoritmo
source_url: https://www.php.net/manual/es/function.mcrypt-enc-get-block-size.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mcrypt-enc-get-block-size.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 45730
---

mcrypt_enc_get_block_size

Devuelve el tamaño de bloque de un algoritmo

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
mcrypt_enc_get_block_size(resource $td): int
```php

Obtiene el tamaño de bloque de un algoritmo.

## Parámetros

`td`  
El gestor de ficheros.

## Valores devueltos

Devuelve el tamaño de bloque del algoritmo, en bytes.
