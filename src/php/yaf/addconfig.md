---
title: Yaf_Router::addConfig
description: Añadir rutas definidas en configuración al Enrutador
source_url: https://www.php.net/manual/es/yaf-router.addconfig.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_router/addconfig.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 22583751f
order: 106920
---

Yaf_Router::addConfig

Añadir rutas definidas en configuración al Enrutador

## Descripción

```php
public Yaf_Router::addConfig(Yaf_Config_Abstract $config): bool
```php

Añade rutas definidas mediante configuraciones en la pila de rutas de `Yaf_Router`

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una instancia de `Yaf_Config_Abstract`, la cual debería contener una o más configuraciones de rutas válidas.

## Ejemplos

Ejemplo de `application.ini`

```
;el orden es muy importante, el primero será llamado en primer lugar

;a rewrite route match request /product/*/*
routes.route_name.type="rewrite"
routes.route_name.match="/product/:name/:value"
routes.route_name.route.controller=product
routes.route_name.route.action=info

;a regex route match request /list/*/*
routes.route_name1.type="regex"
routes.route_name1.match="#^list/([^/]*)/([^/]*)#"
routes.route_name1.route.controller=Index
routes.route_name1.route.action=action
routes.route_name1.map.1=name
routes.route_name1.map.2=value

;a simple route match /**?c=controller&a=action&m=module
routes.route_name2.type="simple"
routes.route_name2.controller=c
routes.route_name2.module=m
routes.route_name2.action=a

;a simple router match /**?r=PATH_INFO
routes.route_name3.type="supervar"
routes.route_name3.varname=r

;a map route match any request to controller
routes.route_name4.type="map"
routes.route_name4.controllerPrefer=TRUE
routes.route_namer.delimiter="#!"

   
```php

Ejemplo de `Yaf_Dispatcher::autoConfig`

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
    }

?>

   
```php

## Véase también

Yaf_Router::addRoute

Yaf_Route_Static

Yaf_Route_Supervar

Yaf_Route_Simple

Yaf_Route_Regex

Yaf_Route_Rewrite

Yaf_Route_Map
