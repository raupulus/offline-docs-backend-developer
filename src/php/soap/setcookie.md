---
title: SoapClient::__setCookie
description: Define un cookie para las peticiones SOAP
source_url: https://www.php.net/manual/es/soapclient.setcookie.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/soapclient/setcookie.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_reviewed: false
translation_revision: fe4e8b87d
order: 75220
---

SoapClient::\_\_setCookie

Define un cookie para las peticiones SOAP

## Descripción

```php
public SoapClient::__setCookie(string $name, [string $value]): void
```php

Se define el cookie que será enviado con la petición SOAP.

> [!NOTE]
> La llamada a este método afectará a todas las llamadas posteriores a los métodos `SoapClient`.

## Parámetros

`name`  
El nombre del cookie.

`value`  
El valor del cookie. Si no se especifica, el cookie será borrado.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción                |
|---------|----------------------------|
| 8.0.0   | `value` ahora es nullable. |
