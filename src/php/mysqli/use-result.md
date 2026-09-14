---
title: mysqli::use_result
description: Inicializa la recuperación de un conjunto de resultados
source_url: https://www.php.net/manual/es/mysqli.use-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/use-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 63b99082e
order: 55440
---

mysqli::use_result

mysqli_use_result

Inicializa la recuperación de un conjunto de resultados

## Descripción

Estilo orientado a objetos

```php
public mysqli::use_result(): mysqli_result
```php

Estilo procedimental

```php
mysqli_use_result(mysqli $mysql): mysqli_result
```

Se utiliza para inicializar la recuperación de un conjunto de resultados a partir de la última consulta ejecutada utilizando la función `mysqli_real_query` en la conexión especificada por el parámetro `link`.

Esta función o la función `mysqli_store_result` deben ser llamadas antes de que el resultado de una consulta pueda ser recuperado, y para evitar el fallo de la próxima consulta en la conexión a la base de datos.

> [!NOTE]
> La función `mysqli_use_result` no transfiere el conjunto de resultados completo desde la base de datos y por lo tanto no se pueden utilizar funciones como `mysqli_data_seek` para moverse entre los registros. Para utilizar esta funcionalidad, se debe recuperar el conjunto de resultados utilizando `mysqli_store_result`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un objeto de resultados no almacenados o `false` si ocurre un error.

## Errores/Excepciones

Si el informe de errores de mysqli está habilitado (`MYSQLI_REPORT_ERROR`) y la operación solicitada falla, se genera una advertencia. Si, además, el modo está configurado como `MYSQLI_REPORT_STRICT`, se lanza una `mysqli_sql_exception` en su lugar.

## Ejemplos

Ejemplo con mysqli::use_result

Estilo orientado a objetos

```php
<?php
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

/* Verificación de la conexión */
if (mysqli_connect_errno()) {
    printf("Fallo en la conexión: %s\n", mysqli_connect_error());
    exit();
}

$query  = "SELECT CURRENT_USER();";
$query .= "SELECT Name FROM City ORDER BY ID LIMIT 20, 5";

/* Ejecución de múltiples consultas */
if ($mysqli->multi_query($query)) {
    do {
        /* Almacenamiento del primer conjunto de resultados */
        if ($result = $mysqli->use_result()) {
            while ($row = $result->fetch_row()) {
                printf("%s\n", $row[0]);
            }
            $result->close();
        }
        /* Visualización de una demarcación */
        if ($mysqli->more_results()) {
            printf("-----------------\n");
        }
    } while ($mysqli->next_result());
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

$query  = "SELECT CURRENT_USER();";
$query .= "SELECT Name FROM City ORDER BY ID LIMIT 20, 5";

/* Ejecución de múltiples consultas */
if (mysqli_multi_query($link, $query)) {
    do {
        /* Almacenamiento del primer conjunto de resultados */
        if ($result = mysqli_use_result($link)) {
            while ($row = mysqli_fetch_row($result)) {
                printf("%s\n", $row[0]);
            }
            mysqli_free_result($result);
        }
        /* Visualización de una demarcación */
        if (mysqli_more_results($link)) {
            printf("-----------------\n");
        }
    } while (mysqli_next_result($link));
}

/* Cierre de la conexión */
mysqli_close($link);
?>

  
```

Los ejemplos anteriores mostrarán:

    my_user@localhost
    -----------------
    Amersfoort
    Maastricht
    Dordrecht
    Leiden
    Haarlemmermeer

## Véase también

`mysqli_real_query`, `mysqli_store_result`
