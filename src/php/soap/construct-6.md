---
title: SoapVar::__construct
description: Constructor de SoapVar
source_url: https://www.php.net/manual/es/soapvar.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/soapvar/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_reviewed: false
translation_revision: fe4e8b87d
order: 75450
---

SoapVar::\_\_construct

Constructor de SoapVar

## Descripción

```php
public SoapVar::__construct(mixed $data, int $encoding, [string $typeName], [string $typeNamespace], [string $nodeName], [string $nodeNamespace])
```php

Construye un nuevo objeto `SoapVar`.

## Parámetros

`data`  
Los datos a pasar o a devolver.

`encoding`  
El ID de codificación, una de las constantes `XSD_...`.

`typeName`  
El nombre del tipo.

`typeNamespace`  
El tipo del espacio de nombres.

`nodeName`  
El nombre del nodo XML.

`nodeNamespace`  
El espacio de nombres del nodo XML.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.3 | `typeName`, `typeNamespace`, `nodeName`, y `nodeNamespace` ahora son nullable. |

## Ejemplos

Ejemplo con `SoapVar::__construct`

```
<?php
class SOAPStruct {
    function SOAPStruct($s, $i, $f)
    {
        $this->varString = $s;
        $this->varInt = $i;
        $this->varFloat = $f;
    }
}
$client = new SoapClient(null, array('location' => "http://localhost/soap.php",
                                     'uri'      => "http://test-uri/"));
$struct = new SOAPStruct('arg', 34, 325.325);
$soapstruct = new SoapVar($struct, SOAP_ENC_OBJECT, "SOAPStruct", "http://soapinterop.org/xsd");
$client->echoStruct(new SoapParam($soapstruct, "inputStruct"));
?>

    
```php

## Véase también

SoapClient::\_\_soapCall, SoapParam::\_\_construct
