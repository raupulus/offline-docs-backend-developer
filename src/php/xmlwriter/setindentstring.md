---
title: XMLWriter::setIndentString
description: Define la cadena a utilizar para la indentación
source_url: https://www.php.net/manual/es/xmlwriter.setindentstring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlwriter/xmlwriter/setindentstring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlwriter
translation_status: ready
translation_revision: 4a742792d
order: 103710
---

XMLWriter::setIndentString

xmlwriter_set_indent_string

Define la cadena a utilizar para la indentación

## Descripción

Estilo orientado a objetos

```php
public XMLWriter::setIndentString(string $indentation): bool
```php

Estilo procedimental

```php
xmlwriter_set_indent_string(XMLWriter $writer, string $indentation): bool
```

Define la cadena que se utilizará para indentar cada elemento/atributo de un documento XML.

## Parámetros

`writer`  
Únicamente para llamadas procedimentales. La instancia `XMLWriter` que es modificada. Este objeto proviene de una llamada a `xmlwriter_open_uri` o `xmlwriter_open_memory`.

`indentation`  
La cadena para la indentación.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `writer` ahora espera una instancia de `XMLWriter` anteriormente, se esperaba una `resource`. |

## Notas

> [!NOTE]
> La indentación se reinicia cuando se abre un XMLWriter.

## Véase también

XMLWriter::setIndent
