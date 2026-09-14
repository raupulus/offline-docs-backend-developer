---
title: Yaf_Application::getDispatcher
description: Obtener la instancia de la clase Yaf_Dispatcher
source_url: https://www.php.net/manual/es/yaf-application.getdispatcher.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_application/getdispatcher.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: a023d0b24
order: 105020
---

Yaf_Application::getDispatcher

Obtener la instancia de la clase Yaf_Dispatcher

## Descripción

```php
public Yaf_Application::getDispatcher(): Yaf_Dispatcher
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

## Ejemplos

Ejemplo de `Yaf_Application::getDispatcher`

```
<?php
$config = array(
    "application" => array(
        "directory" => realpath(dirname(__FILE__)) . "/application",
    ),
);

/** Yaf_Application */
$application = new Yaf_Application($config);
print_r($application->getDispatcher());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Yaf_Dispatcher Object
    (
        [_router:protected] => Yaf_Router Object
            (
                [_routes:protected] => Array
                    (
                        [_default] => Yaf_Route_Static Object
                            (
                            )

                    )

                [_current:protected] =>
            )

        [_view:protected] =>
        [_request:protected] => Yaf_Request_Http Object
            (
                [module] =>
                [controller] =>
                [action] =>
                [method] => Cli
                [params:protected] => Array
                    (
                    )

                [language:protected] =>
                [_exception:protected] =>
                [_base_uri:protected] =>
                [uri:protected] =>
                [dispatched:protected] =>
                [routed:protected] =>
            )

        [_plugins:protected] => Array
            (
            )

        [_auto_render:protected] => 1
        [_return_response:protected] =>
        [_instantly_flush:protected] =>
        [_default_module:protected] => Index
        [_default_controller:protected] => Index
        [_default_action:protected] => index
        [_response] => Yaf_Response_Cli Object
            (
                [_header:protected] => Array
                    (
                    )

                [_body:protected] =>
                [_sendheader:protected] =>
            )

    )
