---
title: oci_fetch_array
description: Lee una línea de un resultado en forma de array asociativo o numérico
source_url: https://www.php.net/manual/es/function.oci-fetch-array.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-fetch-array.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: ed6de1ae2
order: 57290
---

oci_fetch_array

Lee una línea de un resultado en forma de array asociativo o numérico

## Descripción

```php
oci_fetch_array(resource $statement, [int $mode]): array
```php

Devuelve un array que contiene la siguiente línea de una consulta. Cada entrada de este array corresponde a una columna de la línea. Esta función se utiliza típicamente en un ciclo que devuelve `false` cuando ya no hay más líneas disponibles.

Si el parámetro `statement` corresponde a un bloque PL/SQL devuelto por juegos de resultados implícitos de Oracle Database, entonces las líneas de todos los juegos de resultados serán recuperadas consecutivamente. Si `statement` es devuelto por la función `oci_get_implicit_resultset`, entonces solo el subconjunto de líneas de una sola consulta hija será devuelto.

Para más detalles sobre el mapeo de tipos de datos realizado por la extensión OCI8, lea los [tipos de datos soportados por el driver](#oci8.datatypes).

## Parámetros

`statement`  
Un identificador de consulta OCI8 creado por la función `oci_parse` y ejecutado por la función `oci_execute`, o un identificador de consulta `REF CURSOR`.

Puede ser también un identificador de consulta devuelto por la función `oci_get_implicit_resultset`.

`mode`  
El parámetro opcional `mode` puede ser la combinación de las siguientes constantes:

| Constante | Descripción |
|----|----|
| `OCI_BOTH` | Devuelve un array, indexado numéricamente y con los nombres de columnas. Idéntico a `OCI_ASSOC` + `OCI_NUM`). Este es el comportamiento por defecto. |
| `OCI_ASSOC` | Devuelve un array asociativo. |
| `OCI_NUM` | Devuelve un array indexado numéricamente. |
| `OCI_RETURN_NULLS` | Crea elementos vacíos para los valores `null`. El valor de los elementos será el valor `null` de PHP. |
| `OCI_RETURN_LOBS` | Devuelve el contenido del LOB en lugar de su descriptor. |

Modos para `oci_fetch_array`

El `mode` por defecto es `OCI_BOTH`.

Utilice el operador de adición ""+"" para especificar más de un modo a la vez.

## Valores devueltos

Devuelve un array con índices numéricos o asociativos. Si ya no hay más líneas disponibles para la consulta `statement` entonces `false` será devuelto.

Por defecto, las columnas `LOB` son devueltas en forma de descriptores LOB.

Las columnas `DATE` son devueltas en forma de una cadena con el formato de fecha actual. El formato por defecto puede ser modificado mediante las variables de entorno de Oracle, como `NLS_LANG` o mediante la ejecución del comando `ALTER SESSION SET NLS_DATE_FORMAT`.

Los nombres de columnas que no son sensibles a mayúsculas/minúsculas (por defecto en Oracle), tendrán nombres de atributos en mayúsculas. Los nombres de columnas que son sensibles a mayúsculas/minúsculas, tendrán nombres de atributos utilizando exactamente la misma mayúscula/minúscula de la columna. Utilice la función `var_dump` sobre el objeto de resultado para verificar la mayúscula/minúscula apropiada a utilizar para cada consulta.

El nombre de la tabla no está incluido en el índice del array. Si su consulta contiene dos columnas diferentes con el mismo nombre, utilice la constante `OCI_NUM` o añada un alias a la columna en la consulta para asegurar la unicidad del nombre; ver el ejemplo \#7. De lo contrario, solo una columna será devuelta mediante PHP.

## Ejemplos

Ejemplo con `oci_fetch_array` con `OCI_BOTH`

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$stid = oci_parse($conn, 'SELECT department_id, department_name FROM departments');
oci_execute($stid);

while (($row = oci_fetch_array($stid, OCI_BOTH)) != false) {
    // Utilice nombres de columna en mayúsculas para los índices del array asociativo
    echo $row[0] . " and " . $row['DEPARTMENT_ID']   . " son los mismos<br>\n";
    echo $row[1] . " and " . $row['DEPARTMENT_NAME'] . " son los mismos<br>\n";
}

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Ejemplo con `oci_fetch_array` con `OCI_NUM`

```
<?php

/*
  Antes de la ejecución, cree la tabla:
      CREATE TABLE mytab (id NUMBER, description CLOB);
      INSERT INTO mytab (id, description) values (1, 'A very long string');
      COMMIT;
*/

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$stid = oci_parse($conn, 'SELECT id, description FROM mytab');
oci_execute($stid);

while (($row = oci_fetch_array($stid, OCI_NUM)) != false) {
    echo $row[0] . "<br>\n";
    echo $row[1]->read(11) . "<br>\n"; // esto mostrará los 11 primeros bytes desde DESCRIPTION
}

// Muestra:
//    1
//    A very long

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Ejemplo con `oci_fetch_array` con `OCI_ASSOC`

```
<?php

/*
  Antes de la ejecución, cree la tabla:
      CREATE TABLE mytab (id NUMBER, description CLOB);
      INSERT INTO mytab (id, description) values (1, 'A very long string');
      COMMIT;
*/

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$stid = oci_parse($conn, 'SELECT id, description FROM mytab');
oci_execute($stid);

while (($row = oci_fetch_array($stid, OCI_ASSOC)) != false) {
    echo $row['ID'] . "<br>\n";
    echo $row['DESCRIPTION']->read(11) . "<br>\n"; // esto mostrará los 11 primeros bytes desde DESCRIPTION
}

// Muestra:
//    1
//    A very long

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Ejemplo con `oci_fetch_array` con `OCI_RETURN_NULLS`

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$stid = oci_parse($conn, 'SELECT 1, null FROM dual');
oci_execute($stid);
while (($row = oci_fetch_array ($stid, OCI_ASSOC)) != false) { // Ignora NULLs
    var_dump($row);
}

/*
El código anterior muestra:
  array(1) {
    [1]=>
    string(1) "1"
  }
*/

$stid = oci_parse($conn, 'SELECT 1, null FROM dual');
oci_execute($stid);
while (($row = oci_fetch_array ($stid, OCI_ASSOC+OCI_RETURN_NULLS)) != false) { // Recupera NULLs
    var_dump($row);
}

/*
El código anterior muestra:
  array(2) {
    [1]=>
    string(1) "1"
    ["NULL"]=>
    NULL
  }
*/

?>

    
```php

`oci_fetch_array` con `OCI_RETURN_LOBS`

```
<?php

/*
  Antes de la ejecución, cree la tabla:
      CREATE TABLE mytab (id NUMBER, description CLOB);
      INSERT INTO mytab (id, description) values (1, 'A very long string');
      COMMIT;
*/

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$stid = oci_parse($conn, 'SELECT id, description FROM mytab');
oci_execute($stid);

while (($row = oci_fetch_array($stid, OCI_ASSOC+OCI_RETURN_LOBS)) != false) {
    echo $row['ID'] . "<br>\n";
    echo $row['DESCRIPTION'] . "<br>\n"; // contiene todo el contenido de DESCRIPTION

    // En un ciclo, liberar la variable antes de recuperar una segunda
    // línea permite reducir el uso de memoria de PHP
    unset($row);
}

// Muestra:
//    1
//    A very long string

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Ejemplo con `oci_fetch_array` con nombres de columnas sensibles a mayúsculas/minúsculas

```
<?php

/*
   Antes de la ejecución, cree la tabla:
      CREATE TABLE mytab ("Name" VARCHAR2(20), city VARCHAR2(20));
      INSERT INTO mytab ("Name", city) values ('Chris', 'Melbourne');
      COMMIT;
*/

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$stid = oci_parse($conn, 'select * from mytab');
oci_execute($stid);
$row = oci_fetch_array($stid, OCI_ASSOC+OCI_RETURN_NULLS);

// Dado que 'Name' fue creado como una columna sensible a mayúsculas/minúsculas, la misma mayúscula/minúscula
// es utilizada para los índices del array. Sin embargo, 'CITY' debe ser utilizado
// para los índices de columna no sensible a mayúsculas/minúsculas
print $row['Name'] . "<br>\n";   //  muestra Chris
print $row['CITY'] . "<br>\n";   //  muestra Melbourne

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Ejemplo con `oci_fetch_array` con columnas que poseen nombres duplicados

```
<?php

/*
  Antes de la ejecución, cree la tabla:
      CREATE TABLE mycity (id NUMBER, name VARCHAR2(20));
      INSERT INTO mycity (id, name) values (1, 'Melbourne');
      CREATE TABLE mycountry (id NUMBER, name VARCHAR2(20));
      INSERT INTO mycountry (id, name) values (1, 'Australia');
      COMMIT;
*/

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$sql = 'SELECT mycity.name, mycountry.name
        FROM mycity, mycountry
        WHERE mycity.id = mycountry.id';
$stid = oci_parse($conn, $sql);
oci_execute($stid);
$row = oci_fetch_array($stid, OCI_ASSOC);
var_dump($row);

// La salida contiene solo UNA entrada "NAME":
//    array(1) {
//      ["NAME"]=>
//      string(9) "Australia"
//    }

// Para consultar un nombre de columna duplicado, utilice un alias de columna SQL
// como "AS ctnm":
$sql = 'SELECT mycity.name AS ctnm, mycountry.name
        FROM mycity, mycountry
        WHERE mycity.id = mycountry.id';
$stid = oci_parse($conn, $sql);
oci_execute($stid);
$row = oci_fetch_array($stid, OCI_ASSOC);
var_dump($row);

// La salida contiene ahora 2 columnas:
//    array(2) {
//      ["CTNM"]=>
//      string(9) "Melbourne"
//      ["NAME"]=>
//      string(9) "Australia"
//    }

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Ejemplo con `oci_fetch_array` y columnas `DATE`

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

// Define el formato utilizado para las fechas en esta conexión.
// Por razones de rendimiento, debe modificar el formato mediante un disparador o
// utilizando variables de entorno
$stid = oci_parse($conn, "ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD'");
oci_execute($stid);

$stid = oci_parse($conn, 'SELECT hire_date FROM employees WHERE employee_id = 188');
oci_execute($stid);
$row = oci_fetch_array($stid, OCI_ASSOC);
echo $row['HIRE_DATE'] . "<br>\n";  // Muestra 1997-06-14

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Ejemplo con `oci_fetch_array` y `REF CURSOR`

```
<?php
/*
  Cree el procedimiento almacenado PL/SQL siguiente antes de la ejecución:

  CREATE OR REPLACE PROCEDURE myproc(p1 OUT SYS_REFCURSOR) AS
  BEGIN
    OPEN p1 FOR SELECT * FROM all_objects WHERE ROWNUM < 5000;
  END;
*/

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$stid = oci_parse($conn, 'BEGIN myproc(:rc); END;');
$refcur = oci_new_cursor($conn);
oci_bind_by_name($stid, ':rc', $refcur, -1, OCI_B_CURSOR);
oci_execute($stid);

// Ejecuta el REF CURSOR devuelto y recupera un identificador de consulta
oci_execute($refcur);
echo "<table border='1'>\n";
while (($row = oci_fetch_array($refcur, OCI_ASSOC+OCI_RETURN_NULLS)) != false) {
    echo "<tr>\n";
    foreach ($row as $item) {
        echo "    <td>".($item !== null ? htmlentities($item, ENT_QUOTES) : "")."</td>\n";
    }
    echo "</tr>\n";
}
echo "</table>\n";

oci_free_statement($refcur);
oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Paginación con `oci_fetch_array` utilizando una consulta que utiliza el parámetro `LIMIT`

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

// Obtiene la versión de la base de datos
preg_match('/Release ([0-9]+)\./', oci_server_version($conn), $matches);
$oracleversion = $matches[1];

// Consulta para la paginación
$sql = 'SELECT city, postal_code FROM locations ORDER BY city';

if ($oracleversion >= 12) {
    // Utilización de la sintaxis Oracle 12c OFFSET / FETCH NEXT
    $sql = $sql . ' OFFSET :offset ROWS FETCH NEXT :numrows ROWS ONLY';
} else {
    // Las versiones antiguas de Oracle requieren una consulta anidada
    // para seleccionar un subconjunto desde $sql. O, si la consulta SQL
    // es conocida en el momento del desarrollo, utilice una función
    // row_number() en lugar de esta solución de anidación. En los
    // entornos de producción, asegúrese de evitar las inyecciones
    // SQL con la concatenación.
    $sql = "SELECT * FROM (SELECT a.*, ROWNUM AS my_rnum
                           FROM ($sql) a
                           WHERE ROWNUM <= :offset + :numrows)
            WHERE my_rnum > :offset";
}

$offset  = 0;  // No procesar las primeras líneas
$numrows = 5;  // Devuelve 5 líneas
$stid = oci_parse($conn, $sql);
oci_bind_by_name($stid, ':numrows', $numrows);
oci_bind_by_name($stid, ':offset', $offset);
oci_execute($stid);

while (($row = oci_fetch_array($stid, OCI_ASSOC + OCI_RETURN_NULLS)) != false) {
    echo $row['CITY'] . " " . $row['POSTAL_CODE'] . "<br>\n";
}

// Muestra:
//    Beijing 190518
//    Bern 3095
//    Bombay 490231
//    Geneva 1730
//    Hiroshima 6823

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Ejemplo con `oci_fetch_array` con Oracle Database

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/pdborcl');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

// Requiere OCI8 2.0 (o posterior) y Oracle Database 12c (o posterior)
// Ver también oci_get_implicit_resultset()
$sql = 'DECLARE
           c1 SYS_REFCURSOR;
        BEGIN
           OPEN c1 FOR SELECT city, postal_code FROM locations WHERE ROWNUM < 4 ORDER BY city;
           DBMS_SQL.RETURN_RESULT(c1);
           OPEN c1 FOR SELECT country_id FROM locations WHERE ROWNUM < 4 ORDER BY city;
           DBMS_SQL.RETURN_RESULT(c1);
        END;';

$stid = oci_parse($conn, $sql);
oci_execute($stid);

// Nota: oci_fetch_all y oci_fetch() no pueden ser utilizadas de esta manera
echo "<table>\n";
while (($row = oci_fetch_array($stid, OCI_ASSOC+OCI_RETURN_NULLS)) != false) {
    echo "<tr>\n";
    foreach ($row as $item) {
        echo "  <td>".($item!==null?htmlentities($item, ENT_QUOTES|ENT_SUBSTITUTE):"")."</td>\n";
    }
    echo "</tr>\n";
}
echo "</table>\n";

// Muestra:
//    Beijing 190518
//    Bern    3095
//    Bombay  490231
//    CN
//    CH
//    IN

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

## Notas

> [!NOTE]
> Los índices de los arrays asociativos deben estar en mayúsculas para las columnas estándar de Oracle que han sido creadas con nombres sensibles a mayúsculas/minúsculas.

> [!NOTE]
> Para las consultas que devuelven un número muy grande de líneas, el rendimiento puede ser muy significativamente mejorado aumentando el valor de la opción [oci8.default_prefetch](#ini.oci8.default-prefetch) o usando la función `oci_set_prefetch`.

> [!NOTE]
> La función `oci_fetch_array` es *significativamente* más lenta que la función `oci_fetch_assoc` o `oci_fetch_row`, pero es más flexible.

## Véase también

`oci_fetch`, `oci_fetch_all`, `oci_fetch_assoc`, `oci_fetch_object`, `oci_fetch_row`, `oci_set_prefetch`
