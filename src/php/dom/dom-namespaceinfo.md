---
title: La clase Dom\NamespaceInfo
source_url: https://www.php.net/manual/es/class.dom-namespaceinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/dom-namespaceinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: ae7db14ea
order: 12430
---

## Introducción

Representa información inmutable sobre los espacios de nombres de un elemento. Esto desacopla los espacios de nombres de los atributos, que estaban incorrectamente entrelazados en las antiguas clases DOM.

## Sinopsis de la clase

final

readonly

Dom\NamespaceInfo

Propiedades

public

string

null

prefix

public

string

null

namespaceURI

public

Dom\Element

element

## Propiedades

`prefix`  
El prefijo del espacio de nombres del atributo.

`namespaceURI`  
El URI del espacio de nombres del atributo.

`element`  
El elemento concernido por esta información de espacio de nombres.
