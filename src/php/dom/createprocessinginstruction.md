---
title: DOMDocument::createProcessingInstruction
description: Crea un nuevo nodo PI
source_url: https://www.php.net/manual/es/domdocument.createprocessinginstruction.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/createprocessinginstruction.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_revision: 7d5c74c9a
order: 13080
---

DOMDocument::createProcessingInstruction

Crea un nuevo nodo PI

## Descripción

```php
public DOMDocument::createProcessingInstruction(string $target, [string $data]): DOMProcessingInstruction
```php

Esta función crea una nueva instancia de la clase `DOMProcessingInstruction`. Este nodo no será mostrado en el documento, a menos que sea insertado con `DOMNode::appendChild`.

## Parámetros

`target`  
El objetivo de la instrucción de procesamiento.

`data`  
El contenido de la instrucción de procesamiento.

## Valores devueltos

El nuevo `DOMProcessingInstruction` o `false` si ha ocurrido un error.

## Errores/Excepciones

Puede lanzar una DOMException con los siguientes códigos de error:

`DOM_INVALID_CHARACTER_ERR`  
Lanzado si `target` contiene un carácter inválido.

## Véase también

DOMNode::appendChild, DOMDocument::createAttribute, DOMDocument::createAttributeNS, DOMDocument::createCDATASection, DOMDocument::createComment, DOMDocument::createDocumentFragment, DOMDocument::createElement, DOMDocument::createElementNS, DOMDocument::createEntityReference, DOMDocument::createTextNode
