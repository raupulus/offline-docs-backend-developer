---
title: dba_delete
description: Elimina una línea en una base DBA
source_url: https://www.php.net/manual/es/function.dba-delete.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dba/functions/dba-delete.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dba
translation_status: ready
translation_revision: b5fce74a6
order: 11530
---

dba_delete

Elimina una línea en una base DBA

## Descripción

```php
dba_delete(string $key, Dba\Connection $dba): bool
```php

`dba_delete` elimina la entrada especificada de la base de datos.

## Parámetros

`key`  
La clave de la entrada a eliminar.

`dba`  
Una instancia de `Dba\Connection`, devuelta por `dba_open` o `dba_popen`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | El parámetro `dba` ahora espera una instancia de `Dba\Connection` ; anteriormente, se esperaba un `resource` `dba` válido. |

## Véase también

dba_exists

dba_fetch

dba_insert

dba_replace
