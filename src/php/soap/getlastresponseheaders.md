---
title: SoapClient::__getLastResponseHeaders
description: Retorna los encabezados de la última respuesta SOAP
source_url: https://www.php.net/manual/es/soapclient.getlastresponseheaders.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/soapclient/getlastresponseheaders.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_reviewed: false
translation_revision: fe4e8b87d
order: 75200
---

SoapClient::\_\_getLastResponseHeaders

Retorna los encabezados de la última respuesta SOAP

## Descripción

```php
public SoapClient::__getLastResponseHeaders(): string
```php

Retorna los encabezados de la última respuesta SOAP.

> [!NOTE]
> Esta función solo está disponible si el objeto `SoapClient` fue creado con la opción `trace` a `true`

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Los encabezados de la última respuesta SOAP.

## Ejemplos

Ejemplo con `SoapClient::__getLastResponseHeaders`

```
<?php
$client = new SoapClient("some.wsdl", array('trace' => 1));
$result = $client->SomeFunction();
echo "RESPONSE HEADERS:\n" . $client->__getLastResponseHeaders() . "\n";
?>

    
```php

## Véase también

SoapClient::\_\_getLastRequestHeaders, SoapClient::\_\_getLastRequest, SoapClient::\_\_getLastResponse
