---
title: RecursiveCachingIterator::__construct
description: Constructor
source_url: https://www.php.net/manual/es/recursivecachingiterator.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/recursivecachingiterator/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: c142be811
order: 82980
---

RecursiveCachingIterator::\_\_construct

Constructor

## Descripción

```php
public RecursiveCachingIterator::__construct(Iterator $iterator, [int $flags])
```php

Construye un nuevo objeto `RecursiveCachingIterator`, que posteriormente podrá ser pasado como iterador.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`iterator`  
El iterador a utilizar.

`flags`  
El flag. Utilice la constante `CALL_TOSTRING` para llamar a RecursiveCachingIterator::\_\_toString sobre todos los elementos (por omisión), y/o la constante `CATCH_GET_CHILD` para atrapar todas las excepciones emitidas al intentar recuperar hijos.

## Véase también

CachingIterator::\_\_construct
