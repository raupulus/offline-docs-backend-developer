---
title: gmp_intval
description: Convertir un número GMP a entero
source_url: https://www.php.net/manual/es/function.gmp-intval.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-intval.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28540
---

gmp_intval

Convertir un número GMP a entero

## Descripción

```php
gmp_intval(GMP $num): int
```php

Esta función convierte un número GMP an un `int` nativo de PHP.

## Parámetros

`num`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

El valor `int` de `num`.

## Ejemplos

Ejemplo de `gmp_intval`

```
<?php
// muestra el valor correcto
echo gmp_intval("2147483647") . "\n";

//muestra el valor correcto
echo gmp_intval("2147483648") . "\n";

// muestra el valor correcto
echo gmp_strval("2147483648") . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    2147483647
    2147483647
    2147483648

## Notas

> [!WARNING]
> Ésta función retorna un resultado satisfactorio solo si el numero actualmente encaja con el PHP entero (ej., símbolo de tipo largo). Para imprimir simplemente el número GMP, use `gmp_strval`.
