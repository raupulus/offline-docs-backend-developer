---
title: dio_stat
description: Consulta información de estado del descriptor de fichero fd
source_url: https://www.php.net/manual/es/function.dio-stat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dio/functions/dio-stat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dio
translation_status: ready
translation_revision: e41806c30
order: 11900
---

dio_stat

Consulta información de estado del descriptor de fichero fd

## Descripción

```php
dio_stat(resource $fd): array
```php

`dio_stat` devuelve información sobre el descriptor de fichero proporcionado.

## Parámetros

`fd`  
Descriptor de fichero devuelto por `dio_open`.

## Valores devueltos

Devuelve un array asociativo con las siguientes claves:

- "device" - dispositivo

- "inode" - nodo-i

- "mode" - modo

- "nlink" - número de enlaces duros

- "uid" - id de usuario

- "gid" - id de grupo

- "device_type" - tipo de dispositivo (si es un nodo-i de dispositivo)

- "size" - tamaño total en bytes

- "blocksize" - tamaño de bloque

- "blocks" - número de bloques asignados

- "atime" - fecha de último acceso

- "mtime" - fecha de última modificación

- "ctime" - fecha de último cambio

En caso de error, `dio_stat` devuelve `null`.
