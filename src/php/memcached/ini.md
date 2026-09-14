---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/memcached.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: d4d5216e7
order: 46330
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [memcached.sess_locking](#ini.memcached.sess-locking) | On | `INI_ALL` | Disponible a partir de memcached 0.1.0. |
| [memcached.sess_consistent_hash](#ini.memcached.sess-consistent-hash) | On | `INI_ALL` | Disponible a partir de memcached 2.1.0. El valor por omisión es `Activo` a partir de memcached 3.0.0. |
| [memcached.sess_binary](#ini.memcached.sess-binary) | Off | `INI_ALL` | Disponible a partir de memcached 2.0.0. Reemplazado por `memcached.sess_binary_protocol` a partir de memcached 3.0.0. |
| [memcached.sess_lock_wait](#ini.memcached.sess-lock-wait) | 150000 | `INI_ALL` | Disponible a partir de memcached 0.1.0. Eliminado a partir de memcached 3.0.0. |
| [memcached.sess_prefix](#ini.memcached.sess-prefix) | memc.sess.key. | `INI_ALL` | Disponible a partir de memcached 0.1.0. |
| [memcached.sess_number_of_replicas](#ini.memcached.sess-number-of-replicas) | 0 | `INI_ALL` | Disponible a partir de memcached 2.1.0. |
| [memcached.sess_randomize_replica_read](#ini.memcached.sess-randomize-replica-read) | Off | `INI_ALL` | Disponible a partir de memcached 2.1.0. |
| [memcached.sess_remove_failed](#ini.memcached.sess-remove-failed) | On | `INI_ALL` | Disponible a partir de memcached 2.1.0. Reemplazado por `memcached.sess_remove_failed_servers` a partir de memcached 3.0.0. |
| [memcached.compression_type](#ini.memcached.compression-type) | fastlz | `INI_ALL` | Disponible a partir de memcached 0.1.0. |
| [memcached.compression_factor](#ini.memcached.compression-factor) | 1.3 | `INI_ALL` | Disponible a partir de memcached 0.1.0. |
| [memcached.compression_threshold](#ini.memcached.compression-threshold) | 2000 | `INI_ALL` | Disponible a partir de memcached 0.1.0. |
| [memcached.serializer](#ini.memcached.serializer) | igbinary | `INI_ALL` | Disponible a partir de memcached 0.1.0. |
| [memcached.use_sasl](#ini.memcached.use-sasl) | Off | `INI_ALL` | Disponible a partir de memcached 2.2.0. Eliminado a partir de memcached 3.0.0. |
| [memcached.default_binary_protocol](#ini.memcached.default-binary-protocol) | Off | `INI_ALL` | Disponible a partir de memcached 3.0.0. |
| [memcached.default_connect_timeout](#ini.memcached.default-connect-timeout) | 0 | `INI_ALL` | Disponible a partir de memcached 3.0.0. |
| [memcached.default_consistent_hash](#ini.memcached.default-consistent-hash) | Off | `INI_ALL` | Disponible a partir de memcached 3.0.0. |
| [memcached.sess_binary_protocol](#ini.memcached.sess-binary-protocol) | On | `INI_ALL` | Disponible a partir de memcached 3.0.0. Reemplaza `memcached.sess_binary`. |
| [memcached.sess_connect_timeout](#ini.memcached.sess-connect-timeout) | 1000 | `INI_ALL` | Disponible a partir de memcached 2.2.0. |
| [memcached.sess_consistent_hash_type](#ini.memcached.sess-consistent-hash-type) | ketama | `INI_ALL` | Disponible a partir de memcached 3.1.0. |
| [memcached.sess_lock_expire](#ini.memcached.sess-lock-expire) | 0 | `INI_ALL` | Disponible a partir de memcached 2.2.0. |
| [memcached.sess_lock_retries](#ini.memcached.sess-lock-retries) | 5 | `INI_ALL` | Disponible a partir de memcached 3.0.0. |
| [memcached.sess_lock_wait_max](#ini.memcached.sess-lock-wait-max) | 150 | `INI_ALL` | Disponible a partir de memcached 3.0.0. Por omisión a `150` a partir de memcached 3.1.0 (antes `2000`). |
| [memcached.sess_lock_wait_min](#ini.memcached.sess-lock-wait-min) | 150 | `INI_ALL` | Disponible a partir de memcached 3.0.0. Por omisión a `150` a partir de memcached 3.1.0 (antes `1000`). |
| [memcached.sess_persistent](#ini.memcached.sess-persistent) | Off | `INI_ALL` | Disponible a partir de memcached 3.0.0. |
| [memcached.sess_remove_failed_servers](#ini.memcached.sess-remove-failed-servers) | Off | `INI_ALL` | Disponible a partir de memcached 3.0.0. Reemplaza `memcached.sess_remove_failed`. |
| [memcached.sess_server_failure_limit](#ini.memcached.sess-server-failure-limit) | 0 | `INI_ALL` | Disponible a partir de memcached 3.0.0. |
| [memcached.sess_sasl_password](#ini.memcached.sess-sasl-password) | null | `INI_ALL` | Disponible a partir de memcached 2.2.0. |
| [memcached.sess_sasl_username](#ini.memcached.sess-sasl-username) | null | `INI_ALL` | Disponible a partir de memcached 2.2.0. |
| [memcached.store_retry_count](#ini.memcached.store-retry-count) | 0 | `INI_ALL` | Disponible a partir de memcached 2.2.0. Por omisión a `0` a partir de memcached 3.2.0 (antes `2`). |

Opciones de configuración Memcached

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`memcached.sess_locking` `bool`  
Utiliza los cerrojos de sesión. Los valores válidos son `On` y `Off`, el valor por omisión es `On`.

`memcached.sess_consistent_hash` `bool`  
Si se define como `On`, utiliza el hachado consistente (libketama) para la gestión de sesiones. Cuando se utiliza el hachado consistente, se pueden añadir o eliminar nodos de caché sin perturbar las claves existentes. El valor por omisión es `On`.

`memcached.sess_binary` `bool`  
Utiliza el modo binario para las sesiones memcached. Las réplicas de libmemcached solo funcionan si el modo binario está activado. El valor por omisión es `Off`.

`memcached.sess_lock_wait` `int`  
La duración de espera del cerrojo de sesión en microsegundos. Tenga cuidado al definir este valor. Los valores válidos son enteros, donde `0` se interpreta como el valor por omisión. Los valores negativos reducen el bloqueo a un bloqueo de prueba. El valor por omisión es `150000`.

`memcached.sess_prefix` `string`  
El prefijo de clave de sesión Memcached. Los valores válidos son strings de menos de 219 bytes. El valor por omisión es `memc.sess.key`.

`memcached.sess_number_of_replicas` `int`  
Escribe los datos en un cierto número de servidores Memcached adicionales. Esto es lo que libmemcached llama "pobre hombre HA". Si este valor es positivo y `sess_remove_failed_servers` está activado, cuando un servidor Memcached falle, la sesión continuará estando disponible a partir de una réplica. Sin embargo, si el servidor Memcached en fallo vuelve a estar disponible, la sesión se leerá desde allí, lo que podría tener datos obsoletos o ninguna información en absoluto. El valor por omisión es `0`.

`memcached.sess_randomize_replica_read` `bool`  
La sesión Memcached lee la replicación aleatoria.

`memcached.sess_remove_failed` `int`  
Permite que el servidor Memcached en fallo sea eliminado automáticamente.

`memcached.compression_type` `string`  
Define el tipo de compresión, los valores válidos son: `fastlz`, `zlib`. El valor por omisión es `fastlz`.

`memcached.compression_factor` `float`  
El factor de compresión. Almacene el valor comprimido solo si el factor de compresión (ahorro) supera el límite definido. Almacene comprimido si: `plain_len > comp_len * factor`. El valor por omisión es `1.3` (23% de ahorro de espacio).

`memcached.compression_threshold` `int`  
El umbral de compresión. No comprima los valores serializados por debajo de este umbral. El valor por omisión es `2000` bytes.

`memcached.serializer` `string`  
Define el serializador por omisión para los nuevos objetos Memcached. Los valores válidos son: `php`, `igbinary`, `json`, `json_array`, `msgpack`.

json  
La serialización JSON estándar de PHP. Este serializador es rápido y compacto pero solo funciona con datos codificados en UTF-8 y no implementa completamente la serialización. Ver la extensión JSON. Disponible a partir de memcached 0.2.0.

json_array  
Como `json`, pero decodifica en arrays. Disponible a partir de memcached 2.0.0.

php  
El serializador estándar de PHP.

igbinary  
Un serializador binario. Disponible a partir de memcached 0.1.4.

msgpack  
Un serializador binario multi-lenguaje. Disponible a partir de memcached 2.2.0.

El valor por omisión es `igbinary` si está disponible, luego `msgpack` si está disponible, luego de lo contrario `php`.

`memcached.use_sasl` `bool`  
Utilizar la autenticación SASL para las conexiones. Los valores válidos son `On` y `Off`. El valor por omisión es `Off`.

`memcached.default_binary_protocol` `bool`  
Define el protocolo memcached por omisión para las nuevas conexiones. (Para configurar el protocolo memcached para las conexiones utilizadas por las sesiones, utilice `memcached.sess_binary_protocol` en su lugar.) Si se define como `On`, el protocolo binario memcached se utiliza por omisión. Si se define como `Off`, el protocolo de texto memcached se utiliza. El valor por omisión es `Off`.

`memcached.default_connect_timeout` `int`  
Define el tiempo de espera de conexión memcached por omisión para las nuevas conexiones. (Para configurar el tiempo de espera de conexión memcached para las sesiones, utilice `memcached.sess_connect_timeout` en su lugar.) En modo no bloqueante, esto cambia el valor del tiempo de espera. Durante la conexión del socket en milisegundos. Especificar `-1` significa un tiempo de espera infinito. Especificar `0` significa utilizar el tiempo de espera de conexión por omisión de la biblioteca memcached. El valor por omisión es `0`.

`memcached.default_consistent_hash` `bool`  
Define el hachado consistente por omisión para las nuevas conexiones. (Para configurar el hachado consistente para las conexiones utilizadas por las sesiones, utilice `memcached.sess_consistent_hash` en su lugar.) Si se define como `On`, el hachado consistente (libketama) se utiliza para la gestión de sesiones. Cuando se utiliza el hachado consistente, se pueden añadir o eliminar nodos de caché sin perturbar las claves existentes. El valor por omisión es `Off`.

`memcached.sess_binary_protocol` `bool`  
Utilizar el protocolo binario memcached para las sesiones memcached en lugar del protocolo de texto. Las réplicas de libmemcached solo funcionan si el modo binario está activado. Sin embargo, algunos proxies (como twemproxy) solo funcionarán si el protocolo binario está desactivado. El valor por omisión es `On` desde libmemcached 1.0.18. Antes de libmemcached 1.0.18, el valor por omisión era `Off`.

> [!NOTE]
> En versiones anteriores de php-memcached, este parámetro se llamaba `memcached.sess_binary`.

`memcached.sess_connect_timeout` `int`  
El valor del tiempo de espera de conexión memcached. En modo no bloqueante, esto cambia el valor del tiempo de espera durante la conexión del socket en milisegundos. Especificar `-1` significa un tiempo de espera infinito.

`memcached.sess_consistent_hash_type` `string`  
Tipo de hachado consistente de sesión Memcached. Si se define como `ketama`, el hachado consistente (libketama) se utiliza para la gestión de sesiones. Si se define como `ketama_weighted`, el hachado consistente ponderado (libketama) se utiliza para la gestión de sesiones. El valor por omisión es `ketama`. Antes de php-memcached 3.0, el valor por omisión era `ketama_weighted`.

`memcached.sess_lock_expire` `int`  
El tiempo, en segundos, antes de que un cerrojo se libere. Definir como `0` da el comportamiento por omisión, que es utilizar `max_execution_time` de PHP. El valor por omisión es `0`.

`memcached.sess_lock_retries` `int`  
El número de intentos de cerrojo de sesión, sin contar el primer intento. El valor por omisión es `5`.

`memcached.sess_lock_wait_max` `int`  
El tiempo máximo, en milisegundos, de espera entre los intentos de cerrojo de sesión. El valor por omisión es `150`.

`memcached.sess_lock_wait_min` `int`  
El tiempo mínimo, en milisegundos, de espera entre los intentos de cerrojo de sesión. Este valor se duplica en cada nuevo intento de cerrojo hasta que `memcached.sess_lock_wait_max` se alcance, después de lo cual cualquier nuevo intento tomará `memcached.sess_lock_wait_max` segundos. El valor por omisión es `150`.

`memcached.sess_persistent` `bool`  
Si las conexiones memcached coinciden con el/los valor(es) de `session.save_path` deben ser reutilizadas después de la ejecución del script. No utilizar si algunos parámetros (por ejemplo, los parámetros SASL, sess_binary_protocol) serían sobrescritos entre las peticiones. El valor por omisión es `Off`.

`memcached.sess_remove_failed_servers` `bool`  
Permite que el servidor Memcached en fallo sea eliminado automáticamente. El valor por omisión es `Off`.

> [!NOTE]
> En versiones anteriores de php-memcached, este parámetro se llamaba `memcached.sess_remove_failed`.

`memcached.sess_server_failure_limit` `int`  
Definir este valor para permitir la eliminación automática del servidor después de un cierto número de intentos de conexión fallidos. El valor por omisión es `0`.

`memcached.sess_sasl_password` `string`  
La contraseña SASL de sesión. El nombre de usuario y la contraseña deben ser definidos para activar SASL.

`memcached.sess_sasl_username` `string`  
El nombre de usuario SASL de sesión. El nombre de usuario y la contraseña deben ser definidos para activar SASL.

`memcached.store_retry_count` `int`  
La cantidad de intentos para los comandos de almacenamiento fallidos. Este mecanismo permite un fallo transparente hacia los servidores secundarios cuando las operaciones set/increment/decrement/setMulti fallan en el servidor deseado en un entorno multi-servidor. El valor por omisión es `2`.
