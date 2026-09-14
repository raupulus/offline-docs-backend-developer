---
title: use_soap_error_handler
description: Activa el gestor de errores SOAP nativo
source_url: https://www.php.net/manual/es/function.use-soap-error-handler.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/functions/use-soap-error-handler.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_reviewed: true
translation_revision: 40d440e3f
order: 75070
---

use_soap_error_handler

Activa el gestor de errores SOAP nativo

## Descripción

```php
use_soap_error_handler([bool $enable]): bool
```php

`use_soap_error_handler` activa o desactiva el gestor de errores SOAP nativo del servidor SOAP. Retorna el valor previamente utilizado. Si el argumento `handler` es establecido a `true`, los detalles de los errores del servidor `SoapServer` serán enviados al cliente, como mensaje de error SOAP. Si es `false`, se utilizará el gestor de errores estándar de PHP. El comportamiento por omisión es enviar el error al cliente en forma de mensaje SOAP.

## Parámetros

`enable`  
Con el valor `true`, los detalles de los errores serán enviados a los clientes.

## Valores devueltos

Retorna el valor original.

## Véase también

`set_error_handler`, `set_exception_handler`
