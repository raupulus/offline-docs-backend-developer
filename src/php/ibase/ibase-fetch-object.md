---
title: ibase_fetch_object
description: Lee una línea en una base Interbase en un objeto
source_url: https://www.php.net/manual/es/function.ibase-fetch-object.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-fetch-object.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30330
---

ibase_fetch_object

Lee una línea en una base Interbase en un objeto

## Descripción

```php
ibase_fetch_object(resource $result_id, [int $fetch_flag]): object
```php

Lee una línea en una base Interbase y la coloca en un pseudo objeto.

Las siguientes llamadas a la función `ibase_fetch_object` devolverán la siguiente línea del conjunto de resultados.

## Parámetros

`result_id`  
Un identificador de resultado InterBase, obtenido ya sea por la función `ibase_query`, ya sea por la función `ibase_execute`.

`fetch_flag`  
`fetch_flag` es una combinación de las constantes `IBASE_TEXT` y `IBASE_UNIXTIME`. Pasar `IBASE_TEXT` hace que se devuelva el contenido del BLOB en lugar del ID del BLOB. Pasar `IBASE_UNIXTIME` hace que se devuelvan los valores de fecha/hora en forma de timestamps UNIX en lugar de strings formateados.

## Valores devueltos

Devuelve un objeto que contiene la información de la línea, o `false` si no hay más líneas.

## Ejemplos

Ejemplo con `ibase_fetch_object`

```
<?php
$dbh = ibase_connect($host, $username, $password);
$stmt = 'SELECT * FROM tblname';
$sth = ibase_query($dbh, $stmt);
while ($row = ibase_fetch_object($sth)) {
    echo $row->email . "\n";
}
ibase_close($dbh);
?>

   
```php

## Véase también

ibase_fetch_row

ibase_fetch_assoc
