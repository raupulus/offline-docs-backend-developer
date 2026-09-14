---
title: La clase ZMQ
source_url: https://www.php.net/manual/es/class.zmq.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zmq/zmq.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zmq
translation_status: ready
translation_reviewed: false
translation_revision: e50e79746
order: 109070
---

## Introducción

## Sinopsis de la clase

ZMQ

ZMQ

Constantes

const

int

ZMQ::SOCKET_PAIR

const

int

ZMQ::SOCKET_PUB

const

int

ZMQ::SOCKET_SUB

const

int

ZMQ::SOCKET_REQ

const

int

ZMQ::SOCKET_REP

const

int

ZMQ::SOCKET_XREQ

const

int

ZMQ::SOCKET_XREP

const

int

ZMQ::SOCKET_PUSH

const

int

ZMQ::SOCKET_PULL

const

int

ZMQ::SOCKET_ROUTER

const

int

ZMQ::SOCKET_DEALER

const

int

ZMQ::SOCKET_XPUB

const

int

ZMQ::SOCKET_XSUB

const

int

ZMQ::SOCKET_STREAM

const

int

ZMQ::SOCKOPT_HWM

const

int

ZMQ::SOCKOPT_SNDHWM

const

int

ZMQ::SOCKOPT_RCVHWM

const

int

ZMQ::SOCKOPT_AFFINITY

const

int

ZMQ::SOCKOPT_IDENTITY

const

int

ZMQ::SOCKOPT_SUBSCRIBE

const

int

ZMQ::SOCKOPT_UNSUBSCRIBE

const

int

ZMQ::SOCKOPT_RATE

const

int

ZMQ::SOCKOPT_RECOVERY_IVL

const

int

ZMQ::SOCKOPT_RECONNECT_IVL

const

int

ZMQ::SOCKOPT_RECONNECT_IVL_MAX

const

int

ZMQ::SOCKOPT_MCAST_LOOP

const

int

ZMQ::SOCKOPT_SNDBUF

const

int

ZMQ::SOCKOPT_RCVBUF

const

int

ZMQ::SOCKOPT_RCVMORE

const

int

ZMQ::SOCKOPT_TYPE

const

int

ZMQ::SOCKOPT_LINGER

const

int

ZMQ::SOCKOPT_BACKLOG

const

int

ZMQ::SOCKOPT_MAXMSGSIZE

const

int

ZMQ::SOCKOPT_SNDTIMEO

const

int

ZMQ::SOCKOPT_RCVTIMEO

const

int

ZMQ::SOCKOPT_IPV4ONLY

const

int

ZMQ::SOCKOPT_LAST_ENDPOINT

const

int

ZMQ::SOCKOPT_TCP_KEEPALIVE_IDLE

const

int

ZMQ::SOCKOPT_TCP_KEEPALIVE_CNT

const

int

ZMQ::SOCKOPT_TCP_KEEPALIVE_INTVL

const

int

ZMQ::SOCKOPT_TCP_ACCEPT_FILTER

const

int

ZMQ::SOCKOPT_TCP_ACCEPT_FILTER

const

int

ZMQ::SOCKOPT_DELAY_ATTACH_ON_CONNECT

const

int

ZMQ::SOCKOPT_XPUB_VERBOSE

const

int

ZMQ::SOCKOPT_ROUTER_RAW

const

int

ZMQ::SOCKOPT_IPV6

const

int

ZMQ::CTXOPT_MAX_SOCKETS

const

int

ZMQ::POLL_IN

const

int

ZMQ::POLL_OUT

const

int

ZMQ::MODE_NOBLOCK

const

int

ZMQ::MODE_DONTWAIT

const

int

ZMQ::MODE_SNDMORE

const

int

ZMQ::ERR_INTERNAL

const

int

ZMQ::ERR_EAGAIN

const

int

ZMQ::ERR_ENOTSUP

const

int

ZMQ::ERR_EFSM

const

int

ZMQ::ERR_ETERM

Métodos

## Constantes predefinidas

## Tipos de constantes de ZMQ

`ZMQ::SOCKET_PAIR`  
Patrón de par exclusivo

`ZMQ::SOCKET_PUB`  
Socket publicador

`ZMQ::SOCKET_SUB`  
Socket suscriptor

`ZMQ::SOCKET_REQ`  
Socket de petición

`ZMQ::SOCKET_REP`  
Socket de respuesta

`ZMQ::SOCKET_XREQ`  
Alias de SOCKET_DEALER

`ZMQ::SOCKET_XREP`  
Alias de SOCKET_ROUTER

`ZMQ::SOCKET_PUSH`  
Socket "push" ascendente de tubería

`ZMQ::SOCKET_PULL`  
Socket "pull" descendente de tubería

`ZMQ::SOCKET_ROUTER`  
Socket REP ampliado que puede dirigir réplicas a solicitantes

`ZMQ::SOCKET_DEALER`  
Sokect REQ ampliado que equilibra a todos los pares conectados

`ZMQ::SOCKET_XPUB`  
Similar a SOCKET_PUB, excepto que se pueden recibir suscripciones como mensajes. El mensaje de suscripción es 0 (cancelar suscripción) o 1 (suscribirse) seguido del tema.

`ZMQ::SOCKET_XSUB`  
Similar a SOCKET_SUB, excepto que se puede enviar suscripciones como mensajes. Véase SOCKET_XPUB para el formato.

`ZMQ::SOCKET_STREAM`  
Utilizada para enviar y recibir datos TCP de un par que no sea ØMQ. Disponible si se compila con ZeroMQ 4.0 o superior (Valor: `int`).

`ZMQ::SOCKOPT_HWM`  
La marca de agua para mensajes entrantes y salientes es un límite firme sobre el número máximo de mensajes salientes que ØMQ pondrá en cola en la memoria para cualquier único par con que se comunique el socket especificado. Establecer esta opción en un socket solamente afectará a las conexiones realizadas después de haber establecido esta opción. En ZeroMQ 3.x esto es una envoltura para establecer tanto SNDHWM como RCVHWM. (Valor: `int`).

`ZMQ::SOCKOPT_SNDHWM`  
La opción ZMQ_SNDHWM establece la marca de agua alta para mensajes salientes en el socket especificado. Disponible si se compila con ZeroMQ 3.0 o superior (Valor: `int`).

`ZMQ::SOCKOPT_RCVHWM`  
La opción SOCKOPT_RCVHWM establece la marca de agua alta para mensajes entrantes en el socket especificado. Disponible si se compila con ZeroMQ 3.0 o superior (Valor: `int`).

`ZMQ::SOCKOPT_AFFINITY`  
Establecer la afinidad del hilo de E/S (Valor: `int`)

`ZMQ::SOCKOPT_IDENTITY`  
Establecer la identidad del socket identity (Valor: `string`)

`ZMQ::SOCKOPT_SUBSCRIBE`  
Establecer un filtro para mensajes. Válido para socket suscriptores socket (Valor: `string`)

`ZMQ::SOCKOPT_UNSUBSCRIBE`  
Eliminar un filtro para mensajes. Válido para socket suscriptores (Valor: `string`)

`ZMQ::SOCKOPT_RATE`  
Establecer la tasa para los socket de multidifusión (pgm) (Valor: `int` \>= 0)

`ZMQ::SOCKOPT_RECOVERY_IVL`  
Establecer el intervalo de recuperación de la multidifusión (Valor: `int` \>= 0)

`ZMQ::SOCKOPT_RECONNECT_IVL`  
Establecer el intervañp de reconexión inicial (Valor: `int` \>= 0)

`ZMQ::SOCKOPT_RECONNECT_IVL_MAX`  
Establecer el intervalo de reconexión máximo (Valor: `int` \>= 0)

`ZMQ::SOCKOPT_MCAST_LOOP`  
Controlar el loopback de la multidifusión (Valor: `int` \>= 0)

`ZMQ::SOCKOPT_SNDBUF`  
Establecer el tamaño del buffer de transmisión del kernel (Valor: `int` \>= 0)

`ZMQ::SOCKOPT_RCVBUF`  
Establecer el tamaño del buffer de recepción del kernel (Valor: `int` \>= 0)

`ZMQ::SOCKOPT_RCVMORE`  
Recibir mensajes multiparte (Valor: `int`)

`ZMQ::SOCKOPT_TYPE`  
Obtener el tipo de socket. Válido para getSockOpt (Valor: `int`)

`ZMQ::SOCKOPT_LINGER`  
El valor de permanencia ("linger") del socket. Especifica cuánto quedará esperando el socket intentando volcar mensajes después de haber sido cerrado (Valor: `int`)

`ZMQ::SOCKOPT_BACKLOG`  
La opción SOCKOPT_BACKLOG establece la longitud máxima de la cola de las conexiones de pares salientes para el socket especificado; esto solamente se aplica a transportes orientados a conexión. (Valor: `int`)

`ZMQ::SOCKOPT_MAXMSGSIZE`  
Limita el tamaño máximo del mensaje entrante. Un valor de -1 significa sin límite. Disponible si se compila con ZeroMQ 3.0 o superior (Valor: `int`)

`ZMQ::SOCKOPT_SNDTIMEO`  
Establecer el tiempo de espera para la operación de envío del socket. Un valor de -1 significa sin límite. Disponible si se compila con ZeroMQ 3.0 o superior (Valor: `int`)

`ZMQ::SOCKOPT_RCVTIMEO`  
Establecer el tiempo de espera para la operación de recepción del socket. Un valor de -1 significa sin límite. Disponible si se compila con ZeroMQ 3.0 o superior (Valor: `int`)

`ZMQ::SOCKOPT_IPV4ONLY`  
Deshabilitar el soporte para IPV6 si es 1. Disponible si se compila con ZeroMQ 3.x (Valor: `int`)

`ZMQ::SOCKOPT_LAST_ENDPOINT`  
Obtener el último extremo conectado - para emplear con puertos comodín \*. Disponible si se compila con ZeroMQ 3.0 o superior (Valor: `string`)

`ZMQ::SOCKOPT_TCP_KEEPALIVE_IDLE`  
Tiempo de inactividad para el mensaje "keepalive" de TCP. Disponible si se compila con ZeroMQ 3.0 o superior (Valor: `int`)

`ZMQ::SOCKOPT_TCP_KEEPALIVE_CNT`  
Cuante de tiempo para el mensaje "keepalive" de TCP. Disponible si se compila con ZeroMQ 3.0 o superior (Valor: `int`)

`ZMQ::SOCKOPT_TCP_KEEPALIVE_INTVL`  
Intervalo para el mensaje "keepalive" de TCP. Disponible si se compila con ZeroMQ 3.0 o superior (Valor: `int`)

`ZMQ::SOCKOPT_DELAY_ATTACH_ON_CONNECT`  
Establecer un string CIDR para comparar con conexiones TCP entrantes. Disponible si se compila con ZeroMQ 3.0 o superior (Valor: `string`)

`ZMQ::SOCKOPT_TCP_ACCEPT_FILTER`  
Establecer un string CIDR para comparar con conexioines TCP entrantes. Disponible si se compila con ZeroMQ 3.0 o superior (Valor: `string`)

`ZMQ::SOCKOPT_XPUB_VERBOSE`  
Establcer el XPUB para recibir un mensaje de aplicación en cada instancia de una subscripción. Disponible si se compila con ZeroMQ 3.0 o superior (Valor: `string`)

`ZMQ::SOCKOPT_ROUTER_RAW`  
Establece el modo puro ("raw") del ROUTER, cuando se establece a 1. En el modo puro, al usar el transporte tcp://, el socket leerá y escribirá sin el encuadrre de ZeroMQ. Disponible si se compila con ZeroMQ 4.0 o superior (Valor: `string`)

`ZMQ::SOCKOPT_IPV6`  
Habilitar IPV6. Disponible si se compila con ZeroMQ 4.0 o superior (Valor: `string`)

`ZMQ::CTXOPT_MAX_SOCKETS`  
El límite de socket para este contexto. Disponible si se compila con ZeroMQ 3.x o superior (Valor: `int`)

`ZMQ::POLL_IN`  
Sondeo para datos entrantes

`ZMQ::POLL_OUT`  
Sondeo para datos salientes

`ZMQ::MODE_NOBLOCK`  
Operación de no espera. Obsoleta, emplee ZMQ::MODE_DONTWAIT en su lugar

`ZMQ::MODE_DONTWAIT`  
Operación de no espera

`ZMQ::MODE_SNDMORE`  
Enviar un mensaje multiparte

`ZMQ::DEVICE_FORWARDER`  
Dispositivo reenviador

`ZMQ::DEVICE_QUEUE`  
Dispositivo de cola

`ZMQ::DEVICE_STREAMER`  
Dispositivo de flujo

`ZMQ::ERR_INTERNAL`  
Error interno de la extensión ZMQ

`ZMQ::ERR_EAGAIN`  
Implica que la operación debería esperar esperar cuando se emplee ZMQ::MODE_DONTWAIT

`ZMQ::ERR_ENOTSUP`  
La operación no está soportada por el tipo de socket

`ZMQ::ERR_EFSM`  
La operación no se pudo ejecutar debido a que el socket no está en un estado correcto

`ZMQ::ERR_ETERM`  
El contexto ha sido finalizado
