---
title: APCUIterator::__construct
description: Construye un objeto iterador APCUIterator
source_url: https://www.php.net/manual/es/apcuiterator.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/apcu/apcuiterator/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: apcu
translation_status: ready
translation_reviewed: false
translation_revision: 804d8a054
order: 4860
---

APCUIterator::\_\_construct

Construye un objeto iterador APCUIterator

## Descripción

```php
public APCUIterator::__construct([array $search], [int $format], [int $chunk_size], [int $list])
```php

Construye un `APCUIterator` `object`.

## Parámetros

`search`  
O bien una expresión regular [PCRE](#book.pcre) que coincide con nombres de clave APCu, dada como `string`. O una `array` de `string`s con nombres de claves APCu. O, opcionalmente `null` para omitir la búsqueda.

`format`  
El formato deseado, tal como está configurado con una o más de las constantes [APC_ITER\_\*](#apcu.constants).

`chunk_size`  
El tamaño del fragmento. Debe ser un valor mayor que 0. El valor por defecto es 100.

`list`  
El tipo de lista. O bien pasar en `APC_LIST_ACTIVE` o `APC_LIST_DELETED`.

## Ejemplos

Un ejemplo de `APCUIterator::__construct`

```
<?php
foreach (new APCUIterator('/^counter\./') as $counter) {
    echo "$counter[key]: $counter[value]\n";
    apc_dec($counter['key'], $counter['value']);
}
?>

   
```php

## Véase también

apcu_exists

apcu_cache_info
