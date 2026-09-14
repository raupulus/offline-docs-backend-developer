---
title: mysqli_stmt::get_result
description: Obtiene un conjunto de resultados desde una consulta preparada como un
  objeto mysqli_result
source_url: https://www.php.net/manual/es/mysqli-stmt.get-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_stmt/get-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 63b99082e
order: 55870
---

mysqli_stmt::get_result

mysqli_stmt_get_result

Obtiene un conjunto de resultados desde una consulta preparada como un objeto

mysqli_result

## Descripción

Estilo orientado a objetos

```php
public mysqli_stmt::get_result(): mysqli_result
```php

Estilo procedimental

```php
mysqli_stmt_get_result(mysqli_stmt $statement): mysqli_result
```

Obtiene un conjunto de resultados de una declaración preparada en forma de un objeto `mysqli_result`. Los datos serán recuperados desde el servidor MySQL hacia PHP. Este método solo debe ser llamado para las consultas que producen un conjunto de resultados.

> [!NOTE]
> Disponible solo con [mysqlnd](#book.mysqlnd).

> [!NOTE]
> Esta función no puede ser utilizada conjuntamente con la `mysqli_stmt_store_result`. Estas dos funciones recuperan el conjunto de resultados completo del servidor MySQL.

## Parámetros

`statement`  
Solo estilo procedimental: Un objeto `mysqli_stmt` devuelto por `mysqli_stmt_init`.

## Valores devueltos

Retorna un conjunto de resultados para consultas SELECT exitosas, o `false` para otras consultas DML o en caso de fallo. La función `mysqli_errno` puede ser utilizada para distinguir entre estos dos tipos de errores. Retorna `false` en caso de fallo. Para consultas exitosas que producen un conjunto de resultados como `SELECT, SHOW, DESCRIBE` o `EXPLAIN`, `mysqli_stmt_get_result` retornará un objeto `mysqli_result`. Para otros tipos de consultas exitosas, `mysqli_stmt_get_result` retornará `false`. La función `mysqli_stmt_errno` puede ser utilizada para distinguir entre las dos razones para `false` ; debido a un error, anterior a PHP 7.4.13, `mysqli_errno` debía ser utilizada para determinar esto.

## Errores/Excepciones

Si el informe de errores de mysqli está habilitado (`MYSQLI_REPORT_ERROR`) y la operación solicitada falla, se genera una advertencia. Si, además, el modo está configurado como `MYSQLI_REPORT_STRICT`, se lanza una `mysqli_sql_exception` en su lugar.

## Ejemplos

Estilo orientado a objetos

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

$query = "SELECT Name, Population, Continent FROM Country WHERE Continent=? ORDER BY Name LIMIT 1";

$stmt = $mysqli->prepare($query);
$stmt->bind_param("s", $continent);

$continentList = array('Europe', 'Africa', 'Asia', 'North America');

foreach ($continentList as $continent) {
    $stmt->execute();
    $result = $stmt->get_result();
    while ($row = $result->fetch_array(MYSQLI_NUM)) {
        foreach ($row as $r) {
            print "$r ";
        }
        print "\n";
    }
}
?>

   
```

Estilo procedimental

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

$query = "SELECT Name, Population, Continent FROM Country WHERE Continent=? ORDER BY Name LIMIT 1";

$stmt = mysqli_prepare($link, $query);
mysqli_stmt_bind_param($stmt, "s", $continent);

$continentList= array('Europe', 'Africa', 'Asia', 'North America');

foreach ($continentList as $continent) {
    mysqli_stmt_execute($stmt);
    $result = mysqli_stmt_get_result($stmt);
    while ($row = mysqli_fetch_array($result, MYSQLI_NUM)) {
        foreach ($row as $r) {
            print "$r ";
        }
        print "\n";
    }
}
?>

   
```

Los ejemplos anteriores mostrarán algo similar a:

    Albania 3401200 Europe
    Algeria 31471000 Africa
    Afghanistan 22720000 Asia
    Anguilla 8000 North America

## Véase también

`mysqli_prepare`, `mysqli_stmt_result_metadata`, `mysqli_stmt_fetch`, `mysqli_fetch_array`, `mysqli_stmt_store_result`
