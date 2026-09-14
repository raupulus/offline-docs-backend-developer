---
title: XMLWriter::startDocument
description: Crea un documento
source_url: https://www.php.net/manual/es/xmlwriter.startdocument.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlwriter/xmlwriter/startdocument.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlwriter
translation_status: ready
translation_reviewed: false
translation_revision: ca220fb75
order: 103760
---

XMLWriter::startDocument

xmlwriter_start_document

Crea un documento

## Descripción

Estilo orientado a objetos

```php
public XMLWriter::startDocument([string $version], [string $encoding], [string $standalone]): bool
```php

Estilo procedimental

```php
xmlwriter_start_document(XMLWriter $writer, [string $version], [string $encoding], [string $standalone]): bool
```

Comienza un documento.

## Parámetros

`writer`  
Únicamente para llamadas procedimentales. La instancia `XMLWriter` que es modificada. Este objeto proviene de una llamada a `xmlwriter_open_uri` o `xmlwriter_open_memory`.

`version`  
El número de versión del documento en la declaración XML.

`encoding`  
La codificación del documento en la declaración XML.

`standalone`  
`yes` o `no`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Pasar un `encoding` que contenga bytes nulos lanzará una excepción ValueError.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Pasar un `encoding` que contenga bytes nulos lanza ahora una excepción ValueError. |
| 8.0.0 | `writer` ahora espera una instancia de `XMLWriter` anteriormente, se esperaba una `resource`. |

## Véase también

XMLWriter::endDocument
