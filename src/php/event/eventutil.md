---
title: La clase EventUtil
source_url: https://www.php.net/manual/es/class.eventutil.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventutil.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 940ea8c1b
order: 20500
---

## Introducción

La clase `EventUtil` es un esqueleto con métodos y constantes adicionales.

## Sinopsis de la clase

EventUtil

final

EventUtil

Constantes

const

int

EventUtil::AF_INET

2

const

int

EventUtil::AF_INET6

10

const

int

EventUtil::AF_UNSPEC

0

const

int

EventUtil::LIBEVENT_VERSION_NUMBER

33559808

const

int

EventUtil::SO_DEBUG

1

const

int

EventUtil::SO_REUSEADDR

2

const

int

EventUtil::SO_KEEPALIVE

9

const

int

EventUtil::SO_DONTROUTE

5

const

int

EventUtil::SO_LINGER

13

const

int

EventUtil::SO_BROADCAST

6

const

int

EventUtil::SO_OOBINLINE

10

const

int

EventUtil::SO_SNDBUF

7

const

int

EventUtil::SO_RCVBUF

8

const

int

EventUtil::SO_SNDLOWAT

19

const

int

EventUtil::SO_RCVLOWAT

18

const

int

EventUtil::SO_SNDTIMEO

21

const

int

EventUtil::SO_RCVTIMEO

20

const

int

EventUtil::SO_TYPE

3

const

int

EventUtil::SO_ERROR

4

const

int

EventUtil::SOL_SOCKET

1

const

int

EventUtil::SOL_TCP

6

const

int

EventUtil::SOL_UDP

17

const

int

EventUtil::IPPROTO_IP

0

const

int

EventUtil::IPPROTO_IPV6

41

Métodos

## Constantes predefinidas

`EventUtil::AF_INET`  
Familia de direcciones IPv4

`EventUtil::AF_INET6`  
Familia de direcciones IPv6

`EventUtil::AF_UNSPEC`  
Familia de direcciones IP no especificada

`EventUtil::SO_DEBUG`  
Opción del socket. Activa la depuración del socket. Solo permitido para los procesos con la capacidad `CAP_NET_ADMIN` o un ID de usuario efectivo de `0`. (Añadido en event-1.6.0.)

`EventUtil::SO_REUSEADDR`  
Opción del socket. Indica que las reglas utilizadas en la validación de direcciones proporcionadas en una llamada a `bind(2)` deben permitir la reutilización de direcciones locales. Ver la página del manual sobre `socket(7)`. (Añadido en event-1.6.0.)

`EventUtil::SO_KEEPALIVE`  
Opción del socket. Activa el envío de mensajes keep-alive en los sockets de conexión. Espera un entero. Ver la página del manual sobre `socket(7)`. (Añadido en event-1.6.0.)

`EventUtil::SO_DONTROUTE`  
Opción del socket. Ver la página del manual sobre `socket(7)`. (Añadido en event-1.6.0.)

`EventUtil::SO_LINGER`  
Opción del socket. Cuando está activo, una llamada a `close(2)` o a `shutdown(2)` no devolverá hasta que todos los mensajes de la cola del socket hayan sido enviados, o hasta que se alcance el tiempo máximo de espera del linger. De lo contrario, las llamadas devolverán inmediatamente y el cierre se realizará en segundo plano. Ver la página del manual sobre `socket(7)`. (Añadido en event-1.6.0.)

`EventUtil::SO_BROADCAST`  
Opción del socket. Indica si la transmisión de mensajes de broadcast está soportada. Ver la página del manual sobre `socket(7)`. (Añadido en event-1.6.0.)

`EventUtil::SO_OOBINLINE`  
Opción del socket. Ver la página del manual sobre `socket(7)`. (Añadido en event-1.6.0.)

`EventUtil::SO_SNDBUF`  
Opción del socket. Ver la página del manual sobre `socket(7)`. (Añadido en event-1.6.0.)

`EventUtil::SO_RCVBUF`  
Opción del socket. Ver la página del manual sobre `socket(7)`. (Añadido en event-1.6.0.)

`EventUtil::SO_SNDLOWAT`  
Opción del socket. Ver la página del manual sobre `socket(7)`. (Añadido en event-1.6.0.)

`EventUtil::SO_RCVLOWAT`  
Opción del socket. Ver la página del manual sobre `socket(7)`. (Añadido en event-1.6.0.)

`EventUtil::SO_SNDTIMEO`  
Opción del socket. Ver la página del manual sobre `socket(7)`. (Añadido en event-1.6.0.)

`EventUtil::SO_RCVTIMEO`  
Opción del socket. Ver la página del manual sobre `socket(7)`. (Añadido en event-1.6.0.)

`EventUtil::SO_TYPE`  
Opción del socket. Ver la página del manual sobre `socket(7)`. (Añadido en event-1.6.0.)

`EventUtil::SO_ERROR`  
Opción del socket. Ver la página del manual sobre `socket(7)`. (Añadido en event-1.6.0.)

`EventUtil::SOL_SOCKET`  
Opción del socket. Ver la página del manual sobre `socket(7)`. (Añadido en event-1.6.0.)

`EventUtil::SOL_TCP`  
Opción del socket. Ver la página del manual sobre `socket(7)`. (Añadido en event-1.6.0.)

`EventUtil::SOL_UDP`  
Opción del socket. Ver la página del manual sobre `socket(7)`. (Añadido en event-1.6.0.)

`EventUtil::IPPROTO_IP`  
Ver la página del manual sobre `socket(7)`. (Añadido en event-1.6.0.)

`EventUtil::IPPROTO_IPV6`  
Ver la página del manual sobre `socket(7)`. (Añadido en event-1.6.0.)

`EventUtil::LIBEVENT_VERSION_NUMBER`  
Número de versión de Libevent en el momento en que la extensión Event fue compilada con la biblioteca.
