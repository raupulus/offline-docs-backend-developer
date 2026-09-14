---
title: SoapServer::fault
description: Emitir un error SoapServer
source_url: https://www.php.net/manual/es/soapserver.fault.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/soapserver/fault.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_reviewed: false
translation_revision: 9a8c593c0
order: 75370
---

SoapServer::fault

Emitir un error

SoapServer

## Descripción

```php
public SoapServer::fault(string $code, string $string, [string $actor], [mixed $details], [string $name], [string $lang]): void
```php

Envía una respuesta al cliente de la petición actual, con un mensaje de error.

> [!NOTE]
> Esto solo es posible durante la ejecución de la petición.

## Parámetros

`code`  
El código de error a devolver.

`string`  
Una descripción del error.

`actor`  
Una cadena que identifica al actor involucrado.

`details`  
Más detalles sobre el fallo.

`name`  
El nombre del error. Esto puede ser utilizado para seleccionar un nombre en un archivo WSDL.

`lang`  
El idioma humano en el que está escrito el SoapFault. Solo se utiliza para SOAP versión 1.2.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Se ha añadido el parámetro opcional `lang` para cumplir con la especificación SOAP 1.2. |

## Véase también

SoapFault::\_\_construct
