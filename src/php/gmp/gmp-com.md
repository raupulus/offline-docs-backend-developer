---
title: gmp_com
description: Calcula uno de los complementos
source_url: https://www.php.net/manual/es/function.gmp-com.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-com.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28410
---

gmp_com

Calcula uno de los complementos

## Descripción

```php
gmp_com(GMP $num): GMP
```php

Devuelve uno de los complementos de `num`.

## Parámetros

`num`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

Devuelve uno de los complementos de `num`, como un número GMP.

## Ejemplos

Ejemplo de `gmp_com`

```
<?php
$com = gmp_com("1234");
echo gmp_strval($com) . "\n";
?>

   
```php

El ejemplo anterior mostrará:

    -1235
