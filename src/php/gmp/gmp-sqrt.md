---
title: gmp_sqrt
description: Calcula la raíz cuadrada
source_url: https://www.php.net/manual/es/function.gmp-sqrt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-sqrt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28810
---

gmp_sqrt

Calcula la raíz cuadrada

## Descripción

```php
gmp_sqrt(GMP $num): GMP
```php

Calcula la raíz cuadrada de `num`.

## Parámetros

`num`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

La porción entera de la raíz cuadrada, como un número GMP.

## Ejemplos

Ejemplo de `gmp_sqrt`

```
<?php
$sqrt1 = gmp_sqrt("9");
$sqrt2 = gmp_sqrt("7");
$sqrt3 = gmp_sqrt("1524157875019052100");

echo gmp_strval($sqrt1) . "\n";
echo gmp_strval($sqrt2) . "\n";
echo gmp_strval($sqrt3) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    3
    2
    1234567890
