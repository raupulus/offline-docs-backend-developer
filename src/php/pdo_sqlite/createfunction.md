---
title: Pdo\Sqlite::createFunction
description: Registra una función de usuario para su uso en las sentencias SQL
source_url: https://www.php.net/manual/es/pdo-sqlite.createfunction.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_sqlite/pdo/sqlite/createfunction.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_sqlite
translation_status: ready
translation_reviewed: true
translation_revision: 28930349c
order: 62730
---

Pdo\Sqlite::createFunction

Registra una función de usuario para su uso en las sentencias SQL

## Descripción

```php
public Pdo\Sqlite::createFunction(string $function_name, callable $callback, [int $num_args], [int $flags]): bool
```php

Este método permite que las funciones PHP sean registradas con SQLite como funciones definidas por el usuario, de modo que puedan ser llamadas en las consultas SQL. La función definida puede ser utilizada en cualquier consulta SQL que permita llamadas a funciones, por ejemplo `SELECT`, `UPDATE`, o disparadores.

> [!TIP]
> Utilizando este método, es posible reemplazar las funciones SQL nativas.

## Parámetros

`function_name`  
El nombre de la función utilizado en las sentencias SQL.

`callback`  
La retrollamada para gestionar la función SQL definida.

> [!NOTE]
> La retrollamada debe retornar un tipo comprendido por SQLite (es decir, [tipo escalar](#language.types.intro)).

Esta función debe ser definida como:

```php
callback(mixed $value, mixed ...$values): mixed
```

`value`  
El primer argumento pasado a la función SQL.

`values`  
Los argumentos adicionales pasados a la función SQL.

`num_args`  
El número de argumentos que la función SQL toma. Si este parámetro es `-1`, entonces la función SQL puede tomar cualquier número de argumentos.

`flags`  
Una máscara de bits de flags. Actualmente, solo `Pdo\Sqlite::DETERMINISTIC` es soportado, lo que especifica que la función retorna siempre el mismo resultado dados los mismos valores de entrada en una sola sentencia SQL.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de Pdo\Sqlite::createFunction

En este ejemplo, tenemos una función que calcula la suma SHA256 de una string, luego la invierte. Cuando la sentencia SQL es ejecutada, retorna el valor del nombre de fichero transformado por nuestra función. Los datos retornados en `$rows` contienen el resultado procesado.

La ventaja de esta técnica es que no es necesario procesar el resultado utilizando un bucle [`foreach`](#control-structures.foreach) después de la ejecución de la consulta.

```php
<?php
function sha256_and_reverse($string)
{
    return strrev(hash('sha256', $string));
}

$db = new Pdo\Sqlite('sqlite::sqlitedb');
$db->createFunction('sha256rev', 'sha256_and_reverse', 1);
$rows = $db->query('SELECT sha256rev(filename) FROM files')->fetchAll();
?>

   
```

## Véase también

Pdo\Sqlite::createAggregate

Pdo\Sqlite::createCollation

sqlite_create_function

sqlite_create_aggregate
