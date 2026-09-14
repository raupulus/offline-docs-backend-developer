---
title: DOMNode::cloneNode
description: Clona un nodo
source_url: https://www.php.net/manual/es/domnode.clonenode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domnode/clonenode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 4f5e2b225
order: 13920
---

DOMNode::cloneNode

Clona un nodo

## Descripción

```php
public DOMNode::cloneNode([bool $deep]): DOMNode
```php

Crea una copia del nodo.

## Parámetros

`deep`  
Indica si copiar todos los nodos descendientes. Este parámetro es `false` de manera predeterminada.

## Valores devueltos

El nodo clonado.
