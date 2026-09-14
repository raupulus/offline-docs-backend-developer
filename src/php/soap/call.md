---
title: SoapClient::__call
description: Llamada a una función SOAP (obsoleta)
source_url: https://www.php.net/manual/es/soapclient.call.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/soapclient/call.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_reviewed: true
translation_revision: fe4e8b87d
order: 75120
---

SoapClient::\_\_call

Llamada a una función SOAP (obsoleta)

## Descripción

```php
public SoapClient::__call(string $name, array $args): mixed
```php

La llamada directa a este método es obsoleta. Normalmente, las funciones SOAP pueden ser llamadas como métodos del objeto `SoapClient`; en los casos donde esto no es posible, o bien es necesario pasar más opciones, utilícese el método SoapClient::\_\_soapCall.

## Parámetros

`name`  
El nombre de la función SOAP a llamar.

`args`  
Un array de argumentos a pasar a la función. Esto puede ser un array ordenado o un array asociativo. Tenga en cuenta que la mayoría de servidores SOAP exigen que los nombres de los parámetros sean proporcionados, en cuyo caso debe ser un array asociativo.

## Valores devueltos

Las funciones SOAP pueden devolver uno o varios valores. Si solo un valor es devuelto por la función SOAP, el valor de retorno será un escalar. Si varios valores son devueltos, se devuelve un array asociativo de parámetros de salida nombrados en su lugar.

En caso de error, si el objeto `SoapClient` ha sido construido con la opción `exceptions` definida como `false`, se devolverá un objeto `SoapFault`.
