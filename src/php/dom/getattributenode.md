---
title: DOMElement::getAttributeNode
description: Devuelve el nodo de un atributo
source_url: https://www.php.net/manual/es/domelement.getattributenode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement/getattributenode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_revision: 4f5e2b225
order: 13460
---

DOMElement::getAttributeNode

Devuelve el nodo de un atributo

## Descripción

```php
public DOMElement::getAttributeNode(string $qualifiedName): DOMAttr
```php

Devuelve el nodo del atributo con nombre `qualifiedName` para el elemento actual.

## Parámetros

`qualifiedName`  
El nombre del atributo.

## Valores devueltos

El nodo de atributos. Observe que para los atributos de las declaraciones del espacio de nombres XML (`xmlns` y `xmlns:*`) una instancia de `DOMNameSpaceNode` es devuelta en vez de una instancia de `DOMAttr`.

## Véase también

DOMElement::hasAttribute, DOMElement::setAttributeNode, DOMElement::removeAttributeNode
