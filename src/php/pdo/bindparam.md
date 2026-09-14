---
title: PDOStatement::bindParam
description: Vincula un parámetro a una variable específica
source_url: https://www.php.net/manual/es/pdostatement.bindparam.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdostatement/bindparam.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_revision: c142be811
order: 62020
---

PDOStatement::bindParam

Vincula un parámetro a una variable específica

## Descripción

```php
public PDOStatement::bindParam(string $param, mixed $var, [int $type], [int $maxLength], [mixed $driverOptions]): bool
```php

Vincula una variable PHP a un marcador nombrado o interrogativo correspondiente en una consulta SQL utilizada para preparar la consulta. A diferencia de PDOStatement::bindValue, la variable es vinculada como referencia y solo será evaluada en el momento de la llamada a la función PDOStatement::execute.

La mayoría de los parámetros son parámetros de entrada, y son utilizados en modo solo lectura para construir la consulta (aunque pueden ser convertidos según el `data_type`). Algunos drivers soportan la invocación de procedimientos almacenados que retornan datos como parámetros de salida, y algunos otros como parámetros de entrada/salida que son enviados juntos y actualizados para recibirlos.

## Parámetros

`param`  
Identificador. Para una consulta preparada utilizando marcadores nombrados, será el nombre del parámetro en la forma `:name`. Para una consulta preparada utilizando marcadores interrogativos, será la posición indexada +1 del parámetro.

`var`  
Nombre de la variable PHP a vincular al parámetro de la consulta SQL.

`type`  
Tipo explícito de datos para el parámetro utilizando las constantes [`PDO::PARAM_*`](#pdo.constants). Para retornar un parámetro INOUT desde un procedimiento almacenado, se utiliza el operador OR para definir el byte `PDO::PARAM_INPUT_OUTPUT` para el parámetro `type`.

`maxLength`  
Longitud del tipo de datos. Para indicar que un parámetro es un parámetro OUT desde un procedimiento almacenado, se debe definir explícitamente la longitud. Significativo únicamente cuando el parámetro `type` es `PDO::PARAM_INPUT_OUTPUT`.

`driverOptions`  

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Emite un error de nivel `E_WARNING` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_WARNING`.

Lanza una excepción `PDOException` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_EXCEPTION`.

## Ejemplos

Ejecución de una consulta preparada con emplazamientos nombrados

```
<?php
/* Ejecución de una consulta preparada vinculando variables PHP */
$calories = 150;
$couleur = 'rouge';
$sth = $dbh->prepare('SELECT nom, couleur, calories
    FROM fruit
    WHERE calories < :calories AND couleur = :couleur');
$sth->bindParam('calories', $calories, PDO::PARAM_INT);
/* Los nombres también pueden ser prefijados con dos puntos ":" (opcional) */
$sth->bindParam(':couleur', $couleur, PDO::PARAM_STR);
$sth->execute();
?>

   
```php

Ejecución de una consulta preparada con marcadores de posicionamiento

```
<?php
/* Ejecución de una consulta preparada vinculando variables PHP */
$calories = 150;
$couleur = 'rouge';
$sth = $dbh->prepare('SELECT nom, couleur, calories
    FROM fruit
    WHERE calories < ? AND couleur = ?');
$sth->bindParam(1, $calories, PDO::PARAM_INT);
$sth->bindParam(2, $couleur, PDO::PARAM_STR);
$sth->execute();
?>

   
```php

Llamada a un procedimiento almacenado con un parámetro INOUT

```
<?php
/* Llamada a un procedimiento almacenado con un parámetro INOUT */
$couleur = 'rouge';
$sth = $dbh->prepare('CALL puree_fruit(?)');
$sth->bindParam(1, $couleur, PDO::PARAM_STR|PDO::PARAM_INPUT_OUTPUT, 12);
$sth->execute();
print "Después de haber prensado la fruta, el color es: $couleur";
?>

   
```php

## Véase también

PDO::prepare, PDOStatement::execute, PDOStatement::bindValue
