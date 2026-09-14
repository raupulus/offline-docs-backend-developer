---
title: La clase Dom\Element
source_url: https://www.php.net/manual/es/class.dom-element.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/dom-element.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 34314b7c6
order: 12350
---

## Introducción

Representa un elemento.

Este es el equivalente moderno y conforme a las especificaciones de `DOMElement`.

## Sinopsis de la clase

Dom\Element

extends

Dom\Node

implements

Dom\ParentNode

Dom\ChildNode

Constantes heredadas

Propiedades

public

readonly

string

null

namespaceURI

public

readonly

string

null

prefix

public

readonly

string

localName

public

readonly

string

tagName

public

string

id

public

string

className

public

readonly

Dom\TokenList

classList

public

readonly

Dom\NamedNodeMap

attributes

public

readonly

Dom\Element

null

firstElementChild

public

readonly

Dom\Element

null

lastElementChild

public

readonly

int

childElementCount

public

readonly

Dom\Element

null

previousElementSibling

public

readonly

Dom\Element

null

nextElementSibling

public

readonly

Dom\HTMLCollection

children

public

string

innerHTML

public

string

outerHTML

public

string

substitutedNodeValue

Propiedades heredadas

Métodos

Aún no documentado

Métodos heredados

Aún no documentado

## Propiedades

`namespaceURI`  
El URI del espacio de nombres del elemento.

`prefix`  
El prefijo del espacio de nombres del elemento.

`localName`  
El nombre local del elemento.

`tagName`  
El nombre en mayúsculas HTML calificado del elemento.

  

`classList`  
Devuelve una instancia de `Dom\TokenList` para gestionar fácilmente las clases de este elemento.

`attributes`  
Devuelve una instancia de `Dom\NamedNodeMap` que representa los atributos de este elemento.

  

  

  

  

  

  

  

`innerHTML`  
El HTML interno (o XML para documentos XML) del elemento.

`outerHTML`  
El HTML externo (o XML para documentos XML) del elemento, incluyendo el propio elemento. Disponible a partir de PHP 8.5.0.

`substitutedNodeValue`  
El valor del nodo con sustitución de entidad activada.

## Notas

> [!NOTE]
> La extensión DOM utiliza el codificado UTF-8 al utilizar los métodos o las propiedades. Los métodos del analizador detectan automáticamente el codificado o permiten al llamante especificar un codificado.
