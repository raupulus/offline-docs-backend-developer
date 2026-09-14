---
title: mysqli::kill
description: Solicita al servidor que finalice un hilo MySQL
source_url: https://www.php.net/manual/es/mysqli.kill.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/kill.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 9b1673cf1
order: 55180
---

mysqli::kill

mysqli_kill

Solicita al servidor que finalice un hilo MySQL

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.4.0. Depender de esta función está altamente desaconsejado.

## Descripción

Estilo orientado a objetos

```php
#[\Deprecated] public mysqli::kill(int $process_id): bool
```php

Estilo procedimental

```php
#[\Deprecated] mysqli_kill(mysqli $mysql, int $process_id): bool
```

`mysqli_kill` se utiliza para solicitar al servidor que finalice un hilo MySQL especificado por el argumento `process_id`. Este valor debe obtenerse llamando a la función `mysqli_thread_id`.

Para detener una consulta en ejecución, se debe utilizar el comando SQL `KILL QUERY process_id`.

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
| 8.4.0 | Los métodos mysqli::kill y `mysqli_kill` están ahora obsoletos. Se recomienda utilizar el comando SQL `KILL`. |

## Ejemplos

Ejemplo con mysqli::kill

Estilo orientado a objetos

```php
<?php
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

/* Verificación de la conexión */
if (mysqli_connect_errno()) {
    printf("Fallo en la conexión: %s\n", mysqli_connect_error());
    exit();
}

/* Determina el id del hilo */
$thread_id = $mysqli->thread_id;

/* Finaliza el hilo */
$mysqli->kill($thread_id);

/* Esto debería producir un error */
if (!$mysqli->query("CREATE TABLE myCity LIKE City")) {
    printf("Error: %s\n", $mysqli->error);
    exit;
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

/* Determina el id del hilo */
$thread_id = mysqli_thread_id($link);

/* Finaliza el hilo */
mysqli_kill($link, $thread_id);

/* Esto debería producir un error */
if (!mysqli_query($link, "CREATE TABLE myCity LIKE City")) {
    printf("Error: %s\n", mysqli_error($link));
    exit;
}

/* Cierre de la conexión */
mysqli_close($link);
?>

   
```

Los ejemplos anteriores mostrarán:

    Error: MySQL server has gone away

## Véase también

`mysqli_thread_id`
