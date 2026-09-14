---
title: mysqli_stmt::$sqlstate
description: Devuelve el código SQLSTATE de la última operación MySQL
source_url: https://www.php.net/manual/es/mysqli-stmt.sqlstate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_stmt/sqlstate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: d68e83b71
order: 55980
---

mysqli_stmt::\$sqlstate

mysqli_stmt_sqlstate

Devuelve el código SQLSTATE de la última operación MySQL

## Descripción

Estilo orientado a objetos

string

mysqli_stmt-\>sqlstate

Estilo procedimental

```php
mysqli_stmt_sqlstate(mysqli_stmt $statement): string
```php

Devuelve un string que contiene el código de error SQLSTATE de la última sentencia preparada. El código de error consta de 5 caracteres `'00000'`. Los valores de los códigos de error están especificados por las normas ANSI SQL y ODBC. Para la lista completa de valores, consulte el archivo <http://dev.mysql.com/doc/mysql/en/error-handling.html>.

## Parámetros

`statement`  
Solo estilo procedimental: Un objeto `mysqli_stmt` devuelto por `mysqli_stmt_init`.

## Valores devueltos

Devuelve el string que contiene el código de error SQLSTATE. El código de error consta de 5 caracteres. `'00000'` representa la ausencia de error.

## Ejemplos

Estilo orientado a objetos

```
<?php
/* Abre la conexión */
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

/* Verifica la conexión */
if (mysqli_connect_errno()) {
    printf("Fallo en la conexión: %s\n", mysqli_connect_error());
    exit();
}

$mysqli->query("CREATE TABLE myCountry LIKE Country");
$mysqli->query("INSERT INTO myCountry SELECT * FROM Country");

$query = "SELECT Name, Code FROM myCountry ORDER BY Name";
if ($stmt = $mysqli->prepare($query)) {

    /* Borrado de la tabla */
    $mysqli->query("DROP TABLE myCountry");

    /* Ejecución de la consulta */
    $stmt->execute();

    printf("Error: %s.\n", $stmt->sqlstate);

    /* Cierre de la consulta */
    $stmt->close();
}

/* Cierre de la conexión */
$mysqli->close();
?>

   
```php

Estilo procedimental

```
<?php
/* Abre la conexión */
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

/* Verifica la conexión */
if (mysqli_connect_errno()) {
    printf("Fallo en la conexión: %s\n", mysqli_connect_error());
    exit();
}

mysqli_query($link, "CREATE TABLE myCountry LIKE Country");
mysqli_query($link, "INSERT INTO myCountry SELECT * FROM Country");

$query = "SELECT Name, Code FROM myCountry ORDER BY Name";
if ($stmt = mysqli_prepare($link, $query)) {

    /* Borrado de la tabla */
    mysqli_query($link, "DROP TABLE myCountry");

    /* Ejecución de la consulta */
    mysqli_stmt_execute($stmt);

    printf("Error: %s.\n", mysqli_stmt_sqlstate($stmt));

    /* Cierre de la consulta */
    mysqli_stmt_close($stmt);
}

/* Cierre de la conexión */
mysqli_close($link);
?>

   
```php

Los ejemplos anteriores mostrarán:

    Error: 42S02.

## Notas

> [!NOTE]
> Tenga en cuenta que no todos los errores MySQL tienen una correspondencia en SQLSTATE. El valor `HY000` (error general) se utiliza para los errores sin correspondencia.

## Véase también

`mysqli_stmt_errno`, `mysqli_stmt_error`
