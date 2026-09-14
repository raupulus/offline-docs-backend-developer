---
title: ibase_num_fields
description: Devuelve el número de columnas en un resultado iBase
source_url: https://www.php.net/manual/es/function.ibase-num-fields.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-num-fields.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30430
---

ibase_num_fields

Devuelve el número de columnas en un resultado iBase

## Descripción

```php
ibase_num_fields(resource $result_id): int
```php

Devuelve el número de columnas en un resultado iBase.

## Parámetros

`result_id`  
Un identificador de resultado InterBase.

## Valores devueltos

Devuelve el número de campos, en forma de un `int`.

## Ejemplos

Ejemplo con `ibase_num_fields`

```
<?php
$rs = ibase_query("SELECT * FROM tablename");
$coln = ibase_num_fields($rs);
for ($i = 0; $i < $coln; $i++) {
    $col_info = ibase_field_info($rs, $i);
    echo "nombre : " . $col_info['name'] . "\n";
    echo "alias : " . $col_info['alias'] . "\n";
    echo "relación : " . $col_info['relation'] . "\n";
    echo "tamaño : " . $col_info['length'] . "\n";
    echo "tipo : " . $col_info['type'] . "\n";
}
?>

   
```php

## Véase también

ibase_field_info
