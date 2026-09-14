---
title: deg2rad
description: Convierte un número de grados en radianes
source_url: https://www.php.net/manual/es/function.deg2rad.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/deg2rad.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: false
translation_revision: 761d72245
order: 44630
---

deg2rad

Convierte un número de grados en radianes

## Descripción

```php
deg2rad(float $num): float
```php

`deg2rad` convierte `num` de grados a radianes.

## Parámetros

`num`  
El ángulo, en grados

## Valores devueltos

El equivalente, en radianes, de `num`.

## Ejemplos

Ejemplo con `deg2rad`

```
<?php

echo deg2rad(45), PHP_EOL; // 0.785398163397
var_dump(deg2rad(45) === M_PI_4); // bool(true)

?>

    
```php

## Véase también

`rad2deg`
