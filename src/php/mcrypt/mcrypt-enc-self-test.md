---
title: mcrypt_enc_self_test
description: Prueba un módulo abierto
source_url: https://www.php.net/manual/es/function.mcrypt-enc-self-test.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mcrypt-enc-self-test.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 45810
---

mcrypt_enc_self_test

Prueba un módulo abierto

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
mcrypt_enc_self_test(resource $td): int
```php

Realiza una prueba del módulo abierto y designado por `td`.

## Parámetros

`td`  
El recurso de cifrado.

## Valores devueltos

Devuelve `0` en caso de éxito o un `int` negativo en caso de fallo.
