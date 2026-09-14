---
title: PDO::commit
description: Valida una transacción
source_url: https://www.php.net/manual/es/pdo.commit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdo/commit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: false
translation_revision: 661e6858a
order: 61830
---

PDO::commit

Valida una transacción

## Descripción

```php
public PDO::commit(): bool
```php

Valida una transacción, restableciendo la conexión en modo autocommit hasta que se llame a la función PDO::beginTransaction para iniciar una nueva transacción.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Se lanzará una excepción `PDOException` si no hay ninguna transacción activa.

> [!NOTE]
> Una excepción será emitida incluso si el atributo `PDO::ATTR_ERRMODE` no vale `PDO::ERRMODE_EXCEPTION`.

## Ejemplos

Valida una transacción básica

```
<?php
/* Inicia una transacción, desactivando el autocommit */
$dbh->beginTransaction();

/* Insertar múltiples registros en una base de todo-o-nada */
$sql = 'INSERT INTO fruit
    (name, colour, calories)
    VALUES (?, ?, ?)';

$sth = $dbh->prepare($sql);

foreach ($fruits as $fruit) {
    $sth->execute(array(
        $fruit->name,
        $fruit->colour,
        $fruit->calories,
    ));
}

/* Validar los cambios */
$dbh->commit();

/* La conexión a la base de datos está ahora de vuelta en modo autocommit */
?>

    
```php

Confirmando una transacción DDL

```
<?php
/* Inicia una transacción, desactivando el autocommit */
$dbh->beginTransaction();

/* Modificación del esquema de la base de datos */
$sth = $dbh->exec("DROP TABLE fruit");

/* Validar los cambios */
$dbh->commit();

/* La conexión a la base de datos está ahora de vuelta en modo autocommit */
?>

    
```php

> [!NOTE]
> No todas las bases de datos permiten que las transacciones funcionen sobre declaraciones DDL: algunas generarán errores, mientras que otras (incluyendo MySQL) validarán automáticamente la transacción después de que la primera declaración DDL haya sido encontrada.

## Véase también

PDO::beginTransaction, PDO::rollBack, [Transacciones y autocommit](#pdo.transactions)
