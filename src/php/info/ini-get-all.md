---
title: ini_get_all
description: Lee todos los valores de configuración
source_url: https://www.php.net/manual/es/function.ini-get-all.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/ini-get-all.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: c8a8981a9
order: 39040
---

ini_get_all

Lee todos los valores de configuración

## Descripción

```php
ini_get_all([string $extension], [bool $details]): array
```php

Devuelve todas las valores de configuración.

## Parámetros

`extension`  
Un nombre de extensión, opcional. Si no es `null` o diferente de la `string` `core`, esta función devolverá únicamente las opciones específicas de esta extensión.

`details`  
Obtiene los detalles, o únicamente el valor actual de cada configuración. Por omisión, vale `true` (obtiene los detalles).

## Valores devueltos

Devuelve un array asociativo cuyas claves son los nombres de las directivas. Devuelve `false` y genera un error de nivel `E_WARNING` si la `extension` no existe.

Cuando el argumento `details` vale `true` (por defecto), el array contendrá los valores `global_value` (definidos en el archivo `php.ini`), `local_value` (definido eventualmente con la función `ini_set` o mediante un `.htaccess`), y `access` (el grado de acceso).

Cuando el argumento `details` vale `false`, el valor será el valor actual de la opción.

Ver el [manual](#configuration.changes.modes) para más información sobre el significado del grado de acceso.

> [!NOTE]
> Es posible que una directiva tenga varios grados de acceso, y por eso `access` muestra los valores del máscara apropiados.

## Ejemplos

Ejemplo con `ini_get_all`

```
<?php
print_r(ini_get_all("pcre"));
print_r(ini_get_all());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [pcre.backtrack_limit] => Array
            (
                [global_value] => 100000
                [local_value] => 100000
                [access] => 7
            )

        [pcre.recursion_limit] => Array
            (
                [global_value] => 100000
                [local_value] => 100000
                [access] => 7
            )

    )
    Array
    (
        [allow_call_time_pass_reference] => Array
            (
                [global_value] => 0
                [local_value] => 0
                [access] => 6
            )

        [allow_url_fopen] => Array
            (
                [global_value] => 1
                [local_value] => 1
                [access] => 4
            )

        ...

    )

Desactiva el argumento `details`

```
<?php
print_r(ini_get_all("pcre", false)); // Añadido en PHP 5.3.0
print_r(ini_get_all(null, false)); // Añadido en PHP 5.3.0
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [pcre.backtrack_limit] => 100000
        [pcre.recursion_limit] => 100000
    )
    Array
    (
        [allow_call_time_pass_reference] => 0
        [allow_url_fopen] => 1
        ...
    )

## Notas

> [!NOTE]
> `ini_get_all` ignora las opciones ini "array" tales como `pdo.dsn.*`.

## Véase también

[???](#configuration.changes), `ini_get`, `ini_restore`, `ini_set`, `get_loaded_extensions`, `phpinfo`, ReflectionExtension::getINIEntries
