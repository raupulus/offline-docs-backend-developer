---
title: mysqli_stmt::prepare
description: Prepara una consulta SQL para su ejecución
source_url: https://www.php.net/manual/es/mysqli-stmt.prepare.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_stmt/prepare.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 63b99082e
order: 55940
---

mysqli_stmt::prepare

mysqli_stmt_prepare

Prepara una consulta SQL para su ejecución

## Descripción

Estilo orientado a objetos

```php
public mysqli_stmt::prepare(string $query): mixed
```php

Estilo procedimental

```php
mysqli_stmt_prepare(mysqli_stmt $statement, string $query): bool
```

Prepara la consulta SQL `query`, para la sesión de trabajo `stmt`.

Las variables SQL deben asociarse a una variable PHP mediante la función `mysqli_stmt_bind_param` y/o `mysqli_stmt_bind_result`, antes de ejecutar la consulta.

> [!NOTE]
> Si se pasa una consulta a `mysqli_stmt_prepare` que es más larga que `max_allowed_packet`, los códigos de error devueltos serán diferentes según si se utiliza MySQL Native Driver (`mysqlnd`) o MySQL Client Library (`libmysqlclient`). El comportamiento se define como sigue:
>
> - `mysqlnd` en Linux devuelve un código de error 1153. El mensaje de error será “got a packet bigger than `max_allowed_packet` bytes”.
>
> - `mysqlnd` en Windows devuelve un código de error 2006. El mensaje será del tipo “server has gone away”.
>
> - `libmysqlclient` en cualquier plataforma devuelve el código de error 2006. El mensaje será del tipo “server has gone away”.

## Parámetros

`statement`  
Solo estilo procedimental: Un objeto `mysqli_stmt` devuelto por `mysqli_stmt_init`.

`query`  
La consulta, en forma de string. Debe consistir en un comando SQL válido y único.

Este argumento puede incluir una o más variables SQL, utilizando signos de interrogación (`?`) en los lugares adecuados.

> [!NOTE]
> Los marcadores están permitidos únicamente en ciertos lugares de las consultas SQL. Por ejemplo, lo están en la lista `VALUES()` de una consulta `INSERT` (para especificar los valores de las columnas para una fila), o en una comparación de una cláusula `WHERE` para especificar un valor de comparación. Sin embargo, no están permitidos para los identificadores (de tablas o columnas).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Si el informe de errores de mysqli está habilitado (`MYSQLI_REPORT_ERROR`) y la operación solicitada falla, se genera una advertencia. Si, además, el modo está configurado como `MYSQLI_REPORT_STRICT`, se lanza una `mysqli_sql_exception` en su lugar.

## Ejemplos

Ejemplo para mysqli_stmt::prepare

Estilo orientado a objetos

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

$city = "Amersfoort";

/* create a prepared statement */
$stmt = $mysqli->stmt_init();
$stmt->prepare("SELECT District FROM City WHERE Name=?");

/* bind parameters for markers */
$stmt->bind_param("s", $city);

/* execute query */
$stmt->execute();

/* bind result variables */
$stmt->bind_result($district);

/* fetch value */
$stmt->fetch();

printf("%s is in district %s\n", $city, $district);

   
```

Estilo procedimental

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

$city = "Amersfoort";

/* create a prepared statement */
$stmt = mysqli_stmt_init($link);
mysqli_stmt_prepare($stmt, "SELECT District FROM City WHERE Name=?");

/* bind parameters for markers */
mysqli_stmt_bind_param($stmt, "s", $city);

/* execute query */
mysqli_stmt_execute($stmt);

/* bind result variables */
mysqli_stmt_bind_result($stmt, $district);

/* fetch value */
mysqli_stmt_fetch($stmt);

printf("%s is in district %s\n", $city, $district);

   
```

Los ejemplos anteriores mostrarán:

    Amersfoort is in district Utrecht

## Véase también

`mysqli_stmt_init`, `mysqli_stmt_execute`, `mysqli_stmt_fetch`, `mysqli_stmt_bind_param`, `mysqli_stmt_bind_result`, `mysqli_stmt_get_result`, `mysqli_stmt_close`
