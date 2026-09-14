---
title: mysqli::real_escape_string
description: Protege los caracteres especiales de un string para su uso en una consulta
  SQL, teniendo en cuenta el juego de caracteres actual de la conexión
source_url: https://www.php.net/manual/es/mysqli.real-escape-string.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/real-escape-string.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: fc174e8d6
order: 55280
---

mysqli::real_escape_string

mysqli_real_escape_string

Protege los caracteres especiales de un string para su uso en una consulta SQL, teniendo en cuenta el juego de caracteres actual de la conexión

## Descripción

Estilo orientado a objetos

```php
public mysqli::real_escape_string(string $string): string
```php

Estilo procedimental

```php
mysqli_real_escape_string(mysqli $mysql, string $string): string
```

Esta función se utiliza para crear un string SQL válido que podrá ser utilizado en una consulta SQL. El string `string` se codifica para producir un string SQL escapado, teniendo en cuenta el juego de caracteres actual de la conexión.

> [!CAUTION]
> El juego de caracteres debe ser definido ya sea a nivel de servidor, o con la función API `mysqli_set_charset` para que afecte a la función `mysqli_real_escape_string`. Ver la sección sobre los conceptos de [juegos de caracteres](#mysqlinfo.concepts.charset) para más información.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

`string`  
El string a escapar.

Los caracteres codificados son `NUL (ASCII 0)`, `\n`, `\r`, `\`, `'`, `"`, y <span class="keycombo">CTRL+Z</span>.

## Valores devueltos

Devuelve un string escapado.

## Ejemplos

Ejemplo con mysqli::real_escape_string

Estilo orientado a objetos

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

$city = "'s-Hertogenbosch";

/* esta consulta con $city escapado funcionará */
$query = sprintf("SELECT CountryCode FROM City WHERE name='%s'",
    $mysqli->real_escape_string($city));
$result = $mysqli->query($query);
printf("La selección devolvió %d filas.\n", $result->num_rows);

/* esta consulta fallará, porque no escapamos $city */
$query = sprintf("SELECT CountryCode FROM City WHERE name='%s'", $city);
$result = $mysqli->query($query);

   
```

Estilo procedimental

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = mysqli_connect("localhost", "my_user", "my_password", "world");

$city = "'s-Hertogenbosch";

/* esta consulta con $city escapado funcionará */
$query = sprintf("SELECT CountryCode FROM City WHERE name='%s'",
    mysqli_real_escape_string($mysqli, $city));
$result = mysqli_query($mysqli, $query);
printf("La selección devolvió %d filas.\n", mysqli_num_rows($result));

/* esta consulta fallará, porque no escapamos $city */
$query = sprintf("SELECT CountryCode FROM City WHERE name='%s'", $city);
$result = mysqli_query($mysqli, $query);

   
```

Los ejemplos anteriores mostrarán algo similar a:

    Select returned 1 rows.

    Fatal error: Uncaught mysqli_sql_exception: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 's-Hertogenbosch'' at line 1 in...

## Véase también

`mysqli_set_charset`
