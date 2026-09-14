---
title: posix_setrlimit
description: Establecer los límites de recursos del sistema
source_url: https://www.php.net/manual/es/function.posix-setrlimit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-setrlimit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: 42ed815ea
order: 65430
---

posix_setrlimit

Establecer los límites de recursos del sistema

## Descripción

```php
posix_setrlimit(int $resource, int $soft_limit, int $hard_limit): bool
```php

`posix_setrlimit` establece los límites blando y duro para un recurso de sistema dado.

Cada recurso tiene un límite soft y hard asociados. El límite soft corresponde al valor que el núcleo fuerza para el recurso correspondiente. El límite hard actúa como un techo del límite soft. Un proceso no privilegiado solo puede definir su límite soft en un valor comprendido entre 0 y el límite hard, lo que solo hará bajar su límite hard.

## Parámetros

`resource`  
La [constante de límite de recurso](#posix.constants.setrlimit) conrrespondiente al límite a establecer.

`soft_limit`  
El límite blando, en la unidad que el límite del recurso requiera, o `POSIX_RLIMIT_INFINITY`.

`hard_limit`  
El límite duro, en la unidad que el límite del recurso requiera, o `POSIX_RLIMIT_INFINITY`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Ahora lanza una ValueError cuando `hard_limit` o `soft_limit` es menor que -1, o cuando `soft_limit` es mayor que `hard_limit`. |

## Véase también

La página SETRLIMIT(2) de man, `posix_getrlimit`
