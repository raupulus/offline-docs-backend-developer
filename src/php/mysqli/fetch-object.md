---
title: mysqli_result::fetch_object
description: Devuelve la siguiente fila de un conjunto de resultados como objeto
source_url: https://www.php.net/manual/es/mysqli-result.fetch-object.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_result/fetch-object.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: c5ccd084c
order: 55610
---

mysqli_result::fetch_object

mysqli_fetch_object

Devuelve la siguiente fila de un conjunto de resultados como objeto

## Descripción

Estilo orientado a objetos

```php
public mysqli_result::fetch_object([string $class], [array $constructor_args]): object
```php

Estilo procedimental

```php
mysqli_fetch_object(mysqli_result $result, [string $class], [array $constructor_args]): object
```

Devuelve una fila de datos en el conjunto de resultados y la retorna como objeto, donde cada propiedad representa el nombre de la columna del conjunto de resultados. Cada llamada posterior a esta función retornará la siguiente fila en el conjunto de resultados, o `null` si no hay más filas.

Si dos o más columnas del resultado tienen el mismo nombre, la última columna tendrá prioridad y sobrescribirá todos los datos anteriores. Para acceder a múltiples columnas con el mismo nombre, la `mysqli_fetch_row` puede ser utilizada para recuperar el array indexado numéricamente o se pueden usar alias en la lista de selección de la consulta SQL para dar nombres diferentes a las columnas.

> [!NOTE]
> Esta función afecta las propiedades del objeto antes de llamar a su constructor.

> [!NOTE]
> Los nombres de los campos devueltos por esta función son *sensibles a la case*.

> [!NOTE]
> Esta función define los campos NULL al valor PHP `null`.

## Parámetros

`result`  
Solo estilo procedimental: Un objeto `mysqli_result` devuelto por `mysqli_query`, `mysqli_store_result`, `mysqli_use_result` o `mysqli_stmt_get_result`.

`class`  
El nombre de la clase a instanciar. Si no se proporciona, se retornará un objeto `stdClass`.

`constructor_args`  
Un array de argumentos (opcional) a pasar al constructor de la clase `class`.

## Valores devueltos

Retorna un objeto que representa la fila recuperada, donde cada propiedad representa el nombre de la columna del conjunto de resultados, `null` si no hay más filas en el conjunto de resultados, o `false` si ocurre un error.

## Errores/Excepciones

Se lanza una `ValueError` cuando `constructor_args` no está vacío y la clase no tiene constructor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Ahora se lanza una excepción `ValueError` cuando `constructor_args` no está vacío y la clase no tiene constructor; anteriormente, se lanzaba una excepción `Exception`. |
| 8.0.0 | `constructor_args` ahora acepta `[]` para constructores con 0 parámetros; antes se lanzaba una excepción. |

## Ejemplos

Ejemplo mysqli_result::fetch_object

Estilo orientado a objetos

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

$query = "SELECT Name, CountryCode FROM City ORDER BY ID DESC";

$result = $mysqli->query($query);

while ($obj = $result->fetch_object()) {
    printf("%s (%s)\n", $obj->Name, $obj->CountryCode);
}

   
```

Estilo procedimental

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

$query = "SELECT Name, CountryCode FROM City ORDER BY ID DESC";

$result = mysqli_query($link, $query);

while ($obj = mysqli_fetch_object($result)) {
    printf("%s (%s)\n", $obj->Name, $obj->CountryCode);
}

   
```

Los ejemplos anteriores mostrarán algo similar a:

    Pueblo (USA)
    Arvada (USA)
    Cape Coral (USA)
    Green Bay (USA)
    Santa Clara (USA)

## Véase también

`mysqli_fetch_array`, `mysqli_fetch_assoc`, `mysqli_fetch_column`, `mysqli_fetch_row`, `mysqli_query`, `mysqli_data_seek`
