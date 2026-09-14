---
title: SoapClient::__getLastRequest
description: Devuelve la última petición SOAP
source_url: https://www.php.net/manual/es/soapclient.getlastrequest.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/soapclient/getlastrequest.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_reviewed: false
translation_revision: fe4e8b87d
order: 75170
---

SoapClient::\_\_getLastRequest

Devuelve la última petición SOAP

## Descripción

```php
public SoapClient::__getLastRequest(): string
```php

Devuelve el código XML de la última petición SOAP enviada.

> [!NOTE]
> Este método funciona únicamente si el objeto `SoapClient` ha sido creado con la opción `trace` configurada a `true`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La última petición SOAP, en forma de string de código XML.

## Ejemplos

Ejemplo con `SoapClient::__getLastRequest`

```
<?php
$client = new SoapClient("some.wsdl", array('trace' => 1));
$result = $client->SomeFunction();
echo "REQUEST:\n" . $client->__getLastRequest() . "\n";
?>

    
```php

## Véase también

SoapClient::\_\_getLastRequestHeaders, SoapClient::\_\_getLastResponse, SoapClient::\_\_getLastResponseHeaders
