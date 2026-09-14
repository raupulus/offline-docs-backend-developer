---
title: DOMNode::insertBefore
description: Añade un nuevo hijo antes de un nodo de referencia.
source_url: https://www.php.net/manual/es/domnode.insertbefore.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domnode/insertbefore.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: 7d5c74c9a
order: 14000
---

DOMNode::insertBefore

Añade un nuevo hijo antes de un nodo de referencia.

## Descripción

```php
public DOMNode::insertBefore(DOMNode $node, [DOMNode $child]): DOMNode
```php

Esta función inserta un nuevo nodo justo antes del nodo de referencia. Si se planea realizar modificaciones posteriores en el hijo añadido, debe utilizarse el nodo devuelto.

Al utilizar un nodo existente, este será movido.

## Parámetros

`node`  
El nuevo nodo.

`child`  
El nodo referenciado. Si no se especifica, `node` será añadido a los hijos.

## Valores devueltos

El nodo insertado o `false` en caso de error.

## Errores/Excepciones

Puede lanzar una DOMException con los siguientes códigos de error:

`DOM_NO_MODIFICATION_ALLOWED_ERR`  
Lanzado si el nodo es de solo lectura o si el padre anterior al nodo a insertar es de solo lectura.

`DOM_HIERARCHY_REQUEST_ERR`  
Lanzado si este nodo es de un tipo que no permite hijos del tipo del nodo `node`, o si el nodo a añadir es uno de los ancestros de este nodo o este nodo mismo.

`DOM_WRONG_DOCUMENT_ERR`  
Lanzado si `node` ha sido creado desde un documento diferente al que ha creado este nodo.

`DOM_NOT_FOUND_ERR`  
Lanzado si `child` no es un hijo de este nodo.

## Véase también

DOMNode::appendChild
