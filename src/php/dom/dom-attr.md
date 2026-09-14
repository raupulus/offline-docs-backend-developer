---
title: La clase Dom\Attr
source_url: https://www.php.net/manual/es/class.dom-attr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/dom-attr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: ae7db14ea
order: 12260
---

## Introducción

`Dom\Attr` representa un atributo en el objeto `Dom\Element`.

Este es el equivalente moderno y conforme a las especificaciones de `DOMAttr`.

## Sinopsis de la clase

Dom\Attr

extends

Dom\Node

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

name

public

string

value

public

readonly

Dom\Element

null

ownerElement

public

readonly

bool

specified

Propiedades heredadas

Métodos

Métodos heredados

Aún no documentado

## Propiedades

`namespaceURI`  
El URI del espacio de nombres del atributo.

`prefix`  
El prefijo del espacio de nombres del atributo.

`localName`  
El nombre local del atributo.

`name`  
El nombre calificado del atributo.

`value`  
El valor del atributo.

> [!NOTE]
> A diferencia de la propiedad equivalente en `DOMAttr`, esto no sustituye las entidades.

`ownerElement`  
El elemento que contiene el atributo o `null`.

`specified`  
Opción heredada, siempre `true`.

## Véase también

Especificación WHATWG de Attr
