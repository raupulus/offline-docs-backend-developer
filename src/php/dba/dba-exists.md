---
title: dba_exists
description: Verifica si una clave DBA existe
source_url: https://www.php.net/manual/es/function.dba-exists.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dba/functions/dba-exists.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dba
translation_status: ready
translation_revision: b5fce74a6
order: 11540
---

dba_exists

Verifica si una clave DBA existe

## Descripción

```php
dba_exists(string $key, Dba\Connection $dba): bool
```php

`dba_exists` verifica si la `key` especificada existe en la base de datos.

## Parámetros

`key`  
La clave a verificar.

`dba`  
Una instancia de `Dba\Connection`, devuelta por `dba_open` o `dba_popen`.

## Valores devueltos

Retorna `true` si la clave existe, `false` en caso contrario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | El parámetro `dba` ahora espera una instancia de `Dba\Connection` ; anteriormente, se esperaba un `resource` `dba` válido. |

## Véase también

dba_delete

dba_fetch

dba_insert

dba_replace
