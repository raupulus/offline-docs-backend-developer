---
title: dba_fetch
description: Lee los datos asociados a una clave DBA
source_url: https://www.php.net/manual/es/function.dba-fetch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dba/functions/dba-fetch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dba
translation_status: ready
translation_revision: b5fce74a6
order: 11550
---

dba_fetch

Lee los datos asociados a una clave DBA

## Descripción

```php
dba_fetch(string $key, Dba\Connection $dba, [int $skip]): string
```php

Firma sobrecargada obsoleta a partir de 8.3.0:

```php
dba_fetch(string $key, int $skip, resource $dba): string
```

`dba_fetch` lee los datos especificados por la clave `key` en la base identificada por `dba`.

## Parámetros

`key`  
La clave correspondiente a los datos.

> [!NOTE]
> Al trabajar con ficheros .ini, esta función acepta arrays como claves donde el índice 0 es el grupo y el índice 1 es el nombre del valor. Ver la función `dba_key_split`.

`dba`  
Una instancia de `Dba\Connection`, devuelta por `dba_open` o `dba_popen`.

`skip`  
El número de pares clave-valor a ignorar al utilizar bases de datos cdb. Este valor es ignorado para todas las demás bases de datos que no admiten claves múltiples con el mismo nombre.

## Valores devueltos

Devuelve la cadena asociada si se encuentra el par clave/valor, `false` en caso contrario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | El parámetro `dba` ahora espera una instancia de `Dba\Connection` ; anteriormente, se esperaba un `resource` `dba` válido. |
| 8.3.0 | La llamada a `dba_fetch` con `dba` como tercer argumento es ahora obsoleta. |
| 8.2.0 | El argumento opcional "skip" de la función `dba_fetch` ahora se coloca al final, conforme a la semántica PHP lado-usuario. La firma sobrecargada previamente sigue siendo aceptada pero desaconsejada. |

## Véase también

dba_exists

dba_delete

dba_insert

dba_replace

dba_key_split
