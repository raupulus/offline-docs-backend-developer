---
title: ibase_field_info
description: Lee la información sobre un campo iBase
source_url: https://www.php.net/manual/es/function.ibase-field-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-field-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30350
---

ibase_field_info

Lee la información sobre un campo iBase

## Descripción

```php
ibase_field_info(resource $result, int $field_number): array
```php

Devuelve un array que contiene la información de un campo, después de que una consulta de tipo selección haya sido ejecutada.

## Parámetros

`result`  
Un identificador de resultado InterBase.

`field_number`  
Posición del campo.

## Valores devueltos

Devuelve un array que contiene las siguientes claves: `name`, `alias`, `relation`, `length` y `type`.

## Ejemplos

Ejemplo con `ibase_field_info`

```
<?php
$rs = ibase_query("SELECT * FROM tablename");
$coln = ibase_num_fields($rs);
for ($i = 0; $i < $coln; $i++) {
    $col_info = ibase_field_info($rs, $i);
    echo "nombre : ". $col_info['name']. "\n";
    echo "alias : ". $col_info['alias']. "\n";
    echo "relación : ". $col_info['relation']. "\n";
    echo "tamaño : ". $col_info['length']. "\n";
    echo "tipo : ". $col_info['type']. "\n";
}
?>

   
```php

## Véase también

ibase_num_fields
