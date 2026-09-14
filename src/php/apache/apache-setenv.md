---
title: apache_setenv
description: Establece una variable subprocess_env de Apache
source_url: https://www.php.net/manual/es/function.apache-setenv.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/apache/functions/apache-setenv.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: apache
translation_status: ready
translation_revision: b8758b060
order: 4810
---

apache_setenv

Establece una variable subprocess_env de Apache

## Descripción

```php
apache_setenv(string $variable, string $value, [bool $walk_to_top]): bool
```php

`apache_setenv` establece el valor de la variable de entorno de Apache especificado por `variable`.

> [!NOTE]
> Al establecer una variable de entorno de Apache, la correspondiente variable `$_SERVER` no se modifica.

## Parámetros

`variable`  
La variable de entorno que se desea establecer.

`value`  
El nuevo valor de `variable`.

`walk_to_top`  
Indica si se va a establecer la variable de nivel superior disponible para todas las capas de Apache.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Estableciendo una variable de entorno de Apache usando `apache_setenv`

```
<?php
apache_setenv("VARIABLE_EJEMPLO", "Valor de ejemplo");
?>

    
```php

## Notas

> [!NOTE]
> `apache_setenv` puede ser utilizado con `apache_getenv` en páginas separadas o para establecer variables para pasar Server Side Includes (.shtml) que hayan sido incluidos en sprits PHP.

## Véase también

`apache_getenv`
