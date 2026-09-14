---
title: SoapServer::setClass
description: Configura la clase que será utilizada para gestionar las peticiones SOAP
source_url: https://www.php.net/manual/es/soapserver.setclass.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/soapserver/setclass.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_reviewed: false
translation_revision: fe4e8b87d
order: 75410
---

SoapServer::setClass

Configura la clase que será utilizada para gestionar las peticiones SOAP

## Descripción

```php
public SoapServer::setClass(string $class, mixed ...$args): void
```php

Exporta todos los métodos de la clase especificada.

`SoapServer::setClass` configura una clase que servirá como gestor para las peticiones SOAP. El objeto podrá entonces ser mantenido persistente a través de las peticiones durante una sesión PHP, con el método `SoapServer::setPersistence`.

## Parámetros

`class`  
El nombre de la clase exportada.

`args`  
Estos parámetros opcionales serán pasados por defecto al constructor de la clase, durante la fase de creación del objeto.

## Valores devueltos

No se retorna ningún valor.

## Véase también

SoapServer::\_\_construct, SoapServer::addFunction, SoapServer::setPersistence
