---
title: La clase DOMXPath
source_url: https://www.php.net/manual/es/class.domxpath.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domxpath.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: 8aa5f1846
order: 14360
---

## Introducción

Permite utilizar consultas XPath 1.0 en documentos HTML o XML.

## Sinopsis de la clase

DOMXPath

Propiedades

public

readonly

DOMDocument

document

public

bool

registerNodeNamespaces

Métodos

## Propiedades

`document`  
El documento que está ligado a este objeto.

`registerNodeNamespaces`  
Cuando se establece en `true`, los espacios de nombres en el nodo son registrados.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Ya no es posible clonar un objeto `DOMXPath`. Esto lanzará ahora una excepción. Antes de PHP 8.4.0, esto producía un objeto inutilizable. |
| 8.0.0 | La propiedad `registerNodeNamespaces` ha sido añadida. |
