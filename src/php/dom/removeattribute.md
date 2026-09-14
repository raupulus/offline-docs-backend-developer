---
title: DOMElement::removeAttribute
description: Elimina un atributo
source_url: https://www.php.net/manual/es/domelement.removeattribute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement/removeattribute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 7d5c74c9a
order: 13570
---

DOMElement::removeAttribute

Elimina un atributo

## Descripción

```php
public DOMElement::removeAttribute(string $qualifiedName): bool
```php

Elimina el atributo llamado `qualifiedName` del elemento.

## Parámetros

`qualifiedName`  
El nombre del atributo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Puede lanzar una DOMException con los siguientes códigos de error:

`DOM_NO_MODIFICATION_ALLOWED_ERR`  
Lanzado si el nodo es de sólo lectura.

## Véase también

DOMElement::hasAttribute, DOMElement::getAttribute, DOMElement::setAttribute
