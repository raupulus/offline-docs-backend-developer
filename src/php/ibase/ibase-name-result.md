---
title: ibase_name_result
description: Asigna un nombre a un conjunto de resultados iBase
source_url: https://www.php.net/manual/es/function.ibase-name-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-name-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30420
---

ibase_name_result

Asigna un nombre a un conjunto de resultados iBase

## Descripción

```php
ibase_name_result(resource $result, string $name): bool
```php

Asigna un nombre a un conjunto de resultados. Este nombre puede ser utilizado más tarde en las consultas de tipo `UPDATE|DELETE ... WHERE CURRENT OF` `name`.

## Parámetros

`result`  
Un conjunto de resultados InterBase.

`name`  
El nombre a asignar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `ibase_name_result`

```
<?php
$result = ibase_query("SELECT field1,field2 FROM table FOR UPDATE");
ibase_name_result($result, "my_cursor");

$updateqry = ibase_prepare("UPDATE table SET field2 = ? WHERE CURRENT OF my_cursor");

for ($i = 0; ibase_fetch_row($result); ++$i) {
    ibase_execute($updateqry, $i);
}
?>

   
```php

## Véase también

ibase_prepare

ibase_execute
