---
title: gmp_add
description: Adición de 2 números GMP
source_url: https://www.php.net/manual/es/function.gmp-add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 28360
---

gmp_add

Adición de 2 números GMP

## Descripción

```php
gmp_add(GMP $num1, GMP $num2): GMP
```php

Adición de 2 números GMP.

## Parámetros

`num1`  
El primer operando (augend).

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`num2`  
El segundo operando (augend).

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

Un número GMP que representa la suma de los argumentos.

## Ejemplos

Ejemplo con `gmp_add`

```
<?php
$sum = gmp_add("123456789012345", "76543210987655");
echo gmp_strval($sum) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    200000000000000
