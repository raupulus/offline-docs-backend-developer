---
title: PDOStatement::bindValue
description: Asocia un valor a un parámetro
source_url: https://www.php.net/manual/es/pdostatement.bindvalue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdostatement/bindvalue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_revision: c142be811
order: 62030
---

PDOStatement::bindValue

Asocia un valor a un parámetro

## Descripción

```php
public PDOStatement::bindValue(string $param, mixed $value, [int $type]): bool
```php

Asocia un valor a un nombre correspondiente o a un punto de interrogación (como parámetro ficticio) en la consulta SQL que se ha utilizado para preparar la consulta.

## Parámetros

`param`  
Identificador del parámetro. Para una consulta preparada utilizando los marcadores, esto será un nombre de parámetro de la forma `:nombre`. Para una consulta preparada utilizando los puntos de interrogación (como parámetro ficticio), esto será un array indexado numéricamente que comienza en la posición 1 del parámetro.

`value`  
El valor a asociar al parámetro.

`type`  
Tipo de datos explícito para el parámetro utilizando las constantes [`PDO::PARAM_*`](#pdo.constants).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Emite un error de nivel `E_WARNING` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_WARNING`.

Lanza una excepción `PDOException` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_EXCEPTION`.

## Ejemplos

Ejecutar una consulta preparada con marcadores nombrados

```
<?php
/* Ejecutar una consulta preparada asociando variables PHP */
$calorias = 150;
$color = 'rojo';
$sth = $dbh->prepare('SELECT nombre, color, calorias
    FROM fruta
    WHERE calorias < :calorias AND color = :color');

/* Definir el valor de un parámetro utilizando su nombre */
$sth->bindValue('calorias', $calorias, PDO::PARAM_INT);
/* Opcionalmente, los nombres de los parámetros pueden ser prefijados con dos puntos ": " */
$sth->bindValue(':color', $color, PDO::PARAM_STR);
$sth->execute();
?>

   
```php

Ejecutar una consulta preparada con puntos de interrogación como parámetro ficticio

```
<?php
/* Ejecutar una consulta preparada asociando variables PHP */
$calorias = 150;
$color = 'rojo';
$sth = $dbh->prepare('SELECT nombre, color, calorias
    FROM fruta
    WHERE calorias < ? AND color = ?');
$sth->bindValue(1, $calorias, PDO::PARAM_INT);
$sth->bindValue(2, $color, PDO::PARAM_STR);
$sth->execute();
?>

   
```php

## Véase también

PDO::prepare, PDOStatement::execute, PDOStatement::bindParam
