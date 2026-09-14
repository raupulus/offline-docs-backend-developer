---
title: La clase Dom\Document
source_url: https://www.php.net/manual/es/class.dom-document.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/dom-document.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 34314b7c6
order: 12310
---

## 

Esta es la versión moderna y conforme a las especificaciones de `DOMDocument`. Es la clase base para `Dom\XMLDocument` y `Dom\HTMLDocument`.

## Sinopsis de la clase

abstract

Dom\Document

extends

Dom\Node

implements

Dom\ParentNode

Constantes heredadas

Propiedades

public

readonly

Dom\Implementation

implementation

public

string

URL

public

string

documentURI

public

string

characterSet

public

string

charset

public

string

inputEncoding

public

readonly

Dom\DocumentType

null

doctype

public

readonly

Dom\Element

null

documentElement

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

Dom\HTMLCollection

children

public

Dom\HTMLElement

null

body

public

readonly

Dom\HTMLElement

null

head

public

string

title

Propiedades heredadas

Métodos

Aún no documentado

Métodos heredados

Aún no documentado

## Propiedades

`URL`  
Equivalente a `documentURI`.

`characterSet`  
La codificación del documento utilizada para la serialización. Al analizar un documento, esto se define en la codificación de entrada de dicho documento.

`inputEncoding`  
Alias heredado de `characterSet`.

`charset`  
Alias heredado de `characterSet`.

  

`documentElement`  
El `Dom\Element` que es el elemento del documento. Esto evalúa a `null` para documentos sin elementos.

  

  

  

  

`body`  
El primer hijo del elemento `html` que es una etiqueta `body` o una etiqueta `frameset`. Estos elementos deben estar en el espacio de nombres HTML. Si ningún elemento coincide, esto evalúa a `null`.

`head`  
El primer elemento `head` que es un hijo del elemento `html`. Estos elementos deben estar en el espacio de nombres HTML. Si ningún elemento coincide, esto evalúa a `null`.

`title`  
El título del documento tal como se define por el elemento `title` para HTML o el elemento `title` SVG para SVG. Si no hay título, esto evalúa a la cadena vacía.
