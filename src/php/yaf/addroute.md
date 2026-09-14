---
title: Yaf_Router::addRoute
description: Añadir una nueva ruta al Enrutador
source_url: https://www.php.net/manual/es/yaf-router.addroute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_router/addroute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: 73fae4ee5
order: 106930
---

Yaf_Router::addRoute

Añadir una nueva ruta al Enrutador

## Descripción

```php
public Yaf_Router::addRoute(string $name, Yaf_Route_Abstract $route): bool
```php

Por defecto, Yaf_Router usa un `Yaf_Route_Static` como su ruta predeterminada. Se pueden añadir nuevas rutas a la pila de rutas del Enrutador llamando a este método.

La ruta más nueva será llamada antes que la más antigua (pila de rutas), y si la ruta más nueva devuelve `true`, el proceso de enrutamiento finalizará. De otro modo, será llamada la ruta más antigua.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

## Ejemplos

Ejemplo de `Yaf_Dispatcher::autoRender`

```
<?php
class Bootstrap extends Yaf_Bootstrap_Abstract{
    public function _initConfig() {
        $config = Yaf_Application::app()->getConfig();
        Yaf_Registry::set("config", $config);
    }

    public function _initRoute(Yaf_Dispatcher $dispatcher) {
        $router = $dispatcher->getRouter();
        /**
         * podemos añadir algunas rutas predefinidas en application.ini
         */
        $router->addConfig(Yaf_Registry::get("config")->routes);
        /**
         * add a Rewrite route, then for a request uri:
         * http://example.com/product/list/22/foo
         * will be matched by this route, and result:
         *
         *  [module] =>
         *  [controller] => product
         *  [action] => info
         *  [method] => GET
         *  [params:protected] => Array
         *      (
         *          [id] => 22
         *          [name] => foo
         *      )
         *
         */
        $route  = new Yaf_Route_Rewrite(
            "/product/list/:id/:name",
            array(
                "controller" => "product",
                "action"     => "info",
            )
        );

        $router->addRoute('dummy', $route);
    }
}
?>

   
```php

## Véase también

Yaf_Router::addConfig

Yaf_Route_Static

Yaf_Route_Supervar

Yaf_Route_Simple

Yaf_Route_Regex

Yaf_Route_Rewrite

Yaf_Route_Map
