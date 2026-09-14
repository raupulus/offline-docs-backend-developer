---
title: SoapServer::__getLastResponse
description: Devuelve la última respuesta SOAP
source_url: https://www.php.net/manual/es/soapserver.getlastresponse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/soapserver/getlastresponse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_reviewed: true
translation_revision: 7e1f81cbb
order: 75390
---

SoapServer::\_\_getLastResponse

Devuelve la última respuesta SOAP

## Descripción

```php
public SoapServer::__getLastResponse(): string
```php

Devuelve el XML enviado en la última respuesta SOAP.

> [!NOTE]
> Este método solo funciona si el objeto `SoapServer` ha sido creado con la opción `trace` definida a `true`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La última respuesta SOAP, en forma de string XML.

## Ejemplos

Ejemplo de SoapServer::\_\_getLastResponse()

```
<?php
$server = new SoapServer("some.wsdl", ["trace" => 1]);
$server->handle();
echo "Response:\n" . $server->__getLastResponse() . "\n";
?>

   
```php
