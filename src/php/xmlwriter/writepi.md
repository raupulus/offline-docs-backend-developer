---
title: XMLWriter::writePi
description: Escribe un IP
source_url: https://www.php.net/manual/es/xmlwriter.writepi.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlwriter/xmlwriter/writepi.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlwriter
translation_status: ready
translation_revision: 4a742792d
order: 103980
---

XMLWriter::writePi

xmlwriter_write_pi

Escribe un IP

## Descripción

Estilo orientado a objetos

```php
public XMLWriter::writePi(string $target, string $content): bool
```php

Estilo procedimental

```php
xmlwriter_write_pi(XMLWriter $writer, string $target, string $content): bool
```

Escribe una instrucción de procesamiento.

## Parámetros

`writer`  
Únicamente para llamadas procedimentales. La instancia `XMLWriter` que es modificada. Este objeto proviene de una llamada a `xmlwriter_open_uri` o `xmlwriter_open_memory`.

`target`  
El objetivo de la instrucción de procesamiento.

`content`  
El contenido de la instrucción de procesamiento.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `writer` ahora espera una instancia de `XMLWriter` anteriormente, se esperaba una `resource`. |

## Véase también

XMLWriter::startPi, XMLWriter::endPi
