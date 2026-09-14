---
title: DOMElement::getElementsByTagName
description: Obtiene los elementos por nombre de etiqueta
source_url: https://www.php.net/manual/es/domelement.getelementsbytagname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement/getelementsbytagname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 4f5e2b225
order: 13490
---

DOMElement::getElementsByTagName

Obtiene los elementos por nombre de etiqueta

## Descripción

```php
public DOMElement::getElementsByTagName(string $qualifiedName): DOMNodeList
```php

Esta función devuelve una nueva instancia de la clase `DOMNodeList` con todos los elementos descendientes con un nombre de etiqueta dado por `qualifiedName`, en el orden en que fueron encontrados en un recorrido preorden de este elemento árbol.

## Parámetros

`qualifiedName`  
El nombre de la etiqueta. Use `*` para devolver todos los elementos dentro del elemento árbol.

## Valores devueltos

Esta función devuelve una nueva instancia de la clase `DOMNodeList` con todos los elementos coincidentes.

## Véase también

DOMElement::getElementsByTagNameNS
