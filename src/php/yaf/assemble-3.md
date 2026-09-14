---
title: Yaf_Route_Regex::assemble
description: Ensamblar un URL
source_url: https://www.php.net/manual/es/yaf-route-regex.assemble.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_route_regex/assemble.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: c9389e4a0
order: 106770
---

Yaf_Route_Regex::assemble

Ensamblar un URL

## Descripción

```php
public Yaf_Route_Regex::assemble(array $info, [array $query]): string
```php

Ensamblar un URL

## Parámetros

`info`  

`query`  

## Valores devueltos

Devuelve `string` en caso de éxito o `null` en caso de fallo.

## Ejemplos

Ejemplo de `Yaf_Route_Regex::assemble`

```
<?php

$router = new Yaf_Router();

$route  = new Yaf_Route_Regex(
            "#^/product/([^/]+)/([^/])+#",
            array(
                'controller' => "product",  //route to product controller,
                ),
            array(),
            array(),
            '/:m/:c/:a'
        );

$router->addRoute("regex", $route);

var_dump($router->getRoute('regex')->assemble(
            array(
                ':m' => 'module',
                ':c' => 'controller',
                ':a' => 'action'
                ),
            array(
                'tkey1' => 'tval1',
                'tkey2' =>
                'tval2'
                )
            )
        );

   
```php

Resultado del ejemplo anterior es similar a:

    string(49) "/module/controller/action?tkey1=tval1&tkey2=tval2"
