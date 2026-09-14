---
title: xmlrpc_set_type
description: Establece el tipo del xmlrpc, base64 o fecha-hora, para un valor de cadena
  PHP
source_url: https://www.php.net/manual/es/function.xmlrpc-set-type.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlrpc/functions/xmlrpc-set-type.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlrpc
translation_status: ready
translation_revision: 0dade7526
order: 103510
---

xmlrpc_set_type

Establece el tipo del xmlrpc, base64 o fecha-hora, para un valor de cadena PHP

## Descripción

```php
xmlrpc_set_type(string $value, string $type): bool
```php

Establece el tipo del xmlrpc, base64 o fecha-hora, para un valor de cadena PHP.

> [!WARNING]
> Esta función es *EXPERIMENTAL*. El comportamiento de esta función, su nombre, y toda la documentación alrededor de esta función puede cambiar sin previo aviso en una próxima versión de PHP. Esta función debe ser utilizada bajo su propio riesgo.

## Parámetros

`value`  
Valor para establecer el tipo

`type`  
'base64' o 'datetime'

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. Si tiene éxito, `value` se convierte en un objeto.

## Errores/Excepciones

Emite un E_WARNING con un tipo no soportado por XMLRPC.

## Ejemplos

Ejemplo de `xmlrpc_set_type`

```
<?php

$params = date("Ymd\TH:i:s", time());
xmlrpc_set_type($params, 'datetime');
echo xmlrpc_encode($params);

?>

    
```php

Resultado del ejemplo anterior es similar a:

```
<params>
<param>
 <value>
  <dateTime.iso8601>20090322T23:43:03</dateTime.iso8601>
 </value>
</param>
</params>

    
```php
