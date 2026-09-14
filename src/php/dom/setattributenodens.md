---
title: DOMElement::setAttributeNodeNS
description: Añade un nuevo atributo al elemento
source_url: https://www.php.net/manual/es/domelement.setattributenodens.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement/setattributenodens.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: 7d5c74c9a
order: 13640
---

DOMElement::setAttributeNodeNS

Añade un nuevo atributo al elemento

## Descripción

```php
public DOMElement::setAttributeNodeNS(DOMAttr $attr): DOMAttr
```php

Añade un nuevo atributo `attr` al elemento, teniendo en cuenta el espacio de nombres (namespace): Si ya existe un atributo con el mismo nombre en el elemento, este atributo es reemplazado por `attr`.

## Parámetros

`attr`  
El nombre del atributo.

## Valores devueltos

Devuelve el antiguo atributo si ha sido reemplazado o `null` si no había un atributo anterior. Si se produce un error `DOM_WRONG_DOCUMENT_ERR` y `strictErrorChecking` es `false`, entonces se devuelve `false`.

## Errores/Excepciones

Puede lanzar una DOMException con los siguientes códigos de error:

`DOM_WRONG_DOCUMENT_ERR`  
Se lanza si `attr` pertenece a un documento diferente al del elemento.

## Véase también

DOMElement::hasAttributeNS, DOMElement::getAttributeNodeNS, DOMElement::removeAttributeNode
