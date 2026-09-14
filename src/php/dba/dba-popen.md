---
title: dba_popen
description: Establece una conexión persistente a una base de datos DBA
source_url: https://www.php.net/manual/es/function.dba-popen.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dba/functions/dba-popen.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dba
translation_status: ready
translation_revision: b5fce74a6
order: 11640
---

dba_popen

Establece una conexión persistente a una base de datos DBA

## Descripción

```php
dba_popen(string $path, string $mode, [string $handler], [int $permission], [int $map_size], [int $flags]): Dba\Connection
```php

`dba_popen` establece una conexión persistente a la base identificada por `path` con el modo `mode`, utilizando el identificador `handler`.

## Parámetros

`path`  
Ruta en el sistema de ficheros.

`mode`  
Puede ser `r` para solo lectura, `w` para lectura/escritura, `c` para lectura/escritura y creación si la base no existe, y `n` para creación, sobrescritura y acceso en lectura/escritura.

`handler`  
El nombre del [gestor](#dba.requirements) que debe ser utilizado para acceder a `path`. El gestor recibe todos los argumentos adicionales pasados a la función `dba_popen`. Si el argumento `handler` es `null`, entonces se invoca el gestor por defecto.

`permission`  
Argumento opcional de tipo entero (`int`) que se pasa al controlador. Tiene el mismo significado que el argumento `permissions` de la función `chmod`, y su valor por omisión es `0644`.

Los controladores `db1`, `db2`, `db3`, `db4`, `dbm`, `gdbm`, `ndbm` y `lmdb` admiten el argumento `permission`.

`map_size`  
Argumento opcional de tipo `int` que se pasa al controlador. Su valor debe ser un múltiplo de la tamaño de página del sistema operativo, o cero para utilizar el tamaño de mapa por omisión.

El controlador `lmdb` acepta el argumento `map_size`.

`flags`  
Permite pasar banderas a los controladores de base de datos. Actualmente, solo el controlador LMDB con las banderas `DBA_LMDB_USE_SUB_DIR` y `DBA_LMDB_NO_SUB_DIR` es soportado.

## Valores devueltos

Devuelve una instancia de `Dba\Connection` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

El valor `false` es devuelto y un error de nivel `E_WARNING` es emitido cuando el argumento `handler` es `null`, pero no hay ningún gestor por defecto disponible.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Ahora devuelve una instancia de `Dba\Connection`; anteriormente se devolvía un `resource`. |
| 8.2.0 | Se añadió el argumento `flags`. |
| 8.2.0 | El argumento `handler` ahora es nullable. |
| 7.3.14, 7.4.2 | El controlador `lmdb` ahora soporta un argumento adicional `map_size`. |

## Véase también

dba_open

dba_close
