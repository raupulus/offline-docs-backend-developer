---
title: La clase DOMDocumentType
source_url: https://www.php.net/manual/es/class.domdocumenttype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocumenttype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: 63ea498c8
order: 13390
---

## Introducción

Cada `DOMDocument` tiene un atributo `doctype` cuyo valor es o bien `null`, o bien un objeto `DOMDocumentType`.

## Sinopsis de la clase

DOMDocumentType

extends

DOMNode

Constantes heredadas

Propiedades

public

readonly

string

name

public

readonly

DOMNamedNodeMap

entities

public

readonly

DOMNamedNodeMap

notations

public

readonly

string

publicId

public

readonly

string

systemId

public

readonly

string

null

internalSubset

Propiedades heredadas

Métodos heredados

## Propiedades

`publicId`  
El identificador público del subset externo.

`systemId`  
El identificador de sistema del subset externo. Puede ser una URI absoluta o no.

`name`  
El nombre de la DTD; es decir, el nombre que sigue inmediatamente a la palabra clave `DOCTYPE`.

`entities`  
Un `DOMNamedNodeMap` que contiene las entidades generales, tanto externas como internas, declaradas en la DTD.

`notations`  
Un `DOMNamedNodeMap` que contiene las notaciones, declaradas en la DTD.

`internalSubset`  
El subset interno, en forma de `string`, o `null` si no existe. Esta cadena no contiene los corchetes delimitadores.
