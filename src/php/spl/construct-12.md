---
title: LimitIterator::__construct
description: Construye un nuevo objeto LimitIterator
source_url: https://www.php.net/manual/es/limititerator.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/limititerator/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 82520
---

LimitIterator::\_\_construct

Construye un nuevo objeto LimitIterator

## Descripción

```php
public LimitIterator::__construct(Iterator $iterator, [int $offset], [int $limit])
```php

Construye un nuevo objeto `LimitIterator` desde `iterator` con un `offset` y un límite máximo `limit`

## Parámetros

`iterator`  
El `Iterator` a limitar.

`offset`  
Posición opcional del límite.

`limit`  
Número opcional del límite.

## Errores/Excepciones

Lanza una `ValueError` si `offset` es inferior a `0` o si `limit` es inferior a `-1`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Ahora lanza una excepción `ValueError` cuando `offset` es inferior a `0` ; Anteriormente, se lanzaba una `RuntimeException`. |
| 8.0.0 | Ahora lanza una excepción `ValueError` cuando `limit` es inferior a `-1` ; Anteriormente, se lanzaba una `RuntimeException`. |

## Ejemplos

Ejemplo `LimitIterator::__construct`

```
<?php
$ait = new ArrayIterator(array('a', 'b', 'c', 'd', 'e'));
$lit = new LimitIterator($ait, 1, 3);
foreach ($lit as $value) {
    echo $value . "\n";
}
?>

    
```php

El ejemplo anterior mostrará:

    b
    c
    d

## Véase también

[Ejemplos LimitIterator](#limititerator.examples)
