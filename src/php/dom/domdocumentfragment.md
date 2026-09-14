---
title: La clase DOMDocumentFragment
source_url: https://www.php.net/manual/es/class.domdocumentfragment.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocumentfragment.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: d75a54118
order: 13380
---

## Sinopsis de la clase

DOMDocumentFragment

extends

DOMNode

implements

DOMParentNode

Constantes heredadas

Propiedades

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

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Las propiedades `firstElementChild`, `lastElementChild` y `childElementCount` fueron añadidas. |
| 8.0.0 | `DOMDocumentFragment` ahora implementa DOMParentNode. |
