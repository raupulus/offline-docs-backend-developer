---
title: SoapHeader::__construct
description: Constructor SoapHeader
source_url: https://www.php.net/manual/es/soapheader.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/soapheader/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_reviewed: false
translation_revision: fe4e8b87d
order: 75300
---

SoapHeader::\_\_construct

Constructor SoapHeader

## Descripción

```php
public SoapHeader::__construct(string $namespace, string $name, [mixed $data], [bool $mustunderstand], [string $actor])
```php

Construye un nuevo objeto `SoapHeader`.

## Parámetros

`namespace`  
El espacio de nombres del elemento de encabezado SOAP.

`name`  
El nombre del elemento de encabezado SOAP.

`data`  
Un contenido del encabezado SOAP. Puede ser un valor PHP o un objeto `SoapVar`.

`mustUnderstand`  
Valor del atributo `mustUnderstand` del elemento de encabezado SOAP.

`actor`  
Valor del atributo `actor` del elemento de encabezado SOAP.

## Ejemplos

Ejemplo con `SoapHeader::__construct`

```
<?php
$client = new SoapClient(null, array('location' => "http://localhost/soap.php",
                                     'uri'      => "http://test-uri/"));
$client->__soapCall("echoVoid", null, null,
                new SoapHeader('http://soapinterop.org/echoheader/',
                               'echoMeStringRequest',
                               'hello world'));
?>

    
```php

## Véase también

SoapClient::\_\_soapCall, SoapVar::\_\_construct, SoapParam::\_\_construct, SoapServer::addSoapHeader
