---
title: gmp_strval
description: Convierte un número GMP en string
source_url: https://www.php.net/manual/es/function.gmp-strval.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-strval.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_reviewed: false
translation_revision: 43130349a
order: 28830
---

gmp_strval

Convierte un número GMP en string

## Descripción

```php
gmp_strval(GMP $num, [int $base]): string
```php

Convierte un número GMP en string, en la base `base`. La base por omisión es 10.

## Parámetros

`num`  
El número GMP que debe ser convertido.

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`base`  
La base del número devuelto. Por omisión, vale 10. Los valores posibles van de 2 a 62 y de -2 a -36.

## Valores devueltos

El número, en forma de `string`.

## Ejemplos

Convertir un número GMP en `string`

```
<?php
$a = gmp_init("0x41682179fbf5");
printf("Decimal : %s, 36-based : %s", gmp_strval($a), gmp_strval($a,36));
?>

    
```php
