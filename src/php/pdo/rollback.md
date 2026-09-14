---
title: PDO::rollBack
description: Anula una transacción
source_url: https://www.php.net/manual/es/pdo.rollback.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdo/rollback.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: false
translation_revision: 661e6858a
order: 61960
---

PDO::rollBack

Anula una transacción

## Descripción

```php
public PDO::rollBack(): bool
```php

Anula la transacción actual, iniciada por la función PDO::beginTransaction.

Si la base de datos está en modo autocommit, esta función restaurará el modo autocommit después de la anulación de la transacción.

Algunas bases de datos, incluyendo MySQL, ejecutarán automáticamente un COMMIT cuando se ejecute una consulta de definición de lenguaje de base de datos (DDL) como DROP TABLE o CREATE TABLE en una transacción. Este COMMIT implícito impedirá anular cualquier otra modificación realizada en esta transacción.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Se lanzará una excepción `PDOException` si no hay ninguna transacción activa.

> [!NOTE]
> Una excepción será emitida incluso si el atributo `PDO::ATTR_ERRMODE` no vale `PDO::ERRMODE_EXCEPTION`.

## Ejemplos

Anulación de una transacción

El siguiente ejemplo comienza una transacción y ejecuta dos consultas que modifican la base de datos antes de anular las modificaciones. En MySQL, sin embargo, la consulta DROP TABLE validará automáticamente la transacción, por lo que ninguna de las modificaciones de la transacción será anulada.

```
<?php
/* Inicio de una transacción, desactivación del modo autocommit */
$dbh->beginTransaction();

/* Modifica el esquema de la base de datos así como los datos */
$sth = $dbh->exec("DROP TABLE fruit");
$sth = $dbh->exec("UPDATE dessert
    SET name = 'hamburger'");

/* Se detecta un error y se anulan las modificaciones */
$dbh->rollBack();

/* La conexión a la base de datos vuelve al modo autocommit */
?>

    
```php

## Véase también

PDO::beginTransaction, PDO::commit, [Transacciones y auto-commit](#pdo.transactions)
