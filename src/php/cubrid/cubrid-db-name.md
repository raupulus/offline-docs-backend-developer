---
title: cubrid_db_name
description: Obtener el nombre de la base de datos desde los resultados de cubrid_list_dbs
source_url: https://www.php.net/manual/es/function.cubrid-db-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/cubridmysql/cubrid-db-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 8630
---

cubrid_db_name

Obtener el nombre de la base de datos desde los resultados de cubrid_list_dbs

## Descripción

```php
cubrid_db_name(array $result, int $index): string
```php

Recupera el nombre de la base de datos desde una llamada a `cubrid_list_dbs`.

## Parámetros

`result`  
El puntero resultado desde un llamada a `cubrid_list_dbs`.

`index`  
El índice dentro del conjunto resultado.

## Valores devueltos

Devuelve el nombre de la base de datos en caso de éxito, y `false` en caso de fallo. Si se devuelve `false`, use `cubrid_error` para determinar la naturaleza del error.

## Ejemplos

Ejemplo de `cubrid_db_name`

```
<?php
error_reporting(E_ALL);

$conn = cubrid_connect('localhost', 33000, 'demodb', 'dba', '');
$db_list = cubrid_list_dbs($conn);

$i = 0;
$cnt = count($db_list);
while ($i < $cnt) {
    echo cubrid_db_name($db_list, $i) . "\n";
    $i++;
}
?>

   
```php

El ejemplo anterior mostrará:

    demodb

## Véase también

cubrid_list_dbs
