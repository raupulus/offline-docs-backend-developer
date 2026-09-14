---
title: is_iterable
description: Determina si el contenido de la variable es iterable.
source_url: https://www.php.net/manual/es/function.is-iterable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/is-iterable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: true
translation_revision: 0c9c2dd66
order: 100630
---

is_iterable

Determina si el contenido de la variable es iterable.

## Descripción

```php
is_iterable(mixed $value): bool
```php

Verifica que el contenido de la variable es aceptado por el pseudo-tipo `iterable`, es decir, que se trata de un `array` o un objeto que implementa la interfaz `Traversable`.

## Parámetros

`value`  
El valor a verificar.

## Valores devueltos

Retorna `true` si `value` es iterable, `false` en caso contrario.

## Ejemplos

Ejemplos con `is_iterable`

```
<?php

var_dump(is_iterable([1, 2, 3]));  // bool(true)
var_dump(is_iterable(new ArrayIterator([1, 2, 3])));  // bool(true)
var_dump(is_iterable((function () { yield 1; })()));  // bool(true)
var_dump(is_iterable(1));  // bool(false)
var_dump(is_iterable(new stdClass()));  // bool(false)

?>

    
```php

## Véase también

`is_array`
