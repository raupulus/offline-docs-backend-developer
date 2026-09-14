---
title: SQLite3Stmt::bindParam
description: Asocia un parámetro a una variable de declaración
source_url: https://www.php.net/manual/es/sqlite3stmt.bindparam.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3stmt/bindparam.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: true
translation_revision: 525aa5f19
order: 85940
---

SQLite3Stmt::bindParam

Asocia un parámetro a una variable de declaración

## Descripción

```php
public SQLite3Stmt::bindParam(string $param, mixed $var, [int $type]): bool
```php

Asocia un parámetro a una variable de declaración.

> [!CAUTION]
> Antes de PHP 7.2.14 y 7.3.0, respectivamente, SQLite3Stmt::reset debe ser llamado después del primer llamado a SQLite3Stmt::execute si el valor asociado debe ser actualizado correctamente en los llamados siguientes a SQLite3Stmt::execute. Si SQLite3Stmt::reset no es llamado, los valores asociados no serán modificados, incluso si el valor asignado a la variable pasada a SQLite3Stmt::bindParam ha sido modificado, o SQLite3Stmt::bindParam ha sido llamado nuevamente.

## Parámetros

`param`  
Puede ser un `string` (para parámetros nombrados) o un `int` (para parámetros posicionales) que identifica la variable de declaración a la cual el valor debe ser asociado. Si un parámetro nombrado no comienza con un carácter "dos puntos" (`:`) o un arroba (`@`), "dos puntos" (`:`) serán automáticamente prefijados. Los parámetros posicionales comienzan con `1`.

`var`  
El parámetro a asociar a la variable de declaración.

`type`  
El tipo de datos del parámetro a asociar.

- `SQLITE3_INTEGER` : El valor es un entero firmado, almacenado en 1, 2, 3, 4, 6, o 8 bytes, dependiendo del tamaño del valor.

- `SQLITE3_FLOAT` : El valor es un número de punto flotante, almacenado en 8 bytes.

- `SQLITE3_TEXT` : El valor es texto, almacenado utilizando la codificación de la base de datos (UTF-8, UTF-16BE o UTF-16-LE).

- `SQLITE3_BLOB` : El valor es un BLOB, almacenado exactamente de la forma en que fue proporcionado.

- `SQLITE3_NULL` : El valor es la valor NULL.

A partir de PHP 7.0.7, si `type` es omitido, es automáticamente detectado desde el tipo de `var` : `bool` y `int` son tratados como `SQLITE3_INTEGER`, `float` como `SQLITE3_FLOAT`, `null` como `SQLITE3_NULL` y todos los demás como `SQLITE3_TEXT`. Anteriormente, si `type` era omitido, era por omisión `SQLITE3_TEXT`.

> [!NOTE]
> Si `var` es `null`, siempre fue tratado como `SQLITE3_NULL`, independientemente del `type` proporcionado.

## Valores devueltos

Retorna `true` si el parámetro es asociado a la variable de declaración, `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                                 |
|---------|---------------------------------------------|
| 7.4.0   | `param` ahora soporta la notación `@param`. |

## Ejemplos

Uso de `SQLite3Stmt::bindParam`

Este ejemplo muestra cómo una declaración preparada única con un solo parámetro asociado puede ser utilizada para insertar múltiples filas con valores diferentes.

```
<?php
$db = new SQLite3(':memory:');
$db->exec("CREATE TABLE foo (bar TEXT)");

$stmt = $db->prepare("INSERT INTO foo VALUES (:bar)");
$stmt->bindParam(':bar', $bar, SQLITE3_TEXT);

$bar = 'baz';
$stmt->execute();

$bar = 42;
$stmt->execute();

$res = $db->query("SELECT * FROM foo");
while (($row = $res->fetchArray(SQLITE3_ASSOC))) {
    var_dump($row);
}
?>

    
```php

El ejemplo anterior mostrará:

```
array(1) {
  ["bar"]=>
  string(3) "baz"
}
array(1) {
  ["bar"]=>
  string(2) "42"
}

    
```php

## Véase también

SQLite3Stmt::bindValue

SQLite3::prepare
