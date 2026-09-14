---
title: SoapClient::__getFunctions
description: Retorna una lista de funciones SOAP publicadas
source_url: https://www.php.net/manual/es/soapclient.getfunctions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/soapclient/getfunctions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_reviewed: false
translation_revision: fe4e8b87d
order: 75160
---

SoapClient::\_\_getFunctions

Retorna una lista de funciones SOAP publicadas

## Descripción

```php
public SoapClient::__getFunctions(): array
```php

`SoapClient::__getFunctions` retorna un array de funciones SOAP publicadas descritas en el WSDL.

> [!NOTE]
> Esta función solo está disponible en modo WSDL.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El `array` de funciones SOAP con el tipo de retorno, el nombre de la función y los tipos de los argumentos que acepta.

## Ejemplos

Ejemplo con `SoapClient::__getFunctions`

```
<?php
$client = new SoapClient('http://soap.amazon.com/schemas3/AmazonWebServices.wsdl');
var_dump($client->__getFunctions());
?>

    
```php

El ejemplo anterior mostrará:

    array(26) {
      [0]=>
      string(70) "ProductInfo KeywordSearchRequest(KeywordRequest $KeywordSearchRequest)"
      [1]=>
      string(79) "ProductInfo TextStreamSearchRequest(TextStreamRequest $TextStreamSearchRequest)"
      [2]=>
      string(64) "ProductInfo PowerSearchRequest(PowerRequest $PowerSearchRequest)"
    ...
      [23]=>
      string(107) "ShoppingCart RemoveShoppingCartItemsRequest(RemoveShoppingCartItemsRequest $RemoveShoppingCartItemsRequest)"
      [24]=>
      string(107) "ShoppingCart ModifyShoppingCartItemsRequest(ModifyShoppingCartItemsRequest $ModifyShoppingCartItemsRequest)"
      [25]=>
      string(118) "GetTransactionDetailsResponse GetTransactionDetailsRequest(GetTransactionDetailsRequest $GetTransactionDetailsRequest)"
    }

## Véase también

SoapClient::\_\_construct
