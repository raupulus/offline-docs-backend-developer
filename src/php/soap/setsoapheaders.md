---
title: SoapClient::__setSoapHeaders
description: Añade un encabezado SOAP para las peticiones siguientes
source_url: https://www.php.net/manual/es/soapclient.setsoapheaders.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/soapclient/setsoapheaders.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_reviewed: true
translation_revision: fe4e8b87d
order: 75240
---

SoapClient::\_\_setSoapHeaders

Añade un encabezado SOAP para las peticiones siguientes

## Descripción

```php
public SoapClient::__setSoapHeaders([SoapHeader $headers]): bool
```php

Establece un encabezado a utilizar en las peticiones SOAP.

> [!NOTE]
> Este método va a sobrescribir el valor anterior.

## Parámetros

`headers`  
El encabezado a configurar. Puede ser un objeto `SoapHeader` o un array de objetos `SoapHeader`. Si este argumento no es especificado o definido a `null`, los encabezados serán eliminados.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `SoapClient::__setSoapHeaders`

```
<?php

$client = new SoapClient(null, array('location' => "http://localhost/soap.php",
                                     'uri'      => "http://test-uri/"));
$header = new SoapHeader('http://soapinterop.org/echoheader/',
                            'echoMeStringRequest',
                            'hello world');

$client->__setSoapHeaders($header);

$client->__soapCall("echoVoid", null);
?>

    
```php

Configuración de múltiples encabezados para SOAP

```
<?php

$client = new SoapClient(null, array('location' => "http://localhost/soap.php",
                                     'uri'      => "http://test-uri/"));
$headers = array();

$headers[] = new SoapHeader('http://soapinterop.org/echoheader/',
                            'echoMeStringRequest',
                            'hello world');

$headers[] = new SoapHeader('http://soapinterop.org/echoheader/',
                            'echoMeStringRequest',
                            'hello world again');

$client->__setSoapHeaders($headers);

$client->__soapCall("echoVoid", null);
?>

      
```php
