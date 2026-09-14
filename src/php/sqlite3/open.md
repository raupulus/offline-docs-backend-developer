---
title: SQLite3::open
description: Abre una base de datos SQLite
source_url: https://www.php.net/manual/es/sqlite3.open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3/open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: true
translation_revision: 61374bbe2
order: 85770
---

SQLite3::open

Abre una base de datos SQLite

## Descripción

```php
public SQLite3::open(string $filename, [int $flags], [string $encryptionKey]): void
```php

Abre una base de datos SQLite 3. Si el cifrado fue incluido durante la construcción de la base de datos, la clave correspondiente será utilizada.

## Parámetros

`filename`  
Ruta hacia la base de datos SQLite, o `:memory:` para utilizar la base de datos que se encuentra en la memoria RAM.

`flags`  
Banderas opcionales para determinar la manera de abrir la base de datos SQLite. Por omisión, será `SQLITE3_OPEN_READWRITE | SQLITE3_OPEN_CREATE`.

- `SQLITE3_OPEN_READONLY` : Abre la base de datos en modo solo lectura.

- `SQLITE3_OPEN_READWRITE` : Abre la base de datos en modo lectura y escritura.

- `SQLITE3_OPEN_CREATE` : Crea la base de datos si no existe.

`encryptionKey`  
La clave opcional de cifrado utilizada durante el cifrado/descifrado de la base de datos SQLite. Si el módulo de cifrado de SQLite no está instalado, este parámetro no tendrá ningún efecto.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `SQLite3::open`

```
<?php
/**
 * Ejemplo simple que extiende la clase SQLite3 y cambia los parámetros
 * __construct, luego, utiliza el método de conexión para inicializar la
 * base de datos.
 */
class MyDB extends SQLite3
{
    function __construct()
    {
        $this->open('mysqlitedb.db');
    }
}

$db = new MyDB();

$db->exec('CREATE TABLE foo (bar STRING)');
$db->exec("INSERT INTO foo (bar) VALUES ('Esto es una prueba')");

$result = $db->query('SELECT bar FROM foo');
var_dump($result->fetchArray());
?>

    
```php
