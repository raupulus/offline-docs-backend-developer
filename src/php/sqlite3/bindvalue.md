---
title: SQLite3Stmt::bindValue
description: Asocia el valor de un parámetro a una variable de declaración
source_url: https://www.php.net/manual/es/sqlite3stmt.bindvalue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3stmt/bindvalue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: true
translation_revision: 525aa5f19
order: 85950
---

SQLite3Stmt::bindValue

Asocia el valor de un parámetro a una variable de declaración

## Descripción

```php
public SQLite3Stmt::bindValue(string $param, mixed $value, [int $type]): bool
```php

Asocia el valor de un parámetro a una variable de declaración.

> [!CAUTION]
> Antes de PHP 7.2.14 y 7.3.0, respectivamente, una vez que la declaración ha sido ejecutada SQLite3Stmt::reset debe ser llamado para poder cambiar el valor de los parámetros asociados.

## Parámetros

`param`  
Puede ser un `string` (para parámetros nombrados) o un `int` (para parámetros posicionales) que identifica la variable de declaración a la cual el valor debe ser asociado. Si un parámetro nombrado no comienza con un carácter "dos puntos" (`:`) o un arroba (`@`), "dos puntos" (`:`) serán automáticamente prefijados. Los parámetros posicionales comienzan con `1`.

`value`  
El valor a asociar a la variable de declaración.

`type`  
El tipo de datos del valor a asociar.

- `SQLITE3_INTEGER` : El valor es un entero firmado, almacenado en 1, 2, 3, 4, 6, o 8 bytes, según la magnitud del valor.

- `SQLITE3_FLOAT` : El valor es un número de punto flotante, almacenado en 8 bytes.

- `SQLITE3_TEXT` : El valor es texto, almacenado utilizando la codificación de la base de datos (UTF-8, UTF-16BE o UTF-16-LE).

- `SQLITE3_BLOB` : El valor es un BLOB, almacenado exactamente de la forma en que fue proporcionado.

- `SQLITE3_NULL` : El valor es la valor NULL.

A partir de PHP 7.0.7, si `type` es omitido, es automáticamente detectado desde el tipo de `value` : `bool` y `int` son tratados como `SQLITE3_INTEGER`, `float` como `SQLITE3_FLOAT`, `null` como `SQLITE3_NULL` y todos los demás como `SQLITE3_TEXT`. Anteriormente, si `type` era omitido, era por omisión `SQLITE3_TEXT`.

> [!NOTE]
> Si `value` es `null`, siempre fue tratado como `SQLITE3_NULL`, independientemente del `type` proporcionado.

## Valores devueltos

Retorna `true` si el valor fue asociado a la variable de declaración, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                                 |
|---------|---------------------------------------------|
| 7.4.0   | `param` ahora soporta la notación `@param`. |

## Ejemplos

Ejemplo con `SQLite3Stmt::bindValue`

```
<?php
$db = new SQLite3(':memory:');

$db->exec('CREATE TABLE foo (id INTEGER, bar STRING)');
$db->exec("INSERT INTO foo (id, bar) VALUES (1, 'Esto es una prueba')");

$stmt = $db->prepare('SELECT bar FROM foo WHERE id=:id');
$stmt->bindValue(':id', 1, SQLITE3_INTEGER);

$result = $stmt->execute();
var_dump($result->fetchArray(SQLITE3_ASSOC));
?>

    
```php

El ejemplo anterior mostrará:

```
array(1) {
  ["bar"]=>
  string(18) "Esto es una prueba"
}

    
```php

## Véase también

SQLite3Stmt::bindParam

SQLite3::prepare
