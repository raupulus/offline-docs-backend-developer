---
title: PDO::beginTransaction
description: Inicia una transacción
source_url: https://www.php.net/manual/es/pdo.begintransaction.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdo/begintransaction.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: false
translation_revision: 661e6858a
order: 61820
---

PDO::beginTransaction

Inicia una transacción

## Descripción

```php
public PDO::beginTransaction(): bool
```php

Desactiva el modo autocommit. Mientras el autocommit está desactivado, las modificaciones realizadas en la base de datos mediante las instancias de los objetos PDO no se aplican hasta que se finaliza la transacción llamando a la función PDO::commit. La llamada a PDO::rollBack anulará todas las modificaciones realizadas en la base de datos y restablecerá la conexión en modo autocommit.

Algunas bases de datos, incluyendo MySQL, ejecutarán automáticamente un COMMIT cuando se ejecute una consulta de definición de lenguaje de base de datos (DDL) como DROP TABLE o CREATE TABLE dentro de una transacción. Este COMMIT implícito impedirá anular otras modificaciones realizadas en esta transacción.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Se lanza la excepción `PDOException` si ya se ha iniciado una transacción o si el controlador no soporta transacciones.

> [!NOTE]
> Una excepción será emitida incluso si el atributo `PDO::ATTR_ERRMODE` no vale `PDO::ERRMODE_EXCEPTION`.

## Ejemplos

Anular una transacción

El siguiente ejemplo inicia una transacción y ejecuta dos consultas que modifican la base de datos antes de anular las modificaciones. En MySQL, sin embargo, la consulta DROP TABLE validará automáticamente la transacción, por lo que ninguna de las modificaciones de la transacción será anulada.

```
<?php
/* Inicia una transacción, desactivando el auto-commit */
$dbh->beginTransaction();

/* Modificación del esquema de la base de datos y de los datos */
$sth = $dbh->exec("DROP TABLE fruit");
$sth = $dbh->exec("UPDATE dessert
SET name = 'hamburger'");

/* Se detecta un error y se anulan las modificaciones */
$dbh->rollBack();

/* La conexión a la base de datos está ahora de vuelta en modo auto-commit */
?>

    
```php

## Véase también

PDO::commit, PDO::rollBack, [Transacciones y auto-commit](#pdo.transactions)
