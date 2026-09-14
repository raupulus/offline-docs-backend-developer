---
title: mysqli_result::fetch_column
description: Recupera una sola columna de la siguiente fila de un conjunto de resultados
source_url: https://www.php.net/manual/es/mysqli-result.fetch-column.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_result/fetch-column.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 035c126c0
order: 55570
---

mysqli_result::fetch_column

mysqli_fetch_column

Recupera una sola columna de la siguiente fila de un conjunto de resultados

## Descripción

Estilo orientado a objetos

```php
public mysqli_result::fetch_column([int $column]): null
```php

Estilo procedimental

```php
mysqli_fetch_column(mysqli_result $result, [int $column]): null
```

Recupera una fila de datos del conjunto de resultados y devuelve la columna indexada a 0. Cada llamada posterior a esta función devolverá el valor de la siguiente fila del conjunto de resultados, o `false` si no hay más filas.

> [!NOTE]
> Esta función define los campos NULL al valor PHP `null`.

## Parámetros

`result`  
Solo estilo procedimental: Un objeto `mysqli_result` devuelto por `mysqli_query`, `mysqli_store_result`, `mysqli_use_result` o `mysqli_stmt_get_result`.

`column`  
El número indexado a 0 de la columna que se desea recuperar de la fila. Si no se proporciona ningún valor, se devolverá la primera columna.

## Valores devueltos

Devuelve una sola columna de la siguiente fila de un conjunto de resultados o `false` si no hay más filas.

> [!WARNING]
> No hay forma de devolver otra columna de la misma fila si se utiliza esta función para recuperar datos.

## Ejemplos

Ejemplo de mysqli_result::fetch_column

Estilo orientado a objetos

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

$query = "SELECT CountryCode, Name FROM City ORDER BY ID DESC LIMIT 5";

$result = $mysqli->query($query);

/* Recupera un solo valor de la segunda columna */
while ($Name = $result->fetch_column(1)) {
    printf("%s\n", $Name);
}

   
```

Estilo procedimental

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = mysqli_connect("localhost", "my_user", "my_password", "world");

$query = "SELECT CountryCode, Name FROM City ORDER BY ID DESC LIMIT 5";

$result = mysqli_query($mysqli, $query);

/* Recupera un solo valor de la segunda columna */
while ($Name = mysqli_fetch_column($result, 1)) {
    printf("%s\n", $Name);
}

   
```

Los ejemplos anteriores mostrarán algo similar a:

    Rafah
    Nablus
    Jabaliya
    Hebron
    Khan Yunis

## Véase también

`mysqli_fetch_all`, `mysqli_fetch_array`, `mysqli_fetch_assoc`, `mysqli_fetch_object`, `mysqli_fetch_row`, `mysqli_data_seek`
