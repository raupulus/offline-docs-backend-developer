---
title: sqlsrv_field_metadata
description: Recupera los datos meta para los campos de una consulta preparada por
  la función sqlsrv_prepare o la función sqlsrv_query
source_url: https://www.php.net/manual/es/function.sqlsrv-field-metadata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlsrv/functions/sqlsrv-field-metadata.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlsrv
translation_status: ready
translation_reviewed: false
translation_revision: c758e862c
order: 86190
---

sqlsrv_field_metadata

Recupera los datos meta para los campos de una consulta preparada por la función

sqlsrv_prepare

o la función

sqlsrv_query

## Descripción

```php
sqlsrv_field_metadata(resource $stmt): mixed
```php

Recupera los datos meta para los campos de una consulta preparada por la función `sqlsrv_prepare` o la función `sqlsrv_query`. La función `sqlsrv_field_metadata` puede ser llamada sobre una consulta antes o después de su ejecución.

## Parámetros

`stmt`  
Un recurso de consulta desde el cual los datos meta serán recuperados.

## Valores devueltos

Devuelve un array de arrays en caso de éxito. De lo contrario, `false` es devuelto. Cada array devuelto es descrito en la tabla siguiente:

| Clave | Descripción |
|----|----|
| Name | El nombre del campo. |
| Type | El valor numérico para el tipo SQL. |
| Size | El número de caracteres para los campos de tipo caracteres, el número de bytes para los campos de tipo binario, o `null` para los otros tipos. |
| Precision | La precisión para las variables de tipo precisión, `null` para los otros tipos. |
| Scale | La escala para las variables de tipo scale, `null` para los otros tipos. |
| Nullable | Una enumeración indicando si la columna puede ser nula, no puede serlo, o si esta información no es conocida. |

Array devuelto por la función sqlsrv_field_metadata

Para más información, consulte la documentación sobre la función [sqlsrv_field_metadata](http://msdn.microsoft.com/en-us/library/cc296197.aspx) de la documentación Microsoft SQLSRV.

## Ejemplos

Ejemplo con `sqlsrv_field_metadata`

```
<?php
$serverName = "serverName\sqlexpress";
$connectionInfo = array( "Database"=>"AdventureWorks", "UID"=>"username", "PWD"=>"password");
$conn = sqlsrv_connect( $serverName, $connectionInfo);
if( $conn === false ) {
   die( print_r( sqlsrv_errors(), true));
}

$sql = "SELECT * FROM Table_1";
$stmt = sqlsrv_prepare( $conn, $sql );

foreach( sqlsrv_field_metadata( $stmt ) as $fieldMetadata ) {
    foreach( $fieldMetadata as $name => $value) {
       echo "$name: $value<br />";
    }
      echo "<br />";
}
?>

   
```php

## Véase también

sqlsrv_client_info
