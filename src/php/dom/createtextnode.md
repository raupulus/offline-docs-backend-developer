---
title: DOMDocument::createTextNode
description: Crea un nuevo nodo de texto
source_url: https://www.php.net/manual/es/domdocument.createtextnode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/createtextnode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 4f5e2b225
order: 13090
---

DOMDocument::createTextNode

Crea un nuevo nodo de texto

## Descripción

```php
public DOMDocument::createTextNode(string $data): DOMText
```php

Esta función crea una nueva instancia de la clase `DOMText`. Este nodo no será mostrado en el documento, a menos que sea insertado con `DOMNode::appendChild`.

## Parámetros

`data`  
El contenido del texto.

## Valores devueltos

Un nuevo `DOMText`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | En caso de error, una `DomException` es ahora lanzada. Anteriormente, `false` era devuelto. |

## Véase también

DOMNode::appendChild, DOMDocument::createAttribute, DOMDocument::createAttributeNS, DOMDocument::createCDATASection, DOMDocument::createComment, DOMDocument::createDocumentFragment, DOMDocument::createElement, DOMDocument::createElementNS, DOMDocument::createEntityReference, DOMDocument::createProcessingInstruction
