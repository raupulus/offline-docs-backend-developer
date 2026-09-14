---
title: mysqli::store_result
description: Transfiere un conjunto de resultados desde la última consulta
source_url: https://www.php.net/manual/es/mysqli.store-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/store-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 699e596aa
order: 55410
---

mysqli::store_result

mysqli_store_result

Transfiere un conjunto de resultados desde la última consulta

## Descripción

Estilo orientado a objetos

```php
public mysqli::store_result([int $mode]): mysqli_result
```php

Estilo procedimental

```php
mysqli_store_result(mysqli $mysql, [int $mode]): mysqli_result
```

Transfiere el conjunto de resultados desde la última consulta en la conexión a la base de datos especificada por el argumento `mysql` para su uso con `mysqli_data_seek`.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

`mode`  
La opción que se desea definir. A partir de PHP 8.1, este argumento no tiene ningún efecto. Puede tomar uno de los siguientes valores:

| Nombre | Descripción |
|----|----|
| `MYSQLI_STORE_RESULT_COPY_DATA` | Copia los resultados recuperados de un buffer interno mysqlnd a variables PHP. Por omisión, mysqlnd utilizará una referencia lógica para evitar la copia y la duplicación de los resultados contenidos en memoria. Para ciertos conjuntos de resultados, por ejemplo, los conjuntos de resultados con muchas filas pequeñas, el enfoque de copia puede reducir el uso de memoria por las variables PHP que contienen los resultados pueden ser liberadas rápidamente (disponible únicamente con mysqlnd) |

Opciones válidas {#mysqli.store-result.parameters}

## Valores devueltos

Retorna un resultado almacenado en forma de objeto o `false` si ocurre un error.

> [!NOTE]
> `mysqli_store_result` retorna `false` en caso de que la consulta no retorne un conjunto de resultados (si la consulta es de tipo INSERT por ejemplo). Esta función retornará siempre `false` si el conjunto de resultados no puede ser leído. Se puede saber si hay un error utilizando la función `mysqli_error` y mirando si retorna un string vacío, o si `mysqli_errno` retorna cero, o bien si `mysqli_field_count` retorna un valor diferente de cero. Otra razón para que esta función retorne `false` es que el conjunto de resultados retornado después de una consulta exitosa llamada por `mysqli_query` es demasiado largo (la memoria para este no puede ser asignada). Si `mysqli_field_count` retorna un valor diferente de cero, el procesamiento debería producir un conjunto de resultados no vacío.

## Errores/Excepciones

Si el informe de errores de mysqli está habilitado (`MYSQLI_REPORT_ERROR`) y la operación solicitada falla, se genera una advertencia. Si, además, el modo está configurado como `MYSQLI_REPORT_STRICT`, se lanza una `mysqli_sql_exception` en su lugar.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | El paso del argumento `mode` está ahora obsoleto. Este argumento no ha tenido ningún efecto desde PHP 8.1.0. |

## Ejemplos

Ver la función `mysqli_multi_query`.

## Notas

> [!NOTE]
> Siempre se recomienda liberar la memoria asignada para el resultado utilizando la función `mysqli_free_result`, al transferir grandes resultados utilizando la función `mysqli_store_result` esto se vuelve particularmente importante.

## Véase también

`mysqli_real_query`, `mysqli_use_result`
