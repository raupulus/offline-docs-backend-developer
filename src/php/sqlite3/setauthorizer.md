---
title: SQLite3::setAuthorizer
description: Configura una función de retrollamada para utilizar como autorizador
  para limitar lo que una sentencia puede hacer
source_url: https://www.php.net/manual/es/sqlite3.setauthorizer.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3/setauthorizer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: false
translation_revision: 22583751f
order: 85820
---

SQLite3::setAuthorizer

Configura una función de retrollamada para utilizar como autorizador para limitar lo que una sentencia puede hacer

## Descripción

```php
public SQLite3::setAuthorizer(callable $callback): bool
```php

Define una función de retrollamada que será llamada por SQLite cada vez que se realiza una acción (lectura, eliminación, actualización, etc.). Esto se utiliza durante la preparación de una sentencia SQL a partir de una fuente no confiable para asegurarse de que las sentencias SQL no intenten acceder a datos a los que no están autorizadas a acceder, o que no intenten ejecutar sentencias maliciosas que dañen la base de datos. Por ejemplo, una aplicación puede autorizar a un usuario a introducir consultas SQL arbitrarias para evaluación por una base de datos. Pero la aplicación no quiere que el usuario pueda realizar modificaciones arbitrarias en la base de datos. Un autorizador podría entonces establecerse mientras el SQL introducido por el usuario es preparado para prohibir todo excepto las declaraciones SELECT.

La función de retrollamada del autorizador puede ser llamada varias veces para cada sentencia preparada por SQLite. Una consulta `SELECT` o `UPDATE` llamará al autorizador para cada columna que sería leída o actualizada.

La función de retrollamada del autorizador es llamada con hasta cinco parámetros. El primer parámetro siempre es proporcionado, y es un `int` (código de acción) correspondiente a una constante de `SQLite3`. Los otros parámetros solo se pasan para ciertas acciones. La tabla siguiente describe los parámetros segundo y tercero según la acción:

| Acción | Segundo parámetro | Tercer parámetro |
|----|----|----|
| `SQLite3::CREATE_INDEX` | Nombre del índice | Nombre de la tabla |
| `SQLite3::CREATE_TABLE` | Nombre de la tabla | `null` |
| `SQLite3::CREATE_TEMP_INDEX` | Nombre del índice | Nombre de la tabla |
| `SQLite3::CREATE_TEMP_TABLE` | Nombre de la tabla | `null` |
| `SQLite3::CREATE_TEMP_TRIGGER` | Nombre del disparador | Nombre de la tabla |
| `SQLite3::CREATE_TEMP_VIEW` | Nombre de la vista | `null` |
| `SQLite3::CREATE_TRIGGER` | Nombre del disparador | Nombre de la tabla |
| `SQLite3::CREATE_VIEW` | Nombre de la vista | `null` |
| `SQLite3::DELETE` | Nombre de la tabla | `null` |
| `SQLite3::DROP_INDEX` | Nombre del índice | Nombre de la tabla |
| `SQLite3::DROP_TABLE` | Nombre de la tabla | `null` |
| `SQLite3::DROP_TEMP_INDEX` | Nombre del índice | Nombre de la tabla |
| `SQLite3::DROP_TEMP_TABLE` | Nombre de la tabla | `null` |
| `SQLite3::DROP_TEMP_TRIGGER` | Nombre del disparador | Nombre de la tabla |
| `SQLite3::DROP_TEMP_VIEW` | Nombre de la vista | `null` |
| `SQLite3::DROP_TRIGGER` | Nombre del disparador | Nombre de la tabla |
| `SQLite3::DROP_VIEW` | Nombre de la vista | `null` |
| `SQLite3::INSERT` | Nombre de la tabla | `null` |
| `SQLite3::PRAGMA` | Nombre Pragma | El primer argumento pasado al pragma, o `null` |
| `SQLite3::READ` | Nombre de la tabla | Nombre de la columna |
| `SQLite3::SELECT` | `null` | `null` |
| `SQLite3::TRANSACTION` | Operación | `null` |
| `SQLite3::UPDATE` | Nombre de la tabla | Nombre de la columna |
| `SQLite3::ATTACH` | Nombre de fichero | `null` |
| `SQLite3::DETACH` | Nombre de la base de datos | `null` |
| `SQLite3::ALTER_TABLE` | Nombre de la base de datos | Nombre de la tabla |
| `SQLite3::REINDEX` | Nombre del índice | `null` |
| `SQLite3::ANALYZE` | Nombre de la tabla | `null` |
| `SQLite3::CREATE_VTABLE` | Nombre de la tabla | Nombre del módulo |
| `SQLite3::DROP_VTABLE` | Nombre de la tabla | Nombre del módulo |
| `SQLite3::FUNCTION` | `null` | Nombre de la función |
| `SQLite3::SAVEPOINT` | Operación | Nombre del punto de guardado |
| `SQLite3::RECURSIVE` | `null` | `null` |

Lista de códigos de acción y parámetros

El cuarto parámetro será el nombre de la base de datos (`"main"`, `"temp"`, etc.) si es aplicable.

El quinto parámetro de la función de retrollamada del autorizador es el nombre del disparador o de la vista más interno que es responsable del intento de acceso o `null` si este intento de acceso proviene directamente del código SQL de nivel superior.

Cuando la función de retrollamada devuelve `SQLite3::OK`, significa que la operación solicitada es aceptada. Cuando la función de retrollamada devuelve `SQLite3::DENY`, la llamada que provocó el autorizador fallará con un mensaje de error explicando que el acceso es denegado.

Si el código de acción es `SQLite3::READ` y la función de retrollamada devuelve `SQLite3::IGNORE`, entonces la sentencia preparada se construye para sustituir un valor `null` en lugar de la columna de la tabla que se habría leído si `SQLite3::OK` se hubiera devuelto. Devolver `SQLite3::IGNORE` puede ser utilizado para denegar a un usuario no confiable el acceso a columnas individuales de una tabla.

Cuando una tabla es referenciada por un `SELECT` pero no se extrae ningún valor de columna de esa tabla (por ejemplo en una consulta como `"SELECT count(*) FROM table"`), entonces la función de retrollamada del autorizador se invoca una vez para esa tabla con un nombre de columna que es una cadena vacía.

Si el código de acción es `SQLite3::DELETE` y la función de retrollamada devuelve `SQLite3::IGNORE`, entonces la operación DELETE continúa pero la optimización de truncamiento es desactivada y todas las filas se eliminan individualmente.

Solo un autorizador puede estar activo en una conexión de base de datos a la vez. Cada llamada a SQLite3::setAuthorizer reemplaza la llamada anterior. Desactive el autorizador instalando una retrollamada `null`. El autorizador está desactivado por omisión.

La función de retrollamada del autorizador no debe hacer nada que modifique la conexión de base de datos que ha invocado la función de retrollamada del autorizador.

Es importante señalar que el autorizador solo se llama cuando una sentencia es preparada, no cuando es ejecutada.

Más detalles pueden encontrarse en la [documentación de SQLite3](http://sqlite.org/c3ref/set_authorizer.html).

## Parámetros

`callback`  
El `callable` a llamar.

Si se pasa `null`, esto desactivará la retrollamada del autorizador actual.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Este método no lanza ningún error, pero si un autorizador está activado y devuelve un valor inválido, la preparación de la sentencia lanzará un error (o una excepción, según el uso del método SQLite3::enableExceptions).

## Ejemplos

Ejemplo de SQLite3::setAuthorizer

Esto solo autoriza el acceso de lectura, y solo ciertas columnas de la tabla `users` serán devueltas. Las otras columnas serán reemplazadas por `null`.

```
<?php
$db = new SQLite3('data.sqlite');
$db->exec('CREATE TABLE users (id, name, password);');
$db->exec('INSERT INTO users VALUES (1, \'Pauline\', \'Snails4eva\');');

$allowed_columns = ['id', 'name'];

$db->setAuthorizer(function (int $action, ...$args) use ($allowed_columns) {
    if ($action === SQLite3::READ) {
        list($table, $column) = $args;

        if ($table === 'users' && in_array($column, $allowed_columns)) {
            return SQLite3::OK;
        }

        return SQLite3::IGNORE;
    }

    return SQLite3::DENY;
});

print_r($db->querySingle('SELECT * FROM users WHERE id = 1;'));

   
```php

El ejemplo anterior mostrará:

    Array
    (
        [id] => 1
        [name] => Pauline
        [password] =>
    )
