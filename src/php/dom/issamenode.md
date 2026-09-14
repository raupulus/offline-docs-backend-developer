---
title: DOMNode::isSameNode
description: Indica si dos nodos son el mismo nodo
source_url: https://www.php.net/manual/es/domnode.issamenode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domnode/issamenode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 4f5e2b225
order: 14030
---

DOMNode::isSameNode

Indica si dos nodos son el mismo nodo

## Descripción

```php
public DOMNode::isSameNode(DOMNode $otherNode): bool
```php

Esta función indica si dos nodos son el mismo nodo. La comparación *no* está basada en el contenido

## Parámetros

`otherNode`  
El nodo comparado.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
