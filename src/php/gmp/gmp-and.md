---
title: gmp_and
description: AND a nivel de bit
source_url: https://www.php.net/manual/es/function.gmp-and.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-and.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28370
---

gmp_and

AND a nivel de bit

## Descripción

```php
gmp_and(GMP $num1, GMP $num2): GMP
```php

Calcula el AND a nivel de bit de dos números GMP.

## Parámetros

`num1`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`num2`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

Un número representando la comparación del nivel de bit `AND`.

## Ejemplos

Ejemplo de `gmp_and`

```
<?php
$and1 = gmp_and("0xfffffffff4", "0x4");
$and2 = gmp_and("0xfffffffff4", "0x8");
echo gmp_strval($and1) . "\n";
echo gmp_strval($and2) . "\n";
?>

   
```php

El ejemplo anterior mostrará:

    4
    0
