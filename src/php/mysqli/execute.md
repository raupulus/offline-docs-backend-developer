---
title: mysqli_stmt::execute
description: Ejecuta una consulta preparada
source_url: https://www.php.net/manual/es/mysqli-stmt.execute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_stmt/execute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: ec946465e
order: 55830
---

mysqli_stmt::execute

mysqli_stmt_execute

Ejecuta una consulta preparada

## Descripción

Estilo orientado a objetos

```php
public mysqli_stmt::execute([array $params]): bool
```php

Estilo procedimental

```php
mysqli_stmt_execute(mysqli_stmt $statement, [array $params]): bool
```

Ejecuta una consulta que ha sido previamente preparada utilizando la función `mysqli_prepare`, gracias al recurso `stmt`. Durante la ejecución, todas las variables de la consulta serán reemplazadas por los datos apropiados.

Si la consulta es `UPDATE`, `DELETE`, o `INSERT`, el número total de filas afectadas está disponible a través de la función `mysqli_stmt_affected_rows`. Si la consulta produce un conjunto de resultados, puede ser recuperado utilizando la función `mysqli_stmt_get_result` o recuperándolo línea por línea directamente desde la instrucción utilizando la función `mysqli_stmt_fetch`.

## Parámetros

`statement`  
Solo estilo procedimental: Un objeto `mysqli_stmt` devuelto por `mysqli_stmt_init`.

`params`  
Una lista opcional, como `array`, con tantos elementos como parámetros enlazados haya en la instrucción SQL en curso de ejecución. Cada valor es tratado como una `string`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Si el informe de errores de mysqli está habilitado (`MYSQLI_REPORT_ERROR`) y la operación solicitada falla, se genera una advertencia. Si, además, el modo está configurado como `MYSQLI_REPORT_STRICT`, se lanza una `mysqli_sql_exception` en su lugar.

## Historial de cambios

| Versión | Descripción                                     |
|---------|-------------------------------------------------|
| 8.1.0   | El parámetro opcional `params` ha sido añadido. |

## Ejemplos

Ejecutar una instrucción preparada con variables enlazadas

Estilo orientado a objetos

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

$mysqli->query("CREATE TEMPORARY TABLE myCity LIKE City");

/* Preparación de la consulta */
$stmt = $mysqli->prepare("INSERT INTO myCity (Name, CountryCode, District) VALUES (?,?,?)");

/* Enlazar las variables a los parámetros */
$stmt->bind_param("sss", $val1, $val2, $val3);
$val1 = 'Stuttgart';
$val2 = 'DEU';
$val3 = 'Baden-Wuerttemberg';

/* Ejecutar la instrucción */
$stmt->execute();
$val1 = 'Bordeaux';
$val2 = 'FRA';
$val3 = 'Aquitaine';

/* Ejecutar la instrucción */
$stmt->execute();

/* Recuperación de todas las líneas de myCity */
$query = "SELECT Name, CountryCode, District FROM myCity";
$result = $mysqli->query($query);
while ($row = $result->fetch_row()) {
    printf("%s (%s,%s)\n", $row[0], $row[1], $row[2]);
}

   
```

Estilo procedimental

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

mysqli_query($link, "CREATE TEMPORARY TABLE myCity LIKE City");

/* Preparación de la consulta */
$stmt = mysqli_prepare($link, "INSERT INTO myCity (Name, CountryCode, District) VALUES (?,?,?)");

/* Enlazar las variables a los parámetros */
mysqli_stmt_bind_param($stmt, "sss", $val1, $val2, $val3);
$val1 = 'Stuttgart';
$val2 = 'DEU';
$val3 = 'Baden-Wuerttemberg';

/* Ejecutar la instrucción */
mysqli_stmt_execute($stmt);
$val1 = 'Bordeaux';
$val2 = 'FRA';
$val3 = 'Aquitaine';

/* Ejecutar la instrucción */
mysqli_stmt_execute($stmt);

/* Recuperación de todas las líneas de myCity */
$query = "SELECT Name, CountryCode, District FROM myCity";
$result = mysqli_query($link, $query);
while ($row = mysqli_fetch_row($result)) {
    printf("%s (%s,%s)\n", $row[0], $row[1], $row[2]);
}

   
```

Los ejemplos anteriores mostrarán:

    Stuttgart (DEU,Baden-Wuerttemberg)
    Bordeaux (FRA,Aquitaine)

Ejecutar una instrucción preparada con un array de valores

Estilo orientado a objetos

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli('localhost', 'my_user', 'my_password', 'world');

$mysqli->query('CREATE TEMPORARY TABLE myCity LIKE City');

/* Preparación de la consulta */
$stmt = $mysqli->prepare('INSERT INTO myCity (Name, CountryCode, District) VALUES (?,?,?)');

/* Ejecutar la instrucción */
$stmt->execute(['Stuttgart', 'DEU', 'Baden-Wuerttemberg']);

/* Recuperación de todas las líneas de myCity */
$query = 'SELECT Name, CountryCode, District FROM myCity';
$result = $mysqli->query($query);
while ($row = $result->fetch_row()) {
    printf("%s (%s,%s)\n", $row[0], $row[1], $row[2]);
}

   
```

Estilo procedimental

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_connect('localhost', 'my_user', 'my_password', 'world');

mysqli_query($link, 'CREATE TEMPORARY TABLE myCity LIKE City');

/* Preparación de la consulta */
$stmt = mysqli_prepare($link, 'INSERT INTO myCity (Name, CountryCode, District) VALUES (?,?,?)');

/* Ejecutar la instrucción */
mysqli_stmt_execute($stmt, ['Stuttgart', 'DEU', 'Baden-Wuerttemberg']);

/* Recuperación de todas las líneas de myCity */
$query = 'SELECT Name, CountryCode, District FROM myCity';
$result = mysqli_query($link, $query);
while ($row = mysqli_fetch_row($result)) {
    printf("%s (%s,%s)\n", $row[0], $row[1], $row[2]);
}

   
```

Los ejemplos anteriores mostrarán:

    Stuttgart (DEU,Baden-Wuerttemberg)

## Véase también

`mysqli_execute_query`, `mysqli_prepare`, `mysqli_stmt_bind_param`, `mysqli_stmt_get_result`
