---
title: XMLWriter::writeCdata
description: Escribe un bloque CDATA
source_url: https://www.php.net/manual/es/xmlwriter.writecdata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlwriter/xmlwriter/writecdata.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlwriter
translation_status: ready
translation_reviewed: false
translation_revision: 4a742792d
order: 103900
---

XMLWriter::writeCdata

xmlwriter_write_cdata

Escribe un bloque CDATA

## Descripción

Estilo orientado a objetos

```php
public XMLWriter::writeCdata(string $content): bool
```php

Estilo procedimental

```php
xmlwriter_write_cdata(XMLWriter $writer, string $content): bool
```

Escribe un bloque CDATA.

## Parámetros

`writer`  
Únicamente para llamadas procedimentales. La instancia `XMLWriter` que es modificada. Este objeto proviene de una llamada a `xmlwriter_open_uri` o `xmlwriter_open_memory`.

`content`  
El contenido del bloque CDATA.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `writer` ahora espera una instancia de `XMLWriter` anteriormente, se esperaba una `resource`. |

## Ejemplos

Uso Básico de `xmlwriter_write_cdata`

```php
<?php
// configurar el documento
$xml = new XmlWriter();
$xml->openMemory();
$xml->setIndent(true);
$xml->startDocument('1.0', 'UTF-8');
$xml->startElement('mydoc');
$xml->startElement('myele');

// Salida CData
$xml->startElement('mycdataelement');
$xml->writeCData("texto para incluir como CData");
$xml->endElement();

// finalizar el documento y salida
$xml->endElement();
$xml->endElement();
echo $xml->outputMemory(true);
?>

   
```

El ejemplo anterior mostrará:

    <mydoc>
     <myele>
      <mycdataelement><![CDATA[texto para incluir como CData]​]></mycdataelement>
     </myele>
    </mydoc>

## Véase también

XMLWriter::startCdata, XMLWriter::endCdata
