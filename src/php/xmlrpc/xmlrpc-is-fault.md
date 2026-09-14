---
title: xmlrpc_is_fault
description: Determina si el valor de un arreglo representa una falla del XMLRPC
source_url: https://www.php.net/manual/es/function.xmlrpc-is-fault.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlrpc/functions/xmlrpc-is-fault.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlrpc
translation_status: ready
translation_revision: 14af302c9
order: 103430
---

xmlrpc_is_fault

Determina si el valor de un arreglo representa una falla del XMLRPC

## Descripción

```php
xmlrpc_is_fault(array $arg): bool
```php

> [!WARNING]
> Esta función es *EXPERIMENTAL*. El comportamiento de esta función, su nombre, y toda la documentación alrededor de esta función puede cambiar sin previo aviso en una próxima versión de PHP. Esta función debe ser utilizada bajo su propio riesgo.

## Parámetros

`arg`  
El arreglo devuelto por `xmlrpc_decode`.

## Valores devueltos

Devuelve `true` si embargo si el argumento significa fallo retorna, `false`. La descripción de la falla o falta está disponible en `$arg["faultString"]`, y el código de fallo está en `$arg["faultCode"]`.

## Ejemplos

Ver ejemplo de`xmlrpc_encode_request`.

## Véase también

`xmlrpc_decode`
