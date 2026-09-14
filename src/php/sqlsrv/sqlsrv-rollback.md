---
title: sqlsrv_rollback
description: Anula una transacción que ha sido iniciada gracias a la función sqlsrv_begin_transaction
source_url: https://www.php.net/manual/es/function.sqlsrv-rollback.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlsrv/functions/sqlsrv-rollback.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlsrv
translation_status: ready
translation_reviewed: false
translation_revision: c758e862c
order: 86290
---

sqlsrv_rollback

Anula una transacción que ha sido iniciada gracias a la función

sqlsrv_begin_transaction

## Descripción

```php
sqlsrv_rollback(resource $conn): bool
```php

Anula una transacción que ha sido iniciada gracias a la función `sqlsrv_begin_transaction` y devuelve la conexión en modo auto-validación.

## Parámetros

`conn`  
El recurso de conexión devuelto por una llamada a la función `sqlsrv_connect`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `sqlsrv_rollback`

El siguiente ejemplo muestra la forma de utilizar la función `sqlsrv_begin_transaction` con las funciones `sqlsrv_commit` y `sqlsrv_rollback`.

```
<?php
$serverName = "serverName\sqlexpress";
$connectionInfo = array( "Database"=>"dbName", "UID"=>"userName", "PWD"=>"password");
$conn = sqlsrv_connect( $serverName, $connectionInfo);
if( $conn === false ) {
    die( print_r( sqlsrv_errors(), true ));
}

/* Inicia la transacción. */
if ( sqlsrv_begin_transaction( $conn ) === false ) {
     die( print_r( sqlsrv_errors(), true ));
}

/* Inicializa los valores de los argumentos. */
$orderId = 1; $qty = 10; $productId = 100;

/* Ejecución de la primera consulta. */
$sql1 = "INSERT INTO OrdersTable (ID, Quantity, ProductID)
         VALUES (?, ?, ?)";
$params1 = array( $orderId, $qty, $productId );
$stmt1 = sqlsrv_query( $conn, $sql1, $params1 );

/* Ejecuta la segunda consulta. */
$sql2 = "UPDATE InventoryTable
         SET Quantity = (Quantity - ?)
         WHERE ProductID = ?";
$params2 = array($qty, $productId);
$stmt2 = sqlsrv_query( $conn, $sql2, $params2 );

/* Si las dos consultas han sido ejecutadas con éxito,
se valida la transacción */
/* De lo contrario, se anula la transacción. */
if( $stmt1 && $stmt2 ) {
     sqlsrv_commit( $conn );
     echo "Transacción validada.<br />";
} else {
     sqlsrv_rollback( $conn );
     echo "Transacción anulada.<br />";
}
?>

   
```php

## Véase también

sqlsrv_begin_transaction

sqlsrv_commit
