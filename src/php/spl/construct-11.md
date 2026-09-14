---
title: IteratorIterator::__construct
description: Crea un iterador a partir de un objeto traversable
source_url: https://www.php.net/manual/es/iteratoriterator.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/iteratoriterator/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: ff4e9f776
order: 82420
---

IteratorIterator::\_\_construct

Crea un iterador a partir de un objeto traversable

## Descripción

```php
public IteratorIterator::__construct(Traversable $iterator, [string $class])
```php

Crea un iterador a partir de un objeto traversable.

## Parámetros

`iterator`  
El iterador traversable.

`class`  
El nombre de clase a utilizar para el iterador interno. Esto permite especificar una clase de iterador diferente para envolver el iterador proporcionado. Por omisión, la clase `IteratorIterator` misma será utilizada.

## Véase también

`Traversable`
