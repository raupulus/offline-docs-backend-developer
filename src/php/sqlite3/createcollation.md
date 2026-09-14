---
title: SQLite3::createCollation
description: Registra una función PHP para utilizarla como función de clasificación
  SQL
source_url: https://www.php.net/manual/es/sqlite3.createcollation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3/createcollation.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: false
translation_revision: 855bfee2f
order: 85680
---

SQLite3::createCollation

Registra una función PHP para utilizarla como función de clasificación SQL

## Descripción

```php
public SQLite3::createCollation(string $name, callable $callback): bool
```php

Registra una función PHP o una función definida por el usuario para utilizarla como función de clasificación en una consulta SQL.

## Parámetros

`name`  
Nombre de la función de clasificación SQL a crear o redefinir.

`callback`  
El nombre de una función PHP o de una función definida por el usuario a aplicar como función de retorno, definiendo el comportamiento de la clasificación. Debe aceptar dos argumentos y retornará lo mismo que la función `strcmp`, es decir debe retornar -1, 1, o 0 si la primera cadena se clasifica antes, después, o es equivalente a la segunda.

Esta función debe ser definida como:

```php
collation(mixed $value1, mixed $value2): int
```

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `SQLite3::createCollation`

Registra la función PHP `strnatcmp` como secuencia de clasificación en la base de datos SQLite3.

```php
<?php

$db = new SQLite3(":memory:");
$db->exec("CREATE TABLE test (col1 string)");
$db->exec("INSERT INTO test VALUES ('a1')");
$db->exec("INSERT INTO test VALUES ('a10')");
$db->exec("INSERT INTO test VALUES ('a2')");

$db->createCollation('NATURAL_CMP', 'strnatcmp');

$defaultSort = $db->query("SELECT col1 FROM test ORDER BY col1");
$naturalSort = $db->query("SELECT col1 FROM test ORDER BY col1 COLLATE NATURAL_CMP");

echo "Por omisión :\n";
while ($row = $defaultSort->fetchArray()){
    echo $row['col1'], "\n";
}

echo "\nNatural :\n";
while ($row = $naturalSort->fetchArray()){
    echo $row['col1'], "\n";
}

$db->close();

?>

    
```

El ejemplo anterior mostrará:

    Por omisión :
    a1
    a10
    a2

    Natural :
    a1
    a2
    a10

## Véase también

La documentación sobre la clasificación SQLite :

http://sqlite.org/datatype3.html#collation
