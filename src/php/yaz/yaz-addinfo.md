---
title: yaz_addinfo
description: Devuelve un error adicional de información
source_url: https://www.php.net/manual/es/function.yaz-addinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaz/functions/yaz-addinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaz
translation_status: ready
translation_revision: 96c9d88ba
order: 107740
---

yaz_addinfo

Devuelve un error adicional de información

## Descripción

```php
yaz_addinfo(resource $id): string
```php

Devuelve un error adicional de información para el ultimo requerimiento al servidor.

Con algunos servidores, Ésta función puede devolver la misma cadena como `yaz_error`.

## Parámetros

`id`  
El recurso de conexión devuelto por `yaz_connect`.

## Valores devueltos

Una cadena contiene el error adicional de información o una cadena vacia si la ultima operación fue satisfactoria o si ninguna información fue proporcionada por el servidor.

## Véase también

`yaz_error`, `yaz_errno`
