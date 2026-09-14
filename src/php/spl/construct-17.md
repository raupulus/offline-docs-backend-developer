---
title: RecursiveCallbackFilterIterator::__construct
description: Crea un objeto RecursiveCallbackFilterIterator a partir de una interfaz
  RecursiveIterator
source_url: https://www.php.net/manual/es/recursivecallbackfilteriterator.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/recursivecallbackfilteriterator/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 83020
---

RecursiveCallbackFilterIterator::\_\_construct

Crea un objeto RecursiveCallbackFilterIterator a partir de una interfaz RecursiveIterator

## Descripción

```php
public RecursiveCallbackFilterIterator::__construct(RecursiveIterator $iterator, callable $callback)
```php

Crea un iterador filtrado a partir de una interfaz RecursiveIterator utilizando la función de devolución de llamada `callback` para determinar los elementos aceptados o rechazados.

## Parámetros

`iterator`  
El iterador recursivo a filtrar.

`callback`  
La función de devolución de llamada, que debe devolver `true` para aceptar el elemento actual, `false` en caso contrario. Véase también los [ejemplos](#recursivecallbackfilteriterator.examples).

Puede ser cualquier valor de tipo `callable`.

## Véase también

[Ejemplos RecursiveCallbackFilterIterator](#recursivecallbackfilteriterator.examples), RecursiveCallbackFilterIterator::getChildren, RecursiveCallbackFilterIterator::hasChildren
