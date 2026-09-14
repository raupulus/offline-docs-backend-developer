---
title: Yaf_Route_Rewrite::__construct
description: Constructor de Yaf_Route_Rewrite
source_url: https://www.php.net/manual/es/yaf-route-rewrite.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_route_rewrite/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 330a38c4d
order: 106810
---

Yaf_Route_Rewrite::\_\_construct

Constructor de Yaf_Route_Rewrite

## Descripción

```php
public Yaf_Route_Rewrite::__construct(string $match, array $route, [array $verify])
```php

## Parámetros

`match`  
Un patrón de expresión regular completo, se usará para comparar un URI solicitado, si no coincide, `Yaf_Route_Regex` devolverá `false`.

Se puede usar el stilo :name para nombrar segmentos a buscar. y \* para encontrar el resto de segmentos.

`route`  
Cuando el patrón de comparación coincida con el URI solicitado, `Yaf_Route_Regex` lo usará para decidir qué módulo/ccontrolador/acción enrutar.

Cada módulo/ccontrolador/acción en este array es opcional, si no se asigna un valor específico, será enrutada al valor predeterminado.

`verify`  

## Valores devueltos

## Ejemplos

Ejemplo de `Yaf_Route_Rewrite`

```
<?php
   /**
    * Añadir una ruta de reescritura a la pila de rutas de Yaf_Router
    */
    Yaf_Dispatcher::getInstance()->getRouter()->addRoute("name",
        new Yaf_Route_Rewrite(
           "/product/:name/:id/*", //match request uri leading "/product"
           array(
               'controller' => "product",  //route to product controller,
           ),
        )
    );
?>

   
```php

Resultado del ejemplo anterior es similar a:

    /* para http://yourdomain.com/product/foo/22/foo/bar
     * la ruta resultará en los siguientes valores:
     */
    array(
      "controller" => "product",
      "module"     => "index", //(default)
      "action"     => "index", //(default)
    )

    /**
     * y los parámetros de petición:
     */
    array(
      "name" => "foo",
      "id"   => 22,
      "foo"  => bar
    )

Ejemplo de `Yaf_Route_Rewrite`

```
    <?php
   /**
    * Añadir una ruta de reescritura a la pila de rutas de Yaf_Router llamando a addconfig
    */
    $config = array(
        "name" => array(
           "type"  => "rewrite",        //Yaf_Route_Rewrite route
           "match" => "/user-list/:id", //match only /user/list/?/
           "route" => array(
               'controller' => "user",  //route to user controller,
               'action'     => "list",  //route to list action
           ),
        ),
    );
    Yaf_Dispatcher::getInstance()->getRouter()->addConfig(
        new Yaf_Config_Simple($config));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    /* para http://yourdomain.com/user-list/22
     * la ruta resultará en los siguientes valores:
     */
    array(
      "controller" => "user",
      "action"     => "list",
      "module"     => "index", //(default)
    )

    /**
     * y los parámetros de petición:
     */
    array(
      "id"   => 22,
    )

Ejemplo de `Yaf_Route_Rewrite` (como en 2.3.0)

```
    <?php
   /**
    * Añadir una ruta de reescritura para usar el resultado de comparar m/c/a como un nombre
    */
    $config = array(
        "name" => array(
           "type"  => "rewrite",
           "match" => "/user-list/:a/:id", //coincidir solo /user-list/*
           "route" => array(
               'controller' => "user",   //ruta a user controller,
               'action'     => ":a",     //ruta a acción :a
           ),
        ),
    );
    Yaf_Dispatcher::getInstance()->getRouter()->addConfig(
        new Yaf_Config_Simple($config));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    /* para http://yourdomain.com/user-list/list/22
     * la ruta resultará en los siguientes valores:
     */
    array(
      "controller" => "user",
      "action"     => "list",
      "module"     => "index", //(default)
    )

    /**
     * y los parámetros de petición:
     */
    array(
      "id"   => 22,
    )

## Véase también

Yaf_Router::addRoute

Yaf_Router::addConfig

Yaf_Route_Static

Yaf_Route_Supervar

Yaf_Route_Simple

Yaf_Route_Regex

Yaf_Route_Map
