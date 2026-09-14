---
title: sqlsrv_fetch_object
description: Devuelve la siguiente fila de datos de un conjunto resultado como un
  objeto
source_url: https://www.php.net/manual/es/function.sqlsrv-fetch-object.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlsrv/functions/sqlsrv-fetch-object.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlsrv
translation_status: ready
translation_reviewed: false
translation_revision: c758e862c
order: 86170
---

sqlsrv_fetch_object

Devuelve la siguiente fila de datos de un conjunto resultado como un objeto

## Descripción

```php
sqlsrv_fetch_object(resource $stmt, [string $className], [array $ctorParams], [int $row], [int $offset]): mixed
```php

Devuelve la siguiente fila de datos de un conjunto resultado como una instancia de la clase especificada, donde las propiedades correspondientes a los nombres de los campos de la fila recuperada y los valores, se corresponden con los valores de la fila recuperada.

## Parámetros

`stmt`  
Un recurso de consulta creado por `sqlsrv_query` o `sqlsrv_execute`.

`className`  
El nombre de la clase a instanciar. Si no se especifica el nombre de la clase, se instanciará la clase stdClass.

`ctorParams`  
Los valores pasados al constructor de la clase especificada. Si el constructor de la clase especificada tiene parámetros, se proporcionará el array ctorParams.

`row`  
La fila a la que se accederá. Este parámetro únicamente puede utilizarse si la consulta especificada se preparó con un cursor con scroll. En ese caso, este parámetro puede tomar uno de los siguientes valores: SQLSRV_SCROLL_NEXT, SQLSRV_SCROLL_PRIOR, SQLSRV_SCROLL_FIRST, SQLSRV_SCROLL_LAST, SQLSRV_SCROLL_ABSOLUTE, SQLSRV_SCROLL_RELATIVE

`offset`  
Especifica la fila a la que se accederá si el parámetro de fila se ha especificado como `SQLSRV_SCROLL_ABSOLUTE` o `SQLSRV_SCROLL_RELATIVE`. Notar que la primera fila en un conjunto de resultado tiene el índice 0.

## Valores devueltos

Devuelve un objeto en caso de éxito, `null` si no hay más filas a devolver, y `false` si se produce un error o si la clase especificada no existe.

## Ejemplos

Ejemplo con `sqlsrv_fetch_object`

El siguiente ejemplo demuestra cómo devolver una columna como un objeto stdClass.

```
<?php
$serverName = "serverName\sqlexpress";
$connectionInfo = array( "Database"=>"dbName", "UID"=>"username", "PWD"=>"password");
$conn = sqlsrv_connect( $serverName, $connectionInfo);
if( $conn === false ) {
     die( print_r( sqlsrv_errors(), true));
}

$sql = "SELECT fName, lName FROM Table_1";
$stmt = sqlsrv_query( $conn, $sql);
if( $stmt === false ) {
     die( print_r( sqlsrv_errors(), true));
}

// Devolver cada fila como un objeto.
// Puesto que no se especifica ninguna clase, cada fila devolverá un objeto stdClass.
// Los nombres de propiedades corresponden a nombres de campo.
while( $obj = sqlsrv_fetch_object( $stmt)) {
      echo $obj->fName.", ".$obj->lName."<br />";
}
?>

   
```php

## Notas

Si se especifica un nombre de clase con el parámetro opcional \$className y la clase tiene propiedades cuyos nombres coinciden con los nombres de campos del conjunto de resultado, los valores correspondientes del conjunto de resultado se aplicarán a las propiedades. Si un nombre de campo del conjunto resultado no coincide con ninguna propiedad de clase, una propiedad con el nombre de campo se añadirá al objeto del conjunto resultado y el valor del resultado se aplicará a la propiedad. Se aplican las reglas siguientes cuando se utiliza el parámetro \$className: El nombre de propiedad de campo coincidente es sensible al uso de mayúsculas y minúsculas (es case sensitive)., La coincidencia con la propiedad de campo se da aunque se utilicen modificadores de acceso., Los tipos de datos de la propiedad de clase se ignoran cuando se aplica un valor de campo a la propiedad., Si la clase no existe, la función devuelve `false` y añade un error a la colección de errores. A pesar de que se defina el parámetro \$className, si se devuelve un campo sin nombre, el valor de campo será ignorado y se añadirá una alerta a la colección de errores.

Cuando se trate un conjunto de resultado que tenga varias columnas con el mismo nombre, podría ser mejor utilizar `sqlsrv_fetch_array` o la combinación de `sqlsrv_fetch` y `sqlsrv_get_field`.

## Véase también

sqlsrv_fetch

sqlsrv_fetch_array
