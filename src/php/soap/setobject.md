---
title: SoapServer::setObject
description: Configura el objeto que será utilizado para gestionar las peticiones
  SOAP
source_url: https://www.php.net/manual/es/soapserver.setobject.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/soapserver/setobject.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_reviewed: false
translation_revision: fe4e8b87d
order: 75420
---

SoapServer::setObject

Configura el objeto que será utilizado para gestionar las peticiones SOAP

## Descripción

```php
public SoapServer::setObject(object $object): void
```php

`SoapServer::setObject` configura un objeto que servirá como gestor de las peticiones SOAP, en lugar de una simple clase, como con `SoapServer::setClass`.

## Parámetros

`object`  
El objeto que gestionará las peticiones.

## Valores devueltos

No se retorna ningún valor.

## Véase también

SoapServer::setClass
