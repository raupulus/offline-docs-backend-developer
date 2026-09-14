---
title: db2_execute
description: Ejecuta una consulta SQL preparada
source_url: https://www.php.net/manual/es/function.db2-execute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-execute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 30750
---

db2_execute

Ejecuta una consulta SQL preparada

## Descripción

```php
db2_execute(resource $stmt, [array $parameters]): bool
```php

`db2_execute` ejecuta una consulta SQL que ha sido preparada por `db2_prepare`.

Si la consulta SQL devuelve un conjunto de resultados, por ejemplo, una consulta SELECT o CALL a un procedimiento de registro devuelve uno o varios conjuntos de resultados, puede recuperar una fila como un array a partir de la recurso `stmt` utilizando `db2_fetch_assoc`, `db2_fetch_both` o `db2_fetch_array`. Alternativamente, puede utilizar `db2_fetch_row` para mover el puntero a la fila siguiente y recuperar una columna a la vez de esta fila con la función `db2_result`.

Consúltese `db2_prepare` para una breve discusión sobre las ventajas de utilizar `db2_prepare` y `db2_execute` en lugar de `db2_exec`.

## Parámetros

`stmt`  
Una consulta preparada devuelta por `db2_prepare`.

`parameters`  
Un array de parámetros de entrada que contiene los marcadores de variables contenidos en la consulta preparada.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Preparación y ejecución de una consulta SQL con marcadores

El siguiente ejemplo prepara una consulta INSERT que acepta cuatro marcadores, luego itera sobre el array que contiene los valores de entrada que será pasado a la función `db2_execute`.

```
<?php
$pet = array(0, 'chat', 'Pook', 3.2);

$insert = 'INSERT INTO animales (id, raza, nombre, peso)
    VALUES (?, ?, ?, ?)';

$stmt = db2_prepare($conn, $insert);
if ($stmt) {
    $result = db2_execute($stmt, $pet);
    if ($result) {
        print "Añadido un nuevo animal con éxito.";
    }
}
?>

    
```php

El ejemplo anterior mostrará:

    Añadido un nuevo animal con éxito.

Llamada a un procedimiento de registro con un parámetro de SALIDA

El siguiente ejemplo prepara una consulta CALL que acepta un marcador que representa un parámetro de SALIDA, vincula la variable PHP `$my_pets` al parámetro utilizando la función `db2_bind_param` y llama a la función `db2_execute` para ejecutar la consulta CALL. Una vez que la consulta CALL ha sido ejecutada, el valor de `$num_pets` cambia para reflejar el valor devuelto por el procedimiento de registro para este parámetro de SALIDA.

```
<?php
$num_pets = 0;
$res = db2_prepare($conn, "CALL count_my_pets(?)");
$rc = db2_bind_param($res, 1, "num_pets", DB2_PARAM_OUT);
$rc = db2_execute($res);
print "Tengo $num_pets animales !";
?>

    
```php

El ejemplo anterior mostrará:

    Tengo 7 animales !

Devuelve datos XML como ResultSet SQL

El siguiente ejemplo demuestra cómo utilizar documentos almacenados en una columna XML utilizando la base de datos SAMPLE. Utilizando un simple SQL/XML, este ejemplo devuelve algunos nodos en un documento XML en un formato ResultSet SQL con el que la mayoría de los usuarios están familiarizados.

```
<?php

$conn = db2_connect("SAMPLE", "db2inst1", "ibmdb2");

$query = 'SELECT * FROM XMLTABLE(
    XMLNAMESPACES (DEFAULT \'http://posample.org\'),
    \'db2-fn:xmlcolumn("CUSTOMER.INFO")/customerinfo\'
    COLUMNS
    "CID" VARCHAR (50) PATH \'@Cid\',
    "NAME" VARCHAR (50) PATH \'name\',
    "PHONE" VARCHAR (50) PATH \'phone [ @type = "work"]\'
    ) AS T
    WHERE NAME = ?
    ';

$stmt = db2_prepare($conn, $query);

$name = 'Kathy Smith';

if ($stmt) {
    db2_bind_param($stmt, 1, "name", DB2_PARAM_IN);
    db2_execute($stmt);

    while($row = db2_fetch_object($stmt)){
        printf("$row->CID     $row->NAME     $row->PHONE\n");
    }
}
db2_close($conn);

?>

    
```php

El ejemplo anterior mostrará:

    1000     Kathy Smith     416-555-1358
    1001     Kathy Smith     905-555-7258

Ejecutar un "JOIN" con datos XML

El siguiente ejemplo trabaja con documentos almacenados en dos columnas diferentes en la base de datos SAMPLE. Esto crea dos tablas temporales a partir de los documentos XML de dos diferentes columnas XML y devuelve un ResultSet SQL con la información que contiene el estado de envío para un cliente.

```
<?php

$conn = db2_connect("SAMPLE", "db2inst1", "ibmdb2");

$query = '
SELECT A.CID, A.NAME, A.PHONE, C.PONUM, C.STATUS
FROM
XMLTABLE(
XMLNAMESPACES (DEFAULT \'http://posample.org\'),
\'db2-fn:xmlcolumn("CUSTOMER.INFO")/customerinfo\'
COLUMNS
"CID" BIGINT PATH \'@Cid\',
"NAME" VARCHAR (50) PATH \'name\',
"PHONE" VARCHAR (50) PATH \'phone [ @type = "work"]\'
) as A,
PURCHASEORDER AS B,
XMLTABLE (
XMLNAMESPACES (DEFAULT \'http://posample.org\'),
\'db2-fn:xmlcolumn("PURCHASEORDER.PORDER")/PurchaseOrder\'
COLUMNS
"PONUM"  BIGINT PATH \'@PoNum\',
"STATUS" VARCHAR (50) PATH \'@Status\'
) as C
WHERE A.CID = B.CUSTID AND
        B.POID = C.PONUM AND
        A.NAME = ?
';

$stmt = db2_prepare($conn, $query);

$name = 'Kathy Smith';

if ($stmt) {
    db2_bind_param($stmt, 1, "name", DB2_PARAM_IN);
    db2_execute($stmt);

    while($row = db2_fetch_object($stmt)){
        printf("$row->CID     $row->NAME     $row->PHONE     $row->PONUM     $row->STATUS\n");
    }
}

db2_close($conn);

?>

    
```php

El ejemplo anterior mostrará:

    1001     Kathy Smith     905-555-7258     5002     Shipped

Devuelve datos SQL que forman parte de un documento XML grande

El siguiente ejemplo utiliza una porción de los documentos de PRODUCT.DESCRIPTION en la base de datos SAMPLE. Esto crea un documento XML que contiene la descripción del producto (datos XML) y las informaciones concernientes al precio (datos SQL).

```
<?php

$conn = db2_connect("SAMPLE", "db2inst1", "ibmdb2");

$query = '
SELECT
XMLSERIALIZE(
XMLQUERY(\'
    declare boundary-space strip;
    declare default element namespace "http://posample.org";
    <promoList> {
        for $prod in $doc/product
        where $prod/description/price < 10.00
        order by $prod/description/price ascending
        return(
            <promoitem> {
                $prod,
                <startdate> {$start} </startdate>,
                <enddate> {$end} </enddate>,
                <promoprice> {$promo} </promoprice>
            } </promoitem>
        )
    } </promoList>
\' passing by ref DESCRIPTION AS "doc",
PROMOSTART as "start",
PROMOEND as "end",
PROMOPRICE as "promo"
RETURNING SEQUENCE)
AS CLOB (32000))
AS NEW_PRODUCT_INFO
FROM PRODUCT
WHERE PID = ?
';

$stmt = db2_prepare($conn, $query);

$pid = "100-100-01";

if ($stmt) {
    db2_bind_param($stmt, 1, "pid", DB2_PARAM_IN);
    db2_execute($stmt);

    while($row = db2_fetch_array($stmt)){
        printf("$row[0]\n");
    }
}

db2_close($conn);

?>

    
```php

El ejemplo anterior mostrará:

    <promoList xmlns="http://posample.org">
        <promoitem>
        <product pid="100-100-01">
            <description>
                <name>Snow Shovel, Basic 22 inch</name>
                <details>Basic Snow Shovel, 22 inches wide, straight handle with D-Grip</details>
                <price>9.99</price>
                <weight>1 kg</weight>
            </description>
        </product>
        <startdate>2004-11-19</startdate>
        <enddate>2004-12-19</enddate>
        <promoprice>7.25</promoprice>
        </promoitem>
    </promoList>

## Véase también

db2_exec

db2_fetch_array

db2_fetch_assoc

db2_fetch_both

db2_fetch_row

db2_prepare

db2_result
