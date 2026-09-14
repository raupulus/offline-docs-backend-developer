---
title: is_countable
description: Verifica si el contenido de la variable es un valor contable
source_url: https://www.php.net/manual/es/function.is-countable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/is-countable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: true
translation_revision: d816a0fad
order: 100580
---

is_countable

Verifica si el contenido de la variable es un valor contable

## Descripción

```php
is_countable(mixed $value): bool
```php

Verifica si el contenido de la variable es un array `array` o un objeto que implementa `Countable`

## Parámetros

`value`  
La variable a verificar

## Valores devueltos

Retorna `true` si `value` es contable, `false` en caso contrario.

## Historial de cambios

| Versión | Descripción                 |
|---------|-----------------------------|
| 7.3.0   | `is_countable` fue añadido. |

## Ejemplos

Ejemplos con `is_countable`

```
<?php
var_dump(is_countable([1, 2, 3])); // bool(true)
var_dump(is_countable(new ArrayIterator(['foo', 'bar', 'baz']))); // bool(true)
var_dump(is_countable(new ArrayIterator())); // bool(true)
var_dump(is_countable(new stdClass())); // bool(false)
?>

    
```php

## Véase también

`is_array`, `is_object`, `is_iterable`, `is_bool`
