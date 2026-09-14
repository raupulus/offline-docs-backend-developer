---
title: gmp_nextprime
description: Encuentra el siguiente número primo
source_url: https://www.php.net/manual/es/function.gmp-nextprime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-nextprime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28630
---

gmp_nextprime

Encuentra el siguiente número primo

## Descripción

```php
gmp_nextprime(GMP $num): GMP
```php

Encuentra el siguiente número primo

## Parámetros

`num`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

Devuelve el siguiente número primo o mayor `num`, como un número GMP.

## Ejemplos

Ejemplo de `gmp_nextprime`

```
<?php
$prime1 = gmp_nextprime(10); // el siguiente número primo o superior que 10
$prime2 = gmp_nextprime(-1000); // el siguiente número primo o superior que -1000

echo gmp_strval($prime1) . "\n";
echo gmp_strval($prime2) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    11
    2

## Notas

> [!NOTE]
> Ésta función usa un algoritmo probabilístico para identificar el número primo y posibilita la obtención de un número compuesto que sea extremadamente pequeño.
