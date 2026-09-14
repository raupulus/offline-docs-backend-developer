---
title: gmp_neg
description: Número negativo
source_url: https://www.php.net/manual/es/function.gmp-neg.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-neg.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28620
---

gmp_neg

Número negativo

## Descripción

```php
gmp_neg(GMP $num): GMP
```php

Devuelve el valor negativo de un número.

## Parámetros

`num`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

Devuelve -`num`, como un número GMP.

## Ejemplos

Ejemplo de`gmp_neg`

```
<?php
$neg1 = gmp_neg("1");
echo gmp_strval($neg1) . "\n";
$neg2 = gmp_neg("-1");
echo gmp_strval($neg2) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    -1
    1
