---
title: mysqli::$thread_id
description: Devuelve el identificador del hilo para la conexión actual
source_url: https://www.php.net/manual/es/mysqli.thread-id.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/thread-id.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 1afd3581f
order: 55420
---

mysqli::\$thread_id

mysqli_thread_id

Devuelve el identificador del hilo para la conexión actual

## Descripción

Estilo orientado a objetos

int

mysqli-\>thread_id

Estilo procedimental

```php
mysqli_thread_id(mysqli $mysql): int
```php

La función `mysqli_thread_id` devuelve el identificador del hilo de la conexión actual que puede ser terminado posteriormente utilizando la función `mysqli_kill`. Si la conexión se pierde y se reconecta con la función `mysqli_ping`, el identificador del hilo será diferente. Por lo tanto, se debe recuperar el identificador del hilo únicamente cuando sea necesario.

> [!NOTE]
> El identificador del hilo se asigna por conexión. Esto significa que si la conexión se interrumpe y luego se restablece, se le asignará un nuevo identificador de hilo.
>
> Para terminar una consulta en ejecución, se puede utilizar el comando SQL `KILL QUERY processid`.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

## Valores devueltos

Devuelve el identificador del hilo para la conexión actual.

## Ejemplos

Ejemplo con `$mysqli->thread_id`

Estilo orientado a objetos

```
<?php
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

/* Verificación de la conexión */
if (mysqli_connect_errno()) {
    printf("Fallo en la conexión: %s\n", mysqli_connect_error());
    exit();
}

/* Determina el identificador del hilo */
$thread_id = $mysqli->thread_id;

/* Termina la conexión */
$mysqli->kill($thread_id);

/* Esto debe producir un error */
if (!$mysqli->query("CREATE TABLE myCity LIKE City")) {
    printf("Error: %s\n", $mysqli->error);
    exit;
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

/* Determina el identificador del hilo */
$thread_id = mysqli_thread_id($link);

/* Termina la conexión */
mysqli_kill($link, $thread_id);

/* Esto debe producir un error */
if (!mysqli_query($link, "CREATE TABLE myCity LIKE City")) {
    printf("Error: %s\n", mysqli_error($link));
    exit;
}

/* Cierre de la conexión */
mysqli_close($link);
?>

   
```php

Los ejemplos anteriores mostrarán:

    Error: MySQL server has gone away

## Véase también

`mysqli_kill`
