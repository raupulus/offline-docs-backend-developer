---
title: La clase DOMAttr
source_url: https://www.php.net/manual/es/class.domattr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domattr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: d75a54118
order: 12770
---

## Introducción

`DOMAttr` representa un atributo en el objeto `DOMElement`.

## Sinopsis de la clase

DOMAttr

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

bool

specified

public

string

value

public

readonly

DOMElement

null

ownerElement

public

readonly

mixed

schemaTypeInfo

Propiedades heredadas

Métodos

Métodos heredados

## Propiedades

`name`  
El nombre del atributo.

`ownerElement`  
El elemento que contiene el atributo o `null`.

`schemaTypeInfo`  
Aún no implementado, siempre vale `null`.

`specified`  
Aún no implementado, siempre vale `true`.

`value`  
El valor del atributo.

> [!NOTE]
> Tenga en cuenta que las entidades XML se expanden cuando se define un valor. Por lo tanto, el carácter `&` tiene un significado especial. Establecer `valor` a sí mismo fallará cuando `valor` contiene un `&`. Para evitar la expansión de entidades, utilice en su lugar DOMElement::setAttribute.

## Véase también

[Especificación W3C de Attr](http://www.w3.org/TR/2003/WD-DOM-Level-3-Core-20030226/DOM3-Core.html#core-ID-637646024)
