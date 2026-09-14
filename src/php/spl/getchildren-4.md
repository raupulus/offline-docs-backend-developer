---
title: RecursiveCallbackFilterIterator::getChildren
description: Devuelve el iterador hijo interno contenido en un RecursiveCallbackFilterIterator
source_url: https://www.php.net/manual/es/recursivecallbackfilteriterator.getchildren.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/recursivecallbackfilteriterator/getchildren.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 83030
---

RecursiveCallbackFilterIterator::getChildren

Devuelve el iterador hijo interno contenido en un RecursiveCallbackFilterIterator

## Descripción

```php
public RecursiveCallbackFilterIterator::getChildren(): RecursiveCallbackFilterIterator
```php

Obtiene el hijo filtrado del iterador interno.

RecursiveCallbackFilterIterator::hasChildren debe ser utilizado para determinar si existen hijos que puedan ser recuperados.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `RecursiveCallbackFilterIterator` que contiene el hijo.

## Véase también

[Ejemplos con RecursiveCallbackFilterIterator](#recursivecallbackfilteriterator.examples), RecursiveCallbackFilterIterator::\_\_construct, RecursiveCallbackFilterIterator::hasChildren
