---
title: gmp_perfect_power
description: Verifica si un número es una potencia perfecta
source_url: https://www.php.net/manual/es/function.gmp-perfect-power.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-perfect-power.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_reviewed: true
translation_revision: 039ab719e
order: 28650
---

gmp_perfect_power

Verifica si un número es una potencia perfecta

## Descripción

```php
gmp_perfect_power(GMP $num): bool
```php

Verifica si `num` es una potencia perfecta.

## Parámetros

`num`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

Devuelve `true` si `num` es una potencia perfecta, `false` en caso contrario.

## Véase también

gmp_perfect_square
