---
title: Yaf_Application::getConfig
description: Recuperar la instancia de configuración
source_url: https://www.php.net/manual/es/yaf-application.getconfig.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_application/getconfig.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: a023d0b24
order: 105010
---

Yaf_Application::getConfig

Recuperar la instancia de configuración

## Descripción

```php
public Yaf_Application::getConfig(): Yaf_Config_Abstract
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una instancia de la clase `Yaf_Config_Abstract`

## Ejemplos

Ejemplo de `Yaf_Application::getConfig`

```
<?php
$config = array(
    "application" => array(
        "directory" => realpath(dirname(__FILE__)) . "/application",
    ),
);

/** Yaf_Application */
$application = new Yaf_Application($config);
print_r($application->getConfig());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Yaf_Config_Simple Object
    (
        [_config:protected] => Array
            (
                [application] => Array
                    (
                        [directory] => /home/laruence/local/www/htdocs/application
                    )

            )

        [_readonly:protected] => 1
    )
