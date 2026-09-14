---
title: Dom\HTMLDocument::saveXmlFile
description: Serializa el documento en forma de fichero XML
source_url: https://www.php.net/manual/es/dom-htmldocument.savexmlfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/htmldocument/savexmlfile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: a8b6f4dd3
order: 12590
---

Dom\HTMLDocument::saveXmlFile

Serializa el documento en forma de fichero

XML

## Descripción

```php
public Dom\HTMLDocument::saveXmlFile(string $filename, [int $options]): int
```php

Serializa el documento en forma de fichero XML.

## Parámetros

`filename`  
La ruta de acceso del fichero en el que guardar el documento.

`options`  
Opciones adicionales. Las opciones `LIBXML_NOEMPTYTAG` y `LIBXML_NOXMLDECL` son soportadas. Antes de PHP 8.3.0, solo la opción `LIBXML_NOEMPTYTAG` era soportada.

## Valores devueltos

El número de bytes escritos en caso de éxito, o `false` en caso de fallo.

## Errores/Excepciones

- Genera una ValueError si `filename` es un string vacío o contiene bytes nulos.

## Véase también

Dom\HTMLDocument::saveXml

Dom\HTMLDocument::saveHtmlFile
