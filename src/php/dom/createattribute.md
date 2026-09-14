---
title: DOMDocument::createAttribute
description: Crea un nuevo atributo
source_url: https://www.php.net/manual/es/domdocument.createattribute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/createattribute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_revision: 7d5c74c9a
order: 13000
---

DOMDocument::createAttribute

Crea un nuevo atributo

## Descripción

```php
public DOMDocument::createAttribute(string $localName): DOMAttr
```php

Esta función crea una nueva instancia de la clase `DOMAttr`. Este nodo no será mostrado en el documento, a menos que sea insertado con `DOMNode::appendChild`.

## Parámetros

`localName`  
El nombre del atributo.

## Valores devueltos

El nuevo `DOMAttr` o `false` si ha ocurrido un error.

## Errores/Excepciones

Puede lanzar una DOMException con los siguientes códigos de error:

`DOM_INVALID_CHARACTER_ERR`  
Lanzado si `localName` contiene un carácter inválido.

## Véase también

DOMNode::appendChild, DOMDocument::createAttributeNS, DOMDocument::createCDATASection, DOMDocument::createComment, DOMDocument::createDocumentFragment, DOMDocument::createElement, DOMDocument::createElementNS, DOMDocument::createEntityReference, DOMDocument::createProcessingInstruction, DOMDocument::createTextNode
