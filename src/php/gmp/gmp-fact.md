---
title: gmp_fact
description: Factorielle GMP
source_url: https://www.php.net/manual/es/function.gmp-fact.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-fact.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_reviewed: true
translation_revision: 50d9745e6
order: 28480
---

gmp_fact

Factorielle GMP

## Descripción

```php
gmp_fact(GMP $num): GMP
```php

Calcula la factorielle (`num!`) de `num`.

## Parámetros

`num`  
El número factoriel.

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

Un objeto `GMP`.

## Ejemplos

Ejemplo con `gmp_fact`

```
<?php
$fact1 = gmp_fact(5); // 5 * 4 * 3 * 2 * 1
echo gmp_strval($fact1) . "\n";

$fact2 = gmp_fact(50); // 50 * 49 * 48, ... etc
echo gmp_strval($fact2) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    120
    30414093201713378043612608166064768844377641568960512000000000000
