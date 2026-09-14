---
title: XMLReader::next
description: Mueve el cursor al siguiente nodo saltandose todos los subárboles
source_url: https://www.php.net/manual/es/xmlreader.next.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlreader/xmlreader/next.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlreader
translation_status: ready
translation_reviewed: false
translation_revision: 4a742792d
order: 103250
---

XMLReader::next

Mueve el cursor al siguiente nodo saltandose todos los subárboles

## Descripción

```php
public XMLReader::next([string $name]): bool
```php

Posiciona el cursor al siguiente nodo saltandose todos los subárboles. Si no existe tal nodo, el cursor se desplaza al final del documento.

## Parámetros

`name`  
El nodo del siguiente nodoa mover el cursor.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción               |
|---------|---------------------------|
| 8.0.0   | `name` ahora es anulable. |

## Véase también

XMLReader::moveToNextAttribute, XMLReader::moveToElement, XMLReader::moveToAttribute
