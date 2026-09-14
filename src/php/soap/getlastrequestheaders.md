---
title: SoapClient::__getLastRequestHeaders
description: Devuelve los encabezados de la última petición SOAP
source_url: https://www.php.net/manual/es/soapclient.getlastrequestheaders.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/soapclient/getlastrequestheaders.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_reviewed: false
translation_revision: fe4e8b87d
order: 75180
---

SoapClient::\_\_getLastRequestHeaders

Devuelve los encabezados de la última petición SOAP

## Descripción

```php
public SoapClient::__getLastRequestHeaders(): string
```php

Devuelve los encabezados de la última petición SOAP

> [!NOTE]
> Esta función solo está disponible si el objeto `SoapClient` ha sido creado con la opción `trace` a `true`

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Los últimos encabezados SOAP.

## Ejemplos

Ejemplo de SoapClient::\_\_getLastRequestHeaders()

```
<?php
$client = new SoapClient("some.wsdl", array('trace' => 1));
$result = $client->SomeFunction();
echo "REQUEST HEADERS:\n" . $client->__getLastRequestHeaders() . "\n";
?>

    
```php

## Véase también

SoapClient::\_\_getLastResponseHeaders, SoapClient::\_\_getLastRequest, SoapClient::\_\_getLastResponse
