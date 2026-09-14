---
title: Dom\HTMLDocument::saveXml
description: Serializa el documento como un string XML
source_url: https://www.php.net/manual/es/dom-htmldocument.savexml.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/htmldocument/savexml.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 9b26644de
order: 12580
---

Dom\HTMLDocument::saveXml

Serializa el documento como un string

XML

## Descripción

```php
public Dom\HTMLDocument::saveXml([Dom\Node $node], [int $options]): string
```php

Serializa el documento como un string XML.

## Parámetros

`node`  
El nodo a serializar. Si no se proporciona, se serializa el documento completo.

`options`  
Opciones adicionales. Las opciones `LIBXML_NOEMPTYTAG` y `LIBXML_NOXMLDECL` son soportadas. Antes de PHP 8.3.0, solo la opción `LIBXML_NOEMPTYTAG` era soportada.

## Valores devueltos

El documento XML serializado como un string en la codificación del documento actual, o `false` en caso de fallo.

## Errores/Excepciones

- Levanta una excepción Dom\DOMException con el código `Dom\WRONG_DOCUMENT_ERR` si el `node` proviene de otro documento.

## Véase también

Dom\HTMLDocument::saveXmlFile

Dom\XMLDocument::saveHtml
