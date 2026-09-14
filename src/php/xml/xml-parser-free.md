---
title: xml_parser_free
description: Destruye un analizador XML
source_url: https://www.php.net/manual/es/function.xml-parser-free.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xml/functions/xml-parser-free.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xml
translation_status: ready
translation_reviewed: true
translation_revision: 00a8ae0c8
order: 102760
---

xml_parser_free

Destruye un analizador XML

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.5.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] xml_parser_free(XMLParser $parser): bool
```php

> [!NOTE]
> Esta función no tiene ningún efecto. Anterior a PHP 8.0.0, esta función era utilizada para cerrar un recurso.

Destruye el analizador XML `parser`.

> [!CAUTION]
> Anterior a PHP 8.0.0, además de llamar a la función `xml_parser_free` al final del análisis, era necesario eliminar explícitamente la referencia al parámetro `parser` para evitar fugas de memoria, si el recurso analizado es referenciado desde un objeto, y este objeto hace referencia al recurso analizado.

## Parámetros

`parser`  
Una referencia a un analizador XML.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Esta función ha sido marcada como obsoleta. |
| 8.0.0 | `parser` ahora espera una instancia de `XMLParser` ; anteriormente, se esperaba un recurso `xml` de tipo `resource` válido. |
