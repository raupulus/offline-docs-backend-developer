---
title: XMLWriter::writeDtdEntity
description: Escribe una entidad DTD
source_url: https://www.php.net/manual/es/xmlwriter.writedtdentity.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlwriter/xmlwriter/writedtdentity.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlwriter
translation_status: ready
translation_reviewed: true
translation_revision: 4a742792d
order: 103950
---

XMLWriter::writeDtdEntity

xmlwriter_write_dtd_entity

Escribe una entidad DTD

## Descripción

Estilo orientado a objetos

```php
public XMLWriter::writeDtdEntity(string $name, string $content, [bool $isParam], [string $publicId], [string $systemId], [string $notationData]): bool
```php

Estilo procedimental

```php
xmlwriter_write_dtd_entity(XMLWriter $writer, string $name, string $content, [bool $isParam], [string $publicId], [string $systemId], [string $notationData]): bool
```

Escribe una entidad DTD.

## Parámetros

`writer`  
Únicamente para llamadas procedimentales. La instancia `XMLWriter` que es modificada. Este objeto proviene de una llamada a `xmlwriter_open_uri` o `xmlwriter_open_memory`.

`name`  
El nombre de la entidad.

`content`  
El contenido de la entidad.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `writer` ahora espera una instancia de `XMLWriter` anteriormente, se esperaba una `resource`. |
| 8.0.0 | `publicId`, `systemId` y `notationData` son ahora nullable. |

## Véase también

XMLWriter::startDtdEntity, XMLWriter::endDtdEntity
