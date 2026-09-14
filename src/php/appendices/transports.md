---
title: Lista de los modos de transporte de sockets disponibles
source_url: https://www.php.net/manual/es/transports.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/transports.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: true
translation_revision: ae90ecc93
order: 1340
---

## Lista de los modos de transporte de sockets disponibles

A continuación se presenta la lista de los diferentes modos de transporte, en formato URL, de los que PHP dispone internamente para los flujos que explotan los sockets, tales como `fsockopen` y `stream_socket_client`. Estos modos de transporte *no se aplican* a la extensión [Funciones de socket](#ref.sockets) de la extensión Sockets

Para conocer la lista de los modos de transporte instalados en su versión de PHP, utilice `stream_get_transports`.

## Dominios de Internet: TCP, UDP, SSL y TLS

`ssl://`, `tls://`, `sslv2://` & `sslv3://`.

> [!NOTE]
> Los transportes `sslv2://` y `sslv3://` están obsoletos y no deben utilizarse. Se documentan únicamente por compatibilidad con versiones anteriores.

> [!NOTE]
> Si no se especifica ningún transporte, se utiliza `tcp://`.

- `127.0.0.1`

- `fe80::1`

- `www.example.com`

- `tcp://127.0.0.1`

- `tcp://fe80::1`

- `tcp://www.example.com`

- `udp://www.example.com`

- `ssl://www.example.com`

- `tls://www.example.com`

Los sockets del dominio de Internet utilizan un número de puerto además de la dirección del host. En el caso de `fsockopen`, se especifica en el segundo parámetro y, por lo tanto, no tiene impacto en el formato del modo de transporte. Con `stream_socket_client` y otras funciones de la misma familia, el número de puerto se especifica como un sufijo en la URL de transporte, identificado por el signo de dos puntos.

- `tcp://127.0.0.1:80`

- `tcp://[fe80::1]:80`

- `tcp://www.example.com:80`

> [!NOTE]
> En el segundo ejemplo anterior, los ejemplos en IPv4 y los nombres de host son idénticos, pero las IPv6 se colocan entre corchetes, además de tener los dos puntos y el número de puerto: `[fe80::1]`. Esto permite distinguir los dos puntos utilizados en IPv6 y los dos puntos utilizados para delimitar el número de puerto.

Los modos `ssl://` y `tls://` (disponibles únicamente cuando el soporte OpenSSL está compilado con PHP) son extensiones de `tcp://` que incluyen el cifrado SSL.

`ssl://` intentará negociar una conexión SSL/TLS segura según las capacidades y las preferencias tanto del cliente como del host remoto. Los protocolos que pueden ser utilizados están determinados por la configuración de OpenSSL y por las opciones proporcionadas a través de `stream_context_create`, como `ssl.crypto_method`.

Los protocolos SSLv2 y SSLv3 están obsoletos y son inseguros. Su uso está fuertemente desaconsejado y ya no están habilitados por defecto en las versiones modernas de PHP y OpenSSL.

## Dominio Unix: UNIX y UDG

`unix://` y `udg://`.

- `unix:///tmp/mysock`

- `udg:///tmp/mysock`

`unix://` proporciona acceso a un flujo de tipo socket, en un dominio Unix. `udg://` proporciona un modo de transporte alternativo, con un protocolo de datagramas de usuario.

Los sockets del dominio Unix, a diferencia de los del dominio de Internet, no utilizan un número de puerto. En este caso, el parámetro `portno` de `fsockopen` debe valer 0.

> [!NOTE]
> Los sockets del dominio Unix no son compatibles con Windows.
