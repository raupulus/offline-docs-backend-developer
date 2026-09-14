---
title: db2_fetch_object
description: Devuelve un objeto con las propiedades que representan columnas en la
  fila extraída
source_url: https://www.php.net/manual/es/function.db2-fetch-object.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-fetch-object.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: true
translation_revision: 020edc73b
order: 30790
---

db2_fetch_object

Devuelve un objeto con las propiedades que representan columnas en la fila extraída

## Descripción

```php
db2_fetch_object(resource $stmt, [int $row_number]): stdClass
```php

Devuelve un objeto en el que cada propiedad representa una columna devuelta en la fila extraída del conjunto de resultados.

## Parámetros

`stmt`  
Un recurso `stmt` válido que contiene el conjunto de resultados.

`row_number`  
Solicita una fila específica comenzando en el índice 1 del conjunto de resultados. Si se pasa este argumento, se generará una advertencia de PHP si el resultado utiliza un cursor de desplazamiento solo.

## Valores devueltos

Devuelve un objeto que representa una sola fila en el conjunto de resultados. Las propiedades del objeto corresponden al nombre de las columnas en el conjunto de resultados.

Los servidores IBM DB2, Cloudscape y Apache Derby normalmente rellenan los nombres de las columnas con mayúsculas, por lo tanto, las propiedades del objeto reflejarán este caso.

Si su consulta SELECT llama a una función escalar para modificar el valor de una columna, los servidores de base de datos devuelven el número de columna como nombre de columna en el conjunto de resultados. Si se prefiere una descripción más detallada del nombre de las columnas y las propiedades del objeto, se puede utilizar la cláusula AS para asignar un nombre a la columna en el conjunto de resultados.

Devuelve `false` si no se ha recuperado ninguna fila.

## Ejemplos

Ejemplo con `db2_fetch_object`

El ejemplo siguiente envía una consulta SELECT con una función escalar, RTRIM, que elimina los espacios al final de la columna. En lugar de crear un objeto con las propiedades "RACE" y "2", se utiliza la cláusula AS en la consulta SELECT para asignar el nombre "nom" a la columna modificada. El servidor de base de datos rellena el nombre de las columnas con mayúsculas, por lo que el objeto tendrá las propiedades "RACE" y "NOM".

```
<?php
$conn = db2_connect($database, $user, $password);

$sql = "SELECT race, RTRIM(nom) AS nom
    FROM animaux
    WHERE id = ?";

if ($conn) {
    $stmt = db2_prepare($conn, $sql);
    db2_execute($stmt, array(0));

    while ($pet = db2_fetch_object($stmt)) {
        echo "Viens ici, {$pet->NOM}, mon petit {$pet->RACE} !";
    }
    db2_close($conn);
}
?>

   
```php

El ejemplo anterior mostrará:

    Viens ici, Pook, mon petit chat !

## Véase también

db2_fetch_array

db2_fetch_assoc

db2_fetch_both

db2_fetch_row

db2_result
