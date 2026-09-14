---
title: XMLReader::open
description: Fija el URI que contiene el XML a analizar
source_url: https://www.php.net/manual/es/xmlreader.open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlreader/xmlreader/open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlreader
translation_status: ready
translation_reviewed: false
translation_revision: ca220fb75
order: 103260
---

XMLReader::open

Fija el URI que contiene el XML a analizar

## Descripción

```php
public static XMLReader::open(string $uri, [string $encoding], [int $flags]): XMLReader
```php

```php
public XMLReader::open(string $uri, [string $encoding], [int $flags]): bool
```

Fija el URI que contiene el documento XML a ser analizado.

## Parámetros

`uri`  
URI que apunta al documento.

`encoding`  
La codificación del documento, o `null`.

`flags`  
Una máscara de constante [LIBXML\_\*](#libxml.constants).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. Si se llama estáticamente, devuelve un objeto `XMLReader` o `false` si ocurre un error.

## Errores/Excepciones

- Pasar un valor inválido para el `encoding` generará una excepción ValueError.

- Este método puede ser llamado estáticamente, pero, anterior a PHP 8.0.0, esto generará un error `E_DEPRECATED` en tal caso.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Pasar un valor inválido para el `encoding` ahora generará una excepción ValueError. |
| 8.0.0 | XMLReader::open ahora se declara como método estático, pero aún puede ser llamado en una instancia de `XMLReader`. |

## Véase también

XMLReader::XML, XMLReader::close
