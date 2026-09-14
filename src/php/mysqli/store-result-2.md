---
title: mysqli_stmt::store_result
description: Almacena un conjunto de resultados en un búfer interno
source_url: https://www.php.net/manual/es/mysqli-stmt.store-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_stmt/store-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 63b99082e
order: 55990
---

mysqli_stmt::store_result

mysqli_stmt_store_result

Almacena un conjunto de resultados en un búfer interno

## Descripción

Estilo orientado a objetos

```php
public mysqli_stmt::store_result(): bool
```php

Estilo procedimental

```php
mysqli_stmt_store_result(mysqli_stmt $statement): bool
```

Esta función debería ser llamada para consultas que produzcan un conjunto de resultados (por ejemplo, `SELECT, SHOW, DESCRIBE, EXPLAIN`) solo si el conjunto de resultados completo debe ser almacenado en búfer por PHP. Cada llamada sucesiva a `mysqli_stmt_fetch` devolverá los datos almacenados en búfer.

> [!NOTE]
> No es necesario llamar a `mysqli_stmt_store_result` para otros tipos de consultas, pero si se hace, no hay problema y no causará ninguna pérdida notable de rendimiento en ningún caso. Puede detectarse en todos los casos si la consulta va a producir un conjunto de resultados observando si la función `mysqli_stmt_result_metadata` devuelve `false`.

## Parámetros

`statement`  
Solo estilo procedimental: Un objeto `mysqli_stmt` devuelto por `mysqli_stmt_init`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Si el informe de errores de mysqli está habilitado (`MYSQLI_REPORT_ERROR`) y la operación solicitada falla, se genera una advertencia. Si, además, el modo está configurado como `MYSQLI_REPORT_STRICT`, se lanza una `mysqli_sql_exception` en su lugar.

## Ejemplos

Estilo orientado a objetos

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

$query = "SELECT Name, CountryCode FROM City ORDER BY Name LIMIT 20";
$stmt = $mysqli->prepare($query);
$stmt->execute();

/* Almacenar el resultado en un búfer interno */
$stmt->store_result();

printf("Número de filas: %d.\n", $stmt->num_rows);

   
```

Estilo procedimental

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

$query = "SELECT Name, CountryCode FROM City ORDER BY Name LIMIT 20";
$stmt = mysqli_prepare($link, $query);
mysqli_stmt_execute($stmt);

/* Almacenar el resultado en un búfer interno */
mysqli_stmt_store_result($stmt);

printf("Número de filas: %d.\n", mysqli_stmt_num_rows($stmt));

   
```

Los ejemplos anteriores mostrarán:

    Número de filas: 20.

## Véase también

`mysqli_prepare`, `mysqli_stmt_result_metadata`, `mysqli_stmt_fetch`
