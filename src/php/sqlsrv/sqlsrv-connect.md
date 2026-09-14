---
title: sqlsrv_connect
description: Establece una conexión con una base de datos Microsoft SQL Server
source_url: https://www.php.net/manual/es/function.sqlsrv-connect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlsrv/functions/sqlsrv-connect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlsrv
translation_status: ready
translation_reviewed: false
translation_revision: c758e862c
order: 86130
---

sqlsrv_connect

Establece una conexión con una base de datos Microsoft SQL Server

## Descripción

```php
sqlsrv_connect(string $serverName, [array $connectionInfo]): resource
```php

Establece una conexión con una base de datos Microsoft SQL Server. Por omisión, la conexión intenta utilizar la autenticación Windows. Para conectarse utilizando la autenticación SQL Server, se deben añadir los argumentos "UID" y "PWD" en el array de opciones de conexión.

## Parámetros

`serverName`  
El nombre del servidor con el que se desea establecer la conexión. Para conectarse a una instancia particular, se debe especificar el nombre del servidor, seguido de un backslash, y luego el nombre de la instancia (i.e. serverName\sqlexpress).

`connectionInfo`  
Un array asociativo que especifica las opciones para la conexión al servidor. Si los valores de las claves UID y PWD no están especificados, la conexión intentará utilizar la autenticación Windows. Para una lista completa de las claves soportadas, consulte las [opciones de conexión SQLSRV](http://msdn.microsoft.com/en-us/library/ff628167.aspx).

## Valores devueltos

Un recurso de conexión. Si la conexión no pudo ser abierta, se retornará `false`.

## Ejemplos

Conexión utilizando la autenticación Windows.

```
<?php
$serverName = "serverName\\sqlexpress"; //serverName\instanceName

// Dado que UID y PWD no están especificados en el array $connectionInfo,
// la conexión intentará utilizar la autenticación Windows.
$connectionInfo = array( "Database"=>"dbName");
$conn = sqlsrv_connect( $serverName, $connectionInfo);

if( $conn ) {
     echo "Conexión establecida.<br />";
}else{
     echo "La conexión no pudo ser establecida.<br />";
     die( print_r( sqlsrv_errors(), true));
}
?>

   
```php

Conexión especificando un nombre de usuario y una contraseña.

```
<?php
$serverName = "serverName\\sqlexpress"; //serverName\instanceName
$connectionInfo = array( "Database"=>"dbName", "UID"=>"userName", "PWD"=>"password");
$conn = sqlsrv_connect( $serverName, $connectionInfo);

if( $conn ) {
     echo "Conexión establecida.<br />";
}else{
     echo "La conexión no pudo ser establecida.<br />";
     die( print_r( sqlsrv_errors(), true));
}
?>

   
```php

Conexión a un puerto específico.

```
<?php
$serverName = "serverName\\sqlexpress, 1542"; //serverName\instanceName, portNumber (default is 1433)
$connectionInfo = array( "Database"=>"dbName", "UID"=>"userName", "PWD"=>"password");
$conn = sqlsrv_connect( $serverName, $connectionInfo);

if( $conn ) {
     echo "Conexión establecida.<br />";
}else{
     echo "La conexión no pudo ser establecida.<br />";
     die( print_r( sqlsrv_errors(), true));
}
?>

   
```php

## Notas

Por omisión, la función `sqlsrv_connect` utiliza la cola de conexiones para aumentar el rendimiento. Para desactivar esta cola de conexiones (i.e. y así, forzar una nueva conexión en cada llamada a la función), se debe definir la opción "ConnectionPooling" en el array \$connectionOptions a 0 (o `false`). Para más información, consulte el capítulo sobre la [cola de conexiones SQLSRV](http://msdn.microsoft.com/en-us/library/cc644930.aspx).

La extensión SQLSRV no tiene una función dedicada para modificar la base de datos a la que está conectada. La base de datos objetivo se especifica en el array \$connectionOptions pasado a la función sqlsrv_connect. Para cambiar la base de datos en una conexión abierta, se debe ejecutar la siguiente consulta: "USE dbName" (i.e. sqlsrv_query(\$conn, "USE dbName")).

## Véase también

sqlsrv_close

sqlsrv_errors

sqlsrv_query
