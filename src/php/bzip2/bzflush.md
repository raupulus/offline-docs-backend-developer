---
title: bzflush
description: No realiza ninguna acción
source_url: https://www.php.net/manual/es/function.bzflush.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bzip2/functions/bzflush.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bzip2
translation_status: ready
translation_reviewed: true
translation_revision: 5fdeb11b1
order: 6460
---

bzflush

No realiza ninguna acción

## Descripción

```php
bzflush(resource $bz): bool
```php

Esta función está diseñada para forzar la escritura de todos los datos bzip2 almacenados en el búfer para el puntero de archivo representado por `bz`, pero está implementada como una función nula en libbz2, por lo que no realiza ninguna acción.

## Parámetros

`bz`  
El puntero de archivo. Debe ser válido y debe apuntar a un archivo abierto con éxito por la función `bzopen`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

bzread

bzwrite
