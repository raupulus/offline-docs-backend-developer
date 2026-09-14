---
title: Memcache::setServerParams
description: Modifica los parámetros y los estados del servidor durante la ejecución
source_url: https://www.php.net/manual/es/memcache.setserverparams.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcache/memcache/setserverparams.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcache
translation_status: ready
translation_reviewed: false
translation_revision: f4098e2ba
order: 46260
---

Memcache::setServerParams

memcache_set_server_params

Modifica los parámetros y los estados del servidor durante la ejecución

## Descripción

```php
Memcache::setServerParams(string $host, [int $port], [int $timeout], [int $retry_interval], [bool $status], [callable $failure_callback]): bool
```php

```php
memcache_set_server_params(Memcache $memcache, string $host, [int $port], [int $timeout], [int $retry_interval], [bool $status], [callable $failure_callback]): bool
```

`Memcache::setServerParams` modifica los parámetros del servidor durante la ejecución.

> [!NOTE]
> Esta función fue añadida en la versión 2.1.0 de Memcache.

## Parámetros

`host`  
Host donde memcache escucha para conexiones.

`port`  
Puerto donde memcache escucha para conexiones.

`timeout`  
Valor en segundos que será utilizado para conectarse al demonio. Piénselo dos veces antes de cambiar el valor por omisión de un segundo - podría perderse todos los beneficios del uso de la caché si la conexión es demasiado lenta.

`retry_interval`  
Controla cuántas veces se intentará conectar a un servidor que falla: el valor por omisión es de 15 segundos. Si este parámetro vale -1, no se realizará ningún nuevo intento. Ni este parámetro, ni el parámetro `persistent` tienen efecto cuando esta extensión es cargada dinámicamente mediante la función `dl`.

`status`  
Controla si el servidor debe ser indicado como en línea. Cuando este parámetro vale `false` y el parámetro `retry_interval` vale -1, permite mantener un servidor fallido en la lista y no afectará al algoritmo de distribución de claves. Las peticiones para este servidor fallarán inmediatamente según la configuración del parámetro `memcache.allow_failover`. Por omisión, este parámetro vale `true`, significando que el servidor debe ser considerado como en línea.

`failure_callback`  
Permite al usuario especificar una función de devolución de llamada para manejar un error. La función es ejecutada antes de alcanzar el límite de intentos. La función toma dos argumentos; el nombre del host y el puerto del servidor que falló.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `Memcache::setServerParams`

```php
<?php

function _callback_memcache_failure($host, $port) {
    print "memcache '$host:$port' falló";
}

/* API orientada a objetos */

$memcache = new Memcache;

// Añade el servidor en modo fuera de línea
$memcache->addServer('memcache_host', 11211, false, 1, 1, -1, false);

// Reemplaza el servidor en línea
$memcache->setServerParams('memcache_host', 11211, 1, 15, true, '_callback_memcache_failure');

/* API procedimental */

$memcache_obj = memcache_connect('memcache_host', 11211);
memcache_set_server_params($memcache_obj, 'memcache_host', 11211, 1, 15, true, '_callback_memcache_failure');

?>

   
```

## Véase también

Memcache::addServer

Memcache::getServerStatus
