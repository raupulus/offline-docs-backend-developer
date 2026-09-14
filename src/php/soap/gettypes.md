---
title: SoapClient::__getTypes
description: Devuelve una lista de tipos SOAP
source_url: https://www.php.net/manual/es/soapclient.gettypes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/soapclient/gettypes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_reviewed: true
translation_revision: fe4e8b87d
order: 75210
---

SoapClient::\_\_getTypes

Devuelve una lista de tipos SOAP

## Descripción

```php
public SoapClient::__getTypes(): array
```php

`SoapClient::__getTypes` devuelve la lista de tipos SOAP descritos en el archivo WSDL del servicio web actual.

> [!NOTE]
> Esta función solo está disponible en modo WSDL.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un `array` de tipos SOAP que detallan todas las estructuras y los tipos

## Ejemplos

Ejemplo con `SoapClient::__getTypes`

```
<?php
$client = new SoapClient("http://soap.amazon.com/schemas3/AmazonWebServices.wsdl");
var_dump($client->__getTypes());
?>

    
```php

El ejemplo anterior mostrará:

    array(88) {
      [0]=>
      string(30) "ProductLine ProductLineArray[]"
      [1]=>
      string(85) "struct ProductLine {
     string Mode;
     string RelevanceRank;
     ProductInfo ProductInfo;
    }"
      [2]=>
      string(105) "struct ProductInfo {
     string TotalResults;
     string TotalPages;
     string ListName;
     DetailsArray Details;
    }"
    ...
      [85]=>
      string(32) "ShortSummary ShortSummaryArray[]"
      [86]=>
      string(121) "struct GetTransactionDetailsRequest {
     string tag;
     string devtag;
     string key;
     OrderIdArray OrderIds;
     string locale;
    }"
      [87]=>
      string(75) "struct GetTransactionDetailsResponse {
     ShortSummaryArray ShortSummaries;
    }"
    }

## Véase también

SoapClient::\_\_construct
