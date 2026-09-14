---
title: Yar_Server::handle
description: Iniciar un servidor RPC
source_url: https://www.php.net/manual/es/yar-server.handle.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yar/yar_server/handle.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yar
translation_status: ready
translation_reviewed: false
translation_revision: 331fbfeac
order: 107700
---

Yar_Server::handle

Iniciar un servidor RPC

## Descripción

```php
public Yar_Server::handle(): bool
```php

Inicia un servidor de HTTP de RPC listo para aceptar peticiones RPC.

> [!NOTE]
> Las llamadas RPC usuales serán emitidas como peticiones POST de HTTP. Si se emite una petición GET de HTTP al URI, se imprimierá en la página la información del servicio (la sección comentada anteriormente).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

boolean

## Ejemplos

Ejemplo de `Yar_Server::handle`

```
<?php
class API {
    /**
     * the doc info will be generated automatically into service info page.
     * @params
     * @return
     */
    public function some_method($parameter, $option = "foo") {
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

Yar_Server::\_\_construct
