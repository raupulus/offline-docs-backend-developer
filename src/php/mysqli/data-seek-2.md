---
title: mysqli_stmt::data_seek
description: Ajusta el puntero de resultado a una fila arbitraria en el resultado
  almacenado en el búfer.
source_url: https://www.php.net/manual/es/mysqli-stmt.data-seek.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_stmt/data-seek.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 51c34024e
order: 55790
---

mysqli_stmt::data_seek

mysqli_stmt_data_seek

Ajusta el puntero de resultado a una fila arbitraria en el resultado almacenado en el búfer.

## Descripción

Estilo orientado a objetos

```php
public mysqli_stmt::data_seek(int $offset): void
```php

Estilo procedimental

```php
mysqli_stmt_data_seek(mysqli_stmt $statement, int $offset): void
```

Esta función mueve el puntero del conjunto de resultados almacenado en el búfer a una fila arbitraria especificada por el parámetro `offset`.

Esta función solo funciona en el conjunto de resultados interno almacenado en el búfer. `mysqli_stmt_store_result` debe ser llamada antes de la función `mysqli_stmt_data_seek`.

## Parámetros

`statement`  
Solo estilo procedimental: Un objeto `mysqli_stmt` devuelto por `mysqli_stmt_init`.

`offset`  
Debe tomar un valor entre cero y el número total de filas menos 1 (0..`mysqli_stmt_num_rows` - 1).

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Estilo orientado a objetos

```php
<?php
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

$query = "SELECT Name, CountryCode FROM City ORDER BY Name";
$stmt = $mysqli->prepare($query);
$stmt->execute();

/* Cierra la conexión */
$mysqli->close();
?>

  
```

Estilo procedimental

```php
<?php
/* Abre la conexión */
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

/* Verifica la conexión */
if (mysqli_connect_errno()) {
    printf("Fallo en la conexión: %s\n", mysqli_connect_error());
    exit();
}

$query = "SELECT Name, CountryCode FROM City ORDER BY Name";
if ($stmt = mysqli_prepare($link, $query)) {

    /* Ejecuta la consulta */
    mysqli_stmt_execute($stmt);

    /* Vincula las variables de resultado */
    mysqli_stmt_bind_result($stmt, $name, $code);

    /* Almacena el resultado */
    mysqli_stmt_store_result($stmt);

    $stmt->bind_result($name, $code);

    $stmt->store_result();

    /* Lee la fila n°400 */
    $stmt->data_seek(399);

    /* Cierra la sentencia */
    mysqli_stmt_close($stmt);
}

printf("Ciudad: %s Código de País: %s\n", $name, $code);
?>

   
```

El ejemplo anterior mostrará:

    Ciudad: Benin City Código de País: NGA

## Véase también

`mysqli_prepare`
