---
title: XMLReader::XML
description: Establece los datos que contienen el XML a analizar
source_url: https://www.php.net/manual/es/xmlreader.xml.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlreader/xmlreader/xml.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlreader
translation_status: ready
translation_reviewed: true
translation_revision: ca220fb75
order: 103350
---

XMLReader::XML

Establece los datos que contienen el XML a analizar

## Descripción

```php
public static XMLReader::XML(string $source, [string $encoding], [int $flags]): XMLReader
```php

```php
public XMLReader::XML(string $source, [string $encoding], [int $flags]): bool
```

Establece los datos que contienen el XML a analizar.

## Parámetros

`source`  
String que contiene el XML a analizar.

`encoding`  
La codificación del documento, o `null`.

`flags`  
Un máscara de constantes [LIBXML\_\*](#libxml.constants).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. Si se llama estáticamente, devuelve un objeto `XMLReader` o `false` si ocurre un error.

## Errores/Excepciones

- Pasar un valor inválido para el `encoding` generará una excepción ValueError.

- Este método puede ser llamado estáticamente, pero, antes de PHP 8.0.0, esto generará un error `E_DEPRECATED` en este caso.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Pasar un valor inválido para el `encoding` ahora genera una excepción ValueError. |
| 8.0.0 | XMLReader::xml ahora se declara como método estático, pero aún puede ser llamado en una instancia de `XMLReader`. |

## Véase también

XMLReader::open, XMLReader::close
