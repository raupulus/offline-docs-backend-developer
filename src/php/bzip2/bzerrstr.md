---
title: bzerrstr
description: Devuelve una cadena de error de bzip2
source_url: https://www.php.net/manual/es/function.bzerrstr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bzip2/functions/bzerrstr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bzip2
translation_status: ready
translation_revision: 5fdeb11b1
order: 6450
---

bzerrstr

Devuelve una cadena de error de bzip2

## Descripción

```php
bzerrstr(resource $bz): string
```php

Obtiene la cadena de error de cualquier error bzip2 devuelto por el puntero dado.

## Parámetros

`bz`  
El puntero del fichero. Debe ser un puntero a un fichero abierto con `bzopen` satisfactoriamente.

## Valores devueltos

Devuelve una cadena que contiene el mensaje de error.

## Véase también

bzerrno

bzerror
