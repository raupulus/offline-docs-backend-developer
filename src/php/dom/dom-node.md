---
title: La clase Dom\Node
source_url: https://www.php.net/manual/es/class.dom-node.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/dom-node.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: ae7db14ea
order: 12440
---

## Introducción

Esta es la versión moderna y conforme a las especificaciones de `DOMNode`.

## Sinopsis de la clase

Dom\Node

Constantes

public

const

int

Dom\Node::DOCUMENT_POSITION_DISCONNECTED

0x1

public

const

int

Dom\Node::DOCUMENT_POSITION_PRECEDING

0x2

public

const

int

Dom\Node::DOCUMENT_POSITION_FOLLOWING

0x4

public

const

int

Dom\Node::DOCUMENT_POSITION_CONTAINS

0x8

public

const

int

Dom\Node::DOCUMENT_POSITION_CONTAINED_BY

0x10

public

const

int

Dom\Node::DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC

0x20

Propiedades

public

readonly

int

nodeType

public

readonly

string

nodeName

public

readonly

string

baseURI

public

readonly

bool

isConnected

public

readonly

Dom\Document

null

ownerDocument

public

readonly

Dom\Node

null

parentNode

public

readonly

Dom\Element

null

parentElement

public

readonly

Dom\NodeList

childNodes

public

readonly

Dom\Node

null

firstChild

public

readonly

Dom\Node

null

lastChild

public

readonly

Dom\Node

null

previousSibling

public

readonly

Dom\Node

null

nextSibling

public

string

null

nodeValue

public

string

null

textContent

Métodos

Aún no documentado

## Constantes predefinidas

## Propiedades

`nodeName`  
Devuelve el nombre más preciso para el tipo de nodo actual.

- Para los elementos, es el nombre calificado en mayúsculas HTML.

- Para los atributos, es el nombre calificado.

- Para las instrucciones de procesamiento, es el objetivo.

- Para los nodos de tipo documento, es el nombre.

  

  

`ownerDocument`  
El objeto `Dom\Document` asociado a este nodo, o `null` si este nodo es un documento.

  

  

`childNodes`  
Un objeto `Dom\NodeList` que contiene todos los hijos de este nodo. Si no hay hijos, es un `Dom\NodeList`.

  

  

  

  

`nodeValue`  
El valor de este nodo, según su tipo.

## Notas

> [!NOTE]
> La extensión DOM utiliza el codificado UTF-8 al utilizar los métodos o las propiedades. Los métodos del analizador detectan automáticamente el codificado o permiten al llamante especificar un codificado.

## Véase también

Especificación WHATWG de Node
