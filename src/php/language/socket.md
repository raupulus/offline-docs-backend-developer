---
title: Opciones de contexto de los sockets
description: Lista de opciones de contexto de los sockets
source_url: https://www.php.net/manual/es/context.socket.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/context/socket.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 8bc832a46
order: 2030
---

Opciones de contexto de los sockets

Lista de opciones de contexto de los sockets

## Descripción

Las opciones de contexto de los sockets están disponibles para todos los gestores que funcionan a través de los sockets, como `tcp`, `http` y `ftp`.

## Opciones

`bindto`  
Utilizado para especificar la dirección IP (ya sea IPv4 o IPv6), y/o el número del puerto que PHP utilizará para acceder a la red. La sintaxis es `ip:puerto` para las direcciones IPv4, y `[ip]:puerto` para las direcciones IPv6. El hecho de definir la IP o el puerto a `0` permitirá al sistema elegir el puerto y/o la IP por sí mismo.

> [!NOTE]
> Dado que FTP crea 2 sockets de conexión durante una operación normal, el número del puerto no puede ser especificado utilizando esta opción.

`backlog`  
Utilizado para limitar el número de conexiones activas en la lista de espera del socket.

> [!NOTE]
> Esto solo es aplicable a la función `stream_socket_server`.

`ipv6_v6only`  
Sustituye el sistema operativo por defecto en cuanto al mapeo de IPv4 en IPv6.

> [!NOTE]
> Esto es importante en particular cuando se intenta escuchar en las direcciones IPv4 por separado mientras existe una ligadura en `[::]`.
>
> Esto solo es aplicable a la función `stream_socket_server`.

`so_reuseport`  
Permite múltiples ligaduras de una misma pareja ip:puerto, incluso desde procesos distintos.

> [!NOTE]
> Esto solo es aplicable a la función `stream_socket_server`.

`so_broadcast`  
Permite enviar y recibir datos hacia/desde direcciones de difusión.

> [!NOTE]
> Esto solo es aplicable a la función `stream_socket_server`.

`tcp_nodelay`  
Poner el valor a `true` definirá `SOL_TCP,NO_DELAY=1` correctamente, lo que desactivará el algoritmo TCP Nagle.

## Historial de cambios

| Versión | Descripción                          |
|---------|--------------------------------------|
| 7.1.0   | Adición del parámetro `tcp_nodelay`. |
| 7.0.1   | Adición del parámetro `ipv6_v6only`. |

## Ejemplos

Ejemplo de uso del parámetro `bindto`

```php
<?php
// Conexión a Internet utilizando la IP '192.168.0.100'
$opts = array(
    'socket' => array(
        'bindto' => '192.168.0.100:0',
    ),
);

// Conexión a Internet utilizando la IP '192.168.0.100' y el puerto '7000'
$opts = array(
    'socket' => array(
        'bindto' => '192.168.0.100:7000',
    ),
);

// Conexión a Internet utilizando la dirección IPv6 '2001:db8::1'
// y el puerto '7000'
$opts = array(
    'socket' => array(
        'bindto' => '[2001:db8::1]:7000',
    ),
);

// Conexión a Internet utilizando el puerto '7000'
$opts = array(
    'socket' => array(
        'bindto' => '0:7000',
    ),
);

// Creación del contexto...
$context = stream_context_create($opts);

// ...y se utiliza para recuperar los datos
echo file_get_contents('http://www.example.com', false, $context);

?>

    
```
