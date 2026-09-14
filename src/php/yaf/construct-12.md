---
title: Yaf_Route_Map::__construct
description: El propósito de __construct
source_url: https://www.php.net/manual/es/yaf-route-map.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_route_map/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: b37bddfde
order: 106750
---

Yaf_Route_Map::\_\_construct

El propósito de \_\_construct

## Descripción

```php
public Yaf_Route_Map::__construct([string $controller_prefer], [string $delimiter])
```php

## Parámetros

`controller_prefer`  
Si el resultado debería considerarse un controlador o una acción

`delimiter`  

## Valores devueltos

## Ejemplos

Ejemplo de `Yaf_Route_Map`

```
<?php
   /**
    * Añadir una ruta de mapas a la pila de enrutamiento de Yaf_Router
    */
    Yaf_Dispatcher::getInstance()->getRouter()->addRoute("name",
        new Yaf_Route_Map());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    /* para http://sudominio.com/producto/foo/bar
     * la ruta resultará en los siguiente valores:
     */
    array(
      "controller" => "producto_foo_bar",
    )

Ejemplo de `Yaf_Route_Map`

```
<?php
   /**
    * Añadir una ruta de mapas a la pila de enrutamiento de Yaf_Router
    */
    Yaf_Dispatcher::getInstance()->getRouter()->addRoute("name",
        new Yaf_Route_Map(true, "_"));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    /* para http://sudominio.com/user/list/_/foo/22
     * la ruta resultará en los siguientes valores:
     */
    array(
        "action" => "user_list",
    )

    /**
     * y los parámetros de petición:
     */
    array(
      "foo"   => 22,
    )

Ejemplo de `Yaf_Route_Map`

```
<?php
   /**
    * Añadir una ruta de mapas a la pila de enrutamiento de Yaf_Router llamando a addconfig
    */
    $config = array(
        "name" => array(
           "type"  => "map",         //Yaf_Route_Map route
           "controllerPrefer" => FALSE,
           "delimiter"        => "#!",
           ),
    );
    Yaf_Dispatcher::getInstance()->getRouter()->addConfig(
        new Yaf_Config_Simple($config));
?>

   
```php

## Véase también

Yaf_Router::addRoute

Yaf_Route_Static

Yaf_Route_Supervar

Yaf_Route_Simple

Yaf_Route_Regex

Yaf_Route_Rewrite
