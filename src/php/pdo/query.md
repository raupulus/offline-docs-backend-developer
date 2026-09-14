---
title: PDO::query
description: Prepara y ejecuta una consulta SQL sin marcadores de sustitución
source_url: https://www.php.net/manual/es/pdo.query.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdo/query.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: false
translation_revision: 082ddc19f
order: 61940
---

PDO::query

Prepara y ejecuta una consulta SQL sin marcadores de sustitución

## Descripción

```php
public PDO::query(string $query, [int $fetchMode]): PDOStatement
```php

```php
public PDO::query(string $query, [int $fetchMode], int $colno): PDOStatement
```

```php
public PDO::query(string $query, [int $fetchMode], string $classname, array $constructorArgs): PDOStatement
```php

```php
public PDO::query(string $query, [int $fetchMode], object $object): PDOStatement
```

PDO::query prepara y ejecuta una consulta SQL en una sola llamada de función, retornando la consulta como objeto `PDOStatement`.

Para una consulta que debe ejecutarse varias veces, se obtendrán mejores resultados si se prepara el objeto `PDOStatement` utilizando la función PDO::prepare y se ejecuta la consulta mediante múltiples llamadas a la función PDOStatement::execute.

Si no se recuperan todos los datos del conjunto de resultados antes de ejecutar la siguiente llamada a PDO::query, la llamada puede fallar. Llamar a PDOStatement::closeCursor para liberar los recursos de la base de datos asociados al objeto `PDOStatement` antes de ejecutar la siguiente llamada a la función PDO::query.

> [!NOTE]
> Si `query` contiene marcadores de sustitución, la consulta debe prepararse y ejecutarse por separado utilizando las funciones PDO::prepare y PDOStatement::execute.

## Parámetros

`query`  
La consulta SQL a preparar y ejecutar.

Si el SQL contiene marcadores de sustitución, PDO::prepare y PDOStatement::execute deben ser utilizados en su lugar. Alternativamente, el SQL puede ser preparado manualmente antes de llamar a PDO::query, con los datos correctamente formateados utilizando PDO::quote si el controlador lo soporta.

`fetchMode`  
El modo de recuperación por omisión para el `PDOStatement` retornado. Esto debe ser una de las constantes [`PDO::FETCH_*`](#pdo.constants).

Si este argumento es pasado a la función, el resto de los argumentos serán tratados como si PDOStatement::setFetchMode hubiera sido llamado sobre el objeto de la consulta resultante. Los argumentos siguientes dependen del modo de recuperación seleccionado.

## Valores devueltos

Retorna un objeto `PDOStatement` o `false` si ocurre un error.

## Errores/Excepciones

Emite un error de nivel `E_WARNING` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_WARNING`.

Lanza una excepción `PDOException` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_EXCEPTION`.

## Ejemplos

SQL sin marcadores de sustitución puede ser ejecutado utilizando PDO::query

```php
<?php
$sql =  'SELECT name, color, calories FROM fruit ORDER BY name';
foreach  ($conn->query($sql) as $row) {
    print $row['name'] . "\t";
    print  $row['color'] . "\t";
    print $row['calories'] . "\n";
}
?>

    
```

El ejemplo anterior mostrará:

    apple   red     150
    banana  yellow  250
    kiwi    brown   75
    lemon   yellow  25
    orange  orange  300
    pear    green   150
    watermelon      pink    90

## Véase también

PDO::exec, PDO::prepare, PDOStatement::execute
