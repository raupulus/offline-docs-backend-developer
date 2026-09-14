---
title: SoapClient::__soapCall
description: Realiza una llamada SOAP
source_url: https://www.php.net/manual/es/soapclient.soapcall.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/soapclient/soapcall.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_reviewed: false
translation_revision: fe4e8b87d
order: 75250
---

SoapClient::\_\_soapCall

Realiza una llamada SOAP

## Descripción

```php
public SoapClient::__soapCall(string $name, array $args, [array $options], [SoapHeader $inputHeaders], [array $outputHeaders]): mixed
```php

Esta es una función de bajo nivel de la API que se utiliza para realizar llamadas SOAP. Normalmente, en modo WSDL, se pueden llamar simplemente las funciones SOAP como métodos de `SoapClient`. Este método es útil en modo no-WSDL cuando `soapaction` es desconocido, `uri` es diferente del valor por omisión o al enviar y/o recibir encabezados SOAP.

En caso de error, una llamada a una función SOAP puede causar el lanzamiento de una excepción por PHP o devolver un objeto `SoapFault` si las excepciones están desactivadas. Para verificar si la llamada a esta función no logra atrapar las excepciones `SoapFault`, verifique el resultado con la función `is_soap_fault`.

## Parámetros

`name`  
El nombre de la función SOAP a llamar.

`args`  
Un array de argumentos a pasar a la función. Esto puede ser un array asociativo u ordenado. Tenga en cuenta que la mayoría de los servidores SOAP requieren nombres de parámetros, en cuyo caso, debe ser un array asociativo.

`options`  
Un array asociativo de opciones a pasar al cliente.

Una opción de `location` para el servicio web remoto.

Una opción `uri` con el espacio de nombres objetivo del servicio SOAP.

La opción `soapaction` es la acción a llamar.

`inputHeaders`  
Un array de encabezados a enviar con la petición SOAP.

`outputHeaders`  
Si se proporciona, este array será llenado con los encabezados de la respuesta SOAP devuelta.

## Valores devueltos

Las funciones SOAP devuelven uno o varios valores. Si un solo valor es devuelto por la función SOAP, el valor devuelto de `__soapCall` será un valor simple (por ejemplo, un entero, un string, etc.). Si varios valores son devueltos, `__soapCall` devolverá un array asociativo que contiene los nombres de los parámetros mostrados.

En caso de error, si el objeto `SoapClient` fue construido con la opción `exceptions` que valía `false`, un objeto `SoapFault` será devuelto.

## Ejemplos

Ejemplo con `SoapClient::__soapCall`

```
<?php

$client = new SoapClient("some.wsdl");
$client->SomeFunction($a, $b, $c);

$client->__soapCall("SomeFunction", array($a, $b, $c));
$client->__soapCall("SomeFunction", array($a, $b, $c), NULL,
                    new SoapHeader(), $output_headers);

$client = new SoapClient(null, array('location' => "http://localhost/soap.php",
                                     'uri'      => "http://test-uri/"));
$client->SomeFunction($a, $b, $c);
$client->__soapCall("SomeFunction", array($a, $b, $c));
$client->__soapCall("SomeFunction", array($a, $b, $c),
                    array('soapaction' => 'some_action',
                          'uri'        => 'some_uri'));
?>

    
```php

## Véase también

SoapClient::\_\_construct, SoapParam::\_\_construct, SoapVar::\_\_construct, SoapHeader::\_\_construct, SoapFault::\_\_construct, `is_soap_fault`
