---
title: cubrid_unbuffered_query
description: Realiza una consulta sin traer los resultados a memoria
source_url: https://www.php.net/manual/es/function.cubrid-unbuffered-query.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/cubridmysql/cubrid-unbuffered-query.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 8840
---

cubrid_unbuffered_query

Realiza una consulta sin traer los resultados a memoria

## Descripción

```php
cubrid_unbuffered_query(string $query, [resource $conn_identifier]): resource
```php

Esta función realiza una consulta sin esperar a que todos los resultados de consulta hayan sido completados. Devolverá cuando los resultados están siendo generados.

## Parámetros

`query`  
Una consulta SQL.

`conn_identifier`  
La conexión CUBRID. Si el identificador de conexión no se especifica, se asume el último enlace abierto por `cubrid_connect`.

## Valores devueltos

Para sentencias SELECT, SHOW, DESCRIBE o EXPLAIN devuelve un recurso identificador de petición en caso de éxito.

Para otro tipo de sentencias SQL, UPDATE, DELETE, DROP, etc,, devuelve `true` en caso de éxito.

`false` en caso de fallo.

## Ejemplos

Ejemplo de `cubrid_unbuffered_query`

```
<?php
    $enlace = cubrid_connect("localhost", 30000, "demodb", "dba", "");
    if (!$enlace)
    {
        die('No se pudo conectar.');
    }
    $consulta = "select * from code";
    $resultado = cubrid_unbuffered_query($consulta, $enlace);

    while ($fila = cubrid_fetch($resultado))
    {
        var_dump($fila);
    }

    cubrid_close_request($resultado);
    cubrid_disconnect($enlace);
?>

   
```php

## Notas

> [!NOTE]
> Los beneficios de `cubrid_unbuffered_query` tienen un coste: no se puede usar `cubrid_num_rows` y `cubrid_data_seek` en un conjunto de resultados devueltos desde `cubrid_unbuffered_query`.
