---
title: La clase DOMNameSpaceNode
source_url: https://www.php.net/manual/es/class.domnamespacenode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domnamespacenode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: d75a54118
order: 13880
---

## Sinopsis de la clase

DOMNameSpaceNode

Propiedades

public

readonly

string

nodeName

public

readonly

string

null

nodeValue

public

readonly

int

nodeType

public

readonly

string

prefix

public

readonly

string

null

localName

public

readonly

string

null

namespaceURI

public

readonly

bool

isConnected

public

readonly

DOMDocument

null

ownerDocument

public

readonly

DOMNode

null

parentNode

public

readonly

DOMElement

null

parentElement

Métodos

## Propiedades

`nodeName`  
El nombre calificado de este nodo.

`nodeValue`  
El URI del espacio de nombres declarado por este nodo, o `null` si el espacio de nombres está vacío.

`nodeType`  
El tipo de nodo. En este caso, devuelve [ `XML_NAMESPACE_DECL_NODE` ](#dom.constants).

`prefix`  
El prefijo del espacio de nombres declarado por este nodo.

`localName`  
La parte local del nombre calificado de este nodo.

`namespaceURI`  
El URI del espacio de nombres declarado por este nodo, o `null` si no está especificado.

`isConnected`  
Si el nodo está conectado a un documento.

`ownerDocument`  
El objeto `DOMDocument` asociado a este nodo, o `null` si este nodo es un `DOMDocument`.

`parentNode`  
El padre de este nodo. Si no hay tal nodo, devuelve `null`.

`parentElement`  
La clase padre de este nodo. Si no hay tal clase, devuelve `null`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Las propiedades DOMNameSpaceNode::\$parentElement, y DOMNameSpaceNode::\$isConnected han sido añadidas. |
