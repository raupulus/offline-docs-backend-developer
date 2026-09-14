---
title: oci_bind_by_name
description: Asocia una variable PHP a un marcador Oracle
source_url: https://www.php.net/manual/es/function.oci-bind-by-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-bind-by-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: 5e41012cf
order: 57190
---

oci_bind_by_name

Asocia una variable PHP a un marcador Oracle

## Descripción

```php
oci_bind_by_name(resource $statement, string $param, mixed $var, [int $max_length], [int $type]): bool
```php

Vincula una variable PHP `var` al marcador Oracle `param`. El hecho de vincular una variable es importante en términos de rendimiento de la base de datos Oracle, pero también en términos de seguridad relativa a las inyecciones SQL.

El vínculo permite a las bases de datos reutilizar el contexto de ejecución de la consulta así como el caché asociado, incluso cuando otro usuario o proceso la ejecuta. El vínculo reduce el riesgo de inyección SQL ya que los datos asociados a una variable vinculada nunca son tratados como parte de la consulta SQL. Por lo tanto, no es necesario añadir comillas ni escapar estos datos.

Las variables PHP vinculadas pueden cambiarse y la consulta re-ejecutarse sin necesidad de analizar de nuevo la consulta o de vincular de nuevo las variables.

Con Oracle, las variables vinculadas suelen dividirse en vínculo `IN` para los valores pasados a la base de datos, y en vínculo `OUT` para los valores a devolver a PHP. Una variable vinculada puede ser a la vez en vínculo `IN` y `OUT`. En este caso, el hecho de saber si la variable vinculada debe ser utilizada para la entrada o la salida será determinado en el momento de la ejecución.

Debe especificarse el parámetro `max_length` al utilizar el vínculo `OUT` para que PHP asigne suficiente memoria para contener el valor de retorno.

Para los vínculos `IN`, se recomienda definir el parámetro `max_length` si la consulta se ejecuta varias veces con valores diferentes para las variables PHP. De lo contrario, Oracle puede truncar los datos a la longitud del valor inicial de la variable PHP. Si no se conoce la longitud máxima necesaria, entonces llame de nuevo a la función `oci_bind_by_name` con los datos actuales, antes de cada llamada a la función `oci_execute`. El hecho de asociar una longitud superior a la necesaria tiene un impacto en la memoria asociada al proceso para la base de datos.

Una llamada a la funcionalidad de asociación de variables proporciona a Oracle la dirección de memoria a utilizar para leer los datos. Para los vínculos `IN`, esta dirección debe contener datos válidos al llamar a la función `oci_execute`. Esto significa que la variable vinculada debe permanecer en el contexto hasta la ejecución. Si no es así, pueden producirse resultados no esperados, así como errores de tipo "ORA-01460: unimplemented or unreasonable conversion requested". Para los vínculos `OUT`, un síntoma puede ser que no se haya definido ningún valor en la variable PHP.

Para una consulta que se ejecuta varias veces, los valores vinculados que nunca cambian pueden reducir la capacidad del optimizador de Oracle para elegir el mejor plan de ejecución. Para las consultas que tardan mucho tiempo, que rara vez se llaman varias veces, la asociación de variables no aporta ningún beneficio. Sin embargo, en los 2 casos, la asociación es más segura que colocar directamente las cadenas de caracteres en la consulta SQL, sabiendo que existe un riesgo de filtrado incorrecto de la entrada del usuario.

## Parámetros

`statement`  
Un identificador de consulta OCI8 válido.

`param`  
El marcador, prefijado por una coma, utilizado en la consulta. La coma es opcional en el parámetro `param`.

`var`  
La variable PHP a asociar con el marcador del parámetro `param`.

`max_length`  
Especifica la longitud máxima para los datos. Si el valor es -1, la función utilizará la longitud actual de los datos del parámetro `var` para definir la longitud máxima. En este caso, el parámetro `var` debe existir y contener datos al llamar a la función `oci_bind_by_name`.

`type`  
El tipo de datos a utilizar por Oracle para tratar los datos. Por omisión, vale `SQLT_CHR`. Oracle convertirá los datos entre este tipo y la columna de la base de datos (o las variables de tipo PL/SQL), cuando sea posible.

Si debe vincular tipos abstractos de datos (LOB/ROWID/BFILE), deberá asignarlos en primer lugar, con `oci_new_descriptor`. La longitud `length` no sirve para estos tipos y debería fijarse a -1.

Los valores posibles para el parámetro `type` son :

- `SQLT_FILE` o `OCI_B_BFILE` - para los BFILEs ;

- `SQLT_CFILE` o `OCI_B_CFILEE` - para los CFILEs ;

- `SQLT_CLOB` o `OCI_B_CLOB` - para los CLOBs ;

- `SQLT_BLOB` o `OCI_B_BLOB` - para los BLOBs ;

- `SQLT_RDD` o `OCI_B_ROWID` - para los ROWIDs ;

- `SQLT_NTY` o `OCI_B_NTY` - para los tipos de datos nombrados ;

- `SQLT_INT` o `OCI_B_INT` - para los enteros ;

- `SQLT_CHR` - para los VARCHAR ;

- `SQLT_BIN` o `OCI_B_BIN` - para las columnas RAW ;

- `SQLT_LNG` - para las columnas LONG ;

- `SQLT_LBI` - para las columnas LONG RAW ;

- `SQLT_RSET` - para los cursores creados con la función `oci_new_cursor`;

- `SQLT_BOL` o `OCI_B_BOL` - para los booleanos (requiere Oracle Database 12c)

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Inserción de datos con la función `oci_bind_by_name`

```
<?php

// Creación de la tabla con :
//   CREATE TABLE mytab (id NUMBER, text VARCHAR2(40));

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $m = oci_error();
    trigger_error(htmlentities($m['message']), E_USER_ERROR);
}

$stid = oci_parse($conn,"INSERT INTO mytab (id, text) VALUES(:id_bv, :text_bv)");

$id = 1;
$text = "Datos a insertar     ";
oci_bind_by_name($stid, ":id_bv", $id);
oci_bind_by_name($stid, ":text_bv", $text);
oci_execute($stid);

// La tabla contiene ahora : 1, 'Datos a insertar

?>

    
```php

Una asociación con múltiples llamadas

```
<?php

// Creación de la tabla con :
//   CREATE TABLE mytab (id NUMBER);

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $m = oci_error();
    trigger_error(htmlentities($m['message']), E_USER_ERROR);
}

$a = array(1,3,5,7,11);  // Datos a insertar

$stid = oci_parse($conn, 'INSERT INTO mytab (id) VALUES (:bv)');
oci_bind_by_name($stid, ':bv', $v, 20);
foreach ($a as $v) {
    $r = oci_execute($stid, OCI_DEFAULT);  // No validar automáticamente
}
oci_commit($conn); // Una sola validación

// La tabla contiene ahora 5 líneas : 1, 3, 5, 7, 11

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Asociación con un bucle `foreach`

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $m = oci_error();
    trigger_error(htmlentities($m['message']), E_USER_ERROR);
}

$sql = 'SELECT * FROM departments WHERE department_name = :dname AND location_id = :loc';
$stid = oci_parse($conn, $sql);

$ba = array(':dname' => 'IT Support', ':loc' => 1700);

foreach ($ba as $key => $val) {

    // oci_bind_by_name($stid, $key, $val) no funciona porque
    // asocia cada marcador al mismo lugar : $val
    // en lugar de utilizar el lugar actual de la dato $ba[$key]
    oci_bind_by_name($stid, $key, $ba[$key]);
}

oci_execute($stid);
$row = oci_fetch_array($stid, OCI_ASSOC+OCI_RETURN_NULLS);
foreach ($row as $item) {
    print $item."<br>\n";
}

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Asociación en una cláusula WHERE

```
<?php

$conn = oci_connect("hr", "hrpwd", "localhost/XE");
if (!$conn) {
    $m = oci_error();
    trigger_error(htmlentities($m['message']), E_USER_ERROR);
}

$sql = 'SELECT last_name FROM employees WHERE department_id = :didbv ORDER BY last_name';
$stid = oci_parse($conn, $sql);
$didbv = 60;
oci_bind_by_name($stid, ':didbv', $didbv);
oci_execute($stid);
while (($row = oci_fetch_array($stid, OCI_ASSOC)) != false) {
    echo $row['LAST_NAME'] ."<br>\n";
}

// Muestra :
//    Austin
//    Ernst
//    Hunold
//    Lorentz
//    Pataballa

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Asociación con una cláusula LIKE

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $m = oci_error();
    trigger_error(htmlentities($m['message']), E_USER_ERROR);
}

// Encuentra todos los criterios que comienzan por 'South'
$stid = oci_parse($conn, "SELECT city FROM locations WHERE city LIKE :bv");
$city = 'South%';  // '%' es un comodín en SQL
oci_bind_by_name($stid, ":bv", $city);
oci_execute($stid);
oci_fetch_all($stid, $res);

foreach ($res['CITY'] as $c) {
    print $c . "<br>\n";
}
// Muestra :
//   South Brunswick
//   South San Francisco
//   Southlake

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Asociación con REGEXP_LIKE

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $m = oci_error();
    trigger_error(htmlentities($m['message']), E_USER_ERROR);
}

// Encuentra todos los criterios que contienen 'ing'
$stid = oci_parse($conn, "SELECT city FROM locations WHERE REGEXP_LIKE(city, :bv)");
$city = '.*ing.*';
oci_bind_by_name($stid, ":bv", $city);
oci_execute($stid);
oci_fetch_all($stid, $res);

foreach ($res['CITY'] as $c) {
    print $c . "<br>\n";
}
// Muestra :
//   Beijing
//   Singapore

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Para algunas condiciones utilizadas en las cláusulas IN, utilice variables vinculadas individuales. Los valores desconocidos en el momento de la ejecución podrán definirse a NULL. Esto permite utilizar una sola consulta para todos los usuarios de la aplicación, maximizando así la eficacia del caché Oracle DB.

Asociación de múltiples valores en una cláusula IN

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $m = oci_error();
    trigger_error(htmlentities($m['message']), E_USER_ERROR);
}

$sql = 'SELECT last_name FROM employees WHERE employee_id in (:e1, :e2, :e3)';
$stid = oci_parse($conn, $sql);
$mye1 = 103;
$mye2 = 104;
$mye3 = NULL; // fingimos que no nos fue dado este valor
oci_bind_by_name($stid, ':e1', $mye1);
oci_bind_by_name($stid, ':e2', $mye2);
oci_bind_by_name($stid, ':e3', $mye3);
oci_execute($stid);
oci_fetch_all($stid, $res);
foreach ($res['LAST_NAME'] as $name) {
    print $name ."<br>\n";
}

// Muestra :
//   Ernst
//   Hunold

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Asociación de un ROWID devuelto por una consulta

```
<?php

// Creación de la tabla con :
//   CREATE TABLE mytab (id NUMBER, salary NUMBER, name VARCHAR2(40));
//   INSERT INTO mytab (id, salary, name) VALUES (1, 100, 'Chris');
//   COMMIT;

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $m = oci_error();
    trigger_error(htmlentities($m['message']), E_USER_ERROR);
}

$stid = oci_parse($conn, 'SELECT ROWID, name FROM mytab WHERE id = :id_bv FOR UPDATE');
$id = 1;
oci_bind_by_name($stid, ':id_bv', $id);
oci_execute($stid);
$row = oci_fetch_array($stid, OCI_ASSOC+OCI_RETURN_NULLS);
$rid = $row['ROWID'];
$name = $row['NAME'];

// Modificación del nombre en letra mayúscula & guardado de esta modificación
$name = strtoupper($name);
$stid = oci_parse($conn, 'UPDATE mytab SET name = :n_bv WHERE ROWID = :r_bv');
oci_bind_by_name($stid, ':n_bv', $name);
oci_bind_by_name($stid, ':r_bv', $rid, -1, OCI_B_ROWID);
oci_execute($stid);

// La tabla contiene ahora 1, 100, CHRIS

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Asociación de un ROWID en un INSERT

```
<?php

// Este ejemplo inserta un id & un nombre, luego, actualiza el salario
// Creación de la tabla con :
//   CREATE TABLE mytab (id NUMBER, salary NUMBER, name VARCHAR2(40));
//
// Basado en el ejemplo original de ROWID, proporcionado por thies at thieso dot net (980221)

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $m = oci_error();
    trigger_error(htmlentities($m['message']), E_USER_ERROR);
}

$sql = "INSERT INTO mytab (id, name) VALUES(:id_bv, :name_bv)
        RETURNING ROWID INTO :rid";

$ins_stid = oci_parse($conn, $sql);

$rowid = oci_new_descriptor($conn, OCI_D_ROWID);
oci_bind_by_name($ins_stid, ":id_bv",   $id,    10);
oci_bind_by_name($ins_stid, ":name_bv", $name,  32);
oci_bind_by_name($ins_stid, ":rid",     $rowid, -1, OCI_B_ROWID);

$sql = "UPDATE mytab SET salary = :salary WHERE ROWID = :rid";
$upd_stid = oci_parse($conn, $sql);
oci_bind_by_name($upd_stid, ":rid", $rowid, -1, OCI_B_ROWID);
oci_bind_by_name($upd_stid, ":salary", $salary,   32);

// ids y nombres a insertar
$data = array(1111 => "Larry",
              2222 => "Bill",
              3333 => "Jim");

// Salario de cada persona
$salary = 10000;

// Inserción y actualización inmediata de cada línea
foreach ($data as $id => $name) {
    oci_execute($ins_stid);
    oci_execute($upd_stid);
}

$rowid->free();
oci_free_statement($upd_stid);
oci_free_statement($ins_stid);

// Visualización de las nuevas líneas
$stid = oci_parse($conn, "SELECT * FROM mytab");
oci_execute($stid);
while ($row = oci_fetch_array($stid, OCI_ASSOC+OCI_RETURN_NULLS)) {
    var_dump($row);
}

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Asociación para una función almacenada PL/SQL

```
<?php

// Antes de ejecutar el programa PHP, una función almacenada debe ser creada
// en formato SQL*Plus o SQL Developer :
//
//  CREATE OR REPLACE FUNCTION myfunc(p IN NUMBER) RETURN NUMBER AS
//  BEGIN
//      RETURN p * 3;
//  END;

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message']), E_USER_ERROR);
}

$p = 8;

$stid = oci_parse($conn, 'begin :r := myfunc(:p); end;');
oci_bind_by_name($stid, ':p', $p);

// El valor devuelto es un vínculo OUT. El tipo por omisión deberá ser
// de tipo string, también, la asociación sobre una longitud de 40 significa
// que la cadena devuelta tendrá como máximo 40 caracteres.
oci_bind_by_name($stid, ':r', $r, 40);

oci_execute($stid);

print "$r\n";   // Muestra 24

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Asociación de parámetros a un procedimiento almacenado PL/SQL

```
<?php

// Antes de ejecutar el programa PHP, un procedimiento almacenado debe ser creado
// en formato SQL*Plus o SQL Developer :
//
//  CREATE OR REPLACE PROCEDURE myproc(p1 IN NUMBER, p2 OUT NUMBER) AS
//  BEGIN
//      p2 := p1 * 2;
//  END;

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message']), E_USER_ERROR);
}

$p1 = 8;

$stid = oci_parse($conn, 'begin myproc(:p1, :p2); end;');
oci_bind_by_name($stid, ':p1', $p1);

// El segundo parámetro del procedimiento almacenado es un vínculo OUT.
// El tipo por omisión deberá ser de tipo string, también,
// la asociación sobre una longitud de 40 significa
// que la cadena devuelta tendrá como máximo 40 caracteres.

oci_bind_by_name($stid, ':p2', $p2, 40);

oci_execute($stid);

print "$p2\n";   // Muestra 16

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Asociación sobre una columna CLOB

```
<?php

// Antes de la ejecución, es necesario crear la tabla :
//     CREATE TABLE mytab (mykey NUMBER, myclob CLOB);

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message']), E_USER_ERROR);
}

$mykey = 12343;  // Clave arbitraria para el ejemplo ;

$sql = "INSERT INTO mytab (mykey, myclob)
        VALUES (:mykey, EMPTY_CLOB())
        RETURNING myclob INTO :myclob";

$stid = oci_parse($conn, $sql);
$clob = oci_new_descriptor($conn, OCI_D_LOB);
oci_bind_by_name($stid, ":mykey", $mykey, 5);
oci_bind_by_name($stid, ":myclob", $clob, -1, OCI_B_CLOB);
oci_execute($stid, OCI_DEFAULT);
$clob->save("A very long string");

oci_commit($conn);

// Recuperación de los datos CLOB

$query = 'SELECT myclob FROM mytab WHERE mykey = :mykey';

$stid = oci_parse ($conn, $query);
oci_bind_by_name($stid, ":mykey", $mykey, 5);
oci_execute($stid);

print '<table border="1">';
while ($row = oci_fetch_array($stid, OCI_ASSOC+OCI_RETURN_LOBS)) {
    print '<tr><td>'.$row['MYCLOB'].'</td></tr>';
    // En un bucle, el hecho de liberar la variable antes de la recuperación de
    // la línea siguiente reduce el uso de memoria de PHP
    unset($row);
}
print '</table>';

?>

   
```php

Asociación sobre un booleano en un script PL/SQL

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message']), E_USER_ERROR);
}

$plsql =
  "begin
    :output1 := true;
    :output2 := false;
   end;";

$s = oci_parse($c, $plsql);
oci_bind_by_name($s, ':output1', $output1, -1, OCI_B_BOL);
oci_bind_by_name($s, ':output2', $output2, -1, OCI_B_BOL);
oci_execute($s);
var_dump($output1);  // true
var_dump($output2);  // false

?>

   
```php

## Notas

> [!WARNING]
> No utilice la función `addslashes` y `oci_bind_by_name` simultáneamente, ya que no es necesario añadir comillas. Si es así, entonces las comillas añadidas serán escritas en la base de datos ; de hecho, la función `oci_bind_by_name` inserta los datos sin procesar y no elimina ni las comillas añadidas, ni los caracteres de escape.

> [!NOTE]
> Si asocia una cadena de caracteres a una columna de tipo `CHAR` en una cláusula `WHERE`, recuerde que Oracle utiliza una comparación añadiendo caracteres vacíos para las columnas de tipo `CHAR`. Por lo tanto, su variable PHP debe ser completada con caracteres vacíos para alcanzar la misma longitud que la columna para que la cláusula `WHERE` funcione.

> [!NOTE]
> El argumento PHP `var` es una referencia. Por lo tanto, algunos formatos de bucle pueden no funcionar como se espera :
>
> <div class="informalexample">
>
> ```
> <?php
> foreach ($myarray as $key => $value)  {
>     oci_bind_by_name($stid, $key, $value);
> }
> ?>
>
>      
> ```
>
> </div>
>
> Esto asocia cada clave al valor apuntado por \$value, por lo tanto, todas las variables asociadas apuntan hacia el valor de la última iteración del bucle. En su lugar, utilice esto :
>
> <div class="informalexample">
>
> ```
> <?php
> foreach ($myarray as $key => $value) {
>     oci_bind_by_name($stid, $key, $myarray[$key]);
> }
> ?>
>
>      
> ```
>
> </div>

## Véase también

`oci_bind_array_by_name`, `oci_parse`
