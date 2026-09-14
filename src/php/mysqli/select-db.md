---
title: mysqli::select_db
description: Selecciona una base de datos por defecto para las consultas
source_url: https://www.php.net/manual/es/mysqli.select-db.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/select-db.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 63b99082e
order: 55350
---

mysqli::select_db

mysqli_select_db

Selecciona una base de datos por defecto para las consultas

## Descripción

Estilo orientado a objetos

```php
public mysqli::select_db(string $database): bool
```php

Estilo procedimental

```php
mysqli_select_db(mysqli $mysql, string $database): bool
```

Selecciona la base de datos por defecto (especificada por el argumento `database`) para ser utilizada al ejecutar consultas en la conexión representada por el argumento `mysql`.

> [!NOTE]
> Esta función solo debe utilizarse para cambiar la base de datos por defecto para la conexión actual. La base de datos por defecto puede seleccionarse con el cuarto argumento de la función `mysqli_connect`.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

`database`  
El nombre de la base de datos.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Si el informe de errores de mysqli está habilitado (`MYSQLI_REPORT_ERROR`) y la operación solicitada falla, se genera una advertencia. Si, además, el modo está configurado como `MYSQLI_REPORT_STRICT`, se lanza una `mysqli_sql_exception` en su lugar.

## Ejemplos

Ejemplo con mysqli::select_db

Estilo orientado a objetos

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "test");

/* obtener el nombre de la base de datos por defecto actual */
$result = $mysqli->query("SELECT DATABASE()");
$row = $result->fetch_row();
printf("La base de datos por defecto es %s.\n", $row[0]);

/* cambiar la base de datos por defecto a "world" */
$mysqli->select_db("world");

/* obtener el nombre de la base de datos por defecto actual */
$result = $mysqli->query("SELECT DATABASE()");
$row = $result->fetch_row();
printf("La base de datos por defecto es %s.\n", $row[0]);

   
```

Estilo procedimental

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_connect("localhost", "my_user", "my_password", "test");

/* obtener el nombre de la base de datos por defecto actual */
$result = mysqli_query($link, "SELECT DATABASE()");
$row = mysqli_fetch_row($result);
printf("La base de datos por defecto es %s.\n", $row[0]);

/* cambiar la base de datos por defecto a "world" */
mysqli_select_db($link, "world");

/* obtener el nombre de la base de datos por defecto actual */
$result = mysqli_query($link, "SELECT DATABASE()");
$row = mysqli_fetch_row($result);
printf("La base de datos por defecto es %s.\n", $row[0]);

   
```

Los ejemplos anteriores mostrarán:

    La base de datos por defecto es test.
    La base de datos por defecto es world.

## Véase también

`mysqli_connect`, `mysqli_real_connect`
