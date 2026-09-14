---
title: SoapClient::__setLocation
description: Configura la URL del servicio web a utilizar
source_url: https://www.php.net/manual/es/soapclient.setlocation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/soapclient/setlocation.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_reviewed: false
translation_revision: fe4e8b87d
order: 75230
---

SoapClient::\_\_setLocation

Configura la URL del servicio web a utilizar

## Descripción

```php
public SoapClient::__setLocation([string $location]): string
```php

Configura la URL destino a la cual serán enviadas las peticiones SOAP. Esto equivale a especificar la opción `location` durante la construcción del cliente `SoapClient`.

> [!NOTE]
> Este método es opcional. `SoapClient` utiliza la URL indicada en el archivo WDSL por defecto.

## Parámetros

`location`  
La nueva URL.

## Valores devueltos

La URL anterior.

## Historial de cambios

| Versión | Descripción                   |
|---------|-------------------------------|
| 8.0.3   | `location` ahora es nullable. |

## Ejemplos

Ejemplo con `SoapClient::__setLocation`

```
<?php
$client = new SoapClient('http://example.com/webservice.php?wsdl');

$client->__setLocation('http://www.somethirdparty.com');

$old_location = $client->__setLocation(); // desactiva la opción de ubicación

echo $old_location;

?>

    
```php

Resultado del ejemplo anterior es similar a:

    http://www.somethirdparty.com

## Véase también

SoapClient::\_\_construct
