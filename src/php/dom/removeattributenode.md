---
title: DOMElement::removeAttributeNode
description: Elimina un atributo
source_url: https://www.php.net/manual/es/domelement.removeattributenode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement/removeattributenode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 7d5c74c9a
order: 13580
---

DOMElement::removeAttributeNode

Elimina un atributo

## Descripción

```php
public DOMElement::removeAttributeNode(DOMAttr $attr): DOMAttr
```php

Elimina el atributo `attr` del elemento.

## Parámetros

`attr`  
El nodo atributo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Puede lanzar una DOMException con los siguientes códigos de error:

`DOM_NO_MODIFICATION_ALLOWED_ERR`  
Lanzado si el nodo es de sólo lectura.

`DOM_NOT_FOUND_ERR`  
Lanzado si `attr` no es un atributo del elemento.

## Véase también

DOMElement::hasAttribute, DOMElement::getAttributeNode, DOMElement::setAttributeNode
