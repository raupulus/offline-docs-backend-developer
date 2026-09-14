---
title: DOMNode::lookupPrefix
description: Devuelve el prefijo del espacio de nombres según el URI del espacio de
  nombres
source_url: https://www.php.net/manual/es/domnode.lookupprefix.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domnode/lookupprefix.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: 7a4c5cb11
order: 14060
---

DOMNode::lookupPrefix

Devuelve el prefijo del espacio de nombres según el URI del espacio de nombres

## Descripción

```php
public DOMNode::lookupPrefix(string $namespace): string
```php

Devuelve el prefijo del espacio del nodo según el URI del espacio de nombres.

## Parámetros

`namespace`  
El URI del espacio de nombres.

## Valores devueltos

El prefijo del espacio de nombres o `null` en caso de error.

## Véase también

DOMNode::lookupNamespaceUri
