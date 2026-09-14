---
title: DOMText::splitText
description: Rompe este nodo en dos nodos en el índice especificado
source_url: https://www.php.net/manual/es/domtext.splittext.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domtext/splittext.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 4f5e2b225
order: 14270
---

DOMText::splitText

Rompe este nodo en dos nodos en el índice especificado

## Descripción

```php
public DOMText::splitText(int $offset): DOMText
```php

Rompe este nodo en dos nodos en el índice especificado por `offset`, manteniéndolos en el árbol como hermanos.

Después de la separación, este nodo contendrá todos el contenido hata `offset`. Si el nodo original tenía un nodo padre, el nuevo nodo se inserta como el hermano siguiente del nodo original. Cuando `offset` es igual a la longitud de este nodo, el nuevo nodo no tendrá información.

## Parámetros

`offset`  
El índice en el que se hace la separación, comenzando en 0.

## Valores devueltos

El nuevo nodo del mismo tipo, que contiene todo el contenido desde y después de `offset`.
