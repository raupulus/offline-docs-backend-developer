---
title: mysqli::change_user
description: Cambia el usuario de la conexión
source_url: https://www.php.net/manual/es/mysqli.change-user.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/change-user.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: ee14f8248
order: 54920
---

mysqli::change_user

mysqli_change_user

Cambia el usuario de la conexión

## Descripción

Estilo orientado a objetos

```php
public #[\SensitiveParameter] mysqli::change_user(string $username, string $password, string $database): bool
```php

Estilo procedimental

```php
#[\SensitiveParameter] mysqli_change_user(mysqli $mysql, string $username, string $password, string $database): bool
```

Intenta conectarse a la base de datos especificada utilizando las credenciales proporcionadas.

A diferencia de mysqli::connect, este método no desconectará la conexión actual si la nueva conexión no puede establecerse.

Para que esta función tenga éxito, los parámetros `username` y `password` deben ser válidos y el usuario en cuestión debe tener los permisos de acceso a la base de datos deseada. Si por alguna razón la autorización falla, el usuario actual se conservará.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

`username`  
El nombre de usuario MySQL.

`password`  
La contraseña MySQL.

`database`  
El nombre de la base de datos. Si es `null` o una cadena vacía, la conexión al servidor se abrirá sin una base de datos por defecto.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Si el informe de errores de mysqli está habilitado (`MYSQLI_REPORT_ERROR`) y la operación solicitada falla, se genera una advertencia. Si, además, el modo está configurado como `MYSQLI_REPORT_STRICT`, se lanza una `mysqli_sql_exception` en su lugar.

## Ejemplos

Reinicio de la sesión de conexión

Estilo orientado a objetos

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "test");

$mysqli->query("SET @a:=1");

$mysqli->change_user("my_user", "my_password", "world");

$result = $mysqli->query("SELECT DATABASE()");
$row = $result->fetch_row();
printf("Base de datos por defecto: %s\n", $row[0]);

$result = $mysqli->query("SELECT @a");
$row = $result->fetch_row();
if ($row[0] === NULL) {
    printf("El valor de la variable a es NULL\n");
}

?>

   
```

Estilo procedimental

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_connect("localhost", "my_user", "my_password", "test");
mysqli_query($link, "SET @a:=1");

$result = mysqli_query($link, "SELECT DATABASE()");
$row = mysqli_fetch_row($result);
printf("Base de datos por defecto: %s\n", $row[0]);

$result = mysqli_query($link, "SELECT @a");
$row = mysqli_fetch_row($result);
if ($row[0] === NULL) {
    printf("El valor de la variable a es NULL\n");
}

?>

   
```

Los ejemplos anteriores mostrarán:

    Base de datos por defecto: world
    El valor de la variable a es NULL

Si `database` es `null` la conexión se abre sin seleccionar una base de datos por defecto

Estilo orientado a objetos

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "test");

$mysqli->change_user("my_user", "my_password", null);

$result = $mysqli->query("SELECT DATABASE()");
$row = $result->fetch_row();
printf("Base de datos por defecto: %s\n", $row[0]);

   
```

Los ejemplos anteriores mostrarán:

    Base de datos por defecto:

## Notas

> [!NOTE]
> El uso de este comando implica siempre que la conexión sea considerada como nueva, independientemente de si la función tiene éxito o no. Una llamada a esta función anulará por lo tanto todas las transacciones activas, cerrará las tablas temporales y desbloqueará las tablas bloqueadas.

## Véase también

`mysqli_connect`, `mysqli_select_db`
