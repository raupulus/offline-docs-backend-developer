---
title: gmp_mod
description: Modulo de operación
source_url: https://www.php.net/manual/es/function.gmp-mod.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-mod.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28600
---

gmp_mod

Modulo de operación

## Descripción

```php
gmp_mod(GMP $num1, GMP $num2): GMP
```php

Calcula el modulo de `num1` `num2`. El resultado es siempre no negativo, el símbolo de `num2` es ignorado.

## Parámetros

`num1`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`num2`  
El modulo que es evaluado.

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

Un objeto `GMP`.

## Ejemplos

Ejemplo de `gmp_mod`

```
<?php
$mod = gmp_mod("8", "3");
echo gmp_strval($mod) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    2
