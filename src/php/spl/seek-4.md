---
title: SeekableIterator::seek
description: Busca una posición
source_url: https://www.php.net/manual/es/seekableiterator.seek.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/seekableiterator/seek.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: 434557c58
order: 83750
---

SeekableIterator::seek

Busca una posición

## Descripción

```php
public SeekableIterator::seek(int $offset): void
```php

Busca la posición dada en el iterador.

## Parámetros

`offset`  
La posición a alcanzar.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

La implementación debe emitir una excepción `OutOfBoundsException` si la posición `offset` no es alcanzable.

## Ejemplos

Ejemplo con SeekableIterator::seek

Mueve el iterador a la posición 3 (`ArrayIterator` implementa `SeekableIterator`).

```
<?php
$array = array("apple", "banana", "cherry", "damson", "elderberry");
$iterator = new ArrayIterator($array);
$iterator->seek(3);
echo $iterator->current();
?>

    
```php

Resultado del ejemplo anterior es similar a:

    damson

## Véase también

`SeekableIterator`, `Iterator`
