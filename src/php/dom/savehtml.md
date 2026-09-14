---
title: Dom\HTMLDocument::saveHtml
description: Serializa el documento como string HTML
source_url: https://www.php.net/manual/es/dom-htmldocument.savehtml.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/htmldocument/savehtml.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: a8b6f4dd3
order: 12560
---

Dom\HTMLDocument::saveHtml

Serializa el documento como string

HTML

## Descripción

```php
public Dom\HTMLDocument::saveHtml([Dom\Node $node]): string
```php

Serializa el documento como string HTML.

## Parámetros

`node`  
El nodo a serializar. Si no se proporciona, se serializa todo el documento.

## Valores devueltos

El documento HTML serializado como string en la codificación del documento actual.

## Errores/Excepciones

- Levanta una excepción Dom\DOMException con el código `Dom\WRONG_DOCUMENT_ERR` si el `node` proviene de otro documento.

## Véase también

Dom\HTMLDocument::saveHtmlFile

Dom\HTMLDocument::saveXml
