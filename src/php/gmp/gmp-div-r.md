---
title: gmp_div_r
description: El resto de la división de los números
source_url: https://www.php.net/manual/es/function.gmp-div-r.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-div-r.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28440
---

gmp_div_r

El resto de la división de los números

## Descripción

```php
gmp_div_r(GMP $num1, GMP $num2, [int $rounding_mode]): GMP
```php

Calcula el resto de la división entera de `num1` por `num2`. El tiene el signo del argumento `num1`, si no es cero.

## Parámetros

`num1`  
El número que es dividido.

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`num2`  
El número que es dividido por `num1`.

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`rounding_mode`  
Ver la función `gmp_div_q` para la descripción del argumento `rounding_mode`.

## Valores devueltos

El resto, como número GMP.

## Ejemplos

Ejemplo de `gmp_div_r`

```
<?php
$div = gmp_div_r("105", "20");
echo gmp_strval($div) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    5

## Véase también

`gmp_div_q`, `gmp_div_qr`
