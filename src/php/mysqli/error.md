---
title: mysqli::$error
description: Devuelve un string que describe el último error
source_url: https://www.php.net/manual/es/mysqli.error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 7e5d0d1bb
order: 55030
---

mysqli::\$error

mysqli_error

Devuelve un string que describe el último error

## Descripción

Estilo orientado a objetos

string

mysqli-\>error

Estilo procedimental

```php
mysqli_error(mysqli $mysql): string
```php

Devuelve el string que describe el error ocurrido durante la última llamada a una función MySQLi, ya sea que dicha llamada haya tenido éxito o haya fallado.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

## Valores devueltos

Un string que describe el error. Un string vacío si no ha ocurrido ningún error.

## Ejemplos

Ejemplo con `$mysqli->error`

Estilo orientado a objetos

```
<?php
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

/* Verificación de la conexión */
if ($mysqli->connect_errno) {
    printf("Fallo en la conexión: %s\n", $mysqli->connect_error);
    exit();
}

if (!$mysqli->query("SET a=1")) {
    printf("Mensaje de error: %s\n", $mysqli->error);
}

/* Cierre de la conexión */
$mysqli->close();
?>

   
```php

Estilo procedimental

```
<?php
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

/* Verificación de la conexión */
if (mysqli_connect_errno()) {
    printf("Fallo en la conexión: %s\n", mysqli_connect_error());
    exit();
}

if (!mysqli_query($link, "SET a=1")) {
    printf("Mensaje de error: %s\n", mysqli_error($link));
}

/* Cierre de la conexión */
mysqli_close($link);
?>

   
```php

Los ejemplos anteriores mostrarán:

    Mensaje de error: Unknown system variable 'a'

## Véase también

`mysqli_connect_errno`, `mysqli_connect_error`, `mysqli_errno`, `mysqli_sqlstate`
