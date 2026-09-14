---
title: gmp_sub
description: Resta los números
source_url: https://www.php.net/manual/es/function.gmp-sub.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-sub.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28840
---

gmp_sub

Resta los números

## Descripción

```php
gmp_sub(GMP $num1, GMP $num2): GMP
```php

Resta `num2` con `num1` y devuelve el resultado.

## Parámetros

`num1`  
El número a ser restado.

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`num2`  
El número restado con `num1`.

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

Un objeto `GMP`.

## Ejemplos

Ejemplo de `gmp_sub`

```
<?php
$sub = gmp_sub("281474976710656", "4294967296"); // 2^48 - 2^32
echo gmp_strval($sub) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    281470681743360
