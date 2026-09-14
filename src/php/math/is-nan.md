---
title: is_nan
description: Verifica si un número flotante es NAN
source_url: https://www.php.net/manual/es/function.is-nan.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/is-nan.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: false
translation_revision: 61374bbe2
order: 44750
---

is_nan

Verifica si un número flotante es NAN

## Descripción

```php
is_nan(float $num): bool
```php

Devuelve si el `num` dado es `NAN` (“Not A Number”).

`NAN` es devuelto por las operaciones matemáticas que no están definidas, por ejemplo al pasar argumentos fuera del dominio de entrada de la función. La raíz cuadrada (`sqrt`) solo está definida para números positivos, el paso de un número negativo resultará en un `NAN`. Otros ejemplos de operaciones que devuelven `NAN` son la división de `INF` por `INF` y cualquier operación que involucre un valor `NAN` existente.

> [!NOTE]
> A pesar de su nombre “Not A Number”, `NAN` es un valor válido de tipo `float`.

> [!CAUTION]
> `NAN` no se compara igual a `NAN`. Para verificar si un número flotante es `NAN`, `is_nan` debe ser utilizado. La verificación de `$float === NAN` no funcionará.

## Parámetros

`num`  
El `float` a verificar

## Valores devueltos

`true` si `num` es `NAN`, de lo contrario `false`.

## Ejemplos

Ejemplo con `is_nan`

```
<?php
$nan = sqrt(-1);

var_dump($nan, is_nan($nan));
?>

    
```php

El ejemplo anterior mostrará:

    float(NAN)
    bool(true)

## Véase también

`is_finite`, `is_infinite`
