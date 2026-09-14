---
title: SQLite3::openBlob
description: Abre un flujo de recurso para leer un BLOB
source_url: https://www.php.net/manual/es/sqlite3.openblob.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3/openblob.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: false
translation_revision: 855bfee2f
order: 85780
---

SQLite3::openBlob

Abre un flujo de recurso para leer un BLOB

## Descripción

```php
public SQLite3::openBlob(string $table, string $column, int $rowid, [string $database], [int $flags]): resource
```php

Abre un flujo de recurso para leer o escribir un BLOB, que sería seleccionado por:

SELECT `column` FROM `database`.`table` WHERE rowid = `rowid`

> [!NOTE]
> No es posible cambiar el tamaño de un BLOB escribiendo en el flujo. En su lugar, una declaración UPDATE debe ser ejecutada, utilizando, eventualmente, la función zeroblob() de SQLite para definir el tamaño del BLOB deseado.

## Parámetros

`table`  
El nombre de la tabla.

`column`  
El nombre de la columna.

`rowid`  
La ID de la fila.

`database`  
El nombre simbólico de la base de datos.

`flags`  
O bien `SQLITE3_OPEN_READONLY` o `SQLITE3_OPEN_READWRITE` para abrir el flujo en modo de solo lectura o de lectura y escritura, respectivamente.

## Valores devueltos

Devuelve un recurso de flujo, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.2.0 | El argumento `flags` fue añadido, permitiendo escribir BLOBs; anteriormente solo la lectura era soportada. |

## Ejemplos

Ejemplo con `SQLite3::openBlob`

```
<?php
$conn = new SQLite3(':memory:');
$conn->exec('CREATE TABLE test (text text)');
$conn->exec("INSERT INTO test VALUES ('Lorem ipsum')");
$stream = $conn->openBlob('test', 'text', 1);
echo stream_get_contents($stream);
fclose($stream); // obligatorio, de lo contrario la siguiente línea fallaría
$conn->close();
?>

    
```php

El ejemplo anterior mostrará:

    Lorem ipsum

Escribir progresivamente un BLOB

```
<?php
$conn = new SQLite3(':memory:');
$conn->exec('CREATE TABLE test (text text)');
$conn->exec("INSERT INTO test VALUES (zeroblob(36))");
$stream = $conn->openBlob('test', 'text', 1, 'main', SQLITE3_OPEN_READWRITE);
for ($i = 0; $i < 3; $i++) {
    fwrite($stream,  "Lorem ipsum\n");
}
fclose($stream);
echo $conn->querySingle("SELECT text FROM test");
$conn->close();
?>

    
```php

El ejemplo anterior mostrará:

    Lorem ipsum
    Lorem ipsum
    Lorem ipsum
