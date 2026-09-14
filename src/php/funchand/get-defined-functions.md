---
title: get_defined_functions
description: Lista todas las funciones definidas
source_url: https://www.php.net/manual/es/function.get-defined-functions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/funchand/functions/get-defined-functions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: funchand
translation_status: ready
translation_revision: d155d3c30
order: 24810
---

get_defined_functions

Lista todas las funciones definidas

## Descripción

```php
get_defined_functions([bool $exclude_disabled]): array
```php

Lista todas las funciones definidas.

## Parámetros

`exclude_disabled`  
Si las funciones deshabilitadas deben ser excluidas del valor de retorno. Este parámetro no tiene efecto a partir de PHP 8.0.0.

> [!WARNING]
> Esta característica está *OBSOLETA* a partir de PHP 8.5.0. Depender de esta característica está altamente desaconsejado.

## Valores devueltos

Retorna un array multidimensional, que contiene la lista de todas las funciones definidas, tanto las funciones internas de PHP como las definidas por el usuario. Los nombres de las funciones internas son accesibles mediante `$arr["internal"]`, y las funciones de usuario son accesibles mediante `$arr["user"]`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | El parámetro `exclude_disabled` ha sido marcado como obsoleto, ya que no tiene ningún efecto. |
| 8.0.0 | El valor por omisión del argumento `exclude_disabled` ha sido cambiado de `false` a `true`. Sin embargo, no tendrá ningún efecto ya que las funciones deshabilitadas se eliminan de la tabla de funciones en tiempo de compilación. |
| 7.0.15, 7.1.1 | El argumento `exclude_disabled` ha sido añadido. |

## Ejemplos

Ejemplo con `get_defined_functions`

```
<?php
function myrow($id, $data)
{
    return "<tr><th>$id</th><td>$data</td></tr>\n";
}

$arr = get_defined_functions();

print_r($arr);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [internal] => Array
            (
                [0] => zend_version
                [1] => func_num_args
                [2] => func_get_arg
                [3] => func_get_args
                [4] => strlen
                [5] => strcmp
                [6] => strncmp
                ...
                [750] => bcscale
                [751] => bccomp
            )

        [user] => Array
            (
                [0] => myrow
            )

    )

## Véase también

`function_exists`, `get_defined_vars`, `get_defined_constants`, `get_declared_classes`
