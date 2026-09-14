---
title: db2_num_rows
description: Devuelve el número de filas afectadas por una consulta SQL
source_url: https://www.php.net/manual/es/function.db2-num-rows.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-num-rows.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 30960
---

db2_num_rows

Devuelve el número de filas afectadas por una consulta SQL

## Descripción

```php
db2_num_rows(resource $stmt): int
```php

Devuelve el número de filas eliminadas, añadidas o actualizadas por una consulta SQL.

Para determinar el número de filas que devolverá una consulta SELECT, utilice la consulta SELECT COUNT(\*) con los mismos atributos cuando se haya ejecutado la consulta SELECT y la recuperación de los valores.

Si la lógica de la aplicación verifica el número de filas devueltas por una consulta SELECT y salta si el número de filas es 0, modifique la aplicación para intentar devolver la primera fila con `db2_fetch_assoc`, `db2_fetch_both`, `db2_fetch_array` o `db2_fetch_row`, y salte si la función devuelve `false`.

> [!NOTE]
> Si se envía una consulta SELECT con un cursor flotante, `db2_num_rows` devolverá el número de filas devueltas por la consulta SELECT. Sin embargo, el tiempo de sistema asociado con los cursores flotantes degrada considerablemente el rendimiento de la aplicación, por lo que si esta es la única razón para utilizar cursores flotantes, se deberían utilizar cursores de avance solo y además llamar a SELECT COUNT(\*) o confiar en los valores de retorno de las funciones de tipo `bool` para obtener la misma funcionalidad con un rendimiento mucho mejor.

## Parámetros

`stmt`  
Un recurso `stmt` válido que contiene el conjunto de resultados.

## Valores devueltos

Devuelve el número de filas afectadas por la última consulta SQL enviada por una función que ejecuta consultas SQL, o `false` si ocurre un error
