---
title: runkit7_import
description: Realiza la importación de un fichero PHP importando las definiciones
  de funciones y clases, sobrescribiéndolas si es necesario
source_url: https://www.php.net/manual/es/function.runkit7-import.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/runkit7/functions/runkit7-import.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: runkit7
translation_status: ready
translation_reviewed: true
translation_revision: c4625323f
order: 72920
---

runkit7_import

Realiza la importación de un fichero PHP importando las definiciones de funciones y clases, sobrescribiéndolas si es necesario

> [!WARNING]
> Esta característica ha sido *eliminada* en PECL runkit7 4.0.0.

## Descripción

```php
runkit7_import(string $filename, [int $flags]): bool
```php

Similar a `include`. Sin embargo, todo código que se encuentre fuera de una función o clase es simplemente ignorado. Además, en función del valor de `flags`, toda función o clase ya existente en el entorno de ejecución actual puede ser automáticamente sobrescrita por sus nuevas definiciones.

## Parámetros

`filename`  
El nombre del fichero a partir del cual importar las definiciones de funciones y clases

`flags`  
Una operación a nivel de bits de la familia de constantes [`RUNKIT7_IMPORT_*`](#runkit7.constants).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
