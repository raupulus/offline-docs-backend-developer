---
title: mcrypt_enc_is_block_algorithm_mode
description: Comprueba si el modo de cifrado es por bloques
source_url: https://www.php.net/manual/es/function.mcrypt-enc-is-block-algorithm-mode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mcrypt-enc-is-block-algorithm-mode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 45780
---

mcrypt_enc_is_block_algorithm_mode

Comprueba si el modo de cifrado es por bloques

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
mcrypt_enc_is_block_algorithm_mode(resource $td): bool
```php

Comprueba si el modo de cifrado es por bloques (por ejemplo, `false` para un flujo, y `true` para `"cbc"`, `"cfb"`, `"ofb"`).

## Parámetros

`td`  
El recurso de cifrado.

## Valores devueltos

Devuelve `true` si este modo utiliza algoritmos por bloques, y `false` en caso contrario.
