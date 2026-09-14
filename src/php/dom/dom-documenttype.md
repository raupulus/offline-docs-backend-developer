---
title: La clase Dom\DocumentType
source_url: https://www.php.net/manual/es/class.dom-documenttype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/dom-documenttype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: ae7db14ea
order: 12330
---

## Introducción

Cada `Dom\Document` tiene un atributo `doctype` cuyo valor es `null` o un objeto `Dom\DocumentType`.

Este es el equivalente moderno y conforme a las especificaciones de `DOMImplementation`.

## Sinopsis de la clase

Dom\DocumentType

extends

Dom\Node

implements

Dom\ChildNode

Constantes heredadas

Propiedades

public

readonly

string

name

public

readonly

Dom\DtdNamedNodeMap

entities

public

readonly

Dom\DtdNamedNodeMap

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

Métodos

Aún no documentado

Métodos heredados

Aún no documentado

## Propiedades

`entities`  
Un objeto `Dom\DtdNamedNodeMap` que contiene las entidades generales, tanto externas como internas, declaradas en la DTD.

`notations`  
Un `Dom\DtdNamedNodeMap` que contiene las notaciones declaradas en la DTD.
