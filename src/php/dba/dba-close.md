---
title: dba_close
description: Cierra una base DBA
source_url: https://www.php.net/manual/es/function.dba-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dba/functions/dba-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dba
translation_status: ready
translation_revision: b5fce74a6
order: 11520
---

dba_close

Cierra una base DBA

## Descripción

```php
dba_close(Dba\Connection $dba): void
```php

`dba_close` cierra la base de datos establecida y libera todos los recursos del gestor de base de datos especificado.

## Parámetros

`dba`  
Una instancia de `Dba\Connection`, devuelta por `dba_open` o `dba_popen`.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | El parámetro `dba` ahora espera una instancia de `Dba\Connection` ; anteriormente, se esperaba un `resource` `dba` válido. |

## Véase también

dba_open

dba_popen
