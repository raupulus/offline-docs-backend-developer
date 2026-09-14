---
title: mysqli_result::fetch_assoc
description: Recupera la siguiente fila de un conjunto de resultados como un array
  asociativo
source_url: https://www.php.net/manual/es/mysqli-result.fetch-assoc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_result/fetch-assoc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 035c126c0
order: 55560
---

mysqli_result::fetch_assoc

mysqli_fetch_assoc

Recupera la siguiente fila de un conjunto de resultados como un array asociativo

## Descripción

Estilo orientado a objetos

```php
public mysqli_result::fetch_assoc(): array
```php

Estilo procedimental

```php
mysqli_fetch_assoc(mysqli_result $result): array
```

Devuelve una fila de datos del conjunto de resultados y la retorna como un array asociativo. Cada llamada posterior a esta función retornará la siguiente fila en el conjunto de resultados, o `null` si no hay más filas.

Si dos o más columnas del resultado tienen el mismo nombre, la última columna tendrá prioridad y sobrescribirá todos los datos anteriores. Para acceder a múltiples columnas con el mismo nombre, puede utilizarse `mysqli_fetch_row` para recuperar el array indexado numéricamente o pueden utilizarse alias en la lista de selección de la consulta SQL para dar nombres diferentes a las columnas.

> [!NOTE]
> Los nombres de los campos devueltos por esta función son *sensibles a la case*.

> [!NOTE]
> Esta función define los campos NULL al valor PHP `null`.

## Parámetros

`result`  
Solo estilo procedimental: Un objeto `mysqli_result` devuelto por `mysqli_query`, `mysqli_store_result`, `mysqli_use_result` o `mysqli_stmt_get_result`.

## Valores devueltos

Devuelve un array asociativo que representa la fila recuperada, donde cada clave del array representa el nombre de una de las columnas del conjunto de resultados, `null` si no hay más filas en el conjunto de resultados, o `false` si ocurre un error.

## Ejemplos

Ejemplo mysqli_result::fetch_assoc

Estilo orientado a objetos

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

$query = "SELECT Name, CountryCode FROM City ORDER BY ID DESC";

$result = $mysqli->query($query);

/* fetch associative array */
while ($row = $result->fetch_assoc()) {
    printf("%s (%s)\n", $row["Name"], $row["CountryCode"]);
}

   
```

Estilo procedimental

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = mysqli_connect("localhost", "my_user", "my_password", "world");

$query = "SELECT Name, CountryCode FROM City ORDER BY ID DESC";

$result = mysqli_query($mysqli, $query);

/* fetch associative array */
while ($row = mysqli_fetch_assoc($result)) {
    printf("%s (%s)\n", $row["Name"], $row["CountryCode"]);
}

   
```

Los ejemplos anteriores mostrarán algo similar a:

    Pueblo (USA)
    Arvada (USA)
    Cape Coral (USA)
    Green Bay (USA)
    Santa Clara (USA)

Comparación del uso de `mysqli_result` `iterator` y mysqli_result::fetch_assoc

`mysqli_result` puede ser iterado utilizando un [`foreach`](#control-structures.foreach). El conjunto de resultados siempre será iterado desde la primera fila, independientemente de la posición actual.

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

$query = 'SELECT Name, CountryCode FROM City ORDER BY ID DESC';

// Utiliza un iterador
$result = $mysqli->query($query);
foreach ($result as $row) {
    printf("%s (%s)\n", $row["Name"], $row["CountryCode"]);
}

echo "\n==================\n";

// No utiliza iterador
$result = $mysqli->query($query);
while ($row = $result->fetch_assoc()) {
    printf("%s (%s)\n", $row["Name"], $row["CountryCode"]);
}

   
```

Resultado del ejemplo anterior es similar a:

    Pueblo (USA)
    Arvada (USA)
    Cape Coral (USA)
    Green Bay (USA)
    Santa Clara (USA)

    ==================
    Pueblo (USA)
    Arvada (USA)
    Cape Coral (USA)
    Green Bay (USA)
    Santa Clara (USA)

## Véase también

`mysqli_fetch_array`, `mysqli_fetch_column`, `mysqli_fetch_row`, `mysqli_fetch_object`, `mysqli_query`, `mysqli_data_seek`
