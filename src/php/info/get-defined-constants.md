---
title: get_defined_constants
description: Devuelve la lista de constantes y sus valores
source_url: https://www.php.net/manual/es/function.get-defined-constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/get-defined-constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: 525aa5f19
order: 38860
---

get_defined_constants

Devuelve la lista de constantes y sus valores

## Descripción

```php
get_defined_constants([bool $categorize]): array
```php

Devuelve los nombres y valores de las constantes ya definidas. Esto incluye las constantes creadas por las extensiones, y aquellas creadas con la función `define`.

## Parámetros

`categorize`  
Permite a esta función devolver un array multidimensional con las categorías como claves de la primera dimensión y las constantes junto con sus valores en la segunda dimensión.

```
<?php
define("MY_CONSTANT", 1);
print_r(get_defined_constants(true));
?>

        
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [Core] => Array
            (
                [E_ERROR] => 1
                [E_WARNING] => 2
                [E_PARSE] => 4
                [E_NOTICE] => 8
                [E_CORE_ERROR] => 16
                [E_CORE_WARNING] => 32
                [E_COMPILE_ERROR] => 64
                [E_COMPILE_WARNING] => 128
                [E_USER_ERROR] => 256
                [E_USER_WARNING] => 512
                [E_USER_NOTICE] => 1024
                [E_ALL] => 2047
                [TRUE] => 1
            )

        [pcre] => Array
            (
                [PREG_PATTERN_ORDER] => 1
                [PREG_SET_ORDER] => 2
                [PREG_OFFSET_CAPTURE] => 256
                [PREG_SPLIT_NO_EMPTY] => 1
                [PREG_SPLIT_DELIM_CAPTURE] => 2
                [PREG_SPLIT_OFFSET_CAPTURE] => 4
                [PREG_GREP_INVERT] => 1
            )

        [user] => Array
            (
                [MY_CONSTANT] => 1
            )

    )

## Valores devueltos

Devuelve un array de constantes en el formato "nombre de la constante" =\> "valor de la constante", opcionalmente agrupadas por el nombre de la extensión que registró la constante.

## Ejemplos

Ejemplo con `get_defined_constants`

```
<?php
print_r(get_defined_constants());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [E_ERROR] => 1
        [E_WARNING] => 2
        [E_PARSE] => 4
        [E_NOTICE] => 8
        [E_CORE_ERROR] => 16
        [E_CORE_WARNING] => 32
        [E_COMPILE_ERROR] => 64
        [E_COMPILE_WARNING] => 128
        [E_USER_ERROR] => 256
        [E_USER_WARNING] => 512
        [E_USER_NOTICE] => 1024
        [E_ALL] => 2047
        [TRUE] => 1
    )

## Véase también

`defined`, `constant`, `get_loaded_extensions`, `get_defined_functions`, `get_defined_vars`
