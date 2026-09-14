---
title: mysqli::execute_query
description: Prepara, vincula los parámetros y ejecuta una sentencia SQL
source_url: https://www.php.net/manual/es/mysqli.execute-query.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/execute-query.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 035c126c0
order: 55040
---

mysqli::execute_query

mysqli_execute_query

Prepara, vincula los parámetros y ejecuta una sentencia SQL

## Descripción

Estilo orientado a objetos

```php
public mysqli::execute_query(string $query, [array $params]): mysqli_result
```php

Estilo procedimental

```php
mysqli_execute_query(mysqli $mysql, string $query, [array $params]): mysqli_result
```

Prepara la consulta SQL, vincula los parámetros y la ejecuta. El método mysqli::execute_query es un atajo para mysqli::prepare, mysqli_stmt::bind_param, mysqli_stmt::execute, y mysqli_stmt::get_result.

El modelo de sentencia puede contener cero o más marcadores de parámetros (`?`) también llamados espacios reservados. Los valores de los parámetros deben ser proporcionados como un array utilizando el parámetro `params`.

Una sentencia preparada es creada internamente, pero nunca es expuesta fuera de la función. Es imposible acceder a las propiedades de la sentencia como se haría con el objeto `mysqli_stmt`. Debido a esta limitación, la información de estado es copiada al objeto `mysqli` y está disponible utilizando sus métodos, por ejemplo `mysqli_affected_rows` o `mysqli_error`.

> [!NOTE]
> En el caso en que una sentencia es pasada a `mysqli_execute_query` que es más larga que `max_allowed_packet` del servidor, los códigos de error devueltos son diferentes dependiendo del sistema operativo. El comportamiento es el siguiente:
>
> - En Linux devuelve un código de error 1153. El mensaje de error significa “recepción de un paquete más grande que `max_allowed_packet` bytes” (“got a packet bigger than `max_allowed_packet` bytes”).
>
> - En Windows devuelve un código de error 2006. Este mensaje de error significa “el servidor ha desaparecido” (“server has gone away”).

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

`query`  
La consulta, en forma de string. Debe consistir en una sola sentencia SQL.

La sentencia SQL puede contener cero o más marcadores de parámetros representados por un signo de interrogación (`?`) en las posiciones apropiadas.

> [!NOTE]
> Los marcadores de parámetros solo están permitidos en ciertos lugares de las sentencias SQL. Por ejemplo, están permitidos en la lista `VALUES()` de una sentencia `INSERT` (para especificar los valores de columnas para una fila), o en una comparación con una columna en una cláusula `WHERE` para especificar un valor de comparación. Sin embargo, no están permitidos para los identificadores (como nombres de tabla o columna).

`params`  
Una lista opcional con tantos elementos como parámetros vinculados en la sentencia SQL que se está ejecutando. Cada valor es tratado como un `string`.

## Valores devueltos

Devuelve `false` en caso de fallo. Para consultas exitosas que producen un conjunto de resultados, como `SELECT, SHOW, DESCRIBE` o `EXPLAIN`, devuelve un objeto `mysqli_result`. Para otras consultas exitosas, devuelve `true`.

## Ejemplos

Ejemplo de mysqli::execute_query

Estilo orientado a objetos

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli('localhost', 'my_user', 'my_password', 'world');

$query = 'SELECT Name, District FROM City WHERE CountryCode=? ORDER BY Name LIMIT 5';
$result = $mysqli->execute_query($query, ['DEU']);
foreach ($result as $row) {
    printf("%s (%s)\n", $row["Name"], $row["District"]);
}

   
```

Estilo procedimental

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

$query = 'SELECT Name, District FROM City WHERE CountryCode=? ORDER BY Name LIMIT 5';
$result = mysqli_execute_query($link, $query, ['DEU']);
foreach ($result as $row) {
    printf("%s (%s)\n", $row["Name"], $row["District"]);
}

   
```

Los ejemplos anteriores mostrarán algo similar a:

    Aachen (Nordrhein-Westfalen)
    Augsburg (Baijeri)
    Bergisch Gladbach (Nordrhein-Westfalen)
    Berlin (Berliini)
    Bielefeld (Nordrhein-Westfalen)

## Véase también

`mysqli_prepare`, `mysqli_stmt_execute`, `mysqli_stmt_bind_param`, `mysqli_stmt_get_result`
