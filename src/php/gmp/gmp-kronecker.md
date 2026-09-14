---
title: gmp_kronecker
description: Símbolo Kronecker
source_url: https://www.php.net/manual/es/function.gmp-kronecker.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-kronecker.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_reviewed: true
translation_revision: 039ab719e
order: 28570
---

gmp_kronecker

Símbolo Kronecker

## Descripción

```php
gmp_kronecker(GMP $num1, GMP $num2): int
```php

Esta función calcula el símbolo Kronecker de `num1` y `num2`.

## Parámetros

`num1`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`num2`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

Devuelve el símbolo Kronecker de `num1` y `num2`.

## Véase también

gmp_jacobi

gmp_legendre
