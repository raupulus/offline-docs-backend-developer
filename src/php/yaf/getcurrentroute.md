---
title: Yaf_Router::getCurrentRoute
description: Obtener el nombre de la ruta efectiva
source_url: https://www.php.net/manual/es/yaf-router.getcurrentroute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_router/getcurrentroute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: 73fae4ee5
order: 106950
---

Yaf_Router::getCurrentRoute

Obtener el nombre de la ruta efectiva

## Descripción

```php
public Yaf_Router::getCurrentRoute(): string
```php

Obtiene el nombre de la ruta efectiva del proceso de enrutamiento.

> [!NOTE]
> Se debería llamar a este método después de que finalice el proceso de enrutamiento, ya que si se hace antes, este método devolverá siempre `null`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una cadena, el nombre de la ruta efectiva.

## Ejemplos

Registrar algunas rutas en el Arranque

```
<?php
class Bootstrap extends Yaf_Bootstrap_Abstract{
    public function _initConfig() {
        $config = Yaf_Application::app()->getConfig();
        Yaf_Registry::set("config", $config);
    }

    public function _initRoute(Yaf_Dispatcher $dispatcher) {
        $router = $dispatcher->getRouter();
        $rewrite_route  = new Yaf_Route_Rewrite(
            "/product/list/:page",
            array(
                "controller" => "product",
                "action"     => "list",
            )
        );

        $regex_route  = new Yaf_Route_Rewrite(
            "#^/product/info/(\d+)",
            array(
                "controller" => "product",
                "action"     => "info",
            )
        );

        $router->addRoute('rewrite', $rewrite_route)->addRoute('regex', $regex_route);
    }

    /**
     * registrar un complemento
     */
    public function __initPlugins(Yaf_Dispatcher $dispatcher) {
        $dispatcher->registerPlugin(new DummyPlugin());
    }
}
?>

   
```php

Complemento Dummy.php (bajo [application.directory](#configuration.yaf.directory)/plugins)

```
<?php
class DummyPlugin extends Yaf_Plugin_Abstract {
    public function routerShutdown(Yaf_Request_Abstract $request, Yaf_Response_Abstract $response) {
         var_dump(Yaf_Dispatcher::getInstance()->getRouter()->getCurrentRoute());
    }
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    /* para http://yourdomain.com/product/list/1
     * DummyPlugin imprimirá:
     */
    string(7) "rewrite"

    /* para http://yourdomain.com/product/info/34
     * DummyPlugin imprimirá:
     */
    string(5) "regex"

    /* para otros URIs solicitados
     * DummyPlugin imprimirá:
     */
    string(8) "_default"

## Véase también

Yaf_Bootstrap_Abstract

Yaf_Plugin_Abstract

Yaf_Router::addRoute
