---
title: PDOStatement::bindColumn
description: Vincula una columna a una variable PHP
source_url: https://www.php.net/manual/es/pdostatement.bindcolumn.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdostatement/bindcolumn.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_revision: c142be811
order: 62010
---

PDOStatement::bindColumn

Vincula una columna a una variable PHP

## Descripción

```php
public PDOStatement::bindColumn(string $column, mixed $var, [int $type], [int $maxLength], [mixed $driverOptions]): bool
```php

PDOStatement::bindColumn permite que una variable PHP se vincule a una columna específica en el conjunto de resultados de una consulta. Cada llamada a la función PDOStatement::fetch o PDOStatement::fetchAll actualiza todas las variables vinculadas a las columnas.

> [!NOTE]
> Dado que la información sobre las columnas no siempre está disponible para PDO hasta que la consulta se ejecuta, las aplicaciones portables deben llamar a esta función *después* de la función PDOStatement::execute.
>
> Sin embargo, para vincular una columna de tipo LOB con un flujo al utilizar el *controlador PostGreSQL*, las aplicaciones deben llamar a este método *antes* de llamar PDOStatement::execute, de lo contrario se recibirá el objeto OID en forma de un entero.

## Parámetros

`column`  
Número de la columna (comenzando en 1) o nombre de la columna en el conjunto de resultados. Si se utilizan los nombres de columnas, asegúrese de que el nombre coincida con la casilla de la columna, como se devuelve por el controlador.

`var`  
Nombre de la variable PHP a la que se debe vincular la columna.

`type`  
Tipo del argumento, especificado por las constantes [`PDO::PARAM_*`](#pdo.constants).

`maxLength`  
Una sugerencia para la preasignación.

`driverOptions`  
Argumentos opcionales para la biblioteca.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Emite un error de nivel `E_WARNING` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_WARNING`.

Lanza una excepción `PDOException` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_EXCEPTION`.

## Ejemplos

Vincula la visualización del conjunto de resultados a variables PHP

Vincular las columnas del conjunto de resultados a variables PHP es una forma conveniente de hacer que los datos contenidos en cada fila estén inmediatamente disponibles para la aplicación. El siguiente ejemplo muestra cómo PDO permite vincular y recuperar las columnas con una variedad de opciones.

```
<?php
$stmt = $dbh->prepare('SELECT name, colour, calories FROM fruit');
$stmt->execute();

/* Vincula por los números de columnas */
$stmt->bindColumn(1, $name);
$stmt->bindColumn(2, $colour);

/* Vincula por los nombres de columnas */
$stmt->bindColumn('calories', $cals);
while ($stmt->fetch(PDO::FETCH_BOUND)) {
    print $name . "\t" . $colour . "\t" . $cals . "\n";
}
readData($dbh);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    pomme   rouge     150
    banane  jaune  175
    kiwi    vert   75
    orange  orange  150
    mangue   rouge     200
    fraise      rouge     25

## Véase también

PDOStatement::execute, PDOStatement::fetch, PDOStatement::fetchAll, PDOStatement::fetchColumn
