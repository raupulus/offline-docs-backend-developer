---
title: DOMElement::setAttributeNode
description: Añade un nuevo atributo al elemento
source_url: https://www.php.net/manual/es/domelement.setattributenode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement/setattributenode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: 7d5c74c9a
order: 13630
---

DOMElement::setAttributeNode

Añade un nuevo atributo al elemento

## Descripción

```php
public DOMElement::setAttributeNode(DOMAttr $attr): DOMAttr
```php

Añade un nuevo atributo `attr` al elemento. Si ya existe un atributo con el mismo nombre en el elemento, este atributo es reemplazado por `attr`.

## Parámetros

`attr`  
El atributo.

## Valores devueltos

Devuelve el atributo antiguo si ha sido reemplazado o `null` si no había un atributo antiguo. Si se produce un error `DOM_WRONG_DOCUMENT_ERR` y `strictErrorChecking` es `false`, entonces `false` es devuelto.

## Errores/Excepciones

Puede lanzar una DOMException con los siguientes códigos de error:

`DOM_WRONG_DOCUMENT_ERR`  
Lanzado si `attr` pertenece a un documento diferente al del elemento.

## Véase también

DOMElement::hasAttribute, DOMElement::getAttributeNode, DOMElement::removeAttributeNode
