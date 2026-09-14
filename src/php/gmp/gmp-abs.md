---
title: gmp_abs
description: Valor absoluto
source_url: https://www.php.net/manual/es/function.gmp-abs.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-abs.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28350
---

gmp_abs

Valor absoluto

## Descripción

```php
gmp_abs(GMP $num): GMP
```php

Obtiene el valor absoluto de un número.

## Parámetros

`num`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

Devuelve el valor absoluto `num`, como un número GMP.

## Ejemplos

Ejemplo de `gmp_abs`

```
<?php
$abs1 = gmp_abs("274982683358");
$abs2 = gmp_abs("-274982683358");

echo gmp_strval($abs1) . "\n";
echo gmp_strval($abs2) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    274982683358
    274982683358
