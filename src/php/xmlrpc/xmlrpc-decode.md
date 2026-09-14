---
title: xmlrpc_decode
description: Decodifica el XML en los tipos de PHP nativos
source_url: https://www.php.net/manual/es/function.xmlrpc-decode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlrpc/functions/xmlrpc-decode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlrpc
translation_status: ready
translation_revision: 96c9d88ba
order: 103390
---

xmlrpc_decode

Decodifica el XML en los tipos de PHP nativos

## Descripción

```php
xmlrpc_decode(string $xml, [string $encoding]): mixed
```php

> [!WARNING]
> Esta función es *EXPERIMENTAL*. El comportamiento de esta función, su nombre, y toda la documentación alrededor de esta función puede cambiar sin previo aviso en una próxima versión de PHP. Esta función debe ser utilizada bajo su propio riesgo.

## Parámetros

`xml`  
La respuesta XML devuelta por el método XMLRPC.

`encoding`  
Entrada de codificación que admite iconv.

## Valores devueltos

Devuelve o un arreglo, o un entero, o una cadena, o un booleano conforme a la respuesta devuelta por el método XMLRPC.

## Ejemplos

Ver el ejemplo de `xmlrpc_encode_request`.

## Véase también

`xmlrpc_encode_request`, `xmlrpc_is_fault`
