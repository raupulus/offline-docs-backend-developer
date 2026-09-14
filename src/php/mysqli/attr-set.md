---
title: mysqli_stmt::attr_set
description: Modifica el comportamiento de una consulta preparada
source_url: https://www.php.net/manual/es/mysqli-stmt.attr-set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_stmt/attr-set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 4683a073b
order: 55740
---

mysqli_stmt::attr_set

mysqli_stmt_attr_set

Modifica el comportamiento de una consulta preparada

## Descripción

Estilo orientado a objetos

```php
public mysqli_stmt::attr_set(int $attribute, int $value): bool
```php

Estilo procedimental

```php
mysqli_stmt_attr_set(mysqli_stmt $statement, int $attribute, int $value): bool
```

Modifica el comportamiento de una consulta preparada. Esta función puede ser llamada varias veces para definir múltiples atributos.

## Parámetros

`statement`  
Solo estilo procedimental: Un objeto `mysqli_stmt` devuelto por `mysqli_stmt_init`.

`attribute`  
El atributo que se desea definir. Puede tener uno de los siguientes valores:

| Caracteres | Descripción |
|----|----|
| MYSQLI_STMT_ATTR_UPDATE_MAX_LENGTH | Si se define como `true`, la función `mysqli_stmt_store_result` actualizará el valor de los metadatos `MYSQL_FIELD->max_length`. |
| MYSQLI_STMT_ATTR_CURSOR_TYPE | Tipo de cursor que permite abrir la consulta cuando se llama a la función `mysqli_stmt_execute`. `value` puede ser `MYSQLI_CURSOR_TYPE_NO_CURSOR` (por omisión) o `MYSQLI_CURSOR_TYPE_READ_ONLY`. |
| MYSQLI_STMT_ATTR_PREFETCH_ROWS | Número de filas a recuperar desde el servidor de una sola vez al utilizar un cursor. `value` puede estar comprendido entre 1 y el valor máximo de un tipo long sin signo. Por omisión, vale 1. Eliminado a partir de PHP 8.4.0. |

Valores de los atributos {#mysqli-stmt.attr-set.parameters}

Si se utiliza la opción `MYSQLI_STMT_ATTR_CURSOR_TYPE` con `MYSQLI_CURSOR_TYPE_READ_ONLY`, se abrirá un cursor para la consulta al llamar a la función `mysqli_stmt_execute`. Si ya existe un cursor abierto desde una llamada previa a la función `mysqli_stmt_execute`, se cerrará antes de abrir uno nuevo. La función `mysqli_stmt_reset` cierra asimismo todos los cursores antes de preparar la consulta para una nueva ejecución. La función `mysqli_stmt_free_result` cierra cualquier cursor abierto.

Si se abre un cursor para una consulta preparada, la función `mysqli_stmt_store_result` no es necesaria.

`value`  
El valor a asignar al atributo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Si el informe de errores de mysqli está habilitado (`MYSQLI_REPORT_ERROR`) y la operación solicitada falla, se genera una advertencia. Si, además, el modo está configurado como `MYSQLI_REPORT_STRICT`, se lanza una `mysqli_sql_exception` en su lugar.

## Véase también

[Conector / MySQL mysql_stmt_attr_set()](http://dev.mysql.com/doc/en/mysql-stmt-attr-set.html)
