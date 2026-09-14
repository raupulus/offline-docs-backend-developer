---
title: sqlsrv_execute
description: Ejecuta una sentencia preparada con sqlsrv_prepare
source_url: https://www.php.net/manual/es/function.sqlsrv-execute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlsrv/functions/sqlsrv-execute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlsrv
translation_status: ready
translation_reviewed: false
translation_revision: c758e862c
order: 86150
---

sqlsrv_execute

Ejecuta una sentencia preparada con

sqlsrv_prepare

## Descripción

```php
sqlsrv_execute(resource $stmt): bool
```php

Ejecuta una sentencia preparada con `sqlsrv_prepare`. Esta función es ideal para ser ejecutar múltiples veces una sentencia preparada con diferentes valores de parámetros.

## Parámetros

`stmt`  
Un recurso de sentencia devuelto por `sqlsrv_prepare`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

ejemplo de `sqlsrv_execute`

Este ejemplo muestra como preparar una sentencia con `sqlsrv_prepare` y reejecutarla múltiples veces (con diferentes valores de parámetros) utilizando `sqlsrv_execute`.

```
<?php
$serverName = "serverName\sqlexpress";
$connectionInfo = array( "Database"=>"dbName", "UID"=>"username", "PWD"=>"password");
$conn = sqlsrv_connect( $serverName, $connectionInfo);
if( $conn === false) {
    die( print_r( sqlsrv_errors(), true));
}

$sql = "UPDATE Table_1
        SET OrderQty = ?
        WHERE SalesOrderID = ?";

// Inicializar los parámetros y preparar la sentencia.
// Las variables $qty y $id se pasan como parámetro a la sentencia $stmt.
$qty = 0; $id = 0;
$stmt = sqlsrv_prepare( $conn, $sql, array( &$qty, &$id));
if( !$stmt ) {
    die( print_r( sqlsrv_errors(), true));
}

// Configurar la información de SalesOrderDetailID y OrderQty.
// Este array liga el orden ID al orden de cantidad en las parejas  key=>value.
$orders = array( 1=>10, 2=>20, 3=>30);

// Ejecuta la sentencia para cada orden.
foreach( $orders as $id => $qty) {
    // Como $id y $qty se pasan como parámetro a $stmt1, sus valores
    // actualizados se utilizan en cada ejecución de la sentencia.
    if( sqlsrv_execute( $stmt ) === false ) {
          die( print_r( sqlsrv_errors(), true));
    }
}
?>

   
```php

## Notas

Cuando se prepara una sentencia que utiliza variables como parámetros, las variables se pasan como parámetros a la sentencia. Esto significa que si se actualizan los valores de las variables, la próxima vez que se ejecute la sentencia lo hará con los nuevos valores de los parámetros. Para las sentencias que se quieran ejecutar únicamente una vez, utilizar `sqlsrv_query`.

## Véase también

sqlsrv_prepare

sqlsrv_query
