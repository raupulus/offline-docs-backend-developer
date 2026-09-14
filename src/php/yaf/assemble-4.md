---
title: Yaf_Route_Rewrite::assemble
description: Ensamblar un URL
source_url: https://www.php.net/manual/es/yaf-route-rewrite.assemble.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_route_rewrite/assemble.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 8e2cfbdce
order: 106800
---

Yaf_Route_Rewrite::assemble

Ensamblar un URL

## Descripción

```php
public Yaf_Route_Rewrite::assemble(array $info, [array $query]): string
```php

Ensamblar un URL.

## Parámetros

`info`  

`query`  

## Valores devueltos

Devuelve `string`.

## Ejemplos

Ejemplo de `Yaf_Route_Rewrite::assemble`

```
$router = new Yaf_Router();

$route  = new Yaf_Route_Rewrite(
                "/product/:name/:id/*",
                array(
                        'controller' => "product",
                ),
                array()
);

$router->addRoute("rewrite", $route);

var_dump($router->getRoute('rewrite')->assemble(
                        array(
                                ':name' => 'foo',
                                ':id' => 'bar',
                                ':tmpkey1' => 'tmpval1'
                        ),
                        array(
                                'tkey1' => 'tval1',
                                'tkey2' => 'tval2'
                             )
                        )
);

   
```php

Resultado del ejemplo anterior es similar a:

    string(57) "/product/foo/bar/tmpkey1/tmpval1/?tkey1=tval1&tkey2=tval2"
