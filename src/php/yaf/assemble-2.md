---
title: Yaf_Route_Map::assemble
description: Ensamblar un URL
source_url: https://www.php.net/manual/es/yaf-route-map.assemble.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_route_map/assemble.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: c9389e4a0
order: 106740
---

Yaf_Route_Map::assemble

Ensamblar un URL

## Descripción

```php
public Yaf_Route_Map::assemble(array $info, [array $query]): string
```php

Ensamblar un URL.

## Parámetros

`info`  

`query`  

## Valores devueltos

Devuelve `string` en caso de éxito o `null` en caso de fallo.

## Errores/Excepciones

Puede lanzar `Yaf_Exception_TypeError`.

## Ejemplos

Ejemplo de `Yaf_Route_Map::assemble`

```
<?php

$router = new Yaf_Router();

$route  = new Yaf_Route_Map();

$router->addRoute("map", $route);

var_dump($router->getRoute('map')->assemble(
                        array(
                                ':c' => 'foo_bar'
                        ),
                        array(
                                'tkey1' => 'tval1',
                                'tkey2' => 'tval2'
                        )
                   )
);

$route = new Yaf_Route_Map(true, '_');
$router->addRoute("map", $route);

var_dump($router->getRoute('map')->assemble(
                        array(
                                ':a' => 'foo_bar'
                        ),
                        array(
                                'tkey1' => 'tval1',
                                'tkey2' => 'tval2'
                        )
                   )
);

   
```php

Resultado del ejemplo anterior es similar a:

    string(%d) "/foo/bar?tkey1=tval1&tkey2=tval2"
    string(%d) "/foo/bar/_/tkey1/tval1/tkey2/tval2"
