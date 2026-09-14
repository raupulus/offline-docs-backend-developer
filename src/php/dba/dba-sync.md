---
title: dba_sync
description: Sincroniza una base de datos DBA
source_url: https://www.php.net/manual/es/function.dba-sync.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dba/functions/dba-sync.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dba
translation_status: ready
translation_revision: b5fce74a6
order: 11660
---

dba_sync

Sincroniza una base de datos DBA

## Descripción

```php
dba_sync(Dba\Connection $dba): bool
```php

`dba_sync` sincroniza la base de datos. Esto probablemente iniciará una escritura física en el disco, si es admisible.

## Parámetros

`dba`  
Una instancia de `Dba\Connection`, devuelta por `dba_open` o `dba_popen`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | El parámetro `dba` ahora espera una instancia de `Dba\Connection` ; anteriormente, se esperaba un `resource` `dba` válido. |

## Véase también

dba_optimize
