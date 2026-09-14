---
title: db2_exec
description: Ejecuta una consulta SQL directamente
source_url: https://www.php.net/manual/es/function.db2-exec.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-exec.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 30740
---

db2_exec

Ejecuta una consulta SQL directamente

## Descripción

```php
db2_exec(resource $connection, string $statement, [array $options]): resource
```php

Ejecuta una consulta SQL directamente.

Si se prevé insertar variables PHP en la consulta SQL, debe entenderse que esto es una de las fallas de seguridad más comunes. Se recomienda llamar a la función `db2_prepare` para preparar una consulta SQL que contenga marcadores para variables de entrada. Posteriormente, puede llamarse a la función `db2_execute` para pasar los valores de entrada y así evitar ataques por inyección SQL.

Si se prevé llamar repetidamente a la misma consulta SQL con diferentes parámetros, se recomienda utilizar las funciones `db2_prepare` y `db2_execute` para permitir que el servidor de base de datos reutilice su plan de acceso y así mejorar la eficiencia del acceso a la base de datos.

## Parámetros

`connection`  
Una variable de tipo resource de conexión válida devuelta por `db2_connect` o `db2_pconnect`.

`statement`  
Una consulta SQL. La consulta no puede contener marcadores.

`options`  
Un array asociativo que contiene las opciones de la consulta. Este parámetro puede utilizarse para solicitar un cursor flotante en los servidores de base de datos que soportan esta funcionalidad.

Para obtener una descripción de las opciones válidas, consulte la función `db2_set_option`.

## Valores devueltos

Devuelve una variable de tipo resource si la consulta SQL fue enviada correctamente o `false` si la base de datos no pudo ejecutar la consulta SQL.

## Ejemplos

Creación de una tabla con `db2_exec`

El siguiente ejemplo utiliza la función `db2_exec` para enviar un conjunto de consultas DDL con el fin de crear una tabla.

```
<?php
$conn = db2_connect($database, $user, $password);

// Crear la tabla de prueba
$create = 'CREATE TABLE animales (id INTEGER, raza VARCHAR(32),
    nombre CHAR(16), peso DECIMAL(7,2))';
$result = db2_exec($conn, $create);
if ($result) {
    print "La tabla se ha creado correctamente.\n";
}

// Rellenar la tabla de prueba
$animales = array(
    array(0, 'gato', 'Pook', 3.2),
    array(1, 'perro', 'Peaches', 12.3),
    array(2, 'caballo', 'Smarty', 350.0),
    array(3, 'pez dorado', 'Bubbles', 0.1),
    array(4, 'periquito', 'Gizmo', 0.2),
    array(5, 'cabra', 'Rickety Ride', 9.7),
    array(6, 'llama', 'Sweater', 150)
);

foreach ($animales as $animal) {
    $rc = db2_exec($conn, "INSERT INTO animales (id, raza, nombre, peso)
      VALUES ({$animal[0]}, '{$animal[1]}', '{$animal[2]}', {$animal[3]})");
    if ($rc) {
        print "Inserción... ";
    }
}
?>

    
```php

El ejemplo anterior mostrará:

    La tabla se ha creado correctamente.
    Inserción... Inserción... Inserción... Inserción... Inserción... Inserción... Inserción...

Ejecución de una consulta SELECT con un cursor flotante

El siguiente ejemplo muestra cómo solicitar un cursor flotante para una consulta SQL enviada con la función `db2_exec`.

```
<?php
$conn = db2_connect($database, $user, $password);
$sql = "SELECT nombre FROM animales
    WHERE peso < 10.0
    ORDER BY nombre";
if ($conn) {
    require_once 'prepare.inc';
    $stmt = db2_exec($conn, $sql, array('cursor' => DB2_SCROLLABLE));
    while ($row = db2_fetch_array($stmt)) {
        print "$row[0]\n";
    }
}
?>

    
```php

El ejemplo anterior mostrará:

    Bubbles
    Gizmo
    Pook
    Rickety Ride

Devuelve datos XML como ResultSet SQL

El siguiente ejemplo demuestra cómo utilizar documentos almacenados en una columna XML utilizando la base de datos SAMPLE. Mediante un simple SQL/XML, este ejemplo devuelve algunos nodos en un documento XML en un formato ResultSet SQL con el que la mayoría de los usuarios están familiarizados.

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
    WHERE NAME = \'Kathy Smith\'
    ';
$stmt = db2_exec($conn, $query);

while($row = db2_fetch_object($stmt)){
    printf("$row->CID     $row->NAME     $row->PHONE\n");
}
db2_close($conn);

?>

    
```php

El ejemplo anterior mostrará:

    1000     Kathy Smith     416-555-1358
    1001     Kathy Smith     905-555-7258

Ejecutar un "JOIN" con datos XML

El siguiente ejemplo trabaja con documentos almacenados en dos columnas diferentes en la base de datos SAMPLE. Esto crea dos tablas temporales provenientes de los documentos XML de dos columnas XML diferentes y devuelve un ResultSet SQL con la información que contiene el estado de envío para un cliente.

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
 A.NAME = \'Kathy Smith\'
';

$stmt = db2_exec($conn, $query);

while($row = db2_fetch_object($stmt)){
    printf("$row->CID     $row->NAME     $row->PHONE     $row->PONUM     $row->STATUS\n");
}

db2_close($conn);

?>

    
```php

El ejemplo anterior mostrará:

    1001     Kathy Smith     905-555-7258     5002     Shipped

Devuelve datos SQL que forman parte de un documento XML grande

El siguiente ejemplo utiliza una porción de los documentos de PRODUCT.DESCRIPTION en la base de datos SAMPLE. Esto crea un documento XML que contiene la descripción del producto (datos XML) y la información sobre el precio (datos SQL).

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
WHERE PID = \'100-100-01\'
';

$stmt = db2_exec($conn, $query);

while($row = db2_fetch_array($stmt)){
 printf("$row[0]\n");
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

db2_execute

db2_prepare
