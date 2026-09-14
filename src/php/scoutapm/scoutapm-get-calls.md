---
title: scoutapm_get_calls
description: Devuelve una lista de llamadas instrumentadas que se han producido
source_url: https://www.php.net/manual/es/function.scoutapm-get-calls.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/scoutapm/functions/scoutapm-get-calls.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: scoutapm
translation_status: ready
translation_reviewed: true
translation_revision: ed737dd93
order: 73040
---

scoutapm_get_calls

Devuelve una lista de llamadas instrumentadas que se han producido

## Descripción

```php
scoutapm_get_calls(): array
```php

Devuelve una lista de todas las llamadas a funciones instrumentadas registradas desde la última vez que la función `scoutapm_get_calls` fue llamada. La lista se borra cada vez que la función es llamada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`scoutapm_get_calls` devuelve un array que contiene una lista de todas las llamadas registradas a funciones instrumentadas.

## Ejemplos

Obtener las llamadas instrumentadas

```
<?php

file_get_contents('a.txt');
file_get_contents('b.txt');

print_r(scoutapm_get_calls());
?>

   
```php

Resultado del ejemplo anterior es similar a:

        
    Array
    (
        [0] => Array
            (
                [function] => file_get_contents
                [entered] => 1576839727.7934
                [exited] => 1576839727.7935
                [time_taken] => 2.7894973754883E-5
                [argv] => Array
                    (
                        [0] => a.txt
                    )

            )

        [1] => Array
            (
                [function] => file_get_contents
                [entered] => 1576839727.7935
                [exited] => 1576839727.7935
                [time_taken] => 7.8678131103516E-6
                [argv] => Array
                    (
                        [0] => b.txt
                    )

            )

    )
