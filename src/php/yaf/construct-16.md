---
title: Yaf_Route_Supervar::__construct
description: El propósito de __construct
source_url: https://www.php.net/manual/es/yaf-route-supervar.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_route_supervar/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: b37bddfde
order: 106900
---

Yaf_Route_Supervar::\_\_construct

El propósito de \_\_construct

## Descripción

```php
public Yaf_Route_Supervar::__construct(string $supervar_name)
```php

`Yaf_Route_Supervar` es similar a `Yaf_Route_Static`, con la diferencia de que `Yaf_Route_Supervar` buscará información de ruta en la cadena de consulta, y el parámetro `supervar_name` es la clave.

## Parámetros

`supervar_name`  
El nombre de la clave

## Valores devueltos

## Ejemplos

Ejemplo de `Yaf_Route_Supervar`

```
<?php
   /**
    * Añadir una ruta supervar a la pila de rutas de Yaf_Router
    */
    Yaf_Dispatcher::getInstance()->getRouter()->addRoute(
        "name",
        new Yaf_Route_Supervar("r")
    );
?>

   
```php

Resultado del ejemplo anterior es similar a:

    /** para la petición: http://yourdomain.com/xx/oo/?r=/ctr/act/var/value
      * resultará en lo siguiente:
      */
      array (
        "module"   => index(default),
        "controller" => ctr,
        "action"     => act,
        "params"     => array(
              "var" => value,
         )
      )

## Véase también

Yaf_Router::addRoute

Yaf_Router::addConfig

Yaf_Route_Static

Yaf_Route_Regex

Yaf_Route_Simple

Yaf_Route_Rewrite

Yaf_Route_Map
