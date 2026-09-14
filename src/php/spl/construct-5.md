---
title: CallbackFilterIterator::__construct
description: Crear un iterador filtrado desde otro iterador
source_url: https://www.php.net/manual/es/callbackfilteriterator.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/callbackfilteriterator/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: d51166ca1
order: 81780
---

CallbackFilterIterator::\_\_construct

Crear un iterador filtrado desde otro iterador

## Descripción

```php
public CallbackFilterIterator::__construct(Iterator $iterator, callable $callback)
```php

Crea un iterador filtrado usando `callback` (llamada de retorno) para determinar qué elementos van a ser aceptados o rechazados.

## Parámetros

`iterator`  
El iterador a ser filtrado.

`callback`  
La llamada de retorno, debe devolver `true` para aceptar el elemento actual o en caso contrario `false`. Véase los [Ejemplos](#callbackfilteriterator.examples).

Puede ser cualquier valor válido de `callback`.

## Véase también

[Ejemplos de CallbackFilterIterator](#callbackfilteriterator.examples), CallbackFilterIterator::accept
