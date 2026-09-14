---
title: yaz_close
description: Cierra una conexión YAZ
source_url: https://www.php.net/manual/es/function.yaz-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaz/functions/yaz-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaz
translation_status: ready
translation_revision: 96c9d88ba
order: 107770
---

yaz_close

Cierra una conexión YAZ

## Descripción

```php
yaz_close(resource $id): bool
```php

Cierra la conexión dada por un parámetro `id`.

> [!NOTE]
> Esta función va solo a cerrar una conexión no persistente abierta por estableciendo la opción de `persistent` a `false` con `yaz_connect`.

## Parámetros

`id`  
El recurso de conexión retornado por `yaz_connect`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`yaz_connect`
