---
title: Yar_Client::setOpt
description: Establecer los contextos de una llamada
source_url: https://www.php.net/manual/es/yar-client.setopt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yar/yar_client/setopt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yar
translation_status: ready
translation_revision: fade73b9e
order: 107640
---

Yar_Client::setOpt

Establecer los contextos de una llamada

## Descripción

```php
public Yar_Client::setOpt(int $name, mixed $value): Yar_Client
```php

## Parámetros

`name`  
El nombre puede ser: `YAR_OPT_PACKAGER`, `YAR_OPT_PERSISTENT` (Necesita soporte en el servidor), `YAR_OPT_TIMEOUT`, `YAR_OPT_CONNECT_TIMEOUT`, `YAR_OPT_HEADER` (desde 2.0.4), `YAR_OPT_PROXY` (desde 2.2.0)

`value`  

## Valores devueltos

Devuelve `$this` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `Yar_Client::setOpt`

```
<?php

$cliente = new Yar_Client("http://host/api/");

//Establecer el tiempo de espera a 1s
$cliente->SetOpt(YAR_OPT_CONNECT_TIMEOUT, 1000);

//Establecer el empaquetador a JSON
$cliente->SetOpt(YAR_OPT_PACKAGER, "json");

//Establecer cabeceras personalizadas
$client->SetOpt(YAR_OPT_HEADER, array("hr1: val1", "hd2: val2"));

// Establecer Http Proxy
$client->SetOpt(YAR_OPT_PROXY, "127.0.0.1:8888");

/* llamar al servicio remoto */
$result = $cliente->some_method("parameter");
?>

   
```php

Resultado del ejemplo anterior es similar a:

## Véase también

Yar_Client::\_\_call
