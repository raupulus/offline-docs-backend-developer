---
title: mcrypt_generic_deinit
description: Prepara el módulo para la descarga
source_url: https://www.php.net/manual/es/function.mcrypt-generic-deinit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mcrypt-generic-deinit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 45830
---

mcrypt_generic_deinit

Prepara el módulo para la descarga

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
mcrypt_generic_deinit(resource $td): bool
```php

Prepara el módulo de cifrado `td` para la descarga. Todos los búferes se vacían, pero el módulo no se descarga. Se debe llamar a `mcrypt_module_close` manualmente (aunque PHP lo hará por usted al final del script).

## Parámetros

`td`  
El recurso de cifrado.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

mcrypt_module_open

mcrypt_generic_init
