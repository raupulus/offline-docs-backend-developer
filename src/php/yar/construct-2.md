---
title: Yar_Server::__construct
description: Registrar un servidor
source_url: https://www.php.net/manual/es/yar-server.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yar/yar_server/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yar
translation_status: ready
translation_reviewed: false
translation_revision: 914b97130
order: 107690
---

Yar_Server::\_\_construct

Registrar un servidor

## Descripción

```php
final public Yar_Server::__construct(Object $obj)
```php

Configurar un Servidor Yar HTTP RPC. Todos los métodos públicos de \$obj serán registrados como un servicio RPC.

## Parámetros

`obj`  
Un objeto, todos sus métodos publicos serán registrados como servicioes RPC.

## Valores devueltos

Una instancia de `Yar_Server`.

## Ejemplos

Ejemplo de `Yar_Server::__construct`

```
<?php
class API {
    /**
     * the doc info will be generated automatically into service info page.
     * @params
     * @return
     */
    public function some_method($parameter, $option = "foo") {
         return "some_method";
    }

    protected function client_can_not_see() {
    }
}

$service = new Yar_Server(new API());
$service->handle();
?>

   
```php

Resultado del ejemplo anterior es similar a:

## Véase también

Yar_Server::handle
