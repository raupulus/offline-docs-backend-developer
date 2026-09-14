---
title: gmp_sign
description: Signo del número GMP
source_url: https://www.php.net/manual/es/function.gmp-sign.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-sign.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_reviewed: false
translation_revision: a35fce69c
order: 28800
---

gmp_sign

Signo del número GMP

## Descripción

```php
gmp_sign(GMP $num): int
```php

Verifica el signo de un número.

## Parámetros

`num`  
Puede ser un objeto `GMP` o una cadena numérica, siempre que sea posible convertir esta última en un `int`.

## Valores devueltos

Devuelve el signo de `num`: 1 si `num` es positivo, -1 si es negativo y 0 si `num` es igual a cero.

## Ejemplos

Ejemplo con `gmp_sign`

```
<?php
// positivo
echo gmp_sign("500") . "\n";

// negativo
echo gmp_sign("-500") . "\n";

// cero
echo gmp_sign("0") . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    1
    -1
    0

## Véase también

`gmp_abs`, `abs`
