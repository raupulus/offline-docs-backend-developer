---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/memcached.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: b6c220c74
order: 46310
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`Memcached::OPT_COMPRESSION`  
Activa o desactiva la compresión del contenido. Si está activada, los elementos que excedan un tamaño (actualmente 200 bytes), serán comprimidos durante el almacenamiento, y descomprimidos al recuperar, de manera transparente. El umbral puede ser configurado mediante el parámetro ini [memcached.compression_threshold](#ini.memcached.compression-threshold).

Tipo: `bool`, por omisión: `true`.

`Memcached::OPT_COMPRESSION_TYPE`  
Especifica el algoritmo de compresión a utilizar, si la compresión está activada. Los algoritmos válidos son `Memcached::COMPRESSION_FASTLZ`, `Memcached::COMPRESSION_ZLIB` y `Memcached::COMPRESSION_ZSTD`.

Tipo: `int`, por omisión: `Memcached::COMPRESSION_FASTLZ`.

`Memcached::COMPRESSION_FASTLZ`  
El algoritmo de compresión FASTLZ.

`Memcached::COMPRESSION_ZLIB`  
El algoritmo de compresión ZLIB.

`Memcached::COMPRESSION_ZSTD`  
El algoritmo de compresión ZSTD.

Disponible a partir de Memcached 3.3.0.

`Memcached::OPT_COMPRESSION_LEVEL`  
Especifica el nivel de compresión a utilizar, si la compresión está activada.

Memcached::COMPRESSION_FASTLZ

no soporta niveles de compresión.

Memcached::COMPRESSION_ZSTD

: el nivel mínimo es

-22

y el nivel máximo es

22

.

Memcached::COMPRESSION_ZLIB

: el nivel mínimo es

0

y el nivel máximo es

9

.

Tipo: `int`, por omisión: `3`.

`Memcached::OPT_SERIALIZER`  
Especifica la función de serialización a utilizar para los valores no escalares. Las funciones válidas son `Memcached::SERIALIZER_PHP`, `Memcached::SERIALIZER_IGBINARY`, `Memcached::SERIALIZER_JSON`, `Memcached::SERIALIZER_JSON_ARRAY` y `Memcached::SERIALIZER_MSGPACK`.

Tipo: `int`, por omisión: `Memcached::SERIALIZER_IGBINARY` si está disponible, luego `Memcached::SERIALIZER_MSGPACK` si está disponible, luego `Memcached::SERIALIZER_PHP`.

`Memcached::SERIALIZER_PHP`  
La función de serialización por defecto de PHP.

`Memcached::SERIALIZER_IGBINARY`  
El serializador [igbinary](#book.igbinary). En lugar de una representación textual, esta función almacena las estructuras PHP en un formato compacto y binario, con un ahorro de tiempo y espacio.

Este serializador solo es soportado si memcached está configurado con la opción `--enable-memcached-igbinary` y si la extensión [igbinary](#intro.igbinary) está cargada.

`Memcached::SERIALIZER_JSON`  
El serializador JSON. Este serializador deserializa el JSON en un objeto.

`Memcached::SERIALIZER_JSON_ARRAY`  
El serializador JSON en array. Este serializador deserializa el JSON en un array asociativo.

`Memcached::SERIALIZER_MSGPACK`  
El serializador [MessagePack](https://pecl.php.net/package/msgpack).

Este serializador solo es soportado si memcached está configurado con la opción `--enable-memcached-msgpack` y si la extensión `msgpack` está cargada.

`Memcached::OPT_PREFIX_KEY`  
Esta opción puede ser utilizada para crear un "dominio" para las claves. El valor especificado aquí será prefijado a cada clave. No puede ser más largo que `128` caracteres, y reducirá en consecuencia el tamaño máximo de clave disponible. El prefijo solo se aplica a las claves de elemento, y no a las claves de servidor.

Tipo: `string`, por omisión: `""`.

`Memcached::OPT_HASH`  
Especifica el algoritmo de hash utilizado para las claves. Los valores válidos son proporcionados con las constantes `Memcached::HASH_*`. Cada algoritmo de hash tiene sus ventajas y desventajas. Utilice el que se proporciona por omisión, si no comprende, o si no le importa.

Tipo: `int`, por omisión: `Memcached::HASH_DEFAULT`

`Memcached::HASH_DEFAULT`  
El algoritmo por omisión (`Jenkins one-at-a-time`) de hash.

`Memcached::HASH_MD5`  
El algoritmo de hash por MD5

`Memcached::HASH_CRC`  
El algoritmo de hash por CRC

`Memcached::HASH_FNV1_64`  
El algoritmo de hash por FNV1_64

`Memcached::HASH_FNV1A_64`  
El algoritmo de hash por FNV1_64A

`Memcached::HASH_FNV1_32`  
El algoritmo de hash por FNV1_32

`Memcached::HASH_FNV1A_32`  
El algoritmo de hash por FNV1_32A

`Memcached::HASH_HSIEH`  
El algoritmo de hash por Hsieh

`Memcached::HASH_MURMUR`  
El algoritmo de hash por Murmur

`Memcached::OPT_DISTRIBUTION`  
Especifica el método de distribución de claves en los servidores. Actualmente, esta opción soporta el módulo y el hash consistente. El hash consistente proporciona la mejor distribución, y permite añadir servidores al grupo con un mínimo de pérdidas de caché.

Tipo: `int`, por omisión: `Memcached::DISTRIBUTION_MODULA`.

`Memcached::DISTRIBUTION_MODULA`  
El algoritmo de distribución por módulo

`Memcached::DISTRIBUTION_CONSISTENT`  
El algoritmo de distribución por hash consistente

`Memcached::DISTRIBUTION_VIRTUAL_BUCKET`  
Algoritmo de distribución de clave de hash Virtual Bucket (también llamado vbucket).

`Memcached::OPT_LIBKETAMA_COMPATIBLE`  
Activa o no la compatibilidad con el comportamiento tipo libketama. Cuando esta opción está activada, el algoritmo de hash es MD5, y la distribución es el hash consistente. Esto es práctico porque otros clientes que utilizan libketama (Python, Ruby, etc.) con la misma configuración de servidor serán capaces de utilizar las mismas claves, de manera transparente.

> [!NOTE]
> Esta opción es altamente recomendada, si se quiere utilizar el hash consistente, y es probable que esté activada por omisión en futuras versiones.

Tipo: `bool`, por omisión: `false`.

`Memcached::OPT_LIBKETAMA_HASH`  
Especifica el algoritmo de hash para el mapeo del host.

Tipo: `int`.

`Memcached::OPT_TCP_KEEPALIVE`  
Activa el mantenimiento de la conexión TCP (keep-alive).

Tipo: `bool`, por omisión: `false`.

`Memcached::OPT_BUFFER_WRITES`  
Activa o no la bufferización de entrada/salida. La bufferización hace que los comandos de almacenamiento se buffericen, en lugar de enviarse. Cualquier acción que lea datos hace que el buffer de escritura sea enviado al servidor remoto. El cierre de la conexión o su parada también forzarán el envío de los datos del buffer.

Tipo: `bool`, por omisión: `false`.

`Memcached::OPT_BINARY_PROTOCOL`  
Active esta opción para utilizar el protocolo binario. Tenga en cuenta que no puede cambiar esta opción para una conexión ya abierta.

Tipo: `bool`, por omisión: `false`.

`Memcached::OPT_NO_BLOCK`  
Activa o no los transferencias asíncronas. Este es el modo de transferencia más rápido, para las funciones de almacenamiento.

Tipo: `bool`, por omisión: `false`.

`Memcached::OPT_NOREPLY`  
Activa o desactiva la ignoración del resultado de los comandos de almacenamiento (set, add, replace, append, prepend, delete, increment, decrement, etc.). Los comandos de almacenamiento serán enviados sin pasar tiempo esperando una respuesta (no habría respuesta). Los comandos de recuperación como Memcached::get no son afectados por esta configuración.

Tipo: `bool`, por omisión: `false`.

`Memcached::OPT_TCP_NODELAY`  
Activa o no las conexiones sin retraso de los sockets (esto puede ser un aumento de rendimiento en algunos entornos.

Tipo: `bool`, por omisión: `false`.

`Memcached::OPT_SOCKET_SEND_SIZE`  
El tamaño máximo del buffer de envío por socket, en bytes.

Tipo: `int`, por omisión: varía según la configuración de la plataforma/núcleo.

`Memcached::OPT_SOCKET_RECV_SIZE`  
El tamaño máximo del buffer de recepción por socket, en bytes.

Tipo: `int`, por omisión: varía según la configuración de la plataforma/núcleo.

`Memcached::OPT_CONNECT_TIMEOUT`  
En modo no bloqueante, esta opción configura el tiempo de espera durante la conexión del socket, en milisegundos.

Tipo: `int`, por omisión: `1000`.

`Memcached::OPT_RETRY_TIMEOUT`  
La duración, en segundos, de espera antes de intentar nuevamente una conexión que ha fallado.

Tipo: `int`, por omisión: `2`.

`Memcached::OPT_DEAD_TIMEOUT`  
La duración, en segundos, de espera antes de reintentar con los servidores muertos. `0` significa ningún reintento.

Tipo: `int`, por omisión: `0`.

`Memcached::OPT_SEND_TIMEOUT`  
Tiempo de espera de envío para el socket, en microsegundos. En los casos donde se utiliza un socket no bloqueante, esto permitirá tener tiempos de espera en el envío de datos, de todos modos.

Tipo: `int`, por omisión: `0`.

`Memcached::OPT_RECV_TIMEOUT`  
Tiempo de espera de recepción para el socket, en microsegundos. En los casos donde se utiliza un socket no bloqueante, esto permitirá tener tiempos de espera en la recepción de datos, de todos modos.

Tipo: `int`, por omisión: `0`.

`Memcached::OPT_POLL_TIMEOUT`  
Tiempo de espera para la consulta de conexiones, en milisegundos.

Tipo: `int`, por omisión: `1000`.

`Memcached::OPT_CACHE_LOOKUPS`  
Activa o no el caché de DNS.

Tipo: `bool`, por omisión: `false`.

`Memcached::OPT_SERVER_FAILURE_LIMIT`  
Especifica el límite del número de fallos de conexión. El servidor será retirado de la lista después de tantos fallos de conexión consecutivos.

Tipo: `int`, por omisión: `5`.

`Memcached::OPT_SERVER_TIMEOUT_LIMIT`  
Especifica el límite de tiempo de espera para los intentos de conexión al servidor. El servidor será eliminado después de este número de tiempos de espera continuos de conexión.

Tipo: `int`, por omisión: `0`.

`Memcached::OPT_AUTO_EJECT_HOSTS`  
Elimina los servidores desactivados de la lista. Para utilizar con `Memcached::OPT_SERVER_FAILURE_LIMIT` y `Memcached::OPT_SERVER_TIMEOUT_LIMIT`.

> [!NOTE]
> Esta opción es reemplazada por `Memcached::OPT_REMOVE_FAILED_SERVERS`.

Tipo: `bool`, por omisión: `false`.

`Memcached::OPT_VERIFY_KEY`  
Activa la verificación de claves por memcached.

Tipo: `bool`, por omisión: `false`.

`Memcached::OPT_USE_UDP`  
Utiliza UDP en lugar de TCP.

Tipo: `bool`, por omisión: `false`.

`Memcached::OPT_NUMBER_OF_REPLICAS`  
Almacena este número de réplicas de cada elemento en diferentes servidores.

Tipo: `int`, por omisión: `0`.

`Memcached::OPT_RANDOMIZE_REPLICA_READS`  
Randomiza el servidor de lectura de réplica.

Tipo: `bool`, por omisión: `false`.

`Memcached::OPT_REMOVE_FAILED_SERVERS`  
Elimina los servidores desactivados de la lista. Para utilizar con `Memcached::OPT_SERVER_FAILURE_LIMIT` y `Memcached::OPT_SERVER_TIMEOUT_LIMIT`.

Tipo: `bool`, por omisión: `false`.

`Memcached::HAVE_IGBINARY`  
Indica si el soporte de la función de serialización igbinary está activado.

Tipo: `bool`.

`Memcached::HAVE_JSON`  
Indica si la función de serialización JSON está disponible.

Tipo: `bool`.

`Memcached::HAVE_MSGPACK`  
Indica si el soporte del serializador msgpack está disponible.

Tipo: `bool`.

Disponible a partir de Memcached 3.0.0.

`Memcached::HAVE_ZSTD`  
Indica si la soporte de la compresión ZSTD está disponible.

Tipo: `bool`.

Disponible a partir de Memcached 3.3.0.

`Memcached::HAVE_ENCODING`  
Indica si el cifrado de datos mediante Memcached::setEncodingKey está soportado.

Tipo: `bool`.

Disponible a partir de Memcached 3.1.0.

`Memcached::HAVE_SESSION`  
Tipo: `bool`.

Disponible a partir de Memcached 3.0.0.

`Memcached::HAVE_SASL`  
Tipo: `bool`.

Disponible a partir de Memcached 3.0.0.

`Memcached::GET_EXTENDED`  
Una bandera para Memcached::get, Memcached::getMulti y Memcached::getMultiByKey para asegurar que los valores del token CAS también sean devueltos.

Disponible a partir de Memcached 3.0.0.

`Memcached::GET_PRESERVE_ORDER`  
Una opción para Memcached::getMulti y Memcached::getMultiByKey para asegurar que las claves sean devueltas en el mismo orden que su orden de solicitud. Las claves inexistentes toman entonces el valor `null`.

`Memcached::RES_SUCCESS`  
La operación ha tenido éxito.

`Memcached::RES_FAILURE`  
La operación ha fallado, de una manera u otra.

`Memcached::RES_HOST_LOOKUP_FAILURE`  
La búsqueda DNS ha fallado.

`Memcached::RES_UNKNOWN_READ_FAILURE`  
Fallo de lectura en la red.

`Memcached::RES_PROTOCOL_ERROR`  
Comando incorrecto en el protocolo memcached.

`Memcached::RES_CLIENT_ERROR`  
Error del lado del cliente.

`Memcached::RES_SERVER_ERROR`  
Error del lado del servidor.

`Memcached::RES_WRITE_FAILURE`  
Fallo de escritura en la red.

`Memcached::RES_DATA_EXISTS`  
Fallo de comparación y intercambio: el elemento que se intenta almacenar ha sido modificado desde la última lectura.

`Memcached::RES_NOTSTORED`  
El elemento no ha sido almacenado, pero no debido a un error. Esto es normal, y significa que una condición para un añadido "`add`" o un reemplazo "`replace`" no ha sido satisfecha, o que un elemento ha sido puesto en una cola de borrado.

`Memcached::RES_NOTFOUND`  
El elemento con esta clave no ha sido encontrado (con una operación "`get`" o "`cas`").

`Memcached::RES_PARTIAL_READ`  
Error de lectura parcial en la red.

`Memcached::RES_SOME_ERRORS`  
Han ocurrido errores durante una lectura múltiple.

`Memcached::RES_NO_SERVERS`  
Lista de servidores vacía.

`Memcached::RES_END`  
Fin del conjunto de resultados.

`Memcached::RES_ERRNO`  
Error del sistema.

`Memcached::RES_BUFFERED`  
La operación ha sido bufferizada.

`Memcached::RES_TIMEOUT`  
El tiempo de ejecución de la operación ha expirado.

`Memcached::RES_BAD_KEY_PROVIDED`  
Clave incorrecta.

`Memcached::RES_STORED`  
Elemento almacenado.

`Memcached::RES_DELETED`  
Elemento eliminado.

`Memcached::RES_STAT`  
Estadísticas.

`Memcached::RES_ITEM`  
Elemento.

`Memcached::RES_NOT_SUPPORTED`  
No soportado.

`Memcached::RES_FETCH_NOTFINISHED`  
Recuperación no terminada.

`Memcached::RES_SERVER_MARKED_DEAD`  
Servidor marcado como muerto.

`Memcached::RES_UNKNOWN_STAT_KEY`  
Clave de estadística desconocida.

`Memcached::RES_INVALID_HOST_PROTOCOL`  
Protocolo de host inválido.

`Memcached::RES_MEMORY_ALLOCATION_FAILURE`  
Fallo de asignación de memoria.

`Memcached::RES_CONNECTION_SOCKET_CREATE_FAILURE`  
No se puede crear un socket.

`Memcached::RES_PAYLOAD_FAILURE`  
Fallo de procesamiento: no se puede comprimir, descomprimir o serializar el valor.

`Memcached::RES_AUTH_PROBLEM`  
Disponible a partir de Memcached 3.0.0.

`Memcached::RES_AUTH_FAILURE`  
Disponible a partir de Memcached 3.0.0.

`Memcached::RES_AUTH_CONTINUE`  
Disponible a partir de Memcached 3.0.0.

`Memcached::RES_E2BIG`  
Disponible a partir de Memcached 3.0.0.

`Memcached::RES_KEY_TOO_BIG`  
Disponible a partir de Memcached 3.0.0.

`Memcached::RES_SERVER_TEMPORARILY_DISABLED`  
Disponible a partir de Memcached 3.0.0.

`Memcached::RES_SERVER_MEMORY_ALLOCATION_FAILURE`  
Disponible a partir de Memcached 3.0.0.
