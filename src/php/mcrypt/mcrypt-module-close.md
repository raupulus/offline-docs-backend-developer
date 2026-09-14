---
title: mcrypt_module_close
description: Libera el módulo de cifrado
source_url: https://www.php.net/manual/es/function.mcrypt-module-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mcrypt-module-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 45920
---

mcrypt_module_close

Libera el módulo de cifrado

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
mcrypt_module_close(resource $td): bool
```php

Libera el módulo `td`.

## Parámetros

`td`  
El recurso de cifrado.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

mcrypt_module_open
