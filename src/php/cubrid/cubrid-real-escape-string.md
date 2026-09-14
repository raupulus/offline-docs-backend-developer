---
title: cubrid_real_escape_string
description: Escapar caracteres especiales en una cadena para usarla en una sentencia
  SQL
source_url: https://www.php.net/manual/es/function.cubrid-real-escape-string.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/cubridmysql/cubrid-real-escape-string.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_revision: 22492de2e
order: 8820
---

cubrid_real_escape_string

Escapar caracteres especiales en una cadena para usarla en una sentencia SQL

## Descripción

```php
cubrid_real_escape_string(string $unescaped_string, [resource $conn_identifier]): string
```php

Esta función devuelve la versión escapada de la cadena dada. Escapará los siguientes caracteres: `'`. En general, las comillas simples se usan para encerrar strings. Las comillas dobles se pueden usar también dependiendo del valor de ansi_quotes, que es un parámetro relacionado con sentencias SQL. Si el valor de ansi_quotes value está establecido a no, los strings encerrados entre comillas dobles se tratan como strings, no como identificadores. El valor predeterminado es yes. Si quiere incluir una comilla simple como parte de una cadena de caracteres, introduzca dos comillas simples en una fila.

## Parámetros

`unescaped_string`  
La cadena que va a ser escapada.

`conn_identifier`  
La conexión CUBRID. Si el identificador de conexión no se especifica, se asume el último enlace abierto por `cubrid_connect`.

## Valores devueltos

La versión escapada de la cadena dada, en caso de éxito.

`false` en caso de fallo.

## Ejemplos

Ejemplo de `cubrid_real_escape_string`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb");

$unescaped_str = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~';
$escaped_str = cubrid_real_escape_string($unescaped_str);

$len = strlen($unescaped_str);

@cubrid_execute($conn, "DROP TABLE cubrid_test");
cubrid_execute($conn, "CREATE TABLE cubrid_test (t char($len))");
cubrid_execute($conn, "INSERT INTO cubrid_test (t) VALUES('$escaped_str')");

$req = cubrid_execute($conn, "SELECT * FROM cubrid_test");
$row = cubrid_fetch_assoc($req);

var_dump($row);

cubrid_close_request($req);
cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    array(1) {
      ["t"]=>
      string(95) " !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    }
