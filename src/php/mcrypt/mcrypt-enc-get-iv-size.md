---
title: mcrypt_enc_get_iv_size
description: Devuelve el tamaño del VI de un algoritmo
source_url: https://www.php.net/manual/es/function.mcrypt-enc-get-iv-size.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mcrypt-enc-get-iv-size.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_revision: e849a6c42
order: 45740
---

mcrypt_enc_get_iv_size

Devuelve el tamaño del VI de un algoritmo

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
mcrypt_enc_get_iv_size(resource $td): int
```php

Esta función devuelve el tamaño del VI del algoritmo designado por `td`, en bytes. Si el valor devuelto es 0, es que el algoritmo no requiere de VI. Un VI es requerido en modo `"cbc"`, `"cfb"` y `"ofb"`, y a veces en modo `"stream"`.

## Parámetros

`td`  
El gestor de ficheros.

## Valores devueltos

Devuelve el tamaño del IV, o `0` si el IV es ignorado por el algoritmo.
