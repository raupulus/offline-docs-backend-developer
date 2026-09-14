---
title: Pdo\Pgsql::copyFromArray
description: Copia datos de un array PHP a una tabla
source_url: https://www.php.net/manual/es/pdo-pgsql.copyfromarray.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_pgsql/pdo/pgsql/copyfromarray.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_pgsql
translation_status: ready
translation_reviewed: true
translation_revision: 205c3b8ad
order: 62490
---

Pdo\Pgsql::copyFromArray

Copia datos de un array PHP a una tabla

## Descripción

```php
public Pdo\Pgsql::copyFromArray(string $tableName, array $rows, [string $separator], [string $nullAs], [string $fields]): bool
```php

Copia datos del array `rows` a la tabla `tableName` utilizando `separator` como delimitador de campos y la lista `fields`.

## Parámetros

`tableName`  
Una cadena de caracteres que contiene el nombre de la tabla.

`rows`  
Un `array` indexado (o `Traversable`) de `string`s con los campos separados por `separator`.

`separator`  
Un delimitador utilizado para separar los campos en una entrada del array `rows`.

`nullAs`  
Cómo interpretar los valores `NULL`.

`fields`  
La lista de campos a insertar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | `rows` ahora también acepta un `Traversable`; anteriormente sólo se aceptaba un `array`. |

## Ejemplos

Ejemplo de Pdo\Pgsql::copyFromArray

Cada elemento de `rows` es un registro cuyos campos se unen mediante `separator` (un tabulador por omisión).

```
<?php
$db = new Pdo\Pgsql('pgsql:dbname=test host=localhost', $user, $pass);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$db->exec('CREATE TABLE fruits (id int, name text, qty int)');

$rows = [
    "1\tapple\t10",
    "2\tbanana\t20",
    "3\tcherry\t30",
];
$db->copyFromArray('fruits', $rows);

foreach ($db->query('SELECT * FROM fruits ORDER BY id') as $row) {
    echo "{$row['id']} {$row['name']} {$row['qty']}\n";
}
?>

   
```php

El ejemplo anterior mostrará:

    1 apple 10
    2 banana 20
    3 cherry 30

## Véase también

Pdo\Pgsql::copyToArray

Pdo\Pgsql::copyFromFile

Pdo\Pgsql::copyToFile
