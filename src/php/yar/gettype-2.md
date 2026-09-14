---
title: Yar_Server_Exception::getType
description: Recuperar el tipo de excepción
source_url: https://www.php.net/manual/es/yar-server-exception.gettype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yar/yar_server_exception/gettype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yar
translation_status: ready
translation_revision: 8cc7e649d
order: 107710
---

Yar_Server_Exception::getType

Recuperar el tipo de excepción

## Descripción

```php
public Yar_Server_Exception::getType(): string
```php

Obtener el tipo original de la excepción lanzada por el servidor

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

string

## Ejemplos

Ejemplo de `Yar_Server_Exception::getType`

```
//Server.php
<?php
class Custom_Exception extends Exception {};

class API {
    public function throw_exception($name) {
        throw new Custom_Exception($name);
    }
}

$service = new Yar_Server(new API());
$service->handle();
?>

//Client.php
<?php
$client = new Yar_Client("http://host/api.php");

try {
    $client->throw_exception("client");
} catch (Yar_Server_Exception $e) {
    var_dump($e->getType());
    var_dump($e->getMessage());
}

   
```php

Resultado del ejemplo anterior es similar a:

    string(16) "Custom_Exception"
    string(6) "client"

## Véase también
