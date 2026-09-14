---
title: mysqli::multi_query
description: Ejecuta una o varias consultas en la base de datos
source_url: https://www.php.net/manual/es/mysqli.multi-query.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/multi-query.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 1beae37b6
order: 55200
---

mysqli::multi_query

mysqli_multi_query

Ejecuta una o varias consultas en la base de datos

## Descripción

Estilo orientado a objetos

```php
public mysqli::multi_query(string $query): bool
```php

Estilo procedimental

```php
mysqli_multi_query(mysqli $mysql, string $query): bool
```

Ejecuta una o varias consultas, agrupadas en el parámetro `query` mediante puntos y comas.

> [!WARNING]
> Si la consulta contiene alguna entrada de variable, entonces se deben usar [sentencias preparadas parametrizadas](#mysqli.quickstart.prepared-statements) en su lugar. Alternativamente, los datos deben estar correctamente formateados y todas las cadenas deben ser escapadas usando la función `mysqli_real_escape_string` .

Las consultas se envían en una sola llamada a la base de datos y se procesan de manera secuencial. mysqli_multi_query espera a que la primera consulta se complete antes de devolver el control a PHP. Mientras tanto, el servidor MySQL continuará procesando las consultas restantes de manera asíncrona respecto a PHP y pondrá los resultados a disposición para su recuperación.

Se recomienda utilizar una [do-while](#control-structures.do.while) para procesar varias consultas. La conexión estará ocupada hasta que todas las consultas se completen y sus resultados sean recuperados por PHP. Ninguna otra consulta puede ser emitida en la misma conexión, hasta que todas las consultas sean procesadas. Para procesar la siguiente consulta en la secuencia, utilizar `mysqli_next_result`. Si el siguiente resultado no está aún listo, mysqli esperará la respuesta desde el servidor MySQL. Para verificar si hay más resultados, utilizar `mysqli_more_results`.

Para las consultas que producen un conjunto de resultados, como `SELECT, SHOW, DESCRIBE` o `EXPLAIN`, `mysqli_use_result` o `mysqli_store_result` pueden ser utilizados para recuperar el conjunto de resultados. Para las consultas que no producen un conjunto de resultados, las mismas funciones pueden ser utilizadas para recuperar información como el número de filas afectadas.

> [!TIP]
> Ejecutar una consulta `CALL` para procedimientos almacenados puede producir varios conjuntos de resultados. Si el procedimiento almacenado contiene consultas `SELECT`, los conjuntos de resultados son devueltos en el orden en que son producidos por la ejecución del procedimiento. En general, el llamador no puede saber cuántos conjuntos de resultados devolverá un procedimiento y debe estar preparado para recuperar varios resultados. El resultado final del procedimiento es un resultado de estado que no incluye un conjunto de resultados. El estado indica si el procedimiento tuvo éxito o si se produjo un error.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

`query`  
Una `string` que contiene las consultas a ejecutar. Varias consultas deben estar separadas por un punto y coma.

## Valores devueltos

Devuelve `false` únicamente si la primera consulta falla. Para recuperar las subsecuencias de errores provenientes de otras consultas, se debe llamar primero a la función `mysqli_next_result`.

## Errores/Excepciones

Si el informe de errores de mysqli está habilitado (`MYSQLI_REPORT_ERROR`) y la operación solicitada falla, se genera una advertencia. Si, además, el modo está configurado como `MYSQLI_REPORT_STRICT`, se lanza una `mysqli_sql_exception` en su lugar.

## Ejemplos

Ejemplo con mysqli::multi_query

Estilo orientado a objetos

```php
<?php
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

$query = "SELECT CURRENT_USER();";
$query .= "SELECT Name FROM City ORDER BY ID LIMIT 20, 5";

/* Ejecución de una consulta múltiple */
$mysqli->multi_query($query);
do {
    /* Almacenar el conjunto de resultados en PHP */
    if ($result = $mysqli->store_result()) {
        while ($row = $result->fetch_row()) {
            printf("%s\n", $row[0]);
        }
    }
    /* Imprimir divisor */
    if ($mysqli->more_results()) {
        printf("-----------------\n");
    }
} while ($mysqli->next_result());
?>

   
```

Estilo procedimental

```php
<?php
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

$query = "SELECT CURRENT_USER();";
$query .= "SELECT Name FROM City ORDER BY ID LIMIT 20, 5";

/* Ejecución de una consulta múltiple */
mysqli_multi_query($link, $query);
do {
    /* Almacenar el conjunto de resultados en PHP */
    if ($result = mysqli_store_result($link)) {
        while ($row = mysqli_fetch_row($result)) {
            printf("%s\n", $row[0]);
        }
        /* Mostrar una separación */
        if (mysqli_more_results($link)) {
            printf("-----------------\n");
        }
    }
    /* Imprimir divisor */
    if (mysqli_more_results($link)) {
        printf("-----------------\n");
    }
} while (mysqli_next_result($link));
?>

   
```

Los ejemplos anteriores mostrarán algo similar a:

    my_user@localhost
    -----------------
    Amersfoort
    Maastricht
    Dordrecht
    Leiden
    Haarlemmermeer

## Véase también

`mysqli_query`, `mysqli_use_result`, `mysqli_store_result`, `mysqli_next_result`, `mysqli_more_results`
