---
title: sqrt
description: Raíz cuadrada
source_url: https://www.php.net/manual/es/function.sqrt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/sqrt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: false
translation_revision: 761d72245
order: 44880
---

sqrt

Raíz cuadrada

## Descripción

```php
sqrt(float $num): float
```php

Devuelve la raíz cuadrada de `num`.

## Parámetros

`num`  
El argumento a tratar

## Valores devueltos

La raíz cuadrada de `num` o el valor especial `NAN` para los números negativos.

## Ejemplos

Ejemplo con `sqrt`

```
<?php
// La precisión depende de su directiva precision
echo sqrt(9), PHP_EOL; // 3
echo sqrt(10), PHP_EOL; // 3.16227766 ...
?>

    
```php

## Véase también

`pow`, `M_SQRTPI` - `sqrt(pi)`, `M_2_SQRTPI` - `2/sqrt(pi)`, `M_SQRT2` - `sqrt(2)`, `M_SQRT3` - `sqrt(3)`, `M_SQRT1_2` - `1/sqrt(2)`
