---
title: oci_bind_array_by_name
description: Asocia un array PHP a un parámetro de array Oracle PL/SQL
source_url: https://www.php.net/manual/es/function.oci-bind-array-by-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-bind-array-by-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: ed6de1ae2
order: 57180
---

oci_bind_array_by_name

Asocia un array PHP a un parámetro de array Oracle PL/SQL

## Descripción

```php
oci_bind_array_by_name(resource $statement, string $param, array $var, int $max_array_length, [int $max_item_length], [int $type]): bool
```php

Asocia un array PHP `var` a un marcador Oracle `param`, que apunta a un array PL/SQL. Puede ser utilizado para entrada o salida, dependiendo de la configuración en tiempo de ejecución.

## Parámetros

`statement`  
Un identificador de consulta OCI válido.

`param`  
El marcador Oracle.

`var`  
Un array.

`max_array_length`  
Especifica la longitud máxima de los arrays de entrada y resultado.

`max_item_length`  
Define la longitud máxima para los elementos del array. Si `max_item_length` no se proporciona o si vale -1, `oci_bind_array_by_name` buscará el elemento más largo en el array de entrada y lo utilizará como longitud máxima.

`type`  
Debe ser utilizado para definir el tipo de los elementos PL/SQL. Consulte la lista de tipos disponibles a continuación:

- `SQLT_NUM` - para arrays de NUMBER.

- `SQLT_INT` - para arrays INTEGER (Nota: INTEGER actualmente es un sinónimo de NUMBER(38), pero el tipo `SQLT_NUM` no funcionará en este caso aunque sean sinónimos).

- `SQLT_FLT` - para arrays de FLOAT.

- `SQLT_AFC` - para arrays de CHAR.

- `SQLT_CHR` - para arrays de VARCHAR2.

- `SQLT_VCS` - para arrays de VARCHAR.

- `SQLT_AVC` - para arrays de CHARZ.

- `SQLT_STR` - para arrays de STRING.

- `SQLT_LVC` - para arrays de LONG VARCHAR.

- `SQLT_ODT` - para arrays de DATE.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `oci_bind_array_by_name`

```
<?php

$conn = oci_connect("hr", "hrpwd", "localhost/XE");
if (!$conn) {
    $m = oci_error();
    trigger_error(htmlentities($m['message']), E_USER_ERROR);
}

$create = "CREATE TABLE bind_example(name VARCHAR(20))";
$stid = oci_parse($conn, $create);
oci_execute($stid);

$create_pkg = "
CREATE OR REPLACE PACKAGE ARRAYBINDPKG1 AS
  TYPE ARRTYPE IS TABLE OF VARCHAR(20) INDEX BY BINARY_INTEGER;
  PROCEDURE iobind(c1 IN OUT ARRTYPE);
END ARRAYBINDPKG1;";
$stid = oci_parse($conn, $create_pkg);
oci_execute($stid);

$create_pkg_body = "
CREATE OR REPLACE PACKAGE BODY ARRAYBINDPKG1 AS
  CURSOR CUR IS SELECT name FROM bind_example;
  PROCEDURE iobind(c1 IN OUT ARRTYPE) IS
    BEGIN
    -- Bulk Insert
    FORALL i IN INDICES OF c1
      INSERT INTO bind_example VALUES (c1(i));

    -- Fetch and reverse;
    IF NOT CUR%ISOPEN THEN
      OPEN CUR;
    END IF;
    FOR i IN REVERSE 1..5 LOOP
      FETCH CUR INTO c1(i);
      IF CUR%NOTFOUND THEN
        CLOSE CUR;
        EXIT;
      END IF;
    END LOOP;
  END iobind;
END ARRAYBINDPKG1;";
$stid = oci_parse($conn, $create_pkg_body);
oci_execute($stid);

$stid = oci_parse($conn, "BEGIN arraybindpkg1.iobind(:c1); END;");
$array = array("one", "two", "three", "four", "five");
oci_bind_array_by_name($stid, ":c1", $array, 5, -1, SQLT_CHR);
oci_execute($stid);

var_dump($array);

?>

    
```php
