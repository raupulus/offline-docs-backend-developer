---
title: cubrid_set_query_timeout
description: Define el tiempo máximo de ejecución de una consulta
source_url: https://www.php.net/manual/es/function.cubrid-set-query-timeout.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-set-query-timeout.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9520
---

cubrid_set_query_timeout

Define el tiempo máximo de ejecución de una consulta

## Descripción

```php
cubrid_set_query_timeout(resource $req_identifier, int $timeout): bool
```php

La función `cubrid_set_query_timeout` se utiliza para definir el tiempo máximo de ejecución de una consulta.

## Parámetros

`req_identifier`  
Identificador de consulta.

`timeout`  
Tiempo máximo, en milisegundos.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

cubrid_get_query_timeout
