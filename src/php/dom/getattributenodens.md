---
title: DOMElement::getAttributeNodeNS
description: Devuelve el nodo de un atributo
source_url: https://www.php.net/manual/es/domelement.getattributenodens.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement/getattributenodens.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_revision: 4f5e2b225
order: 13470
---

DOMElement::getAttributeNodeNS

Devuelve el nodo de un atributo

## Descripción

```php
public DOMElement::getAttributeNodeNS(string $namespace, string $localName): DOMAttr
```php

Devuelve el nodo del atributo en el espacio de nombres `namespace` con el nombre local `localName` para el nodo actual.

## Parámetros

`namespace`  
La URI del espacio de nombres.

`localName`  
El nombre local.

## Valores devueltos

El nodo de atributos. Observe que para los atributos de las declaraciones del espacio de nombres XML (`xmlns` y `xmlns:*`) una instancia de `DOMNameSpaceNode` es devuelta en vez de una instancia de `DOMAttr`.

## Véase también

DOMElement::hasAttributeNS, DOMElement::setAttributeNodeNS, DOMElement::removeAttributeNode
