---
title: PDOStatement::execute
description: Ejecuta una consulta preparada
source_url: https://www.php.net/manual/es/pdostatement.execute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdostatement/execute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: false
translation_revision: 216c5dc1e
order: 62090
---

PDOStatement::execute

Ejecuta una consulta preparada

## Descripción

```php
public PDOStatement::execute([array $params]): bool
```php

Ejecuta una [consulta preparada](#pdo.prepared-statements). Si la consulta preparada incluye marcadores de posición, se puede:

- PDOStatement::bindParam y/o PDOStatement::bindValue debe ser llamado para vincular variables o valores (respectivamente) a los marcadores de parámetros. Las variables vinculadas pasan sus valores en entrada y reciben los valores de salida, si los hay, de sus respectivos marcadores de posición

- o pasar un array de valores de parámetros, solo en entrada

## Parámetros

`params`  
Un array de valores con tantos elementos como parámetros a asociar en la consulta SQL que será ejecutada. Todos los valores son tratados como constantes `PDO::PARAM_STR`.

Los valores múltiples no pueden ser vinculados a un solo parámetro; por ejemplo, no está permitido vincular dos valores a un solo parámetro nombrado en una cláusula IN().

Vincular más valores de los especificados no es posible; si hay más claves en `params` que en el código SQL utilizado para PDO::prepare, entonces la consulta preparada fallará y se generará un error.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Emite un error de nivel `E_WARNING` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_WARNING`.

Lanza una excepción `PDOException` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_EXCEPTION`.

## Ejemplos

Ejecuta una consulta preparada con variables y valores vinculados

```
<?php
/* Ejecuta una consulta preparada vinculando variables y valores */
$calories = 150;
$couleur = 'ver';
$sth = $dbh->prepare('SELECT nom, couleur, calories
    FROM fruit
    WHERE calories < :calories AND couleur LIKE :couleur');
$sth->bindParam('calories', $calories, PDO::PARAM_INT);
/* Los nombres también pueden ser prefijados con dos puntos ":" (opcional) */
$sth->bindValue(':colour', "%$colour%");
$sth->execute();
?>

   
```php

Ejecuta una consulta preparada con un array de valores nombrados

```
<?php
/* Ejecuta una consulta preparada pasando un array de valores */
$calories = 150;
$couleur = 'rouge';
$sth = $dbh->prepare('SELECT nom, couleur, calories
    FROM fruit
    WHERE calories < :calories AND couleur = :couleur');
$sth->execute(array('calories' => $calories, 'colour' => $couleur));
/* Las claves del array también pueden ser prefijadas con dos puntos ":" (opcional) */
$sth->execute(array(':calories' => $calories, ':couleur' => $couleur));
?>

   
```php

Ejecuta una consulta preparada con un array de valores posicionales

```
<?php
/* Ejecuta una consulta preparada pasando un array de valores */
$calories = 150;
$colour = 'rouge';
$sth = $dbh->prepare('SELECT nom, couleur, calories
    FROM fruit
    WHERE calories < ? AND couleur = ?');
$sth->execute(array($calories, $colour));
?>

   
```php

Ejecuta una consulta preparada con variables vinculadas a un marcador de posición

```
<?php
/* Ejecuta una consulta preparada vinculando variables PHP */
$calories = 150;
$couleur = 'rouge';
$sth = $dbh->prepare('SELECT nom, couleur, calories
    FROM fruit
    WHERE calories < ? AND couleur = ?');
$sth->bindParam(1, $calories, PDO::PARAM_INT);
$sth->bindParam(2, $couleur, PDO::PARAM_STR, 12);
$sth->execute();
?>

   
```php

Ejecuta una consulta preparada utilizando un array para las cláusulas IN

```
<?php
/* Ejecuta una consulta preparada utilizando un array de valores para las cláusulas IN */
$params = array(1, 21, 63, 171);
/* Crea una cadena para los marcadores */
$place_holders = '?' . str_repeat(', ?', count($params) - 1);

/*
    Este fragmento de código prepara la consulta con suficientes marcadores para cada valor
    del array $params. Los valores del array $params son luego vinculados a los marcadores
    de la consulta preparada cuando la consulta es ejecutada. Esto no es lo mismo
    que utilizar el método PDOStatement::bindParam() ya que este impone una referencia
    hacia los valores. El método PDOStatement::execute() solo vincula por valor.
*/
$sth = $dbh->prepare("SELECT id, name FROM contacts WHERE id IN ($place_holders)");
$sth->execute($params);
?>

   
```php

## Notas

> [!NOTE]
> Algunos drivers requieren [cerrar el cursor](#pdostatement.closecursor) antes de ejecutar la siguiente consulta.

## Véase también

PDO::prepare, PDOStatement::bindParam, PDOStatement::fetch, PDOStatement::fetchAll, PDOStatement::fetchColumn
