---
title: La clase DOMElement
source_url: https://www.php.net/manual/es/class.domelement.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 68d8ee572
order: 13700
---

## Sinopsis de la clase

DOMElement

extends

DOMNode

implements

DOMParentNode

DOMChildNode

Constantes heredadas

Propiedades

public

readonly

string

tagName

public

string

className

public

string

id

public

readonly

mixed

schemaTypeInfo

public

readonly

DOMElement

null

firstElementChild

public

readonly

DOMElement

null

lastElementChild

public

readonly

int

childElementCount

public

readonly

DOMElement

null

previousElementSibling

public

readonly

DOMElement

null

nextElementSibling

Propiedades heredadas

Métodos

Métodos heredados

## Propiedades

`childElementCount`  
El número de elementos hijos.

`firstElementChild`  
Primer elemento hijo o `null`.

`lastElementChild`  
Último elemento hijo o `null`.

`nextElementSibling`  
El elemento hermano siguiente o `null`.

`previousElementSibling`  
El elemento hermano anterior o `null`.

`schemaTypeInfo`  
Todavía no implementado, siempre devuelve `null`

`tagName`  
El nombre del elemento

`className`  
Una cadena que representa las clases del elemento, separadas por espacios.

`id`  
Refleja el ID del elemento a través del atributo `"id"`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Las propiedades `className` y `id` y los métodos DOMElement::getAttributeNames, DOMElement::insertAdjacentElement, DOMElement::insertAdjacentText y DOMElement::toggleAttribute han sido añadidos. |
| 8.0.0 | Las propiedades `firstElementChild`, `lastElementChild`, `childElementCount`, `previousElementSibling` y `nextElementSibling` fueron añadidas. |
| 8.0.0 | `DOMElement` ahora implementa DOMParentNode y DOMChildNode. |

## Notas

> [!NOTE]
> La extensión DOM utiliza el codificado UTF-8. Utilice `mb_convert_encoding`, UConverter::transcode, o `iconv` para manipular otros codificados.
