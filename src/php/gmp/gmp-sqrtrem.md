---
title: gmp_sqrtrem
description: Raíz cuadrada con resto
source_url: https://www.php.net/manual/es/function.gmp-sqrtrem.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-sqrtrem.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28820
---

gmp_sqrtrem

Raíz cuadrada con resto

## Descripción

```php
gmp_sqrtrem(GMP $num): array
```php

Calcula la raíz cuadrada de un número, con resto.

## Parámetros

`num`  
El número a ser la raíz cuadrada.

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

Devuelve un arreglo donde el primer elemento es el entero de la raíz cuadrada de `num` y el segundo es el resto (ej., La diferencia entre `num` y el primer elemento de la raíz cuadrada).

## Ejemplos

Ejemplo de`gmp_sqrtrem`

```
<?php
list($sqrt1, $sqrt1rem) = gmp_sqrtrem("9");
list($sqrt2, $sqrt2rem) = gmp_sqrtrem("7");
list($sqrt3, $sqrt3rem) = gmp_sqrtrem("1048576");

echo gmp_strval($sqrt1) . ", " . gmp_strval($sqrt1rem) . "\n";
echo gmp_strval($sqrt2) . ", " . gmp_strval($sqrt2rem) . "\n";
echo gmp_strval($sqrt3) . ", " . gmp_strval($sqrt3rem) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    3, 0
    2, 3
    1024, 0
