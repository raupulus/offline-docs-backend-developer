---
title: scoutapm_list_instrumented_functions
description: Lista las funciones que scoutapm va a instrumentar.
source_url: https://www.php.net/manual/es/function.scoutapm-list-instrumented-functions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/scoutapm/functions/scoutapm-list-instrumented-functions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: scoutapm
translation_status: ready
translation_reviewed: true
translation_revision: ed737dd93
order: 73050
---

scoutapm_list_instrumented_functions

Lista las funciones que scoutapm va a instrumentar.

## Descripción

```php
scoutapm_list_instrumented_functions(): array
```php

Devuelve una lista de las funciones que la extensión va a instrumentar.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`scoutapm_list_instrumented_functions` devuelve un array que contiene una lista de todas las funciones que la extensión scoutapm es capaz de instrumentar en la instalación actual.

## Ejemplos

Obtener la lista de funciones que scoutapm va a instrumentar

```
    
<?php
print_r(scoutapm_list_instrumented_functions());
?>

   
```php

Resultado del ejemplo anterior es similar a:

        
    Array
    (
        [0] => file_get_contents
        [1] => file_put_contents
        [2] => fopen
        [3] => fread
        [4] => fwrite
        [5] => pdo->exec
        [6] => pdo->query
        [7] => pdo->prepare
        [8] => pdostatement->execute
    )
