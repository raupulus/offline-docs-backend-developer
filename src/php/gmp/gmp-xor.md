---
title: gmp_xor
description: Nivel de bit XOR
source_url: https://www.php.net/manual/es/function.gmp-xor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-xor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28860
---

gmp_xor

Nivel de bit XOR

## Descripción

```php
gmp_xor(GMP $num1, GMP $num2): GMP
```php

Calcula el nivel de bit exclusivo OR (XOR) de dos números GMP.

## Parámetros

`num1`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`num2`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

Un objeto `GMP`.

## Ejemplos

Ejemplo de`gmp_xor`

```
<?php
$xor1 = gmp_init("1101101110011101", 2);
$xor2 = gmp_init("0110011001011001", 2);

$xor3 = gmp_xor($xor1, $xor2);

echo gmp_strval($xor3, 2) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    1011110111000100
