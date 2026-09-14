---
title: Yaf_Application::environ
description: Recuperar el entorno
source_url: https://www.php.net/manual/es/yaf-application.environ.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_application/environ.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: a023d0b24
order: 104980
---

Yaf_Application::environ

Recuperar el entorno

## Descripción

```php
public Yaf_Application::environ(): void
```php

Recupera el entorno que fue definido en yaf.environ, el cual tiene el valor predeterminado "product".

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

## Ejemplos

Ejemplo de `Yaf_Application::environ`

```
<?php
$config = array(
    "application" => array(
        "directory" => realpath(dirname(__FILE__)) . "/application",
    ),
);

/** Yaf_Application */
$application = new Yaf_Application($config);
print_r($application->environ());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    product
