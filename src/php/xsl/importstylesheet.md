---
title: XSLTProcessor::importStylesheet
description: Importa una hoja de estilo
source_url: https://www.php.net/manual/es/xsltprocessor.importstylesheet.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xsl/xsltprocessor/importstylesheet.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xsl
translation_status: ready
translation_revision: 256782d03
order: 104140
---

XSLTProcessor::importStylesheet

Importa una hoja de estilo

## Descripción

```php
public XSLTProcessor::importStylesheet(object $stylesheet): bool
```php

Este método importa una hoja de estilo en el `XSLTProcessor` para transformaciones.

## Parámetros

`stylesheet`  
La hoja de estilo importada como objeto `Dom\Document`, `DOMDocument` u objeto `SimpleXMLElement`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Genera una excepción de tipo TypeError si `stylesheet` no es un objeto XML.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Añadido soporte para `Dom\Document`. |
| 8.4.0 | Ahora lanza una excepción de tipo TypeError en lugar de ValueError si `stylesheet` no es un objeto XML. |
