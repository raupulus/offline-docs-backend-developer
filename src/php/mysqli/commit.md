---
title: mysqli::commit
description: Valida la transacción actual
source_url: https://www.php.net/manual/es/mysqli.commit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/commit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 976425d4f
order: 54950
---

mysqli::commit

mysqli_commit

Valida la transacción actual

## Descripción

Estilo orientado a objetos

```php
public mysqli::commit([int $flags], [string $name]): bool
```php

Estilo procedimental

```php
mysqli_commit(mysqli $mysql, [int $flags], [string $name]): bool
```

Valida la transacción actual para la base de datos especificada por el argumento `link`.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

`flags`  
Una máscara de constantes `MYSQLI_TRANS_COR_*`.

`name`  
Si se proporciona, entonces `COMMIT/*name*/` es ejecutado.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Si el informe de errores de mysqli está habilitado (`MYSQLI_REPORT_ERROR`) y la operación solicitada falla, se genera una advertencia. Si, además, el modo está configurado como `MYSQLI_REPORT_STRICT`, se lanza una `mysqli_sql_exception` en su lugar.

## Historial de cambios

| Versión | Descripción               |
|---------|---------------------------|
| 8.0.0   | `name` es ahora nullable. |

## Ejemplos

Ver el ejemplo que se encuentra en la documentación del método [mysqli::begin_transaction](#mysqli.begin-transaction.example.basic).

## Notas

> [!NOTE]
> Esta función no funciona con los tipos de tabla no transaccionales (como MyISAM o ISAM).

## Véase también

`mysqli_autocommit`, `mysqli_begin_transaction`, `mysqli_rollback`, `mysqli_savepoint`
