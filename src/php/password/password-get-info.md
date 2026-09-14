---
title: password_get_info
description: Devuelve información sobre el hash proporcionado
source_url: https://www.php.net/manual/es/function.password-get-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/password/functions/password-get-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: password
translation_status: ready
translation_reviewed: false
translation_revision: 95f6764ae
order: 61100
---

password_get_info

Devuelve información sobre el hash proporcionado

## Descripción

```php
password_get_info(string $hash): array
```php

Cuando se le pasa un hash válido creado con un algoritmo soportado por `password_hash`, esta función devolverá un array con información sobre dicho hash.

## Parámetros

`hash`  
Un hash creado por la función `password_hash`.

## Valores devueltos

Devuelve un array asociativo con tres elementos:

- `algo`, que coincidirá con una [constante de algoritmo de contraseñas](#password.constants)

- `algoName`, que tiene el nombre legible por humanos del algoritmo

- `options`, que incluye las opciones proporcionadas al llamar a `password_hash`
