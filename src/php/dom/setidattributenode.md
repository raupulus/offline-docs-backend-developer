---
title: DOMElement::setIdAttributeNode
description: Declara el atributo especificado por el nodo como de tipo ID
source_url: https://www.php.net/manual/es/domelement.setidattributenode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement/setidattributenode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: 7d5c74c9a
order: 13670
---

DOMElement::setIdAttributeNode

Declara el atributo especificado por el nodo como de tipo ID

## Descripción

```php
public DOMElement::setIdAttributeNode(DOMAttr $attr, bool $isId): void
```php

Declara el atributo especificado por `attr` como de tipo ID.

## Parámetros

`attr`  
El atributo del nodo.

`isId`  
Definir como `true` si se desea que `name` sea de tipo ID, `false` en caso contrario.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Puede lanzar una DOMException con los siguientes códigos de error:

`DOM_NO_MODIFICATION_ALLOWED_ERR`  
Enviado si el nodo es de solo lectura.

`DOM_NOT_FOUND_ERR`  
Enviado si `name` no es un atributo de este elemento.

## Véase también

DOMDocument::getElementById, DOMElement::setIdAttribute, DOMElement::setIdAttributeNS
