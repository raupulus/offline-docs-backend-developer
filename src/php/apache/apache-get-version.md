---
title: apache_get_version
description: Obtiene la versión de Apache
source_url: https://www.php.net/manual/es/function.apache-get-version.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/apache/functions/apache-get-version.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: apache
translation_status: ready
translation_reviewed: true
translation_revision: f3b9d85f7
order: 4750
---

apache_get_version

Obtiene la versión de Apache

## Descripción

```php
apache_get_version(): string
```php

Obtiene la versión de Apache.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la versión de Apache en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `apache_get_version`

```
<?php
$version = apache_get_version();
echo "$version\n";
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Apache/1.3.29 (Unix) PHP/4.3.4

## Véase también

`phpinfo`
