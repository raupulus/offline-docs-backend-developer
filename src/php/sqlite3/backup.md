---
title: SQLite3::backup
description: Realiza una copia de seguridad de una base de datos en otra base de datos
source_url: https://www.php.net/manual/es/sqlite3.backup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3/backup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: false
translation_revision: 855bfee2f
order: 85620
---

SQLite3::backup

Realiza una copia de seguridad de una base de datos en otra base de datos

## Descripción

```php
public SQLite3::backup(SQLite3 $destination, [string $sourceDatabase], [string $destinationDatabase]): bool
```php

SQLite3::backup copia el contenido de una base de datos en otra, sobrescribiendo el contenido de la base de datos de destino. Esto es útil para crear copias de seguridad de bases de datos o para copiar bases de datos en memoria hacia o desde ficheros persistentes.

> [!TIP]
> Desde SQLite 3.27.0 (2019-02-07), también es posible utilizar la instrucción `VACUUM INTO 'file.db';` para guardar la base de datos en un nuevo fichero.

## Parámetros

`destination`  
Una conexión a una base de datos SQLite3 abierta con SQLite3::open.

`sourceDatabase`  
El nombre de la base de datos es `"main"` para la base de datos principal, `"temp"` para la base de datos temporal, o el nombre especificado después del mot-clé `AS` en una instrucción `ATTACH` para una base de datos adjunta.

`destinationDatabase`  
Análogo a `sourceDatabase` pero para la `destination`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Realizar una copia de seguridad de una base de datos existente

```
<?php
// $conn es una conexión a una base de datos sqlite3 ya abierta

$backup = new SQLite3('backup.sqlite');
$conn->backup($backup);
?>

   
```php
