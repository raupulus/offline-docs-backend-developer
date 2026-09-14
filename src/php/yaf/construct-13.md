---
title: Yaf_Route_Regex::__construct
description: Constructor de Yaf_Route_Regex
source_url: https://www.php.net/manual/es/yaf-route-regex.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_route_regex/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: e2f2172bf
order: 106780
---

Yaf_Route_Regex::\_\_construct

Constructor de Yaf_Route_Regex

## Descripción

```php
public Yaf_Route_Regex::__construct(string $match, array $route, [array $map], [array $verify], [string $reverse])
```php

## Parámetros

`match`  
Un patrón de expresión regular completo, se usará para comparar un URI solicitado, si no coincide, `Yaf_Route_Regex` devolverá `false`.

`route`  
Cuando el patrón de comparación coincida con el URI solicitado, `Yaf_Route_Regex` lo usará para decidir qué m/c/a enrutar.

m/c/a en este array son opcionales, si no se asigna un valor específico, será enrutada al valor predeterminado.

`map`  
Un array para asignar nombres a las capturas del resultado de comparación.

`verify`  

`reverse`  
una cadena, usado para ensamblar url, ver Yaf_Route_Regex::assemble.

> [!NOTE]
> este parametro se introdujo en 2.3.0

## Valores devueltos

## Ejemplos

Ejemplo de `Yaf_Route_Regex`

```
<?php
   /**
    * Añade una ruta de expresión regular a la pila de enrutamiento de Yaf_Router
    */
    Yaf_Dispatcher::getInstance()->getRouter()->addRoute("name",
        new Yaf_Route_Regex(
           "#^/product/([^/]+)/([^/])+#", //comparar los URI solicitados que empiecen por "/product"
           array(
               'controller' => "product",  //ruta al controlador product,
           ),
           array(
              1 => "name",   // ahora se puede llamar a $request->getParam("name")
              2 => "id",     // para obtener la primera captura del patrón de comparación.
           )
        )
    );
?>

   
```php

Ejemplo de `Yaf_Route_Regex`(como en 2.3.0)

```
<?php
   /**
    * Usar el resultado de la busqueda como nombre MVC
    */
    Yaf_Dispatcher::getInstance()->getRouter()->addRoute("name",
        new Yaf_Route_Regex(
           "#^/product/([^/]+)/([^/])+#i", //buscar primera peticion uri "/product"
           array(
              'controller' => ":name", // ruta a :name, el cual es $1 en el resultado de busqueda como nombre de controllador
           ),
           array(
              1 => "name",   // ahora puede llamar a $request->getParam("name")
              2 => "id",     // para obtener la primera coincidencia en el patron de busqueda.
           )
        )
    );
?>

   
```php

Ejemplo de `Yaf_Route_Regex` y el nombre de la zona de captura (a partir de 2.3.0)

```
<?php
   /**
    * Usar el resultado de la coincidencia como nombre del MVC
    */
    Yaf_Dispatcher::getInstance()->getRouter()->addRoute("name",
        new Yaf_Route_Regex(
           "#^/product/(?<name>[^/]+)/([^/])+#i", //solicitud de coincidencia uri leading "/product"
           array(
           'controller' => ":name", // ruta a :name,
                                    // que se denomina "nombre" del grupo de captura en el resultado de la coincidencia como nombre del controlador
           ),
           array(
              2 => "id",     // para obtener la primera captura en el patrón de coincidencia.
           )
        )
    );
?>

   
```php

Ejemplo de `Yaf_Route_Regex`

```
<?php
   /**
    * Add a regex route to Yaf_Router route stack by calling addconfig
    */
    $config = array(
        "name" => array(
           "type"  => "regex",          //ruta Yaf_Route_Regex
           "match" => "#(.*)#",         //comparar URIs solicitados arbitrarios
           "route" => array(
               'controller' => "product",  //ruta al controlador product,
               'action'     => "dummy",    //ruta a una acción sin sentido
           ),
           "map" => array(
              1 => "uri",   // ahora se puede llamar a $request->getParam("uri")
           ),
        ),
    );
    Yaf_Dispatcher::getInstance()->getRouter()->addConfig(
        new Yaf_Config_Simple($config));
?>

   
```php

## Véase también

Yaf_Router::addRoute

Yaf_Router::addConfig

Yaf_Route_Static

Yaf_Route_Supervar

Yaf_Route_Simple

Yaf_Route_Rewrite

Yaf_Route_Map
