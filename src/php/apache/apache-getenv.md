---
title: apache_getenv
description: Lee una variable de proceso Apache
source_url: https://www.php.net/manual/es/function.apache-getenv.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/apache/functions/apache-getenv.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: apache
translation_status: ready
translation_reviewed: true
translation_revision: a331ac8a8
order: 4760
---

apache_getenv

Lee una variable de proceso Apache

## Descripción

```php
apache_getenv(string $variable, [bool $walk_to_top]): string
```php

Recupera una variable de entorno de Apache.

## Parámetros

`variable`  
La variable de entorno Apache.

`walk_to_top`  
Si se pasa a `true`, se recupera la variable de nivel superior disponible para todas las capas de Apache.

## Valores devueltos

El valor de la variable de entorno de Apache en caso de éxito o `false` en caso de fallo.

## Ejemplos

Ejemplo con `apache_getenv`

El siguiente ejemplo muestra cómo recuperar el valor de la variable de entorno `SERVER_ADDR`.

```
<?php
$ret = apache_getenv("SERVER_ADDR");
echo $ret;
?>

    
```php

Resultado del ejemplo anterior es similar a:

    42.24.42.240

## Véase también

`apache_setenv`, `getenv`, [Superglobales](#language.variables.superglobals)
