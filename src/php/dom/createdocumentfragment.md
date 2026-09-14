---
title: DOMDocument::createDocumentFragment
description: Crea un nuevo fragmento de documento
source_url: https://www.php.net/manual/es/domdocument.createdocumentfragment.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/createdocumentfragment.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 4f5e2b225
order: 13040
---

DOMDocument::createDocumentFragment

Crea un nuevo fragmento de documento

## Descripción

```php
public DOMDocument::createDocumentFragment(): DOMDocumentFragment
```php

Esta función crea una nueva instancia de la clase `DOMDocumentFragment`. Este nodo no será mostrado en el documento, a menos que sea insertado con `DOMNode::appendChild`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El nuevo `DOMDocumentFragment`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | En caso de error, una `DomException` es lanzada ahora. Anteriormente, `false` era devuelto. |

## Véase también

DOMNode::appendChild, DOMDocument::createAttribute, DOMDocument::createAttributeNS, DOMDocument::createCDATASection, DOMDocument::createComment, DOMDocument::createElement, DOMDocument::createElementNS, DOMDocument::createEntityReference, DOMDocument::createProcessingInstruction, DOMDocument::createTextNode
