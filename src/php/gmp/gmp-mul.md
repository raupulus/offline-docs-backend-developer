---
title: gmp_mul
description: Multiplicación de números
source_url: https://www.php.net/manual/es/function.gmp-mul.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-mul.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28610
---

gmp_mul

Multiplicación de números

## Descripción

```php
gmp_mul(GMP $num1, GMP $num2): GMP
```php

Multiplicación de `num1` por `num2` y devuelve el resultado.

## Parámetros

`num1`  
Un número que va a ser multiplicado por `num2`.

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`num2`  
Un número que va a ser multiplicado por `num1`.

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

Un objeto `GMP`.

## Ejemplos

Ejemplo de`gmp_mul`

```
<?php
$mul = gmp_mul("12345678", "2000");
echo gmp_strval($mul) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    24691356000
