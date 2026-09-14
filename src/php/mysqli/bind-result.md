---
title: mysqli_stmt::bind_result
description: Vincula variables a un conjunto de resultados
source_url: https://www.php.net/manual/es/mysqli-stmt.bind-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_stmt/bind-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 2e61d37d1
order: 55760
---

mysqli_stmt::bind_result

mysqli_stmt_bind_result

Vincula variables a un conjunto de resultados

## Descripción

Estilo orientado a objetos

```php
public mysqli_stmt::bind_result(mixed $var, mixed ...$vars): bool
```php

Estilo procedimental

```php
mysqli_stmt_bind_result(mysqli_stmt $statement, mixed $var, mixed ...$vars): bool
```

Asocia columnas de un resultado a variables.

Cuando se llama a `mysqli_stmt_fetch` para leer valores, el protocolo MySQL coloca los datos en las variables especificadas `var`/`vars`.

Una columna puede ser vinculada en cualquier momento, incluso después de que un conjunto de resultados haya sido parcialmente recuperado. La nueva vinculación entra en vigor la próxima vez que se llame a `mysqli_stmt_fetch`.

> [!NOTE]
> Todas las columnas deben ser vinculadas después de la ejecución de la función `mysqli_stmt_execute` y antes de la llamada a la función `mysqli_stmt_fetch`. Dependiendo del tipo de valor de la columna, el tipo de variable PHP puede ser modificado automáticamente.

> [!NOTE]
> Una columna puede ser asociada o reasociada en cualquier momento, incluso después de una lectura parcial del resultado. La nueva asociación entra en vigor en la próxima llamada a `mysqli_stmt_fetch`.

> [!TIP]
> Esta función es útil para resultados básicos. Para recuperar un conjunto de resultados iterable, o recuperar cada fila como array u objeto, utilice `mysqli_stmt_get_result`.

## Parámetros

`statement`  
Solo estilo procedimental: Un objeto `mysqli_stmt` devuelto por `mysqli_stmt_init`.

`var`  
La primera variable a vincular.

`vars`  
Variables adicionales a vincular.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Estilo orientado a objetos

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

/* Preparación de la consulta */
$stmt = $mysqli->prepare("SELECT Code, Name FROM Country ORDER BY Name LIMIT 5");
$stmt->execute();

/* Vincular variables a una declaración preparada */
$stmt->bind_result($col1, $col2);

/* Recuperación de los valores */
while ($stmt->fetch()) {
    printf("%s %s\n", $col1, $col2);
}
?>

   
```

Estilo procedimental

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

/* Preparación de la consulta */
$stmt = mysqli_prepare($link, "SELECT Code, Name FROM Country ORDER BY Name LIMIT 5");
mysqli_stmt_execute($stmt);

/* Vincular variables a una declaración preparada */
mysqli_stmt_bind_result($stmt, $col1, $col2);

/* Recuperación de los valores */
while (mysqli_stmt_fetch($stmt)) {
    printf("%s %s\n", $col1, $col2);
}
?>

   
```

El ejemplo anterior mostrará:

    AFG Afghanistan
    ALB Albania
    DZA Algeria
    ASM American Samoa
    AND Andorra

## Véase también

`mysqli_stmt_get_result`, `mysqli_stmt_bind_param`, `mysqli_stmt_execute`, `mysqli_stmt_fetch`, `mysqli_prepare`, `mysqli_stmt_prepare`
