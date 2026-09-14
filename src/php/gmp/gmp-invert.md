---
title: gmp_invert
description: Inverso del modulo
source_url: https://www.php.net/manual/es/function.gmp-invert.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-invert.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28550
---

gmp_invert

Inverso del modulo

## Descripción

```php
gmp_invert(GMP $num1, GMP $num2): GMP
```php

Computa el inverso del modulo de `num1` `num2`.

## Parámetros

`num1`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`num2`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

Un número GMO en éxito o `false` Si el inverso.

## Ejemplos

Ejemplo de `gmp_invert`

```
<?php
echo gmp_invert("5", "10"); // sin inverso, ninguna salida, el resultado es falso
$invert = gmp_invert("5", "11");
echo gmp_strval($invert) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    9
