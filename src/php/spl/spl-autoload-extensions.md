---
title: spl_autoload_extensions
description: Registra y devuelve la extensión de archivo por defecto para spl_autoload
source_url: https://www.php.net/manual/es/function.spl-autoload-extensions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/functions/spl-autoload-extensions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 60809ebcf
order: 82260
---

spl_autoload_extensions

Registra y devuelve la extensión de archivo por defecto para spl_autoload

## Descripción

```php
spl_autoload_extensions([string $file_extensions]): string
```php

Esta función puede modificar y verificar las extensiones de archivo para `__autoload` la función interna de respaldo que `spl_autoload` utilizará.

> [!NOTE]
> No debería haber espacios entre las extensiones de archivo definidas.

## Parámetros

`file_extensions`  
Si `null`, simplemente devuelve la lista actual de extensiones, separadas por comas. Para modificar esta lista, llame simplemente a la función con la nueva lista de extensiones a utilizar en un `string`, donde cada extensión estará separada por comas.

## Valores devueltos

Una lista de extensiones de archivo, delimitadas por comas, para `spl_autoload`.

## Historial de cambios

| Versión | Descripción                          |
|---------|--------------------------------------|
| 8.0.0   | `file_extensions` ahora es nullable. |

## Ejemplos

Ejemplo con `spl_autoload_extensions`

```
<?php
spl_autoload_extensions(".php,.inc");
?>

   
```php
