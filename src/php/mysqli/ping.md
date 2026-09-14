---
title: mysqli::ping
description: Verifica la conexión al servidor y reconecta si ya no existe
source_url: https://www.php.net/manual/es/mysqli.ping.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/ping.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 9b1673cf1
order: 55230
---

mysqli::ping

mysqli_ping

Verifica la conexión al servidor y reconecta si ya no existe

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.4.0. Depender de esta función está altamente desaconsejado.

## Descripción

Estilo orientado a objetos

```php
#[\Deprecated] public mysqli::ping(): bool
```php

Estilo procedimental

```php
#[\Deprecated] mysqli_ping(mysqli $mysql): bool
```

Verifica si la conexión al servidor funciona correctamente. Si ha sido cerrada y la opción global [mysqli.reconnect](#ini.mysqli.reconnect) está activada, se intenta una reconexión automática.

> [!NOTE]
> El parámetro `php.ini` mysqli.reconnect es ignorado por el controlador mysqlnd, por lo tanto las reconexiones automáticas nunca se intentan.

Esta función puede ser utilizada para que los clientes que permanecen abiertos durante mucho tiempo sin actividad puedan verificar que la conexión no ha sido cerrada por el servidor y, en caso afirmativo, realizar una reconexión automática.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Si el informe de errores de mysqli está habilitado (`MYSQLI_REPORT_ERROR`) y la operación solicitada falla, se genera una advertencia. Si, además, el modo está configurado como `MYSQLI_REPORT_STRICT`, se lanza una `mysqli_sql_exception` en su lugar.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Los métodos mysqli::ping y `mysqli_ping` están ahora obsoletos. La funcionalidad `reconnect` ya no está disponible desde PHP 8.2.0, lo que hace que esta función sea obsoleta. |

## Ejemplos

Ejemplo con mysqli::ping

Estilo orientado a objetos

```php
<?php
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

/* Verificación de la conexión */
if ($mysqli->connect_errno) {
    printf("Conexión fallida: %s\n", $mysqli->connect_error);
    exit();
}

/* Verificación si la conexión sigue activa */
if ($mysqli->ping()) {
    printf ("¡La conexión está bien!\n");
} else {
    printf ("Error: %s\n", $mysqli->error);
}

/* Cierre de la conexión */
$mysqli->close();
?>

   
```

Estilo procedimental

```php
<?php
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

/* Verificación de la conexión */
if (mysqli_connect_errno()) {
    printf("Fallo en la conexión: %s\n", mysqli_connect_error());
    exit();
}

/* Verificación si la conexión sigue activa */
if (mysqli_ping($link)) {
    printf ("¡La conexión está bien!\n");
} else {
    printf ("Error: %s\n", mysqli_error($link));
}

/* Cierre de la conexión */
mysqli_close($link);
?>

   
```

Los ejemplos anteriores mostrarán:

    ¡La conexión es válida!
