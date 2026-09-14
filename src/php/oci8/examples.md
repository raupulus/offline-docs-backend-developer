---
title: Ejemplos
source_url: https://www.php.net/manual/es/oci8.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: 5e41012cf
order: 57160
---

## Ejemplos

Estos ejemplos utilizan, para conectarse a la base de datos, el usuario `HR` que es el esquema `"Human Resources"` proporcionado por la base de datos Oracle. Esta cuenta debe haber sido desbloqueada y la contraseña reestablecida antes de poder utilizarla.

Estos ejemplos se conectan a la base de datos `XE` de su máquina. Modifique la cadena de conexión para que corresponda a su base de datos antes de ejecutar los ejemplos de esta documentación.

Consulta simple

Este ejemplo muestra la ejecución de una consulta y la visualización de los resultados. Las consultas OCI8 utilizan las etapas preparación/ejecución/recuperación de datos.

```php
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

// Preparación de la consulta
$stid = oci_parse($conn, 'SELECT * FROM departments');
if (!$stid) {
    $e = oci_error($conn);
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

// Ejecución de la lógica de la consulta
$r = oci_execute($stid);
if (!$r) {
    $e = oci_error($stid);
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

// Recuperación de los resultados de la consulta
print "<table border='1'>\n";
while ($row = oci_fetch_array($stid, OCI_ASSOC+OCI_RETURN_NULLS)) {
    print "<tr>\n";
    foreach ($row as $item) {
        print "    <td>" . ($item !== null ? htmlentities($item, ENT_QUOTES) : "") . "</td>\n";
    }
    print "</tr>\n";
}
print "</table>\n";

oci_free_statement($stid);
oci_close($conn);

?>

  
```

Inserción de datos utilizando variables ligadas

Las variables ligadas aumentan el rendimiento permitiendo la reutilización del caché y el contexto de ejecución. Las variables ligadas aumentan también la seguridad previniendo muchos casos de inyección SQL.

```php
<?php

// Antes de la ejecución, cree la siguiente tabla:
//   CREATE TABLE MYTABLE (mid NUMBER, myd VARCHAR2(20));

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$stid = oci_parse($conn, 'INSERT INTO MYTABLE (mid, myd) VALUES(:myid, :mydata)');

$id = 60;
$data = 'Some data';

oci_bind_by_name($stid, ':myid', $id);
oci_bind_by_name($stid, ':mydata', $data);

$r = oci_execute($stid);  // ejecución y validación

if ($r) {
    print "Una fila insertada";
}

oci_free_statement($stid);
oci_close($conn);

?>

  
```

Ligadura de una cláusula WHERE de una consulta

Esto muestra la ligadura simple.

```php
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

// Muestra:
//    Austin
//    Ernst
//    Hunold
//    Lorentz
//    Pataballa

oci_free_statement($stid);
oci_close($conn);

?>

  
```

Inserción de datos en una columna CLOB

Para datos grandes, utilice un objeto binario largo (BLOB) o un objeto de caracteres largo (CLOB). Este ejemplo utiliza los CLOB.

```php
<?php

// Antes de la ejecución, cree la siguiente tabla:
//     CREATE TABLE MYTABLE (mykey NUMBER, myclob CLOB);

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$mykey = 12343;  // clave arbitraria para el ejemplo

$sql = "INSERT INTO mytable (mykey, myclob)
        VALUES (:mykey, EMPTY_CLOB())
        RETURNING myclob INTO :myclob";

$stid = oci_parse($conn, $sql);
$clob = oci_new_descriptor($conn, OCI_D_LOB);
oci_bind_by_name($stid, ":mykey", $mykey, 5);
oci_bind_by_name($stid, ":myclob", $clob, -1, OCI_B_CLOB);
oci_execute($stid, OCI_NO_AUTO_COMMIT);
$clob->save("Una cadena realmente muy larga");

oci_commit($conn);

// Recuperación de datos CLOB

$query = 'SELECT myclob FROM mytable WHERE mykey = :mykey';

$stid = oci_parse ($conn, $query);
oci_bind_by_name($stid, ":mykey", $mykey, 5);
oci_execute($stid);

print '<table border="1">';
while ($row = oci_fetch_array($stid, OCI_ASSOC+OCI_RETURN_LOBS)) {
    print '<tr><td>'.$row['MYCLOB'].'</td></tr>';
    // En un bucle, liberar la variable antes de recuperar la
    // segunda línea permite reducir el uso de memoria de PHP
    unset($row);
}
print '</table>';

?>

  
```

Uso de una función almacenada PL/SQL

Debe ligar una variable para el valor devuelto y, opcionalmente, para todos los argumentos de la función PL/SQL.

```php
<?php

/*
  Antes de ejecutar el programa PHP, cree una función almacenada
  en lenguaje SQL*Plus o SQL Developer:

  CREATE OR REPLACE FUNCTION myfunc(p IN NUMBER) RETURN NUMBER AS
  BEGIN
      RETURN p * 3;
  END;

*/

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$p = 8;

$stid = oci_parse($conn, 'begin :r := myfunc(:p); end;');
oci_bind_by_name($stid, ':p', $p);
oci_bind_by_name($stid, ':r', $r, 40);

oci_execute($stid);

print "$r\n";   // Muestra 24

oci_free_statement($stid);
oci_close($conn);

?>

  
```

Uso de una procedimiento almacenado PL/SQL

Con los procedimientos almacenados, debe ligar las variables para todos los argumentos.

```php
<?php

/*
  Antes de ejecutar el programa PHP, cree un procedimiento almacenado en
  lenguaje SQL*Plus o SQL Developer:

  CREATE OR REPLACE PROCEDURE myproc(p1 IN NUMBER, p2 OUT NUMBER) AS
  BEGIN
      p2 := p1 * 2;
  END;

*/

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$p1 = 8;

$stid = oci_parse($conn, 'begin myproc(:p1, :p2); end;');
oci_bind_by_name($stid, ':p1', $p1);
oci_bind_by_name($stid, ':p2', $p2, 40);

oci_execute($stid);

print "$p2\n";   // muestra 16

oci_free_statement($stid);
oci_close($conn);

?>

  
```

Llamada a una función PL/SQL que devuelve un `REF CURSOR`

Cada valor devuelto por la consulta es un `REF CURSOR` a utilizar para recuperar los datos.

```php
<?php
/*
  Cree una función almacenada PL/SQL de la siguiente manera:

  CREATE OR REPLACE FUNCTION myfunc(p1 IN NUMBER) RETURN SYS_REFCURSOR AS
      rc SYS_REFCURSOR;
  BEGIN
      OPEN rc FOR SELECT city FROM locations WHERE ROWNUM < p1;
      RETURN rc;
  END;
*/

$conn = oci_connect('hr', 'welcome', 'localhost/XE');

$stid = oci_parse($conn, 'SELECT myfunc(5) AS mfrc FROM dual');
oci_execute($stid);

echo "<table border='1'>\n";
while (($row = oci_fetch_array($stid, OCI_ASSOC))) {
    echo "<tr>\n";
    $rc = $row['MFRC'];
    oci_execute($rc);  // El valor de la columna devuelto desde la consulta es una referencia de cursor
    while (($rc_row = oci_fetch_array($rc, OCI_ASSOC))) {
        echo "    <td>" . $rc_row['CITY'] . "</td>\n";
    }
    oci_free_statement($rc);
    echo "</tr>\n";
}
echo "</table>\n";

// Muestra:
//   Beijing
//   Bern
//   Bombay
//   Geneva

oci_free_statement($stid);
oci_close($conn);

?>

  
```
