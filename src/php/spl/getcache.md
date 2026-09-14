---
title: CachingIterator::getCache
description: Recuperar el contenido de la caché
source_url: https://www.php.net/manual/es/cachingiterator.getcache.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/cachingiterator/getcache.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: d51166ca1
order: 81630
---

CachingIterator::getCache

Recuperar el contenido de la caché

## Descripción

```php
public CachingIterator::getCache(): array
```php

Recupera el contenido de la caché.

> [!NOTE]
> Se debe utilizar el indicador `CachingIterator::FULL_CACHE`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un `array` que contiene los elementos de la caché.

## Errores/Excepciones

Lanza una `BadMethodCallException` cuando no se está utilizando el indicador `CachingIterator::FULL_CACHE`.

## Ejemplos

Ejemplo de CachingIterator::getCache.

```
<?php
$iterador = new ArrayIterator(array(1, 2, 3));
$caché    = new CachingIterator($iterador, CachingIterator::FULL_CACHE);

$caché->next();
$caché->next();
var_dump($caché->getCache());

$caché->next();
var_dump($caché->getCache());
?>

    
```php

El ejemplo anterior mostrará:

    array(2) {
      [0]=>
      int(1)
      [1]=>
      int(2)
    }
    array(3) {
      [0]=>
      int(1)
      [1]=>
      int(2)
      [2]=>
      int(3)
    }
