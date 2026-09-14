---
title: DOMElement::getAttribute
description: Devuelve el valor de un atributo
source_url: https://www.php.net/manual/es/domelement.getattribute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement/getattribute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 4f5e2b225
order: 13440
---

DOMElement::getAttribute

Devuelve el valor de un atributo

## Descripción

```php
public DOMElement::getAttribute(string $qualifiedName): string
```php

Obtiene el valor del atributo de nombre `qualifiedName` para el nodo actual.

## Parámetros

`qualifiedName`  
El nombre del atributo.

## Valores devueltos

El valor del atributo, o una cadena vacía si no se encuentra un atributo con el nombre dado por `qualifiedName`.

## Véase también

DOMElement::hasAttribute, DOMElement::setAttribute, DOMElement::removeAttribute
