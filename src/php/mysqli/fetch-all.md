---
title: mysqli_result::fetch_all
description: Recupera todas las filas de resultados en un array asociativo, numérico
  o ambos
source_url: https://www.php.net/manual/es/mysqli-result.fetch-all.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_result/fetch-all.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 035c126c0
order: 55540
---

mysqli_result::fetch_all

mysqli_fetch_all

Recupera todas las filas de resultados en un array asociativo, numérico o ambos

## Descripción

Estilo orientado a objetos

```php
public mysqli_result::fetch_all([int $mode]): array
```php

Estilo procedimental

```php
mysqli_fetch_all(mysqli_result $result, [int $mode]): array
```

Devuelve un array bidimensional de todos los resultados en forma de un array asociativo, numérico o ambos.

> [!NOTE]
> Anterior a PHP 8.1.0, disponible únicamente con [mysqlnd](#book.mysqlnd).

## Parámetros

`result`  
Solo estilo procedimental: Un objeto `mysqli_result` devuelto por `mysqli_query`, `mysqli_store_result`, `mysqli_use_result` o `mysqli_stmt_get_result`.

`mode`  
Este argumento opcional es una constante que indica el tipo de array que debe ser producido a partir del resultado. Los valores posibles son las constantes `MYSQLI_ASSOC`, `MYSQLI_NUM`, o `MYSQLI_BOTH`.

## Valores devueltos

Devuelve un array asociativo o numérico que contiene las filas de resultado.

## Historial de cambios

| Versión | Descripción                                              |
|---------|----------------------------------------------------------|
| 8.1.0   | Ahora también disponible al vincular con libmysqlclient. |

## Ejemplos

Ejemplo de mysqli_result::fetch_all

Estilo orientado a objetos

```php
<?php
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");
$result = $mysqli->query("SELECT Name, CountryCode FROM City ORDER BY ID LIMIT 3");
$rows = $result->fetch_all(MYSQLI_ASSOC);
foreach ($rows as $row) {
    printf("%s (%s)\n", $row["Name"], $row["CountryCode"]);
}

   
```

Estilo procedimental

```php
<?php
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = mysqli_connect("localhost", "my_user", "my_password", "world");
$result = mysqli_query($mysqli, "SELECT Name, CountryCode FROM City ORDER BY ID LIMIT 3");
$rows = mysqli_fetch_all($result, MYSQLI_ASSOC);
foreach ($rows as $row) {
    printf("%s (%s)\n", $row["Name"], $row["CountryCode"]);
}

   
```

Los ejemplos anteriores mostrarán:

    Kabul (AFG)
    Qandahar (AFG)
    Herat (AFG)

## Véase también

`mysqli_fetch_array`, `mysqli_fetch_column`, `mysqli_query`
