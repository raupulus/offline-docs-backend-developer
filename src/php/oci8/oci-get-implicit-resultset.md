---
title: oci_get_implicit_resultset
description: Retorna el hijo siguiente de un recurso de consulta desde un recurso
  de consulta padre que tiene un juego de resultados implícito de Oracle Database
source_url: https://www.php.net/manual/es/function.oci-get-implicit-resultset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-get-implicit-resultset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_revision: 6047c10c1
order: 57430
---

oci_get_implicit_resultset

Retorna el hijo siguiente de un recurso de consulta desde un recurso de consulta padre que tiene un juego de resultados implícito de Oracle Database

## Descripción

```php
oci_get_implicit_resultset(resource $statement): resource
```php

Utilizado para recuperar juegos recursivos de resultados de consultas después de la ejecución de un bloque almacenado o anónimo Oracle PL/SQL donde este bloque retorna resultados de consultas con la función *DBMS_SQL.RETURN_RESULT* Oracle PL/SQL de la base de datos Oracle 12 (o posterior). Esto permite a los bloques PL/SQL retornar fácilmente resultados de consultas.

La consulta hija puede ser utilizada con cualquiera de las funciones de recuperación OCI8: `oci_fetch`, `oci_fetch_all`, `oci_fetch_array`, `oci_fetch_object`, `oci_fetch_assoc` o `oci_fetch_row`

Las consultas hijas heredan los valores pre-recuperados de sus padres, o pueden ser definidas explícitamente con la función `oci_set_prefetch`.

## Parámetros

`statement`  
Un identificador de consulta OCI8 válido creado por la función `oci_parse` y ejecutado por la función `oci_execute`. El identificador de consulta puede o no estar asociado con una consulta OCI8 que retorna juegos de resultados implícitos.

## Valores devueltos

Retorna un gestor de consulta para la próxima consulta hija disponible en `statement`. Retorna `false` cuando la consulta hija no existe, o cuando todas las consultas hijas han sido retornadas por llamados previos a la función `oci_get_implicit_resultset`.

## Ejemplos

Recuperación de los juegos de resultados implícitos mediante un ciclo

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/pdborcl');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

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

while (($stid_c = oci_get_implicit_resultset($stid))) {
    echo "<h2>Nuevo juego de resultados implícito:</h2>\n";
    echo "<table>\n";
    while (($row = oci_fetch_array($stid_c, OCI_ASSOC+OCI_RETURN_NULLS)) != false) {
        echo "<tr>\n";
        foreach ($row as $item) {
            echo "  <td>".($item!==null?htmlentities($item, ENT_QUOTES|ENT_SUBSTITUTE):"")."</td>\n";
        }
        echo "</tr>\n";
    }
    echo "</table>\n";
}

// Muestra:
//    Nuevo juego de resultados implícito:
//     Beijing 190518
//     Bern    3095
//     Bombay  490231
//    Nuevo juego de resultados implícito:
//     CN
//     CH
//     IN

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Recupera individualmente los gestores de consultas hijas

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/pdborcl');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

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

$stid_1 = oci_get_implicit_resultset($stid);
$stid_2 = oci_get_implicit_resultset($stid);

$row = oci_fetch_array($stid_1, OCI_ASSOC+OCI_RETURN_NULLS);
var_dump($row);
$row = oci_fetch_array($stid_2, OCI_ASSOC+OCI_RETURN_NULLS);
var_dump($row);
$row = oci_fetch_array($stid_1, OCI_ASSOC+OCI_RETURN_NULLS);
var_dump($row);
$row = oci_fetch_array($stid_2, OCI_ASSOC+OCI_RETURN_NULLS);
var_dump($row);

// Muestra:
//    array(2) {
//      ["CITY"]=>
//      string(7) "Beijing"
//      ["POSTAL_CODE"]=>
//      string(6) "190518"
//    }
//    array(1) {
//      ["COUNTRY_ID"]=>
//      string(2) "CN"
//    }
//    array(2) {
//      ["CITY"]=>
//      string(4) "Bern"
//      ["POSTAL_CODE"]=>
//      string(4) "3095"
//    }
//    array(1) {
//      ["COUNTRY_ID"]=>
//      string(2) "CH"
//    }

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Definición explícita del contador de pre-recuperación

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/pdborcl');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$sql = 'DECLARE
            c1 SYS_REFCURSOR;
        BEGIN
           OPEN c1 FOR SELECT city, postal_code FROM locations ORDER BY city;
           DBMS_SQL.RETURN_RESULT(c1);
        END;';

$stid = oci_parse($conn, $sql);
oci_execute($stid);

$stid_c = oci_get_implicit_resultset($stid);
oci_set_prefetch($stid_c, 200);   // Establece la pre-recuperación antes de recuperar de la consulta hija
echo "<table>\n";
while (($row = oci_fetch_array($stid_c, OCI_ASSOC+OCI_RETURN_NULLS)) != false) {
    echo "<tr>\n";
    foreach ($row as $item) {
        echo "  <td>".($item!==null?htmlentities($item, ENT_QUOTES|ENT_SUBSTITUTE):"")."</td>\n";
    }
    echo "</tr>\n";
}
echo "</table>\n";

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Ejemplo de juego de resultados implícito sin utilizar la función `oci_get_implicit_resultset`

Todos los resultados de todas las consultas son retornados consecutivamente.

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/pdborcl');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

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

// Nota: oci_fetch_all y oci_fetch() no pueden ser utilizados de esta manera
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
//    Bern 3095
//    Bombay 490231
//    CN
//    CH
//    IN

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

## Notas

> [!NOTE]
> Para las consultas que devuelven un número muy grande de líneas, el rendimiento puede ser muy significativamente mejorado aumentando el valor de la opción [oci8.default_prefetch](#ini.oci8.default-prefetch) o usando la función `oci_set_prefetch`.
