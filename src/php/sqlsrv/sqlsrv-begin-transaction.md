---
title: sqlsrv_begin_transaction
description: Inicia una transacción de base de datos
source_url: https://www.php.net/manual/es/function.sqlsrv-begin-transaction.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlsrv/functions/sqlsrv-begin-transaction.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlsrv
translation_status: ready
translation_reviewed: false
translation_revision: c758e862c
order: 86070
---

sqlsrv_begin_transaction

Inicia una transacción de base de datos

## Descripción

```php
sqlsrv_begin_transaction(resource $conn): bool
```php

La transacción iniciada por `sqlsrv_begin_transaction` incluye todas las sentencias que fueron ejecutadas después de la llamada a `sqlsrv_begin_transaction` y antes de llamar a `sqlsrv_rollback` o `sqlsrv_commit`. Las transacciones explícitas deben empezar y ser consolidadas (commit) o revertidas utilizando estas funciones en vez de ejecutar sentencias SQL que empiecen y consoliden/reviertan transacciones. Para más información, ver [SQLSRV Transactions](http://msdn.microsoft.com/en-us/library/cc296206.aspx).

## Parámetros

`conn`  
El recurso de la conexión devuelta por una llamada a `sqlsrv_connect`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `sqlsrv_begin_transaction`

El siguiente ejemplo demuestra cómo utilizar `sqlsrv_begin_transaction` junto con `sqlsrv_commit` y `sqlsrv_rollback`.

```
<?php
$serverName = "serverName\sqlexpress";
$connectionInfo = array( "Database"=>"dbName", "UID"=>"userName", "PWD"=>"password");
$conn = sqlsrv_connect( $serverName, $connectionInfo);
if( $conn === false ) {
    die( print_r( sqlsrv_errors(), true ));
}

/* Iniciar la transacción. */
if ( sqlsrv_begin_transaction( $conn ) === false ) {
     die( print_r( sqlsrv_errors(), true ));
}

/* Inicializar los parámetros. */
$orderId = 1; $qty = 10; $productId = 100;

/* Preprar y ejecutar la primera sentencia . */
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

/* Si ambas sentencias finalizaran con éxito, consolidar la transacción. */
/* En caso contrario, revertirla. */
if( $stmt1 && $stmt2 ) {
     sqlsrv_commit( $conn );
     echo "Transaccion consolidada.<br />";
} else {
     sqlsrv_rollback( $conn );
     echo "Transaccion revertida.<br />";
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

## Véase también

sqlsrv_commit

sqlsrv_rollback
