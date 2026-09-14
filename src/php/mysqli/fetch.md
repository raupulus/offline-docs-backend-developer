---
title: mysqli_stmt::fetch
description: Lee los resultados de una consulta MySQL preparada en variables vinculadas
source_url: https://www.php.net/manual/es/mysqli-stmt.fetch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_stmt/fetch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: fc7a45481
order: 55840
---

mysqli_stmt::fetch

mysqli_stmt_fetch

Lee los resultados de una consulta MySQL preparada en variables vinculadas

## Descripción

Estilo orientado a objetos

```php
public mysqli_stmt::fetch(): bool
```php

Estilo procedimental

```php
mysqli_stmt_fetch(mysqli_stmt $statement): bool
```

Devuelve el resultado de una consulta preparada en una variable, vinculada por `mysqli_stmt_bind_result`.

> [!NOTE]
> Tenga en cuenta que todas las columnas deben ser vinculadas por la aplicación antes de llamar a `mysqli_stmt_fetch`.

> [!NOTE]
> Los datos se transfieren sin ser almacenados en búfer, sin llamar a la función `mysqli_stmt_store_result`, lo que puede tener un impacto en el rendimiento (pero también, reducir el uso de memoria).

## Parámetros

`statement`  
Solo estilo procedimental: Un objeto `mysqli_stmt` devuelto por `mysqli_stmt_init`.

## Valores devueltos

| Valor   | Descripción                                                 |
|---------|-------------------------------------------------------------|
| `true`  | Éxito. Los datos han sido leídos.                           |
| `false` | Se ha producido un error.                                   |
| `null`  | No hay más líneas para leer o los datos han sido truncados. |

Valores devueltos {#mysqli-stmt.fetch.returnvalues}

## Errores/Excepciones

Si el informe de errores de mysqli está habilitado (`MYSQLI_REPORT_ERROR`) y la operación solicitada falla, se genera una advertencia. Si, además, el modo está configurado como `MYSQLI_REPORT_STRICT`, se lanza una `mysqli_sql_exception` en su lugar.

## Ejemplos

Estilo orientado a objetos

```php
<?php
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

/* Verifica la conexión */
if (mysqli_connect_errno()) {
    printf("Fallo en la conexión: %s\n", mysqli_connect_error());
    exit();
}

$query = "SELECT Name, CountryCode FROM City ORDER by ID DESC LIMIT 150,5";

if ($stmt = $mysqli->prepare($query)) {

    /* Ejecución de la consulta */
    $stmt->execute();

    /* Vinculación de las variables de resultado */
    $stmt->bind_result($name, $code);

    /* Lectura de los valores */
    while ($stmt->fetch()) {
        printf ("%s (%s)\n", $name, $code);
    }

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

/* Verifica la conexión */
if (mysqli_connect_errno()) {
    printf("Fallo en la conexión: %s\n", mysqli_connect_error());
    exit();
}

$query = "SELECT Name, CountryCode FROM City ORDER by ID DESC LIMIT 150,5";

if ($stmt = mysqli_prepare($link, $query)) {

    /* Ejecución de la consulta */
    mysqli_stmt_execute($stmt);

    /* Vinculación de las variables de resultado */
    mysqli_stmt_bind_result($stmt, $name, $code);

    /* Lectura de los valores */
    while (mysqli_stmt_fetch($stmt)) {
        printf ("%s (%s)\n", $name, $code);
    }

    /* Cierre de la sentencia */
    mysqli_stmt_close($stmt);
}

/* Cierre de la conexión */
mysqli_close($link);
?>

   
```

Los ejemplos anteriores mostrarán:

    Rockford (USA)
    Tallahassee (USA)
    Salinas (USA)
    Santa Clarita (USA)
    Springfield (USA)

## Véase también

`mysqli_prepare`, `mysqli_stmt_errno`, `mysqli_stmt_error`, `mysqli_stmt_bind_result`
