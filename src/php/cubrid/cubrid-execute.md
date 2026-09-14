---
title: cubrid_execute
description: Ejecutar una sentencia SQL preparada
source_url: https://www.php.net/manual/es/function.cubrid-execute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-execute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_revision: ee1ce6a0e
order: 9020
---

cubrid_execute

Ejecutar una sentencia SQL preparada

## Descripción

```php
cubrid_execute(resource $conn_identifier, string $sql, [int $option]): resource
```php

```php
cubrid_execute(resource $request_identifier, [int $option]): bool
```

La función `cubrid_execute` se usa para ejecutar la sentencia SQL dada. Ejecuta la consulta usando `conn_identifier` y SQL, y luego devuelve el gestor de solicitud creado. Se usa para la simple ejecución de la consulta, donde el parámetro de enlace no es necesario. Además, la función `cubrid_execute` se usa para ejecutar la sentencia preparada por medio de `cubrid_prepare` y `cubrid_bind`. En este momento se necesitan especificar los argumentos `request_identifier` y `option`.

El argumento `option` se usa para determinar si recibir el OID después de la ejecución de la consulta y si ejecutar la consulta en modo síncrono o asíncrono. Se pueden especificar `CUBRID_INCLUDE_OID` y `CUBRID_ASYNC` (o `CUBRID_EXEC_QUERY_ALL` si se desea ejecutar múltiples sentencias SQL) usando un operador OR a nivel de bit. Si no se especifica, ninguna de ellas será seleccionada. Si la bandera `CUBRID_EXEC_QUERY_ALL` está activa, el modo síncrono (sync_mode) se usa para devolver los resultados de la consulta, y en esos casos las siguientes reglas serán aplicadas:

El valor devuelto es el resultado de la primera petición.

Si sucede un error en la consulta, la ejecución se procesa como un fallo.

En una consulta compuesta por c1, c2, c3, si sucede un error en c2 después del éxito de la ejecución de c1, el resultado de c1 permanece válido. Esto es, los éxitos previos en las ejecucuiones de consultas no se repiten cuando sucede un error.

Si una consulta se ejecuta de forma satisfactoria, el resultado de la segunda consulta puede obtenerse usando la función

cubrid_next_result

.

Si el primer argumento es `request_identifier` para ejecutar la función `cubrid_prepare`, se puede especificar una opción, solamente `CUBRID_ASYNC`.

## Parámetros

`conn_identifier`  
Identificador de conexión.

`sql`  
SQL a ser ejecutado.

`option`  
La opción de ejecución de la consulta CUBRID_INCLUDE_OID, CUBRID_ASYNC, CUBRID_EXEC_QUERY_ALL.

`request_identifier`  
Identificador de `cubrid_prepare`.

## Valores devueltos

Gestor de solicitud, cuando el proceso tiene éxito y el primer parámetro es conn_identifier; `true`, cuando el proceso tiene éxito y el primer argumento es request_identifier, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                                      |
|---------|--------------------------------------------------|
| 8.4.0   | Añade `CUBRID_EXEC_QUERY_ALL` como opción nueva. |

## Ejemplos

Ejemplo de `cubrid_execute`

```php
<?php
$conn = cubrid_connect("localhost", 33000, "demodb");

$result = cubrid_execute($conn, "SELECT code FROM event WHERE name='100m Butterfly' and gender='M'", CUBRID_ASYNC);
$row = cubrid_fetch_array($result, CUBRID_ASSOC);
$event_code = $row["code"];

cubrid_close_request($result);

$history_req = cubrid_prepare($conn, "SELECT * FROM history WHERE event_code=?");
cubrid_bind($history_req, 1, $event_code, "number");
cubrid_execute($history_req);

printf("%-20s %-9s %-10s %-5s\n", "athlete", "host_year", "score", "unit");
while ($row = cubrid_fetch_array($history_req, CUBRID_ASSOC)) {
    printf("%-20s %-9s %-10s %-5s\n",
        $row["athlete"], $row["host_year"], $row["score"], $row["unit"]);
}

cubrid_close_request($history_req);

cubrid_disconnect($conn);
?>

   
```

El ejemplo anterior mostrará:

    athlete              host_year score      unit
    Phelps Michael       2004      51.25      time

## Véase también

cubrid_prepare

cubrid_bind

cubrid_next_result

cubrid_close_request

cubrid_commit

cubrid_rollback
