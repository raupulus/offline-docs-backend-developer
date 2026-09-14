---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/memcache.ini.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcache/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcache
translation_status: ready
translation_reviewed: false
translation_revision: f4098e2ba
order: 46080
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [memcache.allow_failover](#ini.memcache.allow-failover) | "1" | `INI_ALL` | Disponible a partir de memcache 2.0.2. |
| [memcache.max_failover_attempts](#ini.memcache.max-failover-attempts) | "20" | `INI_ALL` | Disponible a partir de memcache 2.1.0. |
| [memcache.chunk_size](#ini.memcache.chunk-size) | "8192" | `INI_ALL` | Disponible a partir de memcache 2.0.2. |
| [memcache.default_port](#ini.memcache.default-port) | "11211" | `INI_ALL` | Disponible a partir de memcache 2.0.2. |
| [memcache.hash_strategy](#ini.memcache.hash-strategy) | "standard" | `INI_ALL` | Disponible a partir de memcache 2.2.0. |
| [memcache.hash_function](#ini.memcache.hash-function) | "crc32" | `INI_ALL` | Disponible a partir de memcache 2.2.0. |
| [memcache.protocol](#ini.memcache.protocol) | ascii | `INI_ALL` | Supportado a partir de memcache 3.0.0 |
| [memcache.redundancy](#ini.memcache.redundancy) | 1 | `INI_ALL` | Supportado a partir de memcache 3.0.0 |
| [memcache.session_redundancy](#ini.memcache.session-redundancy) | 2 | `INI_ALL` | Supportado a partir de memcache 3.0.0 |
| [memcache.compress_threshold](#ini.memcache.compress-threshold) | 20000 | `INI_ALL` | Supportado a partir de memcache 3.0.3 |
| [memcache.lock_timeout](#ini.memcache.lock-timeout) | 15 | `INI_ALL` | Supportado a partir de memcache 3.0.4 |

Opciones de configuración memcache

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [session.save_handler](#ini.memcache.save-handler) | "files" | `INI_ALL` | Supportado a partir de memcache 2.1.2 |
| [session.save_path](#ini.memcache.save-path) | "" | `INI_ALL` | Supportado a partir de memcache 2.1.2 |

Opciones de Configuración de Sesión que Afectan el Comportamiento de Memcache

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`memcache.allow_failover` `bool`  
Si se debe cambiar a otros servidores en caso de error.

`memcache.max_failover_attempts` `int`  
Define cuántos servidores intentar cuando se fijan o recuperan datos. Utilice solo en conjunción con memcache.allow_failover.

`memcache.chunk_size` `int`  
Los datos deben transferirse en fragmentos de este tamaño; Configurar este valor a un valor pequeño provoca más escrituras en la red. Intente aumentar este valor a 32768 si se encuentran retrasos inexplicables.

`memcache.default_port` `string`  
El número de puerto TCP por defecto a utilizar al conectarse al servidor memcache si no se especifica otro puerto.

`memcache.hash_strategy` `string`  
Controla la estrategia a aplicar al mapear las claves en los servidores. Definir este valor a `consistent` para activar el hash consistente que permite añadir o eliminar servidores del grupo sin necesidad de remapear las claves. Definir este valor a `standard` hará que se utilice la estrategia antigua.

`memcache.hash_function` `string`  
Controla la función de hash a aplicar al mapear las claves en los servidores, `crc32` utilizará el CRC32 estándar, mientras que `fnv` utilizará FNV-1a.

`memcache.protocol` `string`  

`memcache.redundancy` `int`  

`memcache.session_redundancy` `int`  

`memcache.compress_threshold` `int`  

`memcache.lock_timeout` `int`  

`session.save_handler` `string`  
Utilice memcache como gestor de sesión definiendo este valor a `memcache`.

`session.save_path` `string`  
Define las URL de servidor, separadas por comas, a utilizar para el almacenamiento de las sesiones, por ejemplo: `"tcp://host1:11211, tcp://host2:11211"`.

Cada URL puede contener parámetros que serán aplicados al servidor, de la misma forma que para el método `Memcache::addServer`. Por ejemplo: `"tcp://host1:11211?persistent=1&weight=1&timeout=1&retry_interval=15"`
