---
title: radius_add_server
description: Añade un servidor
source_url: https://www.php.net/manual/es/function.radius-add-server.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/radius/functions/radius-add-server.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: radius
translation_status: ready
translation_revision: 9ac4d06c0
order: 67550
---

radius_add_server

Añade un servidor

## Descripción

```php
radius_add_server(resource $radius_handle, string $hostname, int $port, string $secret, int $timeout, int $max_tries): bool
```php

`radius_add_server` puede ser utilizado varias veces, y puede ser utilizado junto con la función `radius_config`. Como máximo, pueden especificarse 10 servidores. Cuando se proporcionan varios servidores, se intentan de forma `round-robin` hasta que se recibe una respuesta válida, o hasta que se alcanza el límite `max_tries` de cada servidor.

## Parámetros

`radius_handle`  

`hostname`  
El argumento `hostname` especifica el host servidor, ya sea como nombre de dominio completo o como dirección IP.

`port`  
El `port` especifica el puerto UDP al que conectar en el servidor. Si el puerto dado es `0`, la biblioteca buscará el servicio `radius/udp` o `radacct/udp` en la base de datos de servicios de red y utilizará el puerto encontrado. Si no se encuentra ninguna entrada, la biblioteca utilizará los puertos Radius estándar, 1812 para la autenticación y 1813 para las cuentas.

`secret`  
El secreto compartido para el host servidor se pasa al argumento `secret`. El protocolo Radius ignora todo excepto los primeros 128 bytes del secreto compartido.

`timeout`  
El tiempo límite para recibir respuestas del servidor se pasa al argumento `timeout`, en segundos.

`max_tries`  
El número máximo de solicitudes repetidas a realizar antes de fallar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `radius_add_server`

```
<?php
if (!radius_add_server($res, 'radius.example.com', 1812, 'testing123', 3, 3)) {
    echo 'Error Radius :' . radius_strerror($res). "\n<br>";
    exit;
}
?>

   
```php

## Véase también

radius_config
