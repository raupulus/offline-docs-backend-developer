---
title: XMLWriter::writeComment
description: EScribe la etiqueta del comentario completa
source_url: https://www.php.net/manual/es/xmlwriter.writecomment.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlwriter/xmlwriter/writecomment.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlwriter
translation_status: ready
translation_reviewed: false
translation_revision: 4a742792d
order: 103910
---

XMLWriter::writeComment

xmlwriter_write_comment

EScribe la etiqueta del comentario completa

## Descripción

Estilo orientado a objetos

```php
public XMLWriter::writeComment(string $content): bool
```php

Estilo procedimental

```php
xmlwriter_write_comment(XMLWriter $writer, string $content): bool
```

Escribe un comentario completo.

## Parámetros

`writer`  
Únicamente para llamadas procedimentales. La instancia `XMLWriter` que es modificada. Este objeto proviene de una llamada a `xmlwriter_open_uri` o `xmlwriter_open_memory`.

`content`  
El contenido del comentario.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `writer` ahora espera una instancia de `XMLWriter` anteriormente, se esperaba una `resource`. |

## Véase también

XMLWriter::startComment, XMLWriter::endComment
