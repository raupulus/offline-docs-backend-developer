---
title: pg_client_encoding
description: Lee la codificación del cliente
source_url: https://www.php.net/manual/es/function.pg-client-encoding.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-client-encoding.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: 5f1a92089
order: 62880
---

pg_client_encoding

Lee la codificación del cliente

## Descripción

```php
pg_client_encoding([PgSql\Connection $connection]): string
```php

PostgreSQL soporta la conversión automática entre el servidor y el cliente para ciertos juegos de caracteres. `pg_client_encoding` devuelve la codificación del cliente. La cadena devuelta será una de las codificaciones estándar de PostgreSQL.

> [!NOTE]
> Si la biblioteca libpq es compilada sin el soporte de codificaciones multibyte, `pg_client_encoding` devolverá siempre `SQL_ASCII`. El soporte de codificaciones depende de la versión de PostgreSQL. Consúltese la documentación de PostgreSQL sobre las codificaciones soportadas.
>
> Anteriormente, esta función se llamaba `pg_clientencoding`.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`. Cuando `connection` es `null`, se usa la conexión predeterminada. La conexión predeterminada es la última conexión hecha por `pg_connect` o `pg_pconnect`

> [!WARNING]
> Desde PHP 8.1.0, usar la conexión predeterminada está obsoleto.

## Valores devueltos

La codificación del cliente.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |
| 8.0.0 | `connection` ahora es nullable. |

## Ejemplos

Ejemplo con `pg_client_encoding`

```
<?php
// Se asume que $conn es una conexión a una base de datos ISO-8859-1
$encoding = pg_client_encoding($conn);

echo "La codificación del cliente es: ", $encoding, "\n";
?>

    
```php

El ejemplo anterior mostrará:

    La codificación del cliente es: ISO-8859-1

## Véase también

`pg_set_client_encoding`
