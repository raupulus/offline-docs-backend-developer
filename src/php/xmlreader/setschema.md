---
title: XMLReader::setSchema
description: Valida el documento en contra del XSD
source_url: https://www.php.net/manual/es/xmlreader.setschema.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlreader/xmlreader/setschema.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlreader
translation_status: ready
translation_reviewed: false
translation_revision: 4a742792d
order: 103340
---

XMLReader::setSchema

Valida el documento en contra del XSD

## Descripción

```php
public XMLReader::setSchema(string $filename): bool
```php

Usa el esquema W3C XSD para validar el documento como es procesado. La activación solo es posible antes de la primera lectura o Read().

## Parámetros

`filename`  
El nombre del archivo del esquema XSD.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Las cuestiones `E_WARNING` si la libxml fue construida sin el esquema de soporte, el esquema contiene errores si el `XMLReader::read` ya ha sido llamado.

## Notas

> [!CAUTION]
> Esta función solo está disponible si PHP es compilado utilizando la biblioteca libxml 20620 o posterior.

## Véase también

XMLReader::setRelaxNGSchema, XMLReader::setRelaxNGSchemaSource, XMLReader::isValid
