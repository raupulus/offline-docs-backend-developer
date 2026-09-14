---
title: SoapServer::addFunction
description: Añade una o varias funciones que gestionarán las peticiones SOAP
source_url: https://www.php.net/manual/es/soapserver.addfunction.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/soapserver/addfunction.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_reviewed: false
translation_revision: 577239f64
order: 75340
---

SoapServer::addFunction

Añade una o varias funciones que gestionarán las peticiones SOAP

## Descripción

```php
public SoapServer::addFunction(array $functions): void
```php

Exporta una o varias funciones para los clientes remotos.

## Parámetros

`functions`  
Para exportar una sola función, debe pasarse su nombre en este argumento como string.

Para exportar varias funciones, debe utilizarse un array de nombres de funciones.

Para exportar todas las funciones, debe pasarse un array de nombres de funciones.

A partir de PHP 8.4.0, pasar un valor `int` (incluyendo `SOAP_FUNCTIONS_ALL`) está obsoleto. Utilice `get_defined_functions` para recuperar todas las funciones y páselas como un array.

> [!NOTE]
> `functions` debe recibir todos los argumentos de entrada en el mismo orden que el definido en el fichero WSDL (no debe recibir ningún parámetro de salida como argumento) y devuelve uno o varios valores. Para devolver varios valores, debe devolver un array que contenga los nombres de los parámetros de salida.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Pasar un `int` a SoapServer::addFunction, incluyendo `SOAP_FUNCTIONS_ALL`, ha sido declarado obsoleto. |

## Ejemplos

Ejemplo con `SoapServer::addFunction`

```
<?php

function echoString($inputString)
{
    return $inputString;
}

$server->addFunction("echoString");

function echoTwoStrings($inputString1, $inputString2)
{
    return array("outputString1" => $inputString1,
                 "outputString2" => $inputString2);
}
$server->addFunction(array("echoString", "echoTwoStrings"));

$functions = array_merge(...get_defined_functions());
$server->addFunction($functions);

?>

    
```php

## Véase también

SoapServer::\_\_construct, SoapServer::setClass
