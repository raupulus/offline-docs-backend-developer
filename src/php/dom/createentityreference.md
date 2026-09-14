---
title: DOMDocument::createEntityReference
description: Create new entity reference node
source_url: https://www.php.net/manual/es/domdocument.createentityreference.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/createentityreference.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_revision: 7d5c74c9a
order: 13070
---

DOMDocument::createEntityReference

Create new entity reference node

## Descripción

```php
public DOMDocument::createEntityReference(string $name): DOMEntityReference
```php

Esta función crea una nueva instancia de la clase `DOMEntityReference`. Este nodo no será mostrado en el documento, a menos que sea insertado con `DOMNode::appendChild`.

## Parámetros

`name`  
El contenido de la entidad referencia, p.ej. la entidad referencia menos los caracteres `&` inicial y el `;` final.

## Valores devueltos

El nuevo `DOMEntityReference` o `false` si ha ocurrido un error.

## Errores/Excepciones

Puede lanzar una DOMException con los siguientes códigos de error:

`DOM_INVALID_CHARACTER_ERR`  
Lanzado si `name` contiene un carácter inválido.

## Véase también

DOMNode::appendChild, DOMDocument::createAttribute, DOMDocument::createAttributeNS, DOMDocument::createCDATASection, DOMDocument::createComment, DOMDocument::createDocumentFragment, DOMDocument::createElement, DOMDocument::createElementNS, DOMDocument::createProcessingInstruction, DOMDocument::createTextNode
