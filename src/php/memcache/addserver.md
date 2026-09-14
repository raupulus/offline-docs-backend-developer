---
title: Memcache::addServer
description: Añade un servidor memcache a la lista de conexión
source_url: https://www.php.net/manual/es/memcache.addserver.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcache/memcache/addserver.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcache
translation_status: ready
translation_reviewed: false
translation_revision: f4098e2ba
order: 46100
---

Memcache::addServer

memcache_add_server

Añade un servidor memcache a la lista de conexión

## Descripción

```php
Memcache::addServer(string $host, [int $port], [bool $persistent], [int $weight], [int $timeout], [int $retry_interval], [bool $status], [callable $failure_callback], [int $timeoutms]): bool
```php

```php
memcache_add_server(Memcache $memcache, string $host, [int $port], [bool $persistent], [int $weight], [int $timeout], [int $retry_interval], [bool $status], [callable $failure_callback], [int $timeoutms]): bool
```

`Memcache::addServer` añade un servidor a la lista de conexión.

Al utilizar este método (a diferencia de los métodos `Memcache::connect` y `Memcache::pconnect`), la conexión a la red no se establece hasta que sea necesaria. Además, no hay inconveniente en añadir muchos servidores a la lista, incluso si no todos serán utilizados.

El fallo puede producirse en cualquier momento con cualquier método siempre que otros servidores estén disponibles, la petición no emitirá error. Cualquier interfaz de conexión o nivel de errores de servidor Memcache (a excepción de la falta de memoria) puede lanzar el fallo. Errores normales de cliente como añadir una clave existente no lanzará un fallo.

> [!NOTE]
> Esta función fue añadida en la versión 2.0.0 de Memcache.

## Parámetros

`host`  
Apunta al host donde memcache escucha para conexiones. Este parámetro puede especificar también otros transportes como `unix:///path/to/memcached.sock` para usar sockets Unix, y en este caso, `port` debe definirse también a `0`.

`port`  
Apunta al puerto donde memcache escucha para conexiones. Defínase este parámetro a `0` al usar sockets Unix.

Nota: Por omisión, el parámetro `port` toma el valor de la opción de configuración [memcache.default_port](#ini.memcache.default-port) cuando no se especifica. Por esta razón, es recomendable especificar explícitamente el puerto al llamar a este método.

`persistent`  
Controla el uso de una conexión persistente. El valor por omisión es `true`.

`weight`  
Número de entradas a crear para este servidor que a su vez controla su probabilidad de ser elegido. La probabilidad es relativa al peso total de todos los servidores.

`timeout`  
Valor en segundos que será utilizado para conectarse al demonio. Piénsese dos veces antes de cambiar el valor por omisión de un segundo - podría perderse todos los beneficios de usar la caché si la conexión es demasiado lenta.

`retry_interval`  
Controla cuántas veces se intentará un servidor que falla, el valor por omisión es de 15 segundos. Si este parámetro vale -1, no se realizará ningún nuevo intento. Ni este parámetro, ni el parámetro `persistent` tienen efecto cuando esta extensión se carga dinámicamente mediante la función `dl`.

Cada estructura de conexión fallida tiene su propio tiempo límite y antes de que este expire, será saltada durante la selección del proceso para servir una petición. Una vez expirado, la conexión será correctamente reconectada o marcada como fallida por otro intervalo de `retry_interval` segundos. El efecto típico es que cada hijo de servidor web intentará la conexión cada `retry_interval` segundos al servir una página.

`status`  
Controla si el servidor debe ser indicado como en línea. Cuando este parámetro vale `false` y el parámetro `retry_interval` vale -1, permite mantener un servidor fallido en la lista y no afectará al algoritmo de distribución de claves. Las peticiones para este servidor fallarán inmediatamente según la configuración del parámetro `memcache.allow_failover`. Por omisión, este parámetro vale `true`, significando que el servidor debe ser considerado como en línea.

`failure_callback`  
Permite al usuario especificar una función de retorno para manejar un error. La función de retorno se ejecuta antes de alcanzar el límite de intentos. La función toma dos parámetros; el nombre del host y el puerto del servidor que falló.

`timeoutms`  

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `Memcache::addServer`

```php
<?php

/* API orientada a objetos */

$memcache = new Memcache;
$memcache->addServer('memcache_host', 11211);
$memcache->addServer('memcache_host2', 11211);

/* API procedimental */

$memcache_obj = memcache_connect('memcache_host', 11211);
memcache_add_server($memcache_obj, 'memcache_host2', 11211);

?>

   
```

## Notas

> [!WARNING]
> Cuando el parámetro `port` no se especifica, este método tomará el valor de la directiva de configuración INI [memcache.default_port](#ini.memcache.default-port). Si este valor ha sido modificado en otro lugar de su aplicación, esto puede llevar a resultados inesperados: por esta razón, es recomendable siempre especificar el puerto explícitamente al llamar al método.

## Véase también

Memcache::connect

Memcache::pconnect

Memcache::close

Memcache::setServerParams

Memcache::getServerStatus
