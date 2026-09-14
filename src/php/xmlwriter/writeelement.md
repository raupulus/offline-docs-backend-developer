---
title: XMLWriter::writeElement
description: Escribe una etiqueta completa del elemento
source_url: https://www.php.net/manual/es/xmlwriter.writeelement.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlwriter/xmlwriter/writeelement.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlwriter
translation_status: ready
translation_revision: 4a742792d
order: 103960
---

XMLWriter::writeElement

xmlwriter_write_element

Escribe una etiqueta completa del elemento

## Descripción

Estilo orientado a objetos

```php
public XMLWriter::writeElement(string $name, [string $content]): bool
```php

Estilo procedimental

```php
xmlwriter_write_element(XMLWriter $writer, string $name, [string $content]): bool
```

Escribe una etiqueta completa del elemento.

## Parámetros

`writer`  
Únicamente para llamadas procedimentales. La instancia `XMLWriter` que es modificada. Este objeto proviene de una llamada a `xmlwriter_open_uri` o `xmlwriter_open_memory`.

`name`  
El nombre del elemento.

`content`  
Los contenidos del elemento.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `writer` ahora espera una instancia de `XMLWriter` anteriormente, se esperaba una `resource`. |

## Véase también

XMLWriter::startElement, XMLWriter::endElement, XMLWriter::writeElementNs
