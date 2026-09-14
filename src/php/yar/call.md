---
title: Yar_Client::__call
description: Llamar a un servicio
source_url: https://www.php.net/manual/es/yar-client.call.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yar/yar_client/call.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yar
translation_status: ready
translation_reviewed: false
translation_revision: 914b97130
order: 107620
---

Yar_Client::\_\_call

Llamar a un servicio

## Descripción

```php
public Yar_Client::__call(string $method, array $parameters): void
```php

Emite una llamada a un método RPC remoto.

## Parámetros

`method`  
Nombre del método RPC remoto.

`parameters`  
Parámetros.

## Valores devueltos

## Ejemplos

Ejemplo de `Yar_Client::__call`

```
<?php

$cliente = new Yar_Client("http://host/api/");

/* llamar al servicio remoto */
$resultado = $cliente->some_method("parameter");
?>

   
```php

Resultado del ejemplo anterior es similar a:

## Véase también

Yar_Client::setOpt
