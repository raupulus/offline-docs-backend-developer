---
title: Yaf_Application::getModules
description: Obtener los nombres de los modulos definidos
source_url: https://www.php.net/manual/es/yaf-application.getmodules.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_application/getmodules.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: a023d0b24
order: 105050
---

Yaf_Application::getModules

Obtener los nombres de los modulos definidos

## Descripción

```php
public Yaf_Application::getModules(): array
```php

Obtiene la lista de módulos definidos en config, si no se han definido siempre habrá un módulo llamado "Index".

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

## Ejemplos

Ejemplo de `Yaf_Application::getModules`

```
<?php
$config = array(
    "application" => array(
        "directory" => realpath(dirname(__FILE__)) . "/application",
    ),
);

/** Yaf_Application */
$application = new Yaf_Application($config);
print_r($application->getModules());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => Index
    )
