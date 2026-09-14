---
title: La clase DOMCharacterData
source_url: https://www.php.net/manual/es/class.domcharacterdata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domcharacterdata.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: d75a54118
order: 12890
---

## Introducción

Representa un nodo que contiene datos. Ningún nodo corresponde a esta clase, pero otros nodos heredan de ella.

## Sinopsis de la clase

DOMCharacterData

extends

DOMNode

implements

DOMChildNode

Constantes heredadas

Propiedades

public

string

data

public

readonly

int

length

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

`data`  
El contenido del nodo.

`length`  
El tamaño del contenido.

`nextElementSibling`  
El elemento hermano siguiente o `null`.

`previousElementSibling`  
El elemento hermano anterior o `null`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Las propiedades `nextElementSibling` y `previousElementSibling` fueron añadidas. |
| 8.0.0 | `DOMCharacterData` ahora implementa DOMChildNode. |

## Véase también

[Especificación W3C de CharacterData](http://www.w3.org/TR/2003/WD-DOM-Level-3-Core-20030226/DOM3-Core.html#core-ID-FF21A306)
