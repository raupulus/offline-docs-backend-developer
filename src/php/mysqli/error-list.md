---
title: mysqli::$error_list
description: Devuelve una lista de errores desde el último comando ejecutado
source_url: https://www.php.net/manual/es/mysqli.error-list.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/error-list.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: e2f2172bf
order: 55020
---

mysqli::\$error_list

mysqli_error_list

Devuelve una lista de errores desde el último comando ejecutado

## Descripción

Estilo orientado a objetos

array

mysqli-\>error_list

Estilo procedimental

```php
mysqli_error_list(mysqli $mysql): array
```php

Devuelve un array de errores desde la llamada más reciente a una función MySQLi, ya sea que haya tenido éxito o no.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

## Valores devueltos

Una lista de errores, cada uno en forma de un array asociativo que contiene el número de error (errno), el mensaje de error (error) y el estado SQL (sqlstate).

## Ejemplos

Ejemplo con `$mysqli->error_list`

Estilo orientado a objetos

```
<?php
$mysqli = new mysqli("localhost", "nobody", "");

/* Verifica la conexión */
if (mysqli_connect_errno()) {
    printf("La conexión ha fallado: %s\n", mysqli_connect_error());
    exit();
}

if (!$mysqli->query("SET a=1")) {
    print_r($mysqli->error_list);
}

/* Cierra la conexión */
$mysqli->close();
?>

   
```php

Estilo procedimental

```
<?php
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

/* Verifica la conexión */
if (mysqli_connect_errno()) {
    printf("La conexión ha fallado: %s\n", mysqli_connect_error());
    exit();
}

if (!mysqli_query($link, "SET a=1")) {
    print_r(mysqli_error_list($link));
}

/* Cierra la conexión */
mysqli_close($link);
?>

   
```php

Los ejemplos anteriores mostrarán:

    Array
    (
        [0] => Array
            (
                [errno] => 1193
                [sqlstate] => HY000
                [error] => Unknown system variable 'a'
            )

    )

## Véase también

`mysqli_connect_errno`, `mysqli_connect_error`, `mysqli_error`, `mysqli_sqlstate`
