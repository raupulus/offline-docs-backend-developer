---
title: socket_get_option
description: Lee las opciones del socket
source_url: https://www.php.net/manual/es/function.socket-get-option.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-get-option.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: false
translation_revision: e50e79746
order: 75670
---

socket_get_option

Lee las opciones del socket

## Descripción

```php
socket_get_option(Socket $socket, int $level, int $option): array
```php

`socket_get_option` recupera el valor de la opción especificada por el argumento `option` para el socket especificado por el argumento `socket`.

## Parámetros

`socket`  
Una instancia de `Socket` creada por `socket_create` o `socket_accept`.

`level`  
El argumento `level` especifica la capa de protocolo de la opción. Por ejemplo, para conocer las opciones de la capa socket, el valor `SOL_SOCKET` del argumento `level` será utilizado. Otros niveles, como `TCP`, pueden ser utilizados especificando el número del protocolo de esta capa. Los números de protocolos pueden ser encontrados utilizando la función `getprotobyname`.

`option`  
<table>
<caption>Opciones disponibles para los sockets</caption>
<thead>
<tr>
<th>Opción</th>
<th>Descripción</th>
<th>Tipo</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>SO_DEBUG</code></td>
<td>Reporta si las informaciones de depuración son registradas o no.</td>
<td><code>int</code></td>
</tr>
<tr>
<td><code>SO_BROADCAST</code></td>
<td>Reporta si la transmisión de anuncios globales es soportada o no.</td>
<td><code>int</code></td>
</tr>
<tr>
<td><code>SO_REUSEADDR</code></td>
<td>Indica si las direcciones locales pueden ser reutilizadas o no.</td>
<td><code>int</code></td>
</tr>
<tr>
<td><code>SO_REUSEPORT</code></td>
<td>Indica si los puertos locales pueden ser reutilizados.</td>
<td><code>int</code></td>
</tr>
<tr>
<td><code>SO_KEEPALIVE</code></td>
<td>Reporta si las conexiones son persistentes con transmisiones periódicas de mensajes o no. Si el socket conectado falla en respuesta a estos mensajes, la conexión es interrumpida y el proceso escribirá sobre este socket una notificación con un señal SIGPIPE.</td>
<td><code>int</code></td>
</tr>
<tr>
<td><code>SO_LINGER</code></td>
<td><p>Reporta si el socket <code>socket</code> se demora en la función <code>socket_close</code> si hay datos presentes o no. Por omisión, cuando el socket es cerrado, <code>socket_close</code> intenta enviar todos los datos que no han sido enviados aún.</p>
<p>Si <code>l_onoff</code> no vale cero y que <code>l_linger</code> vale cero, todos los datos que no han sido enviados aún serán cancelados y RST (reinicialización) será enviado en el caso de una conexión orientada socket.</p>
<p>Por otro lado, si <code>l_onoff</code> no vale cero y <code>l_linger</code> no vale cero, <code>socket_close</code> bloqueará hasta que los datos no enviados sean enviados o durante el tiempo especificado por <code>l_linger</code>. Si el socket es no-bloqueante, <code>socket_close</code> fallará y retornará un error.</p></td>
<td><code>array</code>. El array contendrá 2 claves : <code>l_onoff</code> y <code>l_linger</code>.</td>
</tr>
<tr>
<td><code>SO_OOBINLINE</code></td>
<td>Reporta si el socket <code>socket</code> parte sobre datos en línea out-of-band o no.</td>
<td><code>int</code></td>
</tr>
<tr>
<td><code>SO_SNDBUF</code></td>
<td>Reporta las informaciones sobre el tamaño del buffer enviado.</td>
<td><code>int</code></td>
</tr>
<tr>
<td><code>SO_RCVBUF</code></td>
<td>Reporta las informaciones sobre el tamaño del buffer recibido.</td>
<td><code>int</code></td>
</tr>
<tr>
<td><code>SO_ERROR</code></td>
<td>Reporta las informaciones sobre el estado de error y lo vacía.</td>
<td><code>int</code> (no puede ser definido por la función <code>socket_set_option</code>)</td>
</tr>
<tr>
<td><code>SO_TYPE</code></td>
<td>Reporta el tipo del socket <code>socket</code> (ej. <code>SOCK_STREAM</code>).</td>
<td><code>int</code> (no puede ser definido por la función <code>socket_set_option</code>)</td>
</tr>
<tr>
<td><code>SO_DONTROUTE</code></td>
<td>Reporta si los mensajes salientes desvían los equipos estándar de encaminamiento.</td>
<td><code>int</code></td>
</tr>
<tr>
<td><code>SO_RCVLOWAT</code></td>
<td>Reporta el número mínimo de octetos al proceso para las operaciones entrantes sobre el socket <code>socket</code>.</td>
<td><code>int</code></td>
</tr>
<tr>
<td><code>SO_RCVTIMEO</code></td>
<td>Reporta el valor del tiempo límite para las operaciones entrantes.</td>
<td><code>array</code>. El array contendrá 2 claves : <code>sec</code> que es la parte representando los segundos del valor del tiempo de espera y <code>usec</code> que es la parte representando los microsegundos.</td>
</tr>
<tr>
<td><code>SO_SNDTIMEO</code></td>
<td>Reporta el valor del tiempo límite especificando el tiempo máximo de ejecución para las funciones salientes bloqueantes porque el comando de flujo impide que los datos sean enviados.</td>
<td><code>array</code>. El array contendrá 2 claves : <code>sec</code> que es la parte representando los segundos del valor del tiempo de espera y <code>usec</code> que es la parte representando los microsegundos.</td>
</tr>
<tr>
<td><code>SO_SNDLOWAT</code></td>
<td>Reporta el número mínimo de octetos al proceso para las operaciones salientes sobre el socket <code>socket</code>.</td>
<td><code>int</code></td>
</tr>
<tr>
<td><code>TCP_NODELAY</code></td>
<td>Indica si el algoritmo Nagle TCP está desactivado.</td>
<td><code>int</code></td>
</tr>
<tr>
<td><code>MCAST_JOIN_GROUP</code></td>
<td>Se une a un grupo multicast.</td>
<td>Un array con una clave <code>"group"</code>, especificando un string con las direcciones multicast IPv4 o IPv6 y una clave <code>"interface"</code>, especificando ya sea un número de interfaz (de tipo <code>int</code>), ya sea un string con el nombre de la interfaz, como <code>"eth0"</code>. <code>0</code> puede ser especificado para indicar que la interfaz debe ser seleccionada utilizando las reglas de encaminamiento (no puede ser utilizado más que con la función <code>socket_set_option</code>).</td>
</tr>
<tr>
<td><code>MCAST_LEAVE_GROUP</code></td>
<td>Abandona un grupo multicast.</td>
<td>Un array. Ver la constante <code>MCAST_JOIN_GROUP</code> para más informaciones (no puede ser utilizado más que con la función <code>socket_set_option</code>).</td>
</tr>
<tr>
<td><code>MCAST_BLOCK_SOURCE</code></td>
<td>Bloquea paquetes llegando desde una fuente específica hacia un grupo multicast específico, que habrá debido ser unido anteriormente.</td>
<td>Un array conteniendo las mismas claves que las de la constante <code>MCAST_JOIN_GROUP</code>, con una clave adicional <code>source</code>, ligado a un string especificando una dirección IPv4 o IPv6 de la fuente a bloquear (no puede ser utilizado más que con la función <code>socket_set_option</code>).</td>
</tr>
<tr>
<td><code>MCAST_UNBLOCK_SOURCE</code></td>
<td>Desbloquea (recomienza a recibir) los paquetes llegando desde una fuente específica hacia un grupo multicast específico, que habrá debido ser unido anteriormente.</td>
<td>Un array en el mismo formato que el de la constante <code>MCAST_BLOCK_SOURCE</code> (no puede ser utilizado más que con la función <code>socket_set_option</code>).</td>
</tr>
<tr>
<td><code>MCAST_JOIN_SOURCE_GROUP</code></td>
<td>Recibe paquetes destinados a un grupo multicast específico cuya dirección fuente corresponde a un valor específico.</td>
<td>Un array en el mismo formato que el de la constante <code>MCAST_BLOCK_SOURCE</code> (no puede ser utilizado más que con la función <code>socket_set_option</code>).</td>
</tr>
<tr>
<td><code>MCAST_LEAVE_SOURCE_GROUP</code></td>
<td>Deja de recibir paquetes destinados a un grupo multicast específico cuya dirección fuente corresponde a un valor específico.</td>
<td>Un array en el mismo formato que el de la constante <code>MCAST_BLOCK_SOURCE</code> (no puede ser utilizado más que con la función <code>socket_set_option</code>).</td>
</tr>
<tr>
<td><code>IP_MULTICAST_IF</code></td>
<td>La interfaz de salida para los paquetes multicast IPv4.</td>
<td>Ya sea un entero especificando el número de la interfaz, ya sea un string representando el nombre de la interfaz, por ejemplo, <code>eth0</code>. El valor <code>0</code> puede ser utilizado para indicar la tabla de encaminamiento a utilizar en la selección de la interfaz. La función <code>socket_get_option</code> retorna un índice de interfaz. Note que, a diferencia de la API C, esta opción no toma como argumento una dirección IP. Esto elimina la diferencia de interfaz entre las constantes <code>IP_MULTICAST_IF</code> y <code>IPV6_MULTICAST_IF</code>.</td>
</tr>
<tr>
<td><code>IPV6_MULTICAST_IF</code></td>
<td>La interfaz de salida para los paquetes multicast IPv6.</td>
<td>Idéntico a la constante <code>IP_MULTICAST_IF</code>.</td>
</tr>
<tr>
<td><code>IP_MULTICAST_LOOP</code></td>
<td>La política de la bucla local multicast para los paquetes IPv4 activa o desactiva el buclaje de las multidifusiones salientes, que deben haber sido unidas anteriormente. El efecto difiere sin embargo según que se aplique a Unix o a Windows, el primero siendo sobre el camino de recepción mientras que el segundo sobre el camino de envío.</td>
<td>Un entero (ya sea <code>0</code>, ya sea <code>1</code>). Para la función <code>socket_set_option</code>, cualquier valor será aceptado y será convertido en un booleano siguiendo las reglas habituales de PHP.</td>
</tr>
<tr>
<td><code>IPV6_MULTICAST_LOOP</code></td>
<td>Idéntico a la constante <code>IP_MULTICAST_LOOP</code>, pero para el IPv6.</td>
<td>Un entero. Ver la constante <code>IP_MULTICAST_LOOP</code>.</td>
</tr>
<tr>
<td><code>IP_MULTICAST_TTL</code></td>
<td>La duración de vida de los paquetes salientes multicast IPv4. Esto debe ser un valor comprendido entre 0 (no salir de la interfaz) y 255. Por omisión, el valor es a 1 (solo la red local es alcanzada).</td>
<td>Un entero entre 0 y 255.</td>
</tr>
<tr>
<td><code>IPV6_MULTICAST_HOPS</code></td>
<td>Idéntico a la constante <code>IP_MULTICAST_TTL</code>, pero para los paquetes IPv6. El valor -1 es igualmente aceptado, significando que la ruta por omisión debe ser utilizada.</td>
<td>Un entero comprendido entre -1 y 255.</td>
</tr>
<tr>
<td><code>SO_MARK</code></td>
<td>Define un identificador sobre el socket para el propósito de filtrar los paquetes sobre Linux.</td>
<td><code>int</code></td>
</tr>
<tr>
<td><code>SO_ACCEPTFILTER</code></td>
<td>Añade un filtro de aceptación sobre el socket escuchado (FreeBSD/NetBSD). Un módulo kernel de filtro de aceptación debe ser cargado primero sobre FreeBSD (ej. accf_http).</td>
<td><code>string</code> nombre del filtro (longitud 15 max).</td>
</tr>
<tr>
<td><code>SO_USER_COOKIE</code></td>
<td>Define un identificador sobre el socket para el propósito de filtrar los paquetes sobre FreeBSD.</td>
<td><code>int</code></td>
</tr>
<tr>
<td><code>SO_RTABLE</code></td>
<td>Define un identificador sobre el socket para el propósito de filtrar los paquetes sobre OpenBSD.</td>
<td><code>int</code></td>
</tr>
<tr>
<td><code>SO_DONTTRUNC</code></td>
<td>Conserva los datos no leídos.</td>
<td><code>int</code></td>
</tr>
<tr>
<td><code>SO_WANTMORE</code></td>
<td>Proporciona un índice cuando más datos están listos.</td>
<td><code>int</code></td>
</tr>
<tr>
<td><code>TCP_DEFER_ACCEPT</code></td>
<td>No notificar un socket que escucha hasta que los datos no estén listos.</td>
<td><code>int</code></td>
</tr>
<tr>
<td><code>SO_INCOMING_CPU</code></td>
<td>Recupera/Define la afinidad del cpu para un socket.</td>
<td><code>int</code></td>
</tr>
<tr>
<td><code>SO_MEMINFO</code></td>
<td>Recupera toda la meminfo de un socket.</td>
<td><code>int</code></td>
</tr>
<tr>
<td><code>SO_BPF_EXTENSIONS</code></td>
<td>Recupera las extensiones BPF soportadas por el kernel para adjuntar a un socket.</td>
<td><code>int</code></td>
</tr>
<tr>
<td><code>SO_SETFIB</code></td>
<td>Define la tabla de encaminamiento (FIB) de un socket. (FreeBSD solamente)</td>
<td><code>int</code></td>
</tr>
<tr>
<td><code>SOL_FILTER</code></td>
<td>Filtros atribuidos a un socket. (Solaris/Illumos solamente)</td>
<td><code>int</code></td>
</tr>
<tr>
<td><code>TCP_KEEPCNT</code></td>
<td>Define el número máximo de sondas keepalive TCP debería enviar antes de soltar la conexión.</td>
<td><code>int</code></td>
</tr>
<tr>
<td><code>TCP_KEEPIDLE</code></td>
<td>Define el tiempo que la conexión debe permanecer inactiva.</td>
<td><code>int</code></td>
</tr>
<tr>
<td><code>TCP_KEEPINTVL</code></td>
<td>Define el tiempo entre las sondas keepalive individuales.</td>
<td><code>int</code></td>
</tr>
<tr>
<td><code>TCP_KEEPALIVE</code></td>
<td>Define el tiempo que la conexión debe permanecer inactiva. (macOS solamente)</td>
<td><code>int</code></td>
</tr>
<tr>
<td><code>TCP_NOTSENT_LOWAT</code></td>
<td>Define el número límite de datos no enviados en la cola de escritura por el flujo de socket. (Linux solamente)</td>
<td><code>int</code></td>
</tr>
</tbody>
</table>

## Valores devueltos

Retorna el valor de la opción proporcionada, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `socket` ahora es una instancia de `Socket` ; anteriormente, era un `resource`. |

## Ejemplos

Ejemplo con `socket_get_option`

```
<?php
$socket = socket_create_listen(1223);

$linger = array('l_linger' => 1, 'l_onoff' => 1);
socket_set_option($socket, SOL_SOCKET, SO_LINGER, $linger);

var_dump(socket_get_option($socket, SOL_SOCKET, SO_REUSEADDR));
?>

    
```php

## Véase también

`socket_create_listen`, `socket_set_option`
