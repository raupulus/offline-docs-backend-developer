---
title: runkit7_zval_inspect
description: Proporciona información sobre el valor pasado con los tipos de datos,
  los conteos de referencia, etc
source_url: https://www.php.net/manual/es/function.runkit7-zval-inspect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/runkit7/functions/runkit7-zval-inspect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: runkit7
translation_status: ready
translation_reviewed: true
translation_revision: c4625323f
order: 73000
---

runkit7_zval_inspect

Proporciona información sobre el valor pasado con los tipos de datos, los conteos de referencia, etc

## Descripción

```php
runkit7_zval_inspect(string $value): array
```php

## Parámetros

`value`  
El valor para el cual se devuelve la representación

## Valores devueltos

El array devuelto por esta función contiene los siguientes elementos: `address`, `refcount` (opcional), `is_ref` (opcional), `type`

## Ejemplos

Ejemplo de `runkit7_zval_inspect`

```
<?php

$var = new DateTime();
var_dump(runkit7_zval_inspect($var));

$var = 1;
var_dump(runkit7_zval_inspect($var));
?>

   
```php

El ejemplo anterior mostrará:

    array(4) {
      ["address"]=>
      string(14) "0x7f45ab21b1e0"
      ["refcount"]=>
      int(2)
      ["is_ref"]=>
      bool(false)
      ["type"]=>
      int(8)
    }

    array(2) {
      ["address"]=>
      string(14) "0x7f45ab21b1e0"
      ["type"]=>
      int(4)
    }

## Véase también

References Explained

References Explained (by Derick Rethans)
