---
title: SoapClient::__getLastResponse
description: Devuelve la última respuesta SOAP
source_url: https://www.php.net/manual/es/soapclient.getlastresponse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/soapclient/getlastresponse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_reviewed: true
translation_revision: fe4e8b87d
order: 75190
---

SoapClient::\_\_getLastResponse

Devuelve la última respuesta SOAP

## Descripción

```php
public SoapClient::__getLastResponse(): string
```php

Devuelve el código XML de la última respuesta SOAP.

> [!NOTE]
> Esta función solo está disponible si el objeto `SoapClient` ha sido creado con la opción `trace` a `true`

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La última respuesta SOAP, en forma de string XML.

## Ejemplos

Ejemplo con `SoapClient::__getLastResponse`

```
<?php
$client = SoapClient("some.wsdl", array('trace' => 1));
$result = $client->SomeFunction();
echo "Response:\n" . $client->__getLastResponse() . "\n";
?>

    
```php

## Véase también

SoapClient::\_\_getLastResponseHeaders, SoapClient::\_\_getLastRequest, SoapClient::\_\_getLastRequestHeaders
