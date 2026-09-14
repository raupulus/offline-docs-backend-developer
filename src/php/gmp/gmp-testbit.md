---
title: gmp_testbit
description: Prueba si un bit está definido
source_url: https://www.php.net/manual/es/function.gmp-testbit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-testbit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_reviewed: false
translation_revision: 574a644f1
order: 28850
---

gmp_testbit

Prueba si un bit está definido

## Descripción

```php
gmp_testbit(GMP $num, int $index): bool
```php

Prueba si un bit está definido.

## Parámetros

`num`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`index`  
El bit a probar

## Valores devueltos

Devuelve `true` si el bit está definido en el recurso `num`, `false` en caso contrario.

## Errores/Excepciones

Se emite una advertencia de nivel `E_WARNING` cuando el argumento `index` es menor que `0` ; `false` será devuelto en este caso.

## Ejemplos

Ejemplo con `gmp_testbit`

```
<?php
$n = gmp_init("1000000");
var_dump(gmp_testbit($n, 1));
gmp_setbit($n, 1);
var_dump(gmp_testbit($n, 1));
?>

    
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(true)

## Véase también

`gmp_setbit`, `gmp_clrbit`
