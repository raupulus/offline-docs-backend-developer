---
title: SoapClient::__doRequest
description: Ejecuta una solicitud SOAP
source_url: https://www.php.net/manual/es/soapclient.dorequest.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/soapclient/dorequest.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_reviewed: false
translation_revision: 9a8c593c0
order: 75140
---

SoapClient::\_\_doRequest

Ejecuta una solicitud SOAP

## Descripción

```php
public SoapClient::__doRequest(string $request, string $location, string $action, int $version, [bool $oneWay], [string $uriParserClass]): string
```php

Ejecuta una solicitud SOAP.

Este método puede ser sobrescrito en las subclases para implementar diferentes transportes, realizar operaciones XML adicionales o cualquier otra cosa.

## Parámetros

`request`  
La solicitud SOAP en XML.

`location`  
La URL de la solicitud.

`action`  
La acción SOAP.

`version`  
La versión SOAP.

`oneWay`  
Si `oneWay` toma el valor de `true`, este método no devuelve nada. Utilice este valor cuando no se espera una respuesta.

`uriParserClass`  
El nombre de la clase a utilizar para analizar la URI de redirección cuando se recibe una cabecera `"Location"` en la respuesta, o `null` para utilizar el análisis por omisión basado en `parse_url`.

## Valores devueltos

La respuesta SOAP en XML.

## Historial de cambios

| Versión | Descripción                                                   |
|---------|---------------------------------------------------------------|
| 8.5.0   | Se ha añadido el parámetro opcional `uriParserClass`.         |
| 8.0.0   | El tipo de `oneWay` es `bool` ahora; anteriormente era `int`. |

## Ejemplos

Ejemplo con `SoapClient::__doRequest`

```
<?php

function Add($x, $y)
{
    return $x + $y;
}

class LocalSoapClient extends SoapClient
{
     private $server;

     public function __construct($wsdl, $options)
     {
         parent::__construct($wsdl, $options);
         $this->server = new SoapServer($wsdl, $options);
         $this->server->addFunction('Add');
     }

     public function __doRequest(
        $request,
        $location,
        $action,
        $version,
        $one_way = false,
     ): ?string {
         ob_start();
         $this->server->handle($request);
         $response = ob_get_contents();
         ob_end_clean();

         return $response;
     }

}

$x = new LocalSoapClient(
    null,
    [
        'location' => 'test://',
        'uri' => 'http://testuri.org',
    ]
);

var_dump($x->Add(3, 4));

?>

    
```php
