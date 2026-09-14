---
title: decoct
description: Convierte de decimal a octal
source_url: https://www.php.net/manual/es/function.decoct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/decoct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: false
translation_revision: 0c9c2dd66
order: 44620
---

decoct

Convierte de decimal a octal

## Descripción

```php
decoct(int $num): string
```php

Devuelve una cadena que contiene la representación octal del número dado `num`. El número más grande que puede ser convertido es `4294967295` en decimal, lo que dará `37777777777`. Para las plataformas de 64 bits, se trata generalmente de `9223372036854775807` en decimal resultando en `777777777777777777777`.

## Parámetros

`num`  
Valor decimal a convertir

## Valores devueltos

Una representación octal de `num`.

## Ejemplos

Ejemplo con `decoct`

```
<?php
echo decoct(15) . "\n";
echo decoct(264);
?>

    
```php

El ejemplo anterior mostrará:

    17
    410

## Véase también

`octdec`, `decbin`, `dechex`, `base_convert`
