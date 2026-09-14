---
title: gmp_popcount
description: Cuenta la población
source_url: https://www.php.net/manual/es/function.gmp-popcount.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-popcount.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28670
---

gmp_popcount

Cuenta la población

## Descripción

```php
gmp_popcount(GMP $num): int
```php

Obtiene el conteo de la población.

## Parámetros

`num`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

El conteo de la población de `num`, como un `int`.

## Ejemplos

Ejemplo de `gmp_popcount`

```
<?php
$pop1 = gmp_init("10000101", 2); // tres 1
echo gmp_popcount($pop1) . "\n";
$pop2 = gmp_init("11111110", 2); // siete 1
echo gmp_popcount($pop2) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    3
    7
