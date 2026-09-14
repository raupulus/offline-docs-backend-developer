---
title: XMLWriter::text
description: Escribe texto
source_url: https://www.php.net/manual/es/xmlwriter.text.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlwriter/xmlwriter/text.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlwriter
translation_status: ready
translation_reviewed: false
translation_revision: 4a742792d
order: 103840
---

XMLWriter::text

xmlwriter_text

Escribe texto

## Descripción

Estilo orientado a objetos

```php
public XMLWriter::text(string $content): bool
```php

Estilo procedimental

```php
xmlwriter_text(XMLWriter $writer, string $content): bool
```

Escribe texto.

## Parámetros

`writer`  
Únicamente para llamadas procedimentales. La instancia `XMLWriter` que es modificada. Este objeto proviene de una llamada a `xmlwriter_open_uri` o `xmlwriter_open_memory`.

`content`  
El contenido del texto. Los caracteres `<`, `>`, `&` y `"` se escriben como referencias de entidades (es decir, `&lt;`, `&gt;`, `&amp;` y `&quot;`, respectivamente). Todos los otros caracteres `'` incluidos se escriben literalmente. Para escribir los caracteres XML especiales literalmente, o para escribir referencias de entidades literales, `xmlwriter_write_raw` debe ser utilizado.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `writer` ahora espera una instancia de `XMLWriter` anteriormente, se esperaba una `resource`. |
