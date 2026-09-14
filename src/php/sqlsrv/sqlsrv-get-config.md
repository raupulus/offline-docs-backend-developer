---
title: sqlsrv_get_config
description: Devuelve el valor de la configuración especificada
source_url: https://www.php.net/manual/es/function.sqlsrv-get-config.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlsrv/functions/sqlsrv-get-config.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlsrv
translation_status: ready
translation_reviewed: false
translation_revision: c758e862c
order: 86210
---

sqlsrv_get_config

Devuelve el valor de la configuración especificada

## Descripción

```php
sqlsrv_get_config(string $setting): mixed
```php

Devuelve el valor de la configuración especificada.

## Parámetros

`setting`  
El nombre de la configuración para la cual se devolverá el valor. Para una lista de las configuraciones, ver la función `sqlsrv_configure`.

## Valores devueltos

Devuelve el valor de la configuración solicitada. Si se proporciona una configuración no válida, se devolverá `false`.

## Véase también

sqlsrv_configure
