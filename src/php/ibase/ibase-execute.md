---
title: ibase_execute
description: Ejecuta una consulta iBase preparada
source_url: https://www.php.net/manual/es/function.ibase-execute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-execute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30310
---

ibase_execute

Ejecuta una consulta iBase preparada

## Descripción

```php
ibase_execute(resource $query, mixed ...$values): resource
```php

Ejecuta una consulta iBase preparada.

`ibase_execute` es mucho más eficiente que `ibase_query`, si se realiza la misma consulta varias veces cambiando solo algunos argumentos.

## Parámetros

`query`  
Una consulta InterBase, preparada con la función `ibase_prepare`.

`values`  

## Valores devueltos

Si la consulta emite un error, la función devolverá `false`. Si la consulta tiene éxito, y hay un conjunto de resultados (que puede estar vacío), la función devuelve un identificador de resultados. Si la consulta tiene éxito y no hay resultados, la función devuelve `true`.

> [!NOTE]
> `ibase_execute` devuelve el número de registros afectados por la consulta (si es mayor que 0). Para una consulta que tiene éxito pero que no devuelve ningún registro (por ejemplo, un UPDATE en un registro inexistente), `ibase_execute` devolverá `true`.

## Ejemplos

Ejemplo con `ibase_execute`

```
<?php

$dbh = ibase_connect($host, $username, $password);

$updates = array(
    1 => 'Eric',
    5 => 'Filip',
    7 => 'Larry'
);

$query = ibase_prepare($dbh, "UPDATE FOO SET BAR = ? WHERE BAZ = ?");

foreach ($updates as $baz => $bar) {
    ibase_execute($query, $bar, $baz);
}

?>

   
```php

## Véase también

ibase_query
