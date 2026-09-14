---
title: XMLWriter::startDtd
description: Crea la etiqueta DTD inicial
source_url: https://www.php.net/manual/es/xmlwriter.startdtd.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlwriter/xmlwriter/startdtd.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlwriter
translation_status: ready
translation_revision: 4a742792d
order: 103770
---

XMLWriter::startDtd

xmlwriter_start_dtd

Crea la etiqueta DTD inicial

## Descripción

Estilo orientado a objetos

```php
public XMLWriter::startDtd(string $qualifiedName, [string $publicId], [string $systemId]): bool
```php

Estilo procedimental

```php
xmlwriter_start_dtd(XMLWriter $writer, string $qualifiedName, [string $publicId], [string $systemId]): bool
```

Inicia un DTD.

## Parámetros

`writer`  
Únicamente para llamadas procedimentales. La instancia `XMLWriter` que es modificada. Este objeto proviene de una llamada a `xmlwriter_open_uri` o `xmlwriter_open_memory`.

`qualifiedName`  
El nombre calificado del tipo de documento a crear.

`publicId`  
El identificador externo del subconjunto publico.

`systemId`  
El identificador externo del subconjunto del sistema.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `writer` ahora espera una instancia de `XMLWriter` anteriormente, se esperaba una `resource`. |

## Véase también

XMLWriter::endDtd, XMLWriter::writeDtd
