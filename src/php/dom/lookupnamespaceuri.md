---
title: DOMNode::lookupNamespaceURI
description: Obtiene la URI del espacio de nombres del nodo basado en el prefijo
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domnode/lookupnamespaceuri.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: b3ea8eaa2
order: 14050
---

DOMNode::lookupNamespaceURI

Obtiene la URI del espacio de nombres del nodo basado en el prefijo

## Descripción

```php
public DOMNode::lookupNamespaceURI(string $prefix): string
```php

Obtiene la URI del espacio de nombres del nodo basado en `prefix`.

## Parámetros

`prefix`  
El prefijo a buscar. Si este parámetro es `null`, el método devolverá el URI del espacio de nombres por defecto, si existe.

## Valores devueltos

Devuelve el URI del espacio de nombres asociado o `null` si no se encuentra ninguno.

## Véase también

DOMNode::lookupPrefix
