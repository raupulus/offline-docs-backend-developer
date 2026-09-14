---
title: dba_firstkey
description: Lee la primera clave DBA
source_url: https://www.php.net/manual/es/function.dba-firstkey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dba/functions/dba-firstkey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dba
translation_status: ready
translation_revision: b5fce74a6
order: 11560
---

dba_firstkey

Lee la primera clave DBA

## Descripción

```php
dba_firstkey(Dba\Connection $dba): string
```php

`dba_firstkey` devuelve la primera clave de la base de datos y reinicia el puntero interno de clave. Esto permite una búsqueda lineal a través de toda la base de datos.

## Parámetros

`dba`  
Una instancia de `Dba\Connection`, devuelta por `dba_open` o `dba_popen`.

## Valores devueltos

Devuelve la clave en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | El parámetro `dba` ahora espera una instancia de `Dba\Connection` ; anteriormente, se esperaba un `resource` `dba` válido. |

## Véase también

dba_nextkey

dba_key_split

Ejemplo 2 en los

ejemplos DBA
