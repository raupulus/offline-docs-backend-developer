---
title: rad2deg
description: Conversión de radianes a grados
source_url: https://www.php.net/manual/es/function.rad2deg.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/rad2deg.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: false
translation_revision: 0c9c2dd66
order: 44840
---

rad2deg

Conversión de radianes a grados

## Descripción

```php
rad2deg(float $num): float
```php

Convierte `num` (supuesto en radianes) a grados.

## Parámetros

`num`  
Un valor, en radianes

## Valores devueltos

El equivalente de `num`, en grados.

## Ejemplos

Ejemplo con `rad2deg`

```
<?php

echo rad2deg(M_PI_4); // 45

?>

    
```php

## Véase también

`deg2rad`
