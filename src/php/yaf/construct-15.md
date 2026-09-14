---
title: Yaf_Route_Simple::__construct
description: El constructor de la clase Yaf_Route_Simple
source_url: https://www.php.net/manual/es/yaf-route-simple.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_route_simple/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: ecaa21464
order: 106840
---

Yaf_Route_Simple::\_\_construct

El constructor de la clase Yaf_Route_Simple

## Descripción

```php
public Yaf_Route_Simple::__construct(string $module_name, string $controller_name, string $action_name)
```php

`Yaf_Route_Simple` obtendrá la información de la ruta desde una cadena de consulta. Los parámetros de este constructor se usarán como claves mientras se busca la información de la ruta en \$\_GET.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`module_name`  
El nombre de la clave de la información del módulo.

`controller_name`  
El nombre de la clave de la información del controlador.

`action_name`  
El nombre de la clave de la información de la acción.

## Valores devueltos

Siempre devuelve `true`.

## Ejemplos

Ejemplo de `Yaf_Route_Simple::route`

```
<?php
   $route = new Yaf_Route_Simple("m", "controller", "act");
   Yaf_Router::getInstance()->addRoute("simple", $route);
?>

   
```php

Ejemplo de `Yaf_Route_Simple::route`

```
Request: http://yourdomain.com/path/?controller=a&act=b
=> module = default(index), controller = a, action = b

Request: http://yourdomain.com/path
=> module = default(index), controller = default(index), action = default(index)

   
```php

## Véase también

Yaf_Route_Supervar::route

Yaf_Route_Static::route

Yaf_Route_Regex::route

Yaf_Route_Rewrite::route

Yaf_Route_Map::route
