---
title: gmp_random_seed
description: Define la semilla RNG (Generador de Números Aleatorios)
source_url: https://www.php.net/manual/es/function.gmp-random-seed.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-random-seed.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_reviewed: true
translation_revision: b412bbd26
order: 28730
---

gmp_random_seed

Define la semilla RNG (Generador de Números Aleatorios)

## Descripción

```php
gmp_random_seed(GMP $seed): void
```php

## Parámetros

`seed`  
La semilla a definir para las funciones `gmp_random`, `gmp_random_bits`, y `gmp_random_range`.

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Levanta una excepción `ValueError` si el argumento `seed` es inválido.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Si el argumento `seed` es inválido, `gmp_random_seed` levanta una excepción `ValueError` a partir de ahora. Anteriormente se emitía una advertencia `E_WARNING`. |

## Ejemplos

Ejemplo con `gmp_random_seed`

```
<?php
// definir la semilla
gmp_random_seed(100);

var_dump(gmp_strval(gmp_random(1)));

// definir la semilla a otro valor
gmp_random_seed(gmp_init(-100));

var_dump(gmp_strval(gmp_random_bits(10)));

// definir una semilla con un valor inválido
var_dump(gmp_random_seed('not a number'));

    
```php

El ejemplo anterior mostrará:

    string(20) "15370156633245019617"
    string(3) "683"

    Warning: gmp_random_seed(): Unable to convert variable to GMP - string is not an integer in %s on line %d
    bool(false)

## Véase también

gmp_init

gmp_random

gmp_random_bits

gmp_random_range
