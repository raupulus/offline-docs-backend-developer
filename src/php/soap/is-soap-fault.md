---
title: is_soap_fault
description: Verifica si SOAP devuelve un error
source_url: https://www.php.net/manual/es/function.is-soap-fault.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/functions/is-soap-fault.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_reviewed: false
translation_revision: e64ea89bb
order: 75060
---

is_soap_fault

Verifica si SOAP devuelve un error

## Descripción

```php
is_soap_fault(mixed $objeto): bool
```php

`is_soap_fault` sirve para verificar si la API SOAP ha fallado, sin utilizar excepciones. Para usarla, se debe crear un objeto `SoapClient` con la opción `exceptions` configurada a cero o a `false`. En este caso, el método SOAP devolverá un objeto especial `SoapFault`, que encapsula los detalles del error (código de error, mensaje, actor y detalles).

Si `exceptions` no está configurada, SOAP emitirá una excepción. `is_soap_fault` verifica si el argumento proporcionado es un objeto `SoapFault`.

## Parámetros

`objeto`  
El objeto a probar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `is_soap_fault`

```
<?php
$client = new SoapClient("some.wsdl", array('exceptions' => 0));
$result = $client->SomeFunction();
if (is_soap_fault($result)) {
    trigger_error("SOAP Fault: (faultcode: {$result->faultcode}, faultstring: {$result->faultstring})", E_USER_ERROR);
}
?>

    
```php

Manejo de errores por excepción con SOAP

```
<?php
try {
    $client = new SoapClient("some.wsdl");
    $result = $client->SomeFunction(/* ... */);
} catch (SoapFault $fault) {
    trigger_error("SOAP Fault: (faultcode: {$fault->faultcode}, faultstring: {$fault->faultstring})", E_USER_ERROR);
}
?>

    
```php

## Véase también

SoapClient::\_\_construct, SoapFault::\_\_construct
