---
title: XMLWriter::writeAttribute
description: Escribe un atributo
source_url: https://www.php.net/manual/es/xmlwriter.writeattribute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlwriter/xmlwriter/writeattribute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlwriter
translation_status: ready
translation_reviewed: false
translation_revision: 4a742792d
order: 103880
---

XMLWriter::writeAttribute

xmlwriter_write_attribute

Escribe un atributo

## Descripción

Estilo orientado a objetos

```php
public XMLWriter::writeAttribute(string $name, string $value): bool
```php

Estilo procedimental

```php
xmlwriter_write_attribute(XMLWriter $writer, string $name, string $value): bool
```

Escribe un atributo.

## Parámetros

`writer`  
Únicamente para llamadas procedimentales. La instancia `XMLWriter` que es modificada. Este objeto proviene de una llamada a `xmlwriter_open_uri` o `xmlwriter_open_memory`.

`name`  
El nombre del atributo.

`value`  
El valor del atributo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `writer` ahora espera una instancia de `XMLWriter` anteriormente, se esperaba una `resource`. |

## Ejemplos

Mezclar Sub-elementos y Atributos

Al escribir sub-elementos con atributos mezclados, cualquier intento de escribir atributos después del primer sub-elemento fallará y devolverá false.

```php
<?php
$xml = new XMLWriter();
$xml->openMemory();

$xml->startElement('element');
$xml->writeAttribute('attr1', '0');
$xml->writeElement('subelem', '0');
var_dump($xml->writeAttribute('attr2', '0'));
$xml->endElement();

echo $xml->flush();
?>

   
```

El ejemplo anterior mostrará:

    bool(false)
    <element attr1="0"><subelem>0</subelem></element>

## Véase también

XMLWriter::writeAttributeNs, XMLWriter::startAttribute, XMLWriter::startAttributeNs, XMLWriter::endAttribute
