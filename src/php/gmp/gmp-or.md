---
title: gmp_or
description: Nivel de bit OR
source_url: https://www.php.net/manual/es/function.gmp-or.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-or.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28640
---

gmp_or

Nivel de bit OR

## Descripción

```php
gmp_or(GMP $num1, GMP $num2): GMP
```php

Calcula el nivel de bit OR de dos números GMP.

## Parámetros

`num1`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`num2`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

Un objeto `GMP`.

## Ejemplos

Ejemplo de `gmp_or`

```
<?php
$or1 = gmp_or("0xfffffff2", "4");
echo gmp_strval($or1, 16) . "\n";
$or2 = gmp_or("0xfffffff2", "2");
echo gmp_strval($or2, 16) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    fffffff6
    fffffff2
