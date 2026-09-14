---
title: bzerrno
description: Devuelve el número de erro de bzip2
source_url: https://www.php.net/manual/es/function.bzerrno.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bzip2/functions/bzerrno.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bzip2
translation_status: ready
translation_revision: 5fdeb11b1
order: 6430
---

bzerrno

Devuelve el número de erro de bzip2

## Descripción

```php
bzerrno(resource $bz): int
```php

Devuelve el número de error de cualquier error bzip2 devuelto por el puntero del fichero dado.

## Parámetros

`bz`  
El puntero del fichero. Debe ser un puntero a un fichero abierto con `bzopen` satisfactoriamente.

## Valores devueltos

Devuelve el número de error como entero.

## Véase también

bzerror

bzerrstr
