---
title: ftp_append
description: Añade el contenido de un fichero a otro fichero en el servidor FTP
source_url: https://www.php.net/manual/es/function.ftp-append.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-append.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: false
translation_revision: 4d1c34c9b
order: 24360
---

ftp_append

Añade el contenido de un fichero a otro fichero en el servidor FTP

## Descripción

```php
ftp_append(FTP\Connection $ftp, string $remote_filename, string $local_filename, [int $mode]): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`ftp`  
Una instancia de `FTP\Connection`.

`remote_filename`  
El nombre del fichero remoto al que se añadirá el contenido.

`local_filename`  
El nombre del fichero local cuyo contenido se añadirá al fichero remoto.

`mode`  
El modo de transferencia. Debe ser `FTP_ASCII` o `FTP_BINARY`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |
