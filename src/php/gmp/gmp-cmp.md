---
title: gmp_cmp
description: Compara los números
source_url: https://www.php.net/manual/es/function.gmp-cmp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-cmp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28400
---

gmp_cmp

Compara los números

## Descripción

```php
gmp_cmp(GMP $num1, GMP $num2): int
```php

Compara dos números.

## Parámetros

`num1`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`num2`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

Devuelve un valor positivo si `a > b`, el cero si `a = b` y el valor negativo de a si `a < b`.

## Ejemplos

Ejemplo de `gmp_cmp`

```
<?php
$cmp1 = gmp_cmp("1234", "1000"); // mayor que
$cmp2 = gmp_cmp("1000", "1234"); // menor que
$cmp3 = gmp_cmp("1234", "1234"); // igual a

echo "$cmp1 $cmp2 $cmp3\n";
?>

   
```php

El ejemplo anterior mostrará:

    1 -1 0
