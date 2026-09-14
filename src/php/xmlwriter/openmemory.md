---
title: XMLWriter::openMemory
description: Crea un nuevo xmlwriter utilizando la memoria para la visualización de
  la cadena
source_url: https://www.php.net/manual/es/xmlwriter.openmemory.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlwriter/xmlwriter/openmemory.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlwriter
translation_status: ready
translation_reviewed: true
translation_revision: 525aa5f19
order: 103670
---

XMLWriter::openMemory

xmlwriter_open_memory

Crea un nuevo xmlwriter utilizando la memoria para la visualización de la cadena

## Descripción

Estilo orientado a objetos

```php
public XMLWriter::openMemory(): bool
```php

Estilo procedimental

```php
xmlwriter_open_memory(): XMLWriter
```

Crea un nuevo objeto `XMLWriter`, utilizando la memoria para la visualización de las cadenas.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Estilo orientado a objetos : Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

Estilo procedimental : Devuelve una nueva instancia de `XMLWriter` para su uso futuro con las funciones xmlwriter en caso de éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función ahora devuelve una instancia de `XMLWriter` en caso de éxito. Anteriormente, un `resource` era devuelto en este caso. |

## Véase también

XMLWriter::openUri
