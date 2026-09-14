---
title: oci_set_prefetch
description: Indica el número de filas que deben leerse por adelantado por Oracle
source_url: https://www.php.net/manual/es/function.oci-set-prefetch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-set-prefetch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: f80105b4f
order: 57670
---

oci_set_prefetch

Indica el número de filas que deben leerse por adelantado por Oracle

## Descripción

```php
oci_set_prefetch(resource $statement, int $rows): bool
```php

Define el número de filas a pre-cargar por las bibliotecas clientes de Oracle después de una llamada exitosa a la función `oci_execute` pero también para cada llamada a las funciones internas de recuperación de filas en la base de datos. Para las consultas que devuelven un gran número de filas, el rendimiento puede mejorar significativamente aumentando el número de filas a pre-cargar respecto al valor por omisión definido por la opción de configuración [oci8.default_prefetch](#ini.oci8.default-prefetch).

La pre-carga es una forma eficiente de devolver más de una fila de datos desde la base de datos por cada envío de red. Esto permite una mejor utilización de la red y del CPU. La pre-carga de filas es interna a OCI8 y el comportamiento de las funciones de recuperación de datos permanece inalterado según el valor del contador de pre-carga. Por ejemplo, la función `oci_fetch_row` siempre devolverá una fila. El buffer de pre-carga es específico de cada consulta y no será utilizado para re-ejecutar consultas o por otras conexiones.

Es conveniente llamar a la función `oci_set_prefetch` antes de la función `oci_execute`.

Una forma de mejorar la eficiencia es definir el valor de pre-carga a un valor razonable según la red y la base de datos a gestionar. Para las consultas que devuelven un número muy grande de filas, es conveniente recuperar el conjunto de filas por partes (es decir, definir el valor de pre-carga a un valor inferior al número total de filas). Esto permite a la base de datos gestionar las consultas de otros usuarios mientras el script PHP gestiona el conjunto de filas actual.

La pre-carga fue introducida en Oracle 8*i*. La pre-carga `REF CURSOR` fue introducida en Oracle 11*g*R2 y está disponible cuando PHP está vinculado con las bibliotecas clientes de Oracle 11*g*R2 (o superior). Los cursores anidados de pre-carga fueron introducidos en Oracle 11*g*R2 y requieren tanto las bibliotecas clientes de Oracle, como una base de datos en versión 11*g*R2 (o superior).

La pre-carga no es soportada cuando las consultas contienen columnas de tipo LONG o LOB. El valor de pre-carga será utilizado en todas las situaciones donde la pre-carga es soportada.

Al utilizar la base de datos Oracle 12*c*, el conjunto de valores pre-cargados por PHP puede ser sobrescrito por el archivo de configuración cliente de Oracle `oraaccess.xml`. Consulte la documentación de Oracle para más detalles.

## Parámetros

`statement`  
Un identificador de consulta OCI8 creado por la función `oci_parse` y ejecutado por la función `oci_execute`, o un identificador de consulta `REF CURSOR`.

`rows`  
El número de filas a pre-cargar, \>=0

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Modificación del valor de pre-carga para una consulta

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/XE');

$stid = oci_parse($conn, 'SELECT * FROM myverybigtable');
oci_set_prefetch($stid, 300);  // A definir antes de la llamada a la función oci_execute()
oci_execute($stid);

echo "<table border='1'>\n";
while ($row = oci_fetch_array($stid, OCI_ASSOC+OCI_RETURN_NULLS)) {
    echo "<tr>\n";
    foreach ($row as $item) {
        echo "    <td>".($item !== null ? htmlentities($item, ENT_QUOTES) : "")."</td>\n";
    }
    echo "</tr>\n";
}
echo "</table>\n";

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

Modificación del valor de pre-carga para una recuperación REF CURSOR

```
<?php
/*
  Creación del procedimiento almacenado PL/SQL siguiente :

  CREATE OR REPLACE PROCEDURE myproc(p1 OUT SYS_REFCURSOR) AS
  BEGIN
    OPEN p1 FOR SELECT * FROM all_objects WHERE ROWNUM < 5000;
  END;
*/

$conn = oci_connect('hr', 'welcome', 'localhost/XE');

$stid = oci_parse($conn, 'BEGIN myproc(:rc); END;');
$refcur = oci_new_cursor($conn);
oci_bind_by_name($stid, ':rc', $refcur, -1, OCI_B_CURSOR);
oci_execute($stid);

// Modificación del valor de pre-carga antes de la ejecución del cursor.
// La pre-carga REF CURSOR funciona cuando PHP está vinculado con las bibliotecas clientes
// Oracle 11gR2 (o superior)
oci_set_prefetch($refcur, 200);
oci_execute($refcur);

echo "<table border='1'>\n";
while ($row = oci_fetch_array($refcur, OCI_ASSOC+OCI_RETURN_NULLS)) {
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

Si PHP OCI8 recupera datos desde un cursor `REF CURSOR` y luego devuelve el cursor `REF CURSOR` a un segundo procedimiento almacenado para su procesamiento, entonces es conveniente definir la pre-carga de `REF CURSOR` a `0` para evitar perder filas del conjunto de resultados. El valor de pre-carga es el número de filas adicionales a recuperar para cada llamada interna OCI8 a la base de datos, por lo tanto, definirlo a `0` significa simplemente que se desea recuperar una sola fila a la vez.

Definición del valor de pre-carga al devolver un cursor `REF CURSOR` a Oracle

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/orcl');

// Recuperación del cursor REF CURSOR
$stid = oci_parse($conn, 'BEGIN myproc(:rc_out); END;');
$refcur = oci_new_cursor($conn);
oci_bind_by_name($stid, ':rc_out', $refcur, -1, OCI_B_CURSOR);
oci_execute($stid);

// Muestra 2 filas, pero no pre-carga filas adicionales
// de lo contrario, estas filas adicionales no serán pasadas a myproc_use_rc().
oci_set_prefetch($refcur, 0);
oci_execute($refcur);
$row = oci_fetch_array($refcur);
var_dump($row);
$row = oci_fetch_array($refcur);
var_dump($row);

// pasa el cursor REF CURSOR a myproc_use_rc() para realizar otros
// procesamientos en el conjunto de resultados
$stid = oci_parse($conn, 'begin myproc_use_rc(:rc_in); end;');
oci_bind_by_name($stid, ':rc_in', $refcur, -1, OCI_B_CURSOR);
oci_execute($stid);

?>

    
```php

## Véase también

la opción de configuración [oci8.default_prefetch](#ini.oci8.default-prefetch)
