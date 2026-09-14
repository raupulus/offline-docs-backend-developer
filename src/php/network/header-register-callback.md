---
title: header_register_callback
description: Llamar a una función de cabecera
source_url: https://www.php.net/manual/es/function.header-register-callback.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/header-register-callback.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_revision: 5faa7a674
order: 56370
---

header_register_callback

Llamar a una función de cabecera

## Descripción

```php
header_register_callback(callable $callback): bool
```php

Registra una función que será llamada cuando PHP comienza a enviar la salida.

El `callback` se ejecuta inmediatamente después de PHP prepara todos los encabezados que van a ser enviados, y antes de cualquier otra salida es enviado, crea una ventana para manipular las cabeceras de salida antes de ser enviado.

## Parámetros

`callback`  
Función llamada justo antes de que se envíen los encabezados. No tiene parámetros y el valor de retorno se ignora.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `header_register_callback`

```
<?php

header('Content-Type: text/plain');
header('X-Test: foo');

function foo() {
 foreach (headers_list() as $header) {
   if (strpos($header, 'X-Powered-By:') !== false) {
     header_remove('X-Powered-By');
   }
   header_remove('X-Test');
 }
}

$result = header_register_callback('foo');
echo "a";
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Content-Type: text/plain

    a

## Notas

La función `header_register_callback` es ejecutada cuando las cabeceras están a punto de ser enviadas, por lo que cualquier salida de esta función puede romper de salida.

> [!NOTE]
> Los encabezados solo serán accesibles y se mostrarán cuando se utilice un SAPI que los soporte.

## Véase también

headers_list

header_remove

header
