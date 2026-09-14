---
title: Yaf_Request_Http::isXmlHttpRequest
description: Determina si la solicitud es una solicitud de Ajax
source_url: https://www.php.net/manual/es/yaf-request-http.isxmlhttprequest.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_request_http/isxmlhttprequest.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 6ab98a443
order: 106490
---

Yaf_Request_Http::isXmlHttpRequest

Determina si la solicitud es una solicitud de Ajax

## Descripción

```php
public Yaf_Request_Http::isXmlHttpRequest(): bool
```php

Comprueba si la petición es una consulta Ajax.

> [!NOTE]
> Este método depende de la cabecera de petición: HTTP_X_REQUESTED_WITH, algunas bibliotecas de Javascript no establecen esta cabecera mientras se realiza una petición Ajax.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

boolean
