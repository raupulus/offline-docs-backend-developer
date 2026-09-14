---
title: mysqli::prepare
description: Prepara una consulta SQL para su ejecución
source_url: https://www.php.net/manual/es/mysqli.prepare.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/prepare.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 63b99082e
order: 55250
---

mysqli::prepare

mysqli_prepare

Prepara una consulta SQL para su ejecución

## Descripción

Estilo orientado a objetos

```php
public mysqli::prepare(string $query): mysqli_stmt
```php

Estilo procedimental

```php
mysqli_prepare(mysqli $mysql, string $query): mysqli_stmt
```

Prepara la consulta SQL y devuelve un gestor de consulta para ser utilizado en futuras operaciones con la consulta. La consulta debe constar de una única consulta SQL.

Los parámetros de marcadores deben ser vinculados a variables utilizadas en las funciones `mysqli_stmt_bind_param` y/o `mysqli_stmt_bind_result` antes de ejecutar la consulta o recuperar las filas.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

`query`  
La consulta, en forma de `string`.

Este parámetro puede incluir uno o más parámetros de marcadores en la consulta SQL con el carácter "signo de interrogación" (`?`) en la posición apropiada.

> [!NOTE]
> Los marcadores están permitidos únicamente en ciertos lugares de las consultas SQL. Por ejemplo, están permitidos en la lista `VALUES()` de una consulta `INSERT` (para especificar los valores de las columnas para una fila), o en una comparación de una cláusula `WHERE` para especificar un valor de comparación. Sin embargo, no están permitidos para los identificadores (de tablas o columnas).

## Valores devueltos

`mysqli_prepare` devuelve un objeto de sentencia o `false` si ocurre un error.

## Errores/Excepciones

Si el informe de errores de mysqli está habilitado (`MYSQLI_REPORT_ERROR`) y la operación solicitada falla, se genera una advertencia. Si, además, el modo está configurado como `MYSQLI_REPORT_STRICT`, se lanza una `mysqli_sql_exception` en su lugar.

## Ejemplos

Ejemplo con mysqli::prepare

Estilo orientado a objetos

```php
<?php
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

/* Verificación de la conexión */
if (mysqli_connect_errno()) {
    printf("Fallo en la conexión: %s\n", mysqli_connect_error());
    exit();
}

$city = "Amersfoort";

/* Crea una consulta preparada */
if ($stmt = $mysqli->prepare("SELECT District FROM City WHERE Name=?")) {

    /* Vinculación de los marcadores */
    $stmt->bind_param("s", $city);

    /* Ejecución de la consulta */
    $stmt->execute();

    /* Vinculación de las variables resultantes */
    $stmt->bind_result($district);

    /* Obtención de los valores */
    $stmt->fetch();

    printf("%s está en el distrito de %s\n", $city, $district);

    /* Cierre de la sentencia */
    $stmt->close();
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

$city = "Amersfoort";

/* Crea una consulta preparada */
if ($stmt = mysqli_prepare($link, "SELECT District FROM City WHERE Name=?")) {

    /* Vinculación de los marcadores */
    mysqli_stmt_bind_param($stmt, "s", $city);

    /* Ejecución de la consulta */
    mysqli_stmt_execute($stmt);

    /* Vinculación de las variables resultantes */
    mysqli_stmt_bind_result($stmt, $district);

    /* Obtención de los valores */
    mysqli_stmt_fetch($stmt);

    printf("%s está en el distrito de %s\n", $city, $district);

    /* Cierre de la sentencia */
    mysqli_stmt_close($stmt);
}

/* Cierre de la conexión */
mysqli_close($link);
?>

   
```

Los ejemplos anteriores mostrarán:

    Amersfoort está en el distrito de Utrecht

## Véase también

`mysqli_stmt_execute`, `mysqli_stmt_fetch`, `mysqli_stmt_bind_param`, `mysqli_stmt_bind_result`, `mysqli_stmt_get_result`, `mysqli_stmt_close`
