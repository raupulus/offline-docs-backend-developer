---
title: oci_parse
description: Prepara una consulta SQL con Oracle
source_url: https://www.php.net/manual/es/function.oci-parse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-parse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: ed6de1ae2
order: 57520
---

oci_parse

Prepara una consulta SQL con Oracle

## Descripción

```php
oci_parse(resource $connection, string $sql): resource
```php

Prepara la consulta `sql` utilizando la conexión `connection` y devuelve el identificador de consulta que podrá ser utilizado con las funciones `oci_bind_by_name`, `oci_execute`, etc.

Los identificadores de consulta pueden ser liberados utilizando la función `oci_free_statement` o definiendo la variable correspondiente al valor `null`.

## Parámetros

`connection`  
Un identificador de conexión Oracle, devuelto por la función `oci_connect`, `oci_pconnect` o `oci_new_connect`.

`sql`  
La consulta SQL o PL/SQL.

Las consultas SQL *no deben* terminar con un punto y coma (";"). Las consultas PL/SQL *deben* terminar con un punto y coma (";").

## Valores devueltos

Devuelve un manejador de consulta en caso de éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `oci_parse`

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/XE');

// Análisis de la consulta. Note que no hay un punto y coma al final de la consulta SQL
$stid = oci_parse($conn, 'SELECT * FROM employees');
oci_execute($stid);

echo "<table border='1'>\n";
while ($row = oci_fetch_array($stid, OCI_ASSOC+OCI_RETURN_NULLS)) {
    echo "<tr>\n";
    foreach ($row as $item) {
        echo "    <td>" . ($item !== null ? htmlentities($item, ENT_QUOTES) : "") . "</td>\n";
    }
    echo "</tr>\n";
}
echo "</table>\n";

?>

    
```php

Ejemplo con `oci_parse` y una consulta PL/SQL

```
<?php

/*
  Antes de ejecutar este código PHP, debe crear un procedimiento almacenado en
  SQL*Plus o SQL Developer:

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

// Al analizar PL/SQL, debe haber un punto y coma al final de la cadena
$stid = oci_parse($conn, 'begin myproc(:p1, :p2); end;');
oci_bind_by_name($stid, ':p1', $p1);
oci_bind_by_name($stid, ':p2', $p2, 40);

oci_execute($stid);

print "$p2\n";   // muestra 16

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

## Notas

> [!NOTE]
> Esta función *no valida* la consulta `sql`. La única forma de saber si la consulta `sql` es válida es ejecutándola.

## Véase también

`oci_execute`, `oci_free_statement`
