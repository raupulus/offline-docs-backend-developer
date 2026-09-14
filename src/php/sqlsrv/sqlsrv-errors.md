---
title: sqlsrv_errors
description: Devuelve información de errores y alertas (warnings) de la última operación
  SQLSRV realizada
source_url: https://www.php.net/manual/es/function.sqlsrv-errors.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlsrv/functions/sqlsrv-errors.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlsrv
translation_status: ready
translation_reviewed: false
translation_revision: c758e862c
order: 86140
---

sqlsrv_errors

Devuelve información de errores y alertas (warnings) de la última operación SQLSRV realizada

## Descripción

```php
sqlsrv_errors([int $errorsOrWarnings]): mixed
```php

Devuelve información de errores y alertas de la última operación SQLSRV realizada.

## Parámetros

`errorsOrWarnings`  
Determina si se ha de retornar información de error, alertas, o ambas. Si este parámetro no se informa, se devolverá tanto información de error como de alerta. Este parámetro puede tomar los siguientes valores: SQLSRV_ERR_ALL, SQLSRV_ERR_ERRORS, SQLSRV_ERR_WARNINGS.

## Valores devueltos

Si se produjeron errores y/o warnings en la última operación sqlsrv, se devolverá un array de arrays conteniendo información de error. Si no se produjeron errores y/o alertas en la última operación sqlsrv, se devolverá `null`. La siguiente tabla describe la estructura de los arrays devueltos:

| Clave | Descripción |
|----|----|
| SQLSTATE | Para errores que se originan en el driver ODBC driver, el SQLSTATE devuelto por ODBC. Para errores que se originan en los drivers de Microsoft para PHP para SQL Server, un SQLSTATE de IMSSP. Para alertas que se originan en los drivers de Microsoft para PHP para SQL Server, un SQLSTATE de 01SSP. |
| code | Para errores que se originan en SQL Server, el código de error SQL Server nativo. Para errores que se originan en el driver ODBC, el código de error devuelto por ODBC. Para errores que se originan en los Drivers de Microsoft para PHP para SQL Server, los códigos de error de SQL Server para los Drivers de Microsoft para PHP. |
| message | Una descripción del error. |

Array devuelto por sqlsrv_errors

## Ejemplos

ejemplo de `functionname`

```
<?php
$serverName = "serverName/sqlexpress";
$connectionInfo = array( "Database"=>"dbName", "UID"=>"username", "PWD"=>"password");
$conn = sqlsrv_connect( $serverName, $connectionInfo);
if( $conn === false ) {
     die( print_r( sqlsrv_errors(), true));
}

/* Query que selecciona un nombre de columna inválida. */
$sql = "SELECT BadColumnName FROM Table_1";

/* Ejecución de la query que fallará debido al nombre de columna incorrecto. */
$stmt = sqlsrv_query( $conn, $sql );
if( $stmt === false ) {
    if( ($errors = sqlsrv_errors() ) != null) {
        foreach( $errors as $error ) {
            echo "SQLSTATE: ".$error[ 'SQLSTATE']."<br />";
            echo "code: ".$error[ 'code']."<br />";
            echo "message: ".$error[ 'message']."<br />";
        }
    }
}
?>

   
```php

## Notas

Por defecto, las alertas generadas en una llamada a cualquier función SQLSRV se tratarán como errores. Esto significa que si una alerta ocurre en una llamada a una función SQLSRV, la función devolverá `false`. Sin embargo, las alertas correspondientes a los valores de SQLSTATE 01000, 01001, 01003, y 01S02 nunca se tratarán como errores. Para obtener información sobre cómo cambiar este comportamiento, ver `sqlsrv_configure` y la configuración de WarningsReturnAsErrors.

## Véase también

sqlsrv_configure
