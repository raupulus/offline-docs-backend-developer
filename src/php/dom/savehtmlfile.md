---
title: Dom\HTMLDocument::saveHtmlFile
description: Serializa el documento en forma de fichero HTML
source_url: https://www.php.net/manual/es/dom-htmldocument.savehtmlfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/htmldocument/savehtmlfile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: a8b6f4dd3
order: 12570
---

Dom\HTMLDocument::saveHtmlFile

Serializa el documento en forma de fichero

HTML

## Descripción

```php
public Dom\HTMLDocument::saveHtmlFile(string $filename): int
```php

Serializa el documento en forma de fichero HTML.

## Parámetros

`filename`  
La ruta de acceso del fichero en el que guardar el documento.

## Valores devueltos

El número de bytes escritos en caso de éxito, o `false` en caso de fallo.

## Errores/Excepciones

- Genera una ValueError si `filename` es un string vacío o contiene bytes nulos.

## Véase también

Dom\HTMLDocument::saveHtml

Dom\HTMLDocument::saveXmlFile
