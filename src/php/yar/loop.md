---
title: Yar_Concurrent_Client::loop
description: Enviar todas las llamadas
source_url: https://www.php.net/manual/es/yar-concurrent-client.loop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yar/yar_concurrent_client/loop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yar
translation_status: ready
translation_revision: dfd68fd22
order: 107670
---

Yar_Concurrent_Client::loop

Enviar todas las llamadas

## Descripción

```php
public static Yar_Concurrent_Client::loop([callable $callback], [callable $error_callback]): bool
```php

Envía todas las llamadas RPC remotas registradas.

## Parámetros

`callback`  
Si se establece esta retrollamada, Yar la invocará después de haber enviado todas las llamadas y antes de cualquier respuesta, con un \$callinfo NULL.

Entonces, si un usuario no especifica la retrollamada al registrar una llamada concurretne, esta retrollamada se utilizará para manejar la resupesta, o si no, se utilizará la retrollamada especificada durante el registro.

`error_callback`  
Si se establece esta retrollamada, Yar la invocará cuando suceda un error.

## Valores devueltos

## Ejemplos

Ejemplo de `Yar_Concurrent_Client::loop`

```
<?php
function callback($retval, $callinfo) {
     if ($callinfo == NULL) {
        echo "Now, all requests are sent, and no response available\n";
     } else {
        echo "This is a remote call response, the method name is", $callinfo["method"],
             ". calling sequence is " , $callinfo["sequence"] , "\n";
        var_dump($retval);
     }
}

function error_callback($type, $error, $callinfo) {
    error_log($error);
}

Yar_Concurrent_Client::call("http://host/api/", "some_method", array("parameters"), "callback");
Yar_Concurrent_Client::call("http://host/api/", "some_method", array("parameters"));   // if the callback is not specificed,
                                                                               // callback in loop will be used
Yar_Concurrent_Client::call("http://host/api/", "some_method", array("parameters"), "callback", NULL, array(YAR_OPT_PACKAGER => "json"));
                                                                               //this server accept json packager
Yar_Concurrent_Client::call("http://host/api/", "some_method", array("parameters"), "callback", NULL, array(YAR_OPT_TIMEOUT=>1));
                                                                               //custom timeout

Yar_Concurrent_Client::loop("callback", "error_callback"); //send the requests,
                                                           //the error_callback is optional
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Now, all requests are sent, and no response available
    This is a remote call response, the method name issome_method. calling sequence is 4
    string(11) "some_method"
    This is a remote call response, the method name issome_method. calling sequence is 1
    string(11) "some_method"
    This is a remote call response, the method name issome_method. calling sequence is 2
    string(11) "some_method"
    This is a remote call response, the method name issome_method. calling sequence is 3
    string(11) "some_method"

## Véase también

Yar_Concurrent_Client::call

Yar_Concurrent_Client::reset

Yar_Server::\_\_construct

Yar_Server::handle
