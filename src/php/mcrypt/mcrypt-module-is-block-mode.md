---
title: mcrypt_module_is_block_mode
description: Indica si un modo trabaja por bloques
source_url: https://www.php.net/manual/es/function.mcrypt-module-is-block-mode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mcrypt-module-is-block-mode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 45980
---

mcrypt_module_is_block_mode

Indica si un modo trabaja por bloques

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
mcrypt_module_is_block_mode(string $mode, [string $lib_dir]): bool
```php

Esta función devuelve `true` si este modo proporciona bloques de bytes o `false` si solo produce bytes. (i.e. `true` para `"cbc"` y `"ecb"`, y `false` para `"cfb"` y `"stream"`).

## Parámetros

`mode`  
Una de las constantes `MCRYPT_MODE_modename`, o una de las siguientes cadenas: "ecb", "cbc", "cfb", "ofb", "nofb" o "stream".

`lib_dir`  
El parámetro opcional `lib_dir` contiene la ruta de acceso hasta el módulo del algoritmo en el sistema.

## Valores devueltos

Esta función devuelve `true` si este modo proporciona bloques de bytes o `false` si solo produce bytes. (i.e. `true` para `"cbc"` y `"ecb"`, y `false` para `"cfb"` y `"stream"`).
