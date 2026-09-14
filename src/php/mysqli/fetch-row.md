---
title: mysqli_result::fetch_row
description: Obtiene una fila de resultado como un array indexado
source_url: https://www.php.net/manual/es/mysqli-result.fetch-row.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_result/fetch-row.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 035c126c0
order: 55620
---

mysqli_result::fetch_row

mysqli_fetch_row

Obtiene una fila de resultado como un array indexado

## Descripción

Estilo orientado a objetos

```php
public mysqli_result::fetch_row(): array
```php

Estilo procedimental

```php
mysqli_fetch_row(mysqli_result $result): array
```

Obtiene una fila de datos del conjunto de resultados representado por `result` y la devuelve como un array indexado, donde cada columna es un elemento del array, comenzando en 0 (cero). Cada nueva llamada a `mysqli_fetch_row` devolverá la siguiente fila en el conjunto de resultados, o `null` si no hay más filas.

> [!NOTE]
> Esta función define los campos NULL al valor PHP `null`.

## Parámetros

`result`  
Solo estilo procedimental: Un objeto `mysqli_result` devuelto por `mysqli_query`, `mysqli_store_result`, `mysqli_use_result` o `mysqli_stmt_get_result`.

## Valores devueltos

Devuelve un array enumerado que representa la fila obtenida, `null` si no hay más filas en el conjunto de resultados, o `false` si ocurre un error.

## Ejemplos

Ejemplo mysqli_result::fetch_row

Estilo orientado a objetos

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

$query = "SELECT Name, CountryCode FROM City ORDER BY ID DESC";

$result = $mysqli->query($query);

/* Obtiene un array de objetos */
while ($row = $result->fetch_row()) {
    printf("%s (%s)\n", $row[0], $row[1]);
}

   
```

Estilo procedimental

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = mysqli_connect("localhost", "my_user", "my_password", "world");

$query = "SELECT Name, CountryCode FROM City ORDER BY ID DESC";

$result = mysqli_query($mysqli, $query);

/* Obtiene un array asociativo */
while ($row = mysqli_fetch_row($result)) {
    printf("%s (%s)\n", $row[0], $row[1]);
}

   
```

Los ejemplos anteriores mostrarán algo similar a:

    Pueblo (USA)
    Arvada (USA)
    Cape Coral (USA)
    Green Bay (USA)
    Santa Clara (USA)

## Véase también

`mysqli_fetch_array`, `mysqli_fetch_assoc`, `mysqli_fetch_column`, `mysqli_fetch_object`, `mysqli_query`, `mysqli_data_seek`
