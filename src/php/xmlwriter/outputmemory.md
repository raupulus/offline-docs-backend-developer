---
title: XMLWriter::outputMemory
description: Devuelve el actual búfer
source_url: https://www.php.net/manual/es/xmlwriter.outputmemory.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlwriter/xmlwriter/outputmemory.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlwriter
translation_status: ready
translation_revision: 4a742792d
order: 103690
---

XMLWriter::outputMemory

xmlwriter_output_memory

Devuelve el actual búfer

## Descripción

Estilo orientado a objetos

```php
public XMLWriter::outputMemory([bool $flush]): string
```php

Estilo procedimental

```php
xmlwriter_output_memory(XMLWriter $writer, [bool $flush]): string
```

Devuelve el búfer actual.

## Parámetros

`writer`  
Únicamente para llamadas procedimentales. La instancia `XMLWriter` que es modificada. Este objeto proviene de una llamada a `xmlwriter_open_uri` o `xmlwriter_open_memory`.

`flush`  
Si se mantiene la salida del búfer o no. Por defecto es `true`.

## Valores devueltos

Devuelve el búfer actual como una cadena.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `writer` ahora espera una instancia de `XMLWriter` anteriormente, se esperaba una `resource`. |

## Véase también

XMLWriter::flush
