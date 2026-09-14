---
title: oci_fetch_all
description: Lee múltiples líneas de un resultado en un array multidimensional
source_url: https://www.php.net/manual/es/function.oci-fetch-all.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-fetch-all.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: d33a6756e
order: 57280
---

oci_fetch_all

Lee múltiples líneas de un resultado en un array multidimensional

## Descripción

```php
oci_fetch_all(resource $statement, array $output, [int $offset], [int $limit], [int $flags]): int
```php

Lee todas las líneas de un resultado Oracle en un array de 2 dimensiones. Por omisión, se devuelven todas las líneas.

Esta función puede ser llamada una sola vez para cada consulta ejecutada mediante la función `oci_execute`.

## Parámetros

`statement`  
Un identificador de consulta OCI8 creado por la función `oci_parse` y ejecutado por la función `oci_execute`, o un identificador de consulta `REF CURSOR`.

`output`  
La variable que contendrá las líneas devueltas.

Las columnas LOB se devuelven en forma de string cuando Oracle soporta la conversión.

Ver la función `oci_fetch_array` para más información sobre cómo se recuperan los datos y sus tipos.

`offset`  
Número de líneas iniciales a ignorar al leer el resultado. Por omisión, este parámetro vale 0, para comenzar la lectura en la primera línea.

`limit`  
Número máximo de líneas a devolver. Por omisión, vale -1, lo que significa que todas las líneas disponibles serán devueltas desde el parámetro `offset` + 1.

`flags`  
El parámetro `flags` indica la estructura del array pero también si deben usarse arrays asociativos.

| Constante | Descripción |
|----|----|
| `OCI_FETCHSTATEMENT_BY_ROW` | El array devuelto contendrá un solo subarray por líneas. |
| `OCI_FETCHSTATEMENT_BY_COLUMN` | El array devuelto contendrá un solo subarray por columnas. Este es el comportamiento por omisión. |

Modos de estructura de arrays para la función `oci_fetch_all`

Los arrays pueden ser indexados ya sea por el encabezado de columna, o numéricamente.

| Constante | Descripción |
|----|----|
| `OCI_NUM` | Se usan índices numéricos para cada array de columnas. |
| `OCI_ASSOC` | Se usan índices asociativos para cada array de columnas. Este es el comportamiento por omisión. |

Modos de indexación de arrays para la función `oci_fetch_all`

Utilice el operador de adición ""+"" para elegir una combinación de estructuras de arrays y modos de indexación.

Los nombres de columnas que no son sensibles a mayúsculas/minúsculas (por omisión en Oracle), tendrán nombres de atributos en mayúsculas. Los nombres de columnas que son sensibles a mayúsculas/minúsculas, tendrán nombres de atributos usando exactamente la misma casilla de la columna. Utilice la función `var_dump` en el objeto de resultado para verificar la casilla apropiada a usar para cada consulta.

Las consultas que poseen más de una columna con el mismo nombre deben usar alias. De lo contrario, solo una de las columnas aparecerá en el array asociativo.

## Valores devueltos

Devuelve el número de líneas recuperadas en el parámetro `output` que puede ser 0 o más.

## Ejemplos

Ejemplo con `oci_fetch_all`

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$stid = oci_parse($conn, 'SELECT POSTAL_CODE, CITY FROM locations WHERE ROWNUM < 3');
oci_execute($stid);

$nrows = oci_fetch_all($stid, $res);

echo "$nrows rows fetched<br>\n";
var_dump($res);

// var_dump mostrará:
//    2 rows fetched
//    array(2) {
//      ["POSTAL_CODE"]=>
//      array(2) {
//        [0]=>
//        string(6) "00989x"
//        [1]=>
//        string(6) "10934x"
//      }
//      ["CITY"]=>
//      array(2) {
//        [0]=>
//        string(4) "Roma"
//        [1]=>
//        string(6) "Venice"
//      }
//    }

// Mostrar resultados
echo "<table border='1'>\n";
foreach ($res as $col) {
    echo "<tr>\n";
    foreach ($col as $item) {
        echo "    <td>".($item !== null ? htmlentities($item, ENT_QUOTES) : "")."</td>\n";
    }
    echo "</tr>\n";
}
echo "</table>\n";

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Ejemplo con `oci_fetch_all` y `OCI_FETCHSTATEMENT_BY_ROW`

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$stid = oci_parse($conn, 'SELECT POSTAL_CODE, CITY FROM locations WHERE ROWNUM < 3');
oci_execute($stid);

$nrows = oci_fetch_all($stid, $res, null, null, OCI_FETCHSTATEMENT_BY_ROW);

echo "$nrows líneas recuperadas<br>\n";
var_dump($res);

// Muestra:
//    2 líneas recuperadas
//    array(2) {
//      [0]=>
//      array(2) {
//        ["POSTAL_CODE"]=>
//        string(6) "00989x"
//        ["CITY"]=>
//        string(4) "Roma"
//      }
//      [1]=>
//      array(2) {
//        ["POSTAL_CODE"]=>
//        string(6) "10934x"
//        ["CITY"]=>
//        string(6) "Venice"
//      }
//    }

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Ejemplo con `oci_fetch_all` y `OCI_NUM`

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$stid = oci_parse($conn, 'SELECT POSTAL_CODE, CITY FROM locations WHERE ROWNUM < 3');
oci_execute($stid);

$nrows = oci_fetch_all($stid, $res, null, null, OCI_FETCHSTATEMENT_BY_ROW + OCI_NUM);

echo "$nrows líneas recuperadas<br>\n";
var_dump($res);

// Muestra:
//    2 líneas recuperadas
//    array(2) {
//      [0]=>
//      array(2) {
//        [0]=>
//        string(6) "00989x"
//        [1]=>
//        string(4) "Roma"
//      }
//      [1]=>
//      array(2) {
//        [0]=>
//        string(6) "10934x"
//        [1]=>
//        string(6) "Venice"
//      }
//    }

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

## Notas

> [!NOTE]
> El uso del parámetro `offset` es realmente ineficiente. Todas las líneas a evitar están incluidas en el conjunto de resultados devuelto por la base de datos a PHP. Luego, son descartadas. Es más eficiente usar una consulta SQL para restringir el alcance de las líneas deseadas. Ver la función `oci_fetch_array` para un ejemplo concreto.

> [!NOTE]
> Las consultas que devuelven un número muy grande de líneas pueden ahorrar memoria al usar funciones que recuperan una sola línea, como hace la función `oci_fetch_array`.

> [!NOTE]
> Para las consultas que devuelven un número muy grande de líneas, el rendimiento puede ser muy significativamente mejorado aumentando el valor de la opción [oci8.default_prefetch](#ini.oci8.default-prefetch) o usando la función `oci_set_prefetch`.

> [!NOTE]
> Esta función no devolverá líneas desde un conjunto de resultados implícito de una base de datos Oracle 12*c*. Utilice en su lugar la función `oci_fetch_array`.

## Véase también

`oci_fetch`, `oci_fetch_array`, `oci_fetch_assoc`, `oci_fetch_object`, `oci_fetch_row`, `oci_set_prefetch`
