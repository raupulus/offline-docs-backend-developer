---
title: La classe DOMEntity
source_url: https://www.php.net/manual/es/class.domentity.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domentity.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: d75a54118
order: 13710
---

## Introducción

Esta interfaz representa una entidad conocida, analizada o no, en un documento XML.

## Sinopsis de la clase

DOMEntity

extends

DOMNode

Constantes heredadas

Propiedades

public

readonly

string

null

publicId

public

readonly

string

null

systemId

public

readonly

string

null

notationName

public

readonly

string

null

actualEncoding

public

readonly

string

null

encoding

public

readonly

string

null

version

Propiedades heredadas

Métodos heredados

## Propiedades

`publicId`  
El identificador público asociado con la entidad, si está especificado, y `null` de lo contrario.

`systemId`  
El identificador del sistema asociado con la entidad, si está especificado, y `null` de lo contrario. Puede ser una URI absoluta o relativa.

`notationName`  
Para las entidades no analizadas, el nombre de la notación de la entidad. Para las entidades analizadas, vale `null`.

`actualEncoding`  
*Deprecado a partir de PHP 8.4.0*. Esto siempre ha sido igual a `null`.

`encoding`  
*Deprecado a partir de PHP 8.4.0*. Esto siempre ha sido igual a `null`.

`version`  
*Deprecado a partir de PHP 8.4.0*. Esto siempre ha sido igual a `null`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `actualEncoding`, `encoding`, y `version` ahora están oficialmente depreciados porque siempre han sido iguales a `null`. |
