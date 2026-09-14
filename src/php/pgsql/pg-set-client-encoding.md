---
title: pg_set_client_encoding
description: Establece la codificación del cliente PostgreSQL
source_url: https://www.php.net/manual/es/function.pg-set-client-encoding.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-set-client-encoding.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63700
---

pg_set_client_encoding

Establece la codificación del cliente PostgreSQL

## Descripción

```php
pg_set_client_encoding([PgSql\Connection $connection], string $encoding): int
```php

`pg_set_client_encoding` establece la codificación del cliente. Devuelve 0 en caso de éxito y -1 en caso de error.

PostgreSQL convertirá automáticamente los datos de la codificación de la base de datos a la codificación del cliente.

> [!NOTE]
> Anteriormente, esta función se llamaba `pg_setclientencoding`.

## Parámetros

`connection`  
Una `PgSql\Connection` instancia. Cuando `connection` no es especificado, se usa la conexión por defecto. La conexión predeterminada es la última conexión hecha por `pg_connect` o `pg_pconnect`

> [!WARNING]
> Desde PHP 8.1.0, usar la conexión predeterminada está obsoleto.

`encoding`  
La codificación del cliente solicitada. Una de estas constantes: `SQL_ASCII`, `EUC_JP`, `EUC_CN`, `EUC_KR`, `EUC_TW`, `UNICODE`, `MULE_INTERNAL`, `LATINX` (X=1...9), `KOI8`, `WIN`, `ALT`, `SJIS`, `BIG5` o `WIN1250`.

La lista exacta de codificaciones disponibles depende de la versión de PostgreSQL, por lo que se debe consultar el manual de PostgreSQL para obtener una lista más específica.

## Valores devueltos

Devuelve `0` en caso de éxito o `-1` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_set_client_encoding`

```
<?php

$conn = pg_pconnect("dbname=editeur");
if (!$conn) {
  echo "Se ha producido un error.\n";
  exit;
}

// Establece la codificación del cliente a UNICODE. Los datos se convertirán automáticamente
// de la codificación del servidor a la codificación del cliente.
pg_set_client_encoding($conn, "UNICODE");

$result = pg_query($conn, "SELECT autor, email FROM autores");
if (!$result) {
  echo "Se ha producido un error.\n";
  exit;
}

// Escritura de datos UTF-8
while ($row = pg_fetch_row($result)) {
  echo "Autor: $row[0]  E-mail: $row[1]";
  echo "<br />\n";
}

?>

    
```php

## Véase también

`pg_client_encoding`
