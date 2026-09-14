---
title: XMLWriter::startAttribute
description: Crea un atributo
source_url: https://www.php.net/manual/es/xmlwriter.startattribute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlwriter/xmlwriter/startattribute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlwriter
translation_status: ready
translation_revision: 4a742792d
order: 103720
---

XMLWriter::startAttribute

xmlwriter_start_attribute

Crea un atributo

## Descripción

Estilo orientado a objetos

```php
public XMLWriter::startAttribute(string $name): bool
```php

Estilo procedimental

```php
xmlwriter_start_attribute(XMLWriter $writer, string $name): bool
```

Comienza un atributo.

## Parámetros

`writer`  
Únicamente para llamadas procedimentales. La instancia `XMLWriter` que es modificada. Este objeto proviene de una llamada a `xmlwriter_open_uri` o `xmlwriter_open_memory`.

`name`  
El nombre del atributo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `writer` ahora espera una instancia de `XMLWriter` anteriormente, se esperaba una `resource`. |

## Ejemplos

Uso Básico de XMLWriter::startAttribute

```php
<?php
$writer = new XMLWriter;
$writer->openURI('php://output');
$writer->startDocument('1.0', 'UTF-8');
$writer->startElement('element');
$writer->startAttribute('attribute');
$writer->text('value');
$writer->endAttribute();
$writer->endElement();
$writer->endDocument();

   
```

Resultado del ejemplo anterior es similar a:

    <element attribute="value"/>

## Véase también

XMLWriter::startAttributeNs, XMLWriter::endAttribute, XMLWriter::writeAttribute, XMLWriter::writeAttributeNs
