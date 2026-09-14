---
title: XMLReader::isValid
description: Indica si el documento analizado es válido
source_url: https://www.php.net/manual/es/xmlreader.isvalid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlreader/xmlreader/isvalid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlreader
translation_status: ready
translation_reviewed: false
translation_revision: c1f37a6c2
order: 103170
---

XMLReader::isValid

Indica si el documento analizado es válido

## Descripción

```php
public XMLReader::isValid(): bool
```php

Devuelve un valor booleano que indica si el documento que se está analizando es válido según el DTD, o un esquema XML o RelaxNG. Si no hay esquema y la opción de validación DTD no está proporcionada, este método devolverá `false`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` cuando el documento es válido, de lo contrario `false`.

## Ejemplos

Validación XML

```
<?php
$xml = XMLReader::open('examples/book-simple.xml');

// La opción de validación del analizador debe estar
// activa para que este método funcione correctamente
$xml->setParserProperty(XMLReader::VALIDATE, true);

var_dump($xml->isValid());
?>

    
```php

## Notas

> [!NOTE]
> Este método verifica el nodo actual, no el documento completo.

## Véase también

XMLReader::setParserProperty, XMLReader::setRelaxNGSchema, XMLReader::setRelaxNGSchemaSource, XMLReader::setSchema
