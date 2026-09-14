---
title: mysqli::$errno
description: Devuelve el último código de error producido
source_url: https://www.php.net/manual/es/mysqli.errno.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/errno.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_revision: 614d77598
order: 55010
---

mysqli::\$errno

mysqli_errno

Devuelve el último código de error producido

## Descripción

Estilo orientado a objetos

int

mysqli-\>errno

Estilo procedimental

```php
mysqli_errno(mysqli $mysql): int
```php

Devuelve el código de error para la última llamada a una función MySQLi que puede fallar o tener éxito, respetando la conexión definida por el parámetro `link`.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

## Valores devueltos

El valor del código de error para la última llamada, si falla. `0` significa que no ha ocurrido ningún error.

## Ejemplos

Ejemplo con `$mysqli->errno`

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
    printf("Código de Error: %d\n", $mysqli->errno);
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
    printf("Código de Error: %d\n", mysqli_errno($link));
}

/* Cierre de la conexión */
mysqli_close($link);
?>

   
```php

Los ejemplos anteriores mostrarán:

    Código de Error: 1193

## Véase también

`mysqli_connect_errno`, `mysqli_connect_error`, `mysqli_error`, `mysqli_sqlstate`
