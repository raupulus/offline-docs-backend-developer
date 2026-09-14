---
title: XMLWriter::flush
description: Vacía el búfer actual
source_url: https://www.php.net/manual/es/xmlwriter.flush.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlwriter/xmlwriter/flush.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlwriter
translation_status: ready
translation_reviewed: false
translation_revision: 4a742792d
order: 103650
---

XMLWriter::flush

xmlwriter_flush

Vacía el búfer actual

## Descripción

Estilo orientado a objetos

```php
public XMLWriter::flush([bool $empty]): string
```php

Estilo procedimental

```php
xmlwriter_flush(XMLWriter $writer, [bool $empty]): string
```

Vacía el búfer actual.

## Parámetros

`writer`  
Únicamente para llamadas procedimentales. La instancia `XMLWriter` que es modificada. Este objeto proviene de una llamada a `xmlwriter_open_uri` o `xmlwriter_open_memory`.

`empty`  
Si se debe vaciar el búfer o no. Por omisión, este parámetro vale `true`.

## Valores devueltos

Si se abrió el gestor de escritura en memoria, esta función devuelve el búfer XML generado. Si se utiliza una URI, esta función escribirá el búfer y devolverá el número de bytes escritos.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `writer` ahora espera una instancia de `XMLWriter` anteriormente, se esperaba una `resource`. |
| 8.0.0 | Esta función ya no puede devolver `false`. |
