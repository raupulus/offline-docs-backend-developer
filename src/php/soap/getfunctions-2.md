---
title: SoapServer::getFunctions
description: Devuelve la lista de funciones definidas
source_url: https://www.php.net/manual/es/soapserver.getfunctions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/soapserver/getfunctions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_reviewed: false
translation_revision: fe4e8b87d
order: 75380
---

SoapServer::getFunctions

Devuelve la lista de funciones definidas

## Descripción

```php
public SoapServer::getFunctions(): array
```php

`SoapServer::getFunctions` devuelve la lista de todas las funciones añadidas al objeto servidor `SoapServer`. Devuelve la lista de todas las funciones añadidas mediante los métodos `SoapServer::addFunction` y `SoapServer::setClass`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un `array` de todas las funciones.

## Ejemplos

Ejemplo con `SoapServer::getFunctions`

```
<?php
$server = new SoapServer(NULL, array("uri" => "http://test-uri"));
$server->addFunction(SOAP_FUNCTIONS_ALL);
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $server->handle();
} else {
  echo "Este servidor SOAP puede gestionar las siguientes funciones: ";
  $functions = $server->getFunctions();
  foreach($functions as $func) {
    echo $func . "\n";
  }
}
?>

    
```php

## Véase también

SoapServer::\_\_construct, SoapServer::addFunction, SoapServer::setClass
