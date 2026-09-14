---
title: php_sapi_name
description: Devuelve el tipo de interfaz utilizada entre el servidor web y PHP
source_url: https://www.php.net/manual/es/function.php-sapi-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/php-sapi-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: 8dd14a886
order: 39140
---

php_sapi_name

Devuelve el tipo de interfaz utilizada entre el servidor web y PHP

## Descripción

```php
php_sapi_name(): string
```php

Devuelve una cadena en minúsculas que describe el tipo de interfaz (la API, SAPI del servidor) que PHP utiliza. Por ejemplo, en PHP CLI, esta cadena será "cli" mientras que con Apache, puede tener varios valores diferentes según el SAPI exacto utilizado. Las posibles valores se listan a continuación.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el tipo de la interfaz, en forma de `string` en minúsculas, o `false` si ocurre un error.

A continuación se muestra una lista no exhaustiva de los posibles valores : `apache`, `apache2handler`, `cgi` (hasta PHP 5.3), `cgi-fcgi`, `cli`, `cli-server`, `embed`, `fpm-fcgi`, `litespeed`, `phpdbg`.

## Ejemplos

Ejemplo con `php_sapi_name`

Este ejemplo busca la subcadena `cgi` ya que también puede ser `cgi-fcgi`.

```
<?php
$sapi_type = php_sapi_name();
if (substr($sapi_type, 0, 3) == 'cgi') {
    echo "Se utiliza CGI PHP\n";
} else {
    echo "No se utiliza CGI PHP\n";
}
?>

    
```php

## Notas

> [!NOTE]
> La constante PHP `PHP_SAPI` tiene un valor idéntico a `php_sapi_name`.

> [!TIP]
> El SAPI definido no debe ser ambiguo, ya que por ejemplo, en lugar de `apache`, puede ser definido como `apache2handler`.

## Véase también

[PHP_SAPI](#reserved.constants.core)
