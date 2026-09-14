---
title: gmp_lcm
description: Calcula el Mínimo Común Múltiplo (MCM)
source_url: https://www.php.net/manual/es/function.gmp-lcm.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-lcm.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_reviewed: true
translation_revision: 039ab719e
order: 28580
---

gmp_lcm

Calcula el Mínimo Común Múltiplo (MCM)

## Descripción

```php
gmp_lcm(GMP $num1, GMP $num2): GMP
```php

Esta función calcula el mínimo común múltiplo (MCM) de `num1` y `num2`.

## Parámetros

`num1`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`num2`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

Un objeto `GMP`.

## Véase también

gmp_gcd
