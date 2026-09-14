---
title: pg_fetch_object
description: Lee una fila de resultado PostgreSQL en un objeto
source_url: https://www.php.net/manual/es/function.pg-fetch-object.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-fetch-object.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: 39bb8a868
order: 63110
---

pg_fetch_object

Lee una fila de resultado PostgreSQL en un objeto

## Descripción

```php
pg_fetch_object(PgSql\Result $result, [int $row], [string $class], [array $constructor_args]): object
```php

`pg_fetch_object` devuelve un objeto con sus propiedades que corresponden a los nombres de los campos de la fila. La función puede instanciar opcionalmente un objeto de una clase específica y pasar los argumentos al constructor de dicha clase.

> [!NOTE]
> Esta función define los campos NULL al valor PHP `null`.

En cuanto a velocidad, la función es idéntica a `pg_fetch_array` y es casi tan rápida como `pg_fetch_row` (la diferencia es insignificante).

## Parámetros

`result`  
Una instancia `PgSql\Result`, devuelta por `pg_query`, `pg_query_params`, o `pg_execute` (entre otros).

`row`  
Número de la fila a recuperar. Las filas se numeran comenzando por 0. Si el argumento se omite o es `null`, se recupera la siguiente fila.

`class`  
El nombre de la clase a instanciar, fija las propiedades de esta y sus valores de retorno. Si no se especifica nada, se devuelve un objeto de tipo `stdClass`.

`constructor_args`  
Parámetro opcional de tipo `array` para pasar argumentos al constructor de la clase `class`.

## Valores devueltos

Un objeto de tipo `object` con los atributos para cada campo en el conjunto de resultados. Los valores `null` de la base de datos se devuelven como `null`.

`false` se devuelve si `row` excede el número de filas en el conjunto de resultados, no hay más filas disponibles o cualquier otro error.

## Errores/Excepciones

Se lanza una `ValueError` cuando el argumento `constructor_args` no está vacío y la clase no tiene constructor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Ahora lanza una excepción `ValueError` cuando el argumento `constructor_args` no está vacío y la clase no tiene constructor; anteriormente, se lanzaba una excepción `Exception`. |
| 8.1.0 | El parámetro `result` ahora espera una instancia de `PgSql\Result` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_fetch_object`

```
<?php

$database = 'store';

$db_conn = pg_connect("host=localhost port=5432 dbname=$database");
if (!$db_conn) {
  echo "La conexión a la base $database ha fallado\n";
  exit;
}

$qu = pg_query($db_conn, "SELECT * FROM libros ORDER BY autor");

while ($data = pg_fetch_object($qu)) {
  echo $data->autor . " (";
  echo $data->anio . "): ";
  echo $data->titulo . "<br />";
}

pg_free_result($qu);
pg_close($db_conn);

?>

    
```php

## Véase también

`pg_query`, `pg_fetch_array`, `pg_fetch_assoc`, `pg_fetch_row`, `pg_fetch_result`
