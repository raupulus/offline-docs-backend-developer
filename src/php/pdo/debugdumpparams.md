---
title: PDOStatement::debugDumpParams
description: Detalla una instrucción SQL preparada
source_url: https://www.php.net/manual/es/pdostatement.debugdumpparams.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdostatement/debugdumpparams.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: true
translation_revision: 661e6858a
order: 62060
---

PDOStatement::debugDumpParams

Detalla una instrucción SQL preparada

## Descripción

```php
public PDOStatement::debugDumpParams(): bool
```php

Detalla la información contenida en una instrucción preparada, directamente en la salida estándar. La información incluye la consulta `SQL` utilizada, el número de parámetros usados (`Params`), la lista de parámetros, con el nombre de clave o su posición, su nombre, su posición en la consulta (si esta última información no es soportada por el controlador PDO, es siempre -1), un tipo (`param_type`) en forma de entero, y un valor booleano `is_param`.

Esta es una función de depuración, que muestra directamente información en la salida estándar.

> [!TIP]
> Al igual que con cualquier cosa que envíe sus resultados directamente al navegador, las [funciones de control de salida](#book.outcontrol) se pueden usar para capturar la salida de esta función y guardarla en un `string` (por ejemplo).

Los parámetros mostrados son aquellos que han sido añadidos en la consulta hasta el momento de la llamada. Los parámetros adicionales son ignorados.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `null`, o `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.2.0 | PDOStatement::debugDumpParams ahora devuelve el SQL enviado a la base de datos, incluyendo la consulta completa, RAW (incluyendo los marcadores de posición reemplazados con sus valores delimitados). Tenga en cuenta que esto solo estará disponible si las instrucciones preparadas emuladas están activadas. |

## Ejemplos

Ejemplo con PDOStatement::debugDumpParams y parámetros nombrados

```
<?php
/* ejecución de una instrucción preparada con enlace a variables PHP */
$calories = 150;
$colour = 'red';
$sth = $dbh->prepare('SELECT name, colour, calories
    FROM fruit
    WHERE calories < :calories AND colour = :colour');
$sth->bindParam(':calories', $calories, PDO::PARAM_INT);
$sth->bindValue(':colour', $colour, PDO::PARAM_STR, 12);
$sth->execute();

$sth->debugDumpParams();

?>

   
```php

El ejemplo anterior mostrará:

    SQL: [96] SELECT name, colour, calories
        FROM fruit
        WHERE calories < :calories AND colour = :colour
    Params:  2
    Key: Name: [9] :calories
    paramno=-1
    name=[9] ":calories"
    is_param=1
    param_type=1
    Key: Name: [7] :colour
    paramno=-1
    name=[7] ":colour"
    is_param=1
    param_type=2

Ejemplo con PDOStatement::debugDumpParams y parámetros anónimos

```
<?php

/* ejecución de una instrucción preparada con enlace a variables PHP */
$calories = 150;
$colour = 'red';
$name = 'apple';

$sth = $dbh->prepare('SELECT name, colour, calories
    FROM fruit
    WHERE calories < ? AND colour = ?');
$sth->bindParam(1, $calories, PDO::PARAM_INT);
$sth->bindValue(2, $colour, PDO::PARAM_STR);
$sth->execute();

$sth->debugDumpParams();

?>

   
```php

El ejemplo anterior mostrará:

    SQL: [82] SELECT name, colour, calories
        FROM fruit
        WHERE calories < ? AND colour = ?
    Params:  2
    Key: Position #0:
    paramno=0
    name=[0] ""
    is_param=1
    param_type=1
    Key: Position #1:
    paramno=1
    name=[0] ""
    is_param=1
    param_type=2

## Véase también

PDO::prepare, PDOStatement::bindParam, PDOStatement::bindValue
