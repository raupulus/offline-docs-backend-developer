---
title: La clase DOMText
source_url: https://www.php.net/manual/es/class.domtext.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domtext.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: d75a54118
order: 14280
---

## Introducción

La clase `DOMText` hereda de `DOMCharacterData` y representa el contenido textual de `DOMElement` o `DOMAttr`.

## Sinopsis de la clase

DOMText

extends

DOMCharacterData

Constantes heredadas

Propiedades

public

readonly

string

wholeText

Propiedades heredadas

Métodos

Métodos heredados

## Propiedades

`wholeText`  
Contiene todo el texto de los nodos de texto adyacentes (es decir, nodos que no están separados por etiquetas Element, Comment o Processing Instruction).

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | El método no implementado DOMText::replaceWholeText ha sido eliminado. |
