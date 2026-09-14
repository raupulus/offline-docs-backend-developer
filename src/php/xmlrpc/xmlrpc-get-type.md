---
title: xmlrpc_get_type
description: Obtiene el tipo del xmlrpc para un valor PHP
source_url: https://www.php.net/manual/es/function.xmlrpc-get-type.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlrpc/functions/xmlrpc-get-type.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlrpc
translation_status: ready
translation_revision: 80ae0ac08
order: 103420
---

xmlrpc_get_type

Obtiene el tipo del xmlrpc para un valor PHP

## Descripción

```php
xmlrpc_get_type(mixed $value): string
```php

> [!WARNING]
> Esta función es *EXPERIMENTAL*. El comportamiento de esta función, su nombre, y toda la documentación alrededor de esta función puede cambiar sin previo aviso en una próxima versión de PHP. Esta función debe ser utilizada bajo su propio riesgo.

Ésta función es específicamente útil para la base64 y las cadenas fecha-hora.

## Parámetros

`value`  
valor de PHP

## Valores devueltos

Devuelve el tipo de XML-RPC.

## Ejemplos

Ejemplo de tipo de XML-RPC

```
<?php
echo xmlrpc_get_type(null) . "\n"; // base64
echo xmlrpc_get_type(false) . "\n"; // boolean
echo xmlrpc_get_type(1) . "\n"; // int
echo xmlrpc_get_type(1.0) . "\n"; // double
echo xmlrpc_get_type("") . "\n"; // string
echo xmlrpc_get_type(array()) . "\n"; // array
echo xmlrpc_get_type(new stdClass) . "\n"; // array
echo xmlrpc_get_type(STDIN) . "\n"; // int
?>

    
```php

## Véase también

`xmlrpc_set_type`
