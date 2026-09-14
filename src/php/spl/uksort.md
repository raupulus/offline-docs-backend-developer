---
title: ArrayIterator::uksort
description: Ordenar por claves utilizando una función de comparación definida por
  el usuario
source_url: https://www.php.net/manual/es/arrayiterator.uksort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayiterator/uksort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 56b048277
order: 81310
---

ArrayIterator::uksort

Ordenar por claves utilizando una función de comparación definida por el usuario

## Descripción

```php
public ArrayIterator::uksort(callable $callback): true
```php

Este método ordena los elementos por claves utilizando una función de comparación proporcionada por el usuario.

> [!NOTE]
> Si dos miembros se comparan como iguales, mantienen su orden original. Anterior a PHP 8.0.0, su orden relativo en el array ordenado no está definido.

## Parámetros

`callback`  
La función de comparación debe retornar un entero menor que, igual a, o mayor que 0 si el primer argumento es considerado, respectivamente, menor que, igual a, o mayor que el segundo.

```php
callback(mixed $a, mixed $b): int
```

> [!CAUTION]
> Devolver valores *no enteros* (como `float`) desde la función de comparación resultará en una conversión interna del valor de retorno de la retrollamada a `int`. Así, valores como `0.99` y `0.1` serán convertidos ambos al valor entero `0`, por lo que se compararán como iguales.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción                                                   |
|---------|---------------------------------------------------------------|
| 8.2.0   | El tipo de retorno es ahora `true`, anteriormente era `bool`. |

## Véase también

ArrayIterator::asort, ArrayIterator::ksort, ArrayIterator::natcasesort, ArrayIterator::natsort, ArrayIterator::uasort, `uksort`
