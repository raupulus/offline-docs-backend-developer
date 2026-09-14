---
title: pg_meta_data
description: Lee los metadatos de la tabla PostgreSQL
source_url: https://www.php.net/manual/es/function.pg-meta-data.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-meta-data.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63450
---

pg_meta_data

Lee los metadatos de la tabla PostgreSQL

## Descripción

```php
pg_meta_data(PgSql\Connection $connection, string $table_name, [bool $extended]): array
```php

`pg_meta_data` devuelve la definición de la tabla `table_name` en forma de array.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`.

`table_name`  
El nombre de la tabla.

`extended`  
Flag para devolver los metadatos extendidos. Por omisión, vale `false`.

## Valores devueltos

Un `array` de la definición de la tabla, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Recuperación de los metadatos de una tabla

```
<?php
  $dbconn = pg_connect("dbname=publisher") or die("Conexión imposible");

  $meta = pg_meta_data($dbconn,'auteurs');
  if (is_array ($meta)) {
       echo '<pre>';
       var_dump ($meta);
       echo '</pre>';
  }
?>

    
```php

El ejemplo anterior mostrará:

    array(3) {
    ["auteur"]=>
    array(5) {
      ["num"]=>
      int(1)
      ["type"]=>
      string(7) "varchar"
      ["len"]=>
      int(-1)
      ["not null"]=>
      bool(false)
      ["has default"]=>
      bool(false)
    }
    ["annee"]=>
    array(5) {
      ["num"]=>
      int(2)
      ["type"]=>
      string(4) "int2"
      ["len"]=>
      int(2)
      ["not null"]=>
      bool(false)
      ["has default"]=>
      bool(false)
    }
    ["titre"]=>
    array(5) {
      ["num"]=>
      int(3)
      ["type"]=>
      string(7) "varchar"
      ["len"]=>
      int(-1)
      ["not null"]=>
      bool(false)
      ["has default"]=>
      bool(false)
    }
    }

## Véase también

`pg_convert`
