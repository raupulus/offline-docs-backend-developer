---
title: pg_close
description: Finaliza una conexión PostgreSQL
source_url: https://www.php.net/manual/es/function.pg-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: 2ca090342
order: 62890
---

pg_close

Finaliza una conexión PostgreSQL

## Descripción

```php
pg_close([PgSql\Connection $connection]): true
```php

`pg_close` cierra la conexión al servidor PostgreSQL asociada a `connection`.

> [!NOTE]
> No es generalmente necesario cerrar una conexión no persistente, ya que estas son cerradas automáticamente al final de un script.

Si existen instancias de `PgSql\Lob` que han sido abiertas con esta conexión, no se debe cerrar la conexión antes de haber cerrado todas las instancias de `PgSql\Lob`.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`. Cuando `connection` es `null`, se usa la conexión predeterminada. La conexión predeterminada es la última conexión hecha por `pg_connect` o `pg_pconnect`

> [!WARNING]
> Desde PHP 8.1.0, usar la conexión predeterminada está obsoleto.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | El tipo de retorno es ahora `true`, anteriormente era `bool`. |
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |
| 8.0.0 | `connection` ahora es nullable. |

## Ejemplos

Ejemplo con `pg_close`

```
<?php
$dbconn = pg_connect("host=localhost port=5432 dbname=marie")
      or die("Conexión imposible");
echo 'Conexión exitosa';
pg_close($dbconn);
?>

    
```php

El ejemplo anterior mostrará:

    Conexión exitosa

## Véase también

`pg_connect`
