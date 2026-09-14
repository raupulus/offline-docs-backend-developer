---
title: SoapServer::__construct
description: Constructor de SoapServer
source_url: https://www.php.net/manual/es/soapserver.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/soapserver/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_reviewed: false
translation_revision: fe4e8b87d
order: 75360
---

SoapServer::\_\_construct

Constructor de SoapServer

## Descripción

```php
public SoapServer::__construct(string $wsdl, [array $options])
```php

Este constructor permite la creación de objetos `SoapServer` en modo WSDL o no-WSDL.

## Parámetros

`wsdl`  
Para utilizar el modo WSDL, debe definirse la URI del fichero WSDL en este argumento. En otras situaciones, debe definirse este argumento a `null` y definirse la opción `uri`.

`options`  
Permite definir una versión SOAP por omisión (`soap_version`), un juego de caracteres de codificación interna (`encoding`) y una URI actor (`actor`).

La opción `classmap` puede ser utilizada para ligar algunos tipos WSDL a clases PHP. Esta opción debe ser un array con los tipos WSDL como claves y los nombres de las clases PHP como valores.

La opción `typemap` es un array cuyas claves son `type_name`, `type_ns` (URI del espacio de nombres), `from_xml` (función de retrollamada aceptando un argumento de tipo `string`) y `to_xml` (función de retrollamada aceptando un argumento de tipo `object`).

La opción `cache_wsdl` puede tomar uno de los valores `WSDL_CACHE_NONE`, `WSDL_CACHE_DISK`, `WSDL_CACHE_MEMORY` o `WSDL_CACHE_BOTH`.

La última opción es `features` que puede ser definida a `SOAP_WAIT_ONE_WAY_CALLS`, `SOAP_SINGLE_ELEMENT_ARRAYS`, `SOAP_USE_XSI_ARRAY_TYPE`.

La opción `send_errors` puede ser definida a `false` para enviar un mensaje de error genérico ("Internal error") en lugar del mensaje de error específico.

## Ejemplos

Ejemplos con `SoapServer::__construct`

```
<?php
$server = new SoapServer("some.wsdl");

$server = new SoapServer("some.wsdl", array('soap_version' => SOAP_1_2));

$server = new SoapServer("some.wsdl", array('actor' => "http://example.org/ts-tests/C"));

$server = new SoapServer("some.wsdl", array('encoding'=>'ISO-8859-1'));

$server = new SoapServer(null, array('uri' => "http://test-uri/"));

class MyBook {
    public $title;
    public $author;
}

$server = new SoapServer("books.wsdl", array('classmap' => array('book' => "MyBook")));

?>

    
```php

## Véase también

SoapClient::\_\_construct
