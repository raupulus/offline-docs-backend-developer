---
title: XMLWriter::endDtdEntity
description: Finaliza el actual ente DTD
source_url: https://www.php.net/manual/es/xmlwriter.enddtdentity.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlwriter/xmlwriter/enddtdentity.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlwriter
translation_status: ready
translation_revision: 4a742792d
order: 103620
---

XMLWriter::endDtdEntity

xmlwriter_end_dtd_entity

Finaliza el actual ente DTD

## Descripción

Estilo orientado a objetos

```php
public XMLWriter::endDtdEntity(): bool
```php

Estilo procedimental

```php
xmlwriter_end_dtd_entity(XMLWriter $writer): bool
```

Finaliza el actual ente DTD.

## Parámetros

`writer`  
Únicamente para llamadas procedimentales. La instancia `XMLWriter` que es modificada. Este objeto proviene de una llamada a `xmlwriter_open_uri` o `xmlwriter_open_memory`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `writer` ahora espera una instancia de `XMLWriter` anteriormente, se esperaba una `resource`. |

## Véase también

XMLWriter::startDtdEntity, XMLWriter::writeDtdEntity
