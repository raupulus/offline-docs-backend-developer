---
title: zip_entry_open
description: Abre un directorio de archivo para lectura
source_url: https://www.php.net/manual/es/function.zip-entry-open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/functions/zip-entry-open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_reviewed: true
translation_revision: 963af75fa
order: 108090
---

zip_entry_open

Abre un directorio de archivo para lectura

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] zip_entry_open(resource $zip_dp, resource $zip_entry, [string $mode]): bool
```php

`zip_entry_open` abre un directorio en un archivo ZIP para lectura.

## Parámetros

`zip_dp`  
Un recurso válido devuelto por la función `zip_open`.

`zip_entry`  
Un directorio de archivo devuelto por la función `zip_read`.

`mode`  
Todos los métodos especificados en la documentación de la función `fopen`.

> [!NOTE]
> Actualmente, `mode` es ignorado y siempre vale `"rb"`. Esto se debe a que el soporte ZIP de PHP es solo de lectura.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

> [!NOTE]
> A diferencia de `fopen` y otras funciones de archivos, el valor devuelto por `zip_entry_open` solo indica el resultado de la operación y no es necesario para la lectura o el cierre del archivo del directorio de archivo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función está obsoleta en favor de la API orientada a objetos. |

## Véase también

`zip_entry_close`, `zip_entry_read`
