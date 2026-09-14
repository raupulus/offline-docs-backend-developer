---
title: SoapServer::handle
description: Procesa una solicitud SOAP
source_url: https://www.php.net/manual/es/soapserver.handle.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/soapserver/handle.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_reviewed: false
translation_revision: fe4e8b87d
order: 75400
---

SoapServer::handle

Procesa una solicitud SOAP

## Descripción

```php
public SoapServer::handle([string $request]): void
```php

Realiza una solicitud SOAP, llama a las funciones necesarias y envía una respuesta en retorno.

## Parámetros

`request`  
La solicitud SOAP. Si este argumento es omitido, se asume que la solicitud se encuentra en los datos POST sin tratar de la petición HTTP.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción                  |
|---------|------------------------------|
| 8.0.0   | `request` ahora es nullable. |

## Ejemplos

Ejemplo con `SoapServer::handle`

```
<?php
function test($x)
{
    return $x;
}

$server = new SoapServer(null, array('uri' => "http://test-uri/"));
$server->addFunction("test");
$server->handle();
?>

    
```php

## Véase también

SoapServer::\_\_construct
