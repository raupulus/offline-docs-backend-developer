---
title: bzclose
description: Cierra un fichero bzip2
source_url: https://www.php.net/manual/es/function.bzclose.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bzip2/functions/bzclose.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bzip2
translation_status: ready
translation_revision: 5fdeb11b1
order: 6400
---

bzclose

Cierra un fichero bzip2

## Descripción

```php
bzclose(resource $bz): bool
```php

Cierra el dado puntero del fichero bzip2.

## Parámetros

`bz`  
El puntero del fichero. Debe ser un puntero válido a un fichero abierto con `bzopen` satisfactoriamente.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

bzopen
