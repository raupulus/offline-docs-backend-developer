---
title: ps_open_file
description: Abrir un fichero para su impresión
source_url: https://www.php.net/manual/es/function.ps-open-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-open-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 65890
---

ps_open_file

Abrir un fichero para su impresión

## Descripción

```php
ps_open_file(resource $psdoc, [string $filename]): bool
```php

Crea un fichero en disco y escribe el documento PostScript en él. El fichero será cerrado cuando se llame a la función `ps_close`.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`filename`  
El nombre del fichero postscript. Si no se proporciona `filename` el documento será creado en memoria y todas las salidas irán directas al visualizador.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_close`
