---
title: SoapFault::__construct
description: Constructor de SoapFault
source_url: https://www.php.net/manual/es/soapfault.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/soapfault/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_reviewed: false
translation_revision: d9cfd78e5
order: 75270
---

SoapFault::\_\_construct

Constructor de SoapFault

## Descripción

```php
public SoapFault::__construct(array $code, string $string, [string $actor], [mixed $details], [string $name], [mixed $headerFault], [string $lang])
```php

`SoapFault` sirve para enviar errores SOAP desde PHP.`code`, `string`, `actor` y `details` son los elementos estándar SOAP.

## Parámetros

`code`  
El código de error de `SoapFault`.

`string`  
El mensaje de error de `SoapFault`.

`actor`  
Una cadena que identifica al actor que causó el error.

`details`  

`name`  
Puede ser utilizado para seleccionar la codificación adecuada desde WSDL.

`headerFault`  
Puede ser utilizado durante la gestión del encabezado SOAP para reportar un error en el encabezado de respuesta.

`lang`  
El idioma humano en el que está escrito el SoapFault. Solo se utiliza para SOAP versión 1.2.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Se ha añadido el parámetro opcional `lang` para cumplir con la especificación SOAP 1.2. |

## Ejemplos

Algunos ejemplos con `SoapFault`

```
<?php
function test($x)
{
    return new SoapFault("Server", "Un mensaje de error");
}

$server = new SoapServer(null, array('uri' => "http://test-uri/"));
$server->addFunction("test");
$server->handle();
?>

    
```php

Es posible utilizar el mecanismo de excepciones de PHP para lanzar excepciones `SoapFault`.

Emisión de excepciones `SoapFault`

```
<?php
function test($x)
{
    throw new SoapFault("Server", "Un mensaje de error");
}

$server = new SoapServer(null, array('uri' => "http://test-uri/"));
$server->addFunction("test");
$server->handle();
?>

    
```php

## Véase también

SoapServer::fault, `is_soap_fault`
