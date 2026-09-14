---
title: sqlsrv_commit
description: Consolida una transacción que se inició con sqlsrv_begin_transaction
source_url: https://www.php.net/manual/es/function.sqlsrv-commit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlsrv/functions/sqlsrv-commit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlsrv
translation_status: ready
translation_reviewed: false
translation_revision: c758e862c
order: 86110
---

sqlsrv_commit

Consolida una transacción que se inició con

sqlsrv_begin_transaction

## Descripción

```php
sqlsrv_commit(resource $conn): bool
```php

Consolida una transacción que se inició con `sqlsrv_begin_transaction`. La conexión retorna al modo auto-commit después de que se llame a `sqlsrv_commit`. La transacción que se consolida incluye todas las sentencias que fueron ejecutadas después de la llamada a `sqlsrv_begin_transaction`. Las transacciones explícitas deben iniciarse y consolidarse o revertirse utilizando estas funciones en vez de ejecutar las sentencias SQL que empiezan y consolidan/revierten transacciones. Para más información, ver [SQLSRV Transactions](http://msdn.microsoft.com/en-us/library/cc296206.aspx).

## Parámetros

`conn`  
La conexión en la que se va a consolidar la transacción.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `sqlsrv_commit`

El siguiente ejemplo demuestra cómo utilizar `sqlsrv_commit` junto con `sqlsrv_begin_transaction` y `sqlsrv_rollback`.

```
<?php
$serverName = "serverName\sqlexpress";
$connectionInfo = array( "Database"=>"dbName", "UID"=>"userName", "PWD"=>"password");
$conn = sqlsrv_connect( $serverName, $connectionInfo);
if( $conn === false ) {
    die( print_r( sqlsrv_errors(), true ));
}

/* Empezar la transacción. */
if ( sqlsrv_begin_transaction( $conn ) === false ) {
     die( print_r( sqlsrv_errors(), true ));
}

/* Inicializar los parámetros. */
$orderId = 1; $qty = 10; $productId = 100;

/* Preparar y ejecutar la primera sentencia. */
$sql1 = "INSERT INTO OrdersTable (ID, Quantity, ProductID)
         VALUES (?, ?, ?)";
$params1 = array( $orderId, $qty, $productId );
$stmt1 = sqlsrv_query( $conn, $sql1, $params1 );

/* Preparar y ejecutar la segunda sentencia. */
$sql2 = "UPDATE InventoryTable
         SET Quantity = (Quantity - ?)
         WHERE ProductID = ?";
$params2 = array($qty, $productId);
$stmt2 = sqlsrv_query( $conn, $sql2, $params2 );

/* Si ambas sentencias finalizan con éxito, consolidar la transacción. */
/* En caso contrario, revertir la transacción. */
if( $stmt1 && $stmt2 ) {
     sqlsrv_commit( $conn );
     echo "Transacción consolidada.<br />";
} else {
     sqlsrv_rollback( $conn );
     echo "Transacción revertida.<br />";
}
?>

   
```php

## Véase también

sqlsrv_begin_transaction

sqlsrv_rollback
