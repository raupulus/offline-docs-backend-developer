---
title: DOMElement::setIdAttributeNS
description: Declara el atributo especificado por su nombre local y su URI del espacio
  de nombres como de tipo ID
source_url: https://www.php.net/manual/es/domelement.setidattributens.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement/setidattributens.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 7d5c74c9a
order: 13680
---

DOMElement::setIdAttributeNS

Declara el atributo especificado por su nombre local y su URI del espacio de nombres como de tipo ID

## Descripción

```php
public DOMElement::setIdAttributeNS(string $namespace, string $qualifiedName, bool $isId): void
```php

Declara el atributo especificado por `qualifiedName` y `namespaceURI` como de tipo ID.

## Parámetros

`namespaceURI`  
La URI del espacio de nombres del atributo.

`qualifiedName`  
El nombre local del atributo, como `prefijo:nombre_etiqueta`.

`isId`  
Establecer a `true` si se quiere que `name` sea de tipo ID, `false` si no.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Puede lanzar una DOMException con los siguientes códigos de error:

`DOM_NO_MODIFICATION_ALLOWED_ERR`  
Lanzado si el nodo es de sólo lectura.

`DOM_NOT_FOUND_ERR`  
Lanzado si `name` no es un atributo de este elemento.

## Véase también

DOMDocument::getElementById, DOMElement::setIdAttribute, DOMElement::setIdAttributeNode
