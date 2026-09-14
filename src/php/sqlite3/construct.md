---
title: SQLite3::__construct
description: Instancia un objeto SQLite3 y abre la base de datos SQLite 3
source_url: https://www.php.net/manual/es/sqlite3.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: false
translation_revision: 61374bbe2
order: 85660
---

SQLite3::\_\_construct

Instancia un objeto SQLite3 y abre la base de datos SQLite 3

## Descripción

```php
public SQLite3::__construct(string $filename, [int $flags], [string $encryptionKey])
```php

Inicializa un objeto SQLite3 y abre una conexión a la base de datos SQLite 3. Si el cifrado ha sido incluido durante la compilación, entonces esta función intentará utilizar la clave correspondiente.

## Parámetros

`filename`  
Ruta hacia la base de datos SQLite, o `:memory:` para utilizar la base de datos que se encuentra en la memoria RAM. Si `filename` es una cadena vacía, se creará una base de datos temporal privada en el disco. Esta base de datos privada será automáticamente eliminada tan pronto como la conexión de la base de datos sea cerrada.

`flags`  
Bandera opcional utilizada para determinar la manera de apertura de la base de datos SQLite. Por omisión, la apertura se efectúa utilizando `SQLITE3_OPEN_READWRITE | SQLITE3_OPEN_CREATE`.

- `SQLITE3_OPEN_READONLY` : Abre la base de datos en modo solo lectura.

- `SQLITE3_OPEN_READWRITE` : Abre la base de datos en modo lectura y escritura.

- `SQLITE3_OPEN_CREATE` : Crea la base de datos si no existe.

`encryptionKey`  
Una clave de cifrado opcional, a utilizar durante el cifrado/descifrado de la base de datos SQLite. Si el módulo SQLite no está instalado, este parámetro no tendrá ningún efecto.

## Errores/Excepciones

Lanza una `Exception` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.0.10 | El `filename` puede ahora estar vacío para utilizar una base de datos privada, temporal en disco. |

## Ejemplos

Ejemplo con `SQLite3::__construct`

```
<?php
$db = new SQLite3('mysqlitedb.db');

$db->exec('CREATE TABLE foo (bar TEXT)');
$db->exec("INSERT INTO foo (bar) VALUES ('Esto es una prueba')");

$result = $db->query('SELECT bar FROM foo');
var_dump($result->fetchArray());
?>

    
```php
