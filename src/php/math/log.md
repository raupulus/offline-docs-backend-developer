---
title: log
description: Logaritmo natural (neperiano)
source_url: https://www.php.net/manual/es/function.log.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/log.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: true
translation_revision: 26ce97891
order: 44760
---

log

Logaritmo natural (neperiano)

## Descripción

```php
log(float $num, [float $base]): float
```php

Si el argumento opcional `base` es especificado, `log` devuelve entonces log<sub>base</sub> `num`, de lo contrario `log` devuelve el logaritmo natural (o neperiano) de `num`.

## Parámetros

`num`  
El valor para el cual se calcula el logaritmo

`base`  
La base logarítmica opcional a utilizar (por omisión, 'e' y por lo tanto, el logaritmo natural).

## Valores devueltos

El logaritmo de `num` en base `base`, si se proporciona, o el logaritmo natural.

## Véase también

`log10`, `exp`, `pow`, `error_log`
