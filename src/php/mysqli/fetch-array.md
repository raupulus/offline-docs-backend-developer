---
title: mysqli_result::fetch_array
description: Obtiene la siguiente fila de un conjunto de resultados como un array
  asociativo, numérico o ambos
source_url: https://www.php.net/manual/es/mysqli-result.fetch-array.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_result/fetch-array.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 035c126c0
order: 55550
---

mysqli_result::fetch_array

mysqli_fetch_array

Obtiene la siguiente fila de un conjunto de resultados como un array asociativo, numérico o ambos

## Descripción

Estilo orientado a objetos

```php
public mysqli_result::fetch_array([int $mode]): array
```php

Estilo procedimental

```php
mysqli_fetch_array(mysqli_result $result, [int $mode]): array
```

Devuelve una fila de datos del conjunto de resultados y la retorna como un array. Cada llamada posterior a esta función retornará la siguiente fila en el conjunto de resultados, o `null` si no hay más filas.

Además de almacenar los datos como un array con índices numéricos, también puede almacenarlos en un array asociativo, utilizando los nombres de los campos como claves.

Si dos o más columnas del resultado tienen el mismo nombre, la última columna tendrá prioridad y sobrescribirá todos los datos anteriores. Para acceder a las otras columnas con el mismo nombre, se debe utilizar el índice numérico o crear un alias para cada columna.

> [!NOTE]
> Los nombres de los campos devueltos por esta función son *sensibles a la case*.

> [!NOTE]
> Esta función define los campos NULL al valor PHP `null`.

## Parámetros

`result`  
Solo estilo procedimental: Un objeto `mysqli_result` devuelto por `mysqli_query`, `mysqli_store_result`, `mysqli_use_result` o `mysqli_stmt_get_result`.

`mode`  
El segundo argumento opcional es una constante que indica qué tipo de array debe ser retornado a partir de la fila de datos actual. Los valores posibles para este parámetro son las constantes `MYSQLI_ASSOC`, `MYSQLI_NUM`, y `MYSQLI_BOTH`.

Al utilizar la constante `MYSQLI_ASSOC`, esta función se comportará como la función `mysqli_fetch_assoc`, mientras que `MYSQLI_NUM` hará que actúe como la función `mysqli_fetch_row`. La constante `MYSQLI_BOTH` creará un array que será tanto asociativo como indexado numéricamente.

## Valores devueltos

Retorna un array que representa la fila recuperada, `null` si no hay más filas en el conjunto de resultados, o `false` si ocurre un error.

## Ejemplos

Ejemplo de mysqli_result::fetch_array

Estilo orientado a objetos

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

$query = "SELECT Name, CountryCode FROM City ORDER BY ID LIMIT 3";
$result = $mysqli->query($query);

/* Array numérico */
$row = $result->fetch_array(MYSQLI_NUM);
printf("%s (%s)\n", $row[0], $row[1]);

/* Array asociativo */
$row = $result->fetch_array(MYSQLI_ASSOC);
printf("%s (%s)\n", $row["Name"], $row["CountryCode"]);

/* Array asociativo y numérico */
$row = $result->fetch_array(MYSQLI_BOTH);
printf("%s (%s)\n", $row[0], $row["CountryCode"]);

   
```

Estilo procedimental

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = mysqli_connect("localhost", "my_user", "my_password", "world");

$query = "SELECT Name, CountryCode FROM City ORDER by ID LIMIT 3";
$result = mysqli_query($mysqli, $query);

/* Array numérico */
$row = mysqli_fetch_array($result, MYSQLI_NUM);
printf("%s (%s)\n", $row[0], $row[1]);

/* Array asociativo */
$row = mysqli_fetch_array($result, MYSQLI_ASSOC);
printf("%s (%s)\n", $row["Name"], $row["CountryCode"]);

/* Array asociativo y numérico */
$row = mysqli_fetch_array($result, MYSQLI_BOTH);
printf("%s (%s)\n", $row[0], $row["CountryCode"]);

   
```

Los ejemplos anteriores mostrarán algo similar a:

    Kabul (AFG)
    Qandahar (AFG)
    Herat (AFG)

## Véase también

`mysqli_fetch_assoc`, `mysqli_fetch_column`, `mysqli_fetch_row`, `mysqli_fetch_object`, `mysqli_query`, `mysqli_data_seek`
