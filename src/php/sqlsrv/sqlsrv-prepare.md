---
title: sqlsrv_prepare
description: Prepara una consulta para su ejecución
source_url: https://www.php.net/manual/es/function.sqlsrv-prepare.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlsrv/functions/sqlsrv-prepare.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlsrv
translation_status: ready
translation_reviewed: false
translation_revision: c758e862c
order: 86270
---

sqlsrv_prepare

Prepara una consulta para su ejecución

## Descripción

```php
sqlsrv_prepare(resource $conn, string $sql, [array $params], [array $options]): mixed
```php

Prepara una consulta para su ejecución. Esta función es ideal para preparar una consulta que será ejecutada varias veces con diferentes valores de argumentos.

## Parámetros

`conn`  
Un recurso de conexión devuelto por la función `sqlsrv_connect`.

`sql`  
La cadena que define la consulta a preparar y ejecutar.

`params`  
Un array especificando la información de los argumentos al ejecutar una consulta que contiene argumentos. Los elementos del array pueden ser cualquiera de los siguientes: Un valor literal, Una variable PHP, Un array con la siguiente estructura: array(\$value \[, \$direction \[, \$phpType \[, \$sqlType\]\]\]) La tabla siguiente describe los elementos de la estructura del array anterior:

| Elemento | Descripción |
|----|----|
| \$value | Un valor literal, una variable PHP o una variable PHP pasada por referencia. |
| \$direction (opcional) | Una de las constantes SQLSRV siguientes, utilizadas para indicar la dirección del argumento: SQLSRV_PARAM_IN, SQLSRV_PARAM_OUT, SQLSRV_PARAM_INOUT. El valor por defecto es SQLSRV_PARAM_IN. |
| \$phpType (opcional) | Una constante SQLSRV_PHPTYPE\_\* que especifica el tipo de datos PHP del valor devuelto. |
| \$sqlType (opcional) | Una constante SQLSRV_SQLTYPE\_\* que especifica el tipo de datos del servidor SQL del valor de entrada. |

Estructura del array

`options`  
Un array especificando las opciones de propiedades de la consulta. Las claves soportadas se describen en la tabla siguiente:

| Clave | Valores | Descripción |
|----|----|----|
| QueryTimeout | Un valor entero positivo. | Define el tiempo máximo de ejecución de la consulta, en segundos. Por defecto, el controlador esperará indefinidamente los resultados. |
| SendStreamParamsAtExec | `true` o `false` (por defecto, `true`) | Configura el controlador para enviar los datos del flujo a la ejecución (`true`), o enviar los datos del flujo por partes (`false`). Por defecto, el valor está definido a `true`. Para más información, consulte la función `sqlsrv_send_stream_data`. |
| Scrollable | SQLSRV_CURSOR_FORWARD, SQLSRV_CURSOR_STATIC, SQLSRV_CURSOR_DYNAMIC, o SQLSRV_CURSOR_KEYSET | Ver la sección sobre [la especificación de un tipo de cursor y la selección de filas](http://msdn.microsoft.com/en-us/library/ee376927.aspx) de la documentación Microsoft SQLSRV. |

Opciones de la consulta

## Valores devueltos

Devuelve un recurso de consulta en caso de éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `sqlsrv_prepare`

Este ejemplo muestra cómo preparar una consulta con la función `sqlsrv_prepare` y su re-ejecución varias veces (con diferentes valores de argumentos) utilizando la función `sqlsrv_execute`.

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

// Inicializa los argumentos y prepara la consulta.
// Las variables $qty y $id están ligadas a la consulta $stmt.
$qty = 0; $id = 0;
$stmt = sqlsrv_prepare( $conn, $sql, array( &$qty, &$id));
if( !$stmt ) {
    die( print_r( sqlsrv_errors(), true));
}

// Define la información SalesOrderDetailID y OrderQty.
// Este array liga el orden de los IDs con el orden de las cantidades con pares clave=>valor.
$orders = array( 1=>10, 2=>20, 3=>30);

// Ejecuta la consulta para cada orden.
foreach( $orders as $id => $qty) {
    // Debido a que $id y $qty están ligados a $stmt1,
    // sus valores actualizados se utilizan en cada ejecución
    // de la consulta.
    if( sqlsrv_execute( $stmt ) === false ) {
          die( print_r( sqlsrv_errors(), true));
    }
}
?>

   
```php

## Notas

Cuando se prepara una consulta que utiliza variables como argumentos, las variables están ligadas a la consulta. Esto significa que si se actualizan los valores de estas variables, la próxima ejecución de la consulta tomará en cuenta estos nuevos valores. Para las consultas que se prevé ejecutar solo una vez, utilice la función `sqlsrv_query`.

## Véase también

sqlsrv_execute

sqlsrv_query
