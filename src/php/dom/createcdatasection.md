---
title: DOMDocument::createCDATASection
description: Crea un nuevo nodo cdata
source_url: https://www.php.net/manual/es/domdocument.createcdatasection.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/createcdatasection.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_revision: 4f5e2b225
order: 13020
---

DOMDocument::createCDATASection

Crea un nuevo nodo cdata

## Descripción

```php
public DOMDocument::createCDATASection(string $data): DOMCdataSection
```php

Esta función crea una nueva instancia de la clase `DOMCDATASection`. Este nodo no será mostrado en el documento, a menos que sea insertado con `DOMNode::appendChild`.

## Parámetros

`data`  
El contenido del cdata.

## Valores devueltos

El nuevo `DOMCDATASection` o `false` si ha ocurrido un error.

## Véase también

DOMNode::appendChild, DOMDocument::createAttribute, DOMDocument::createAttributeNS, DOMDocument::createComment, DOMDocument::createDocumentFragment, DOMDocument::createElement, DOMDocument::createElementNS, DOMDocument::createEntityReference, DOMDocument::createProcessingInstruction, DOMDocument::createTextNode
