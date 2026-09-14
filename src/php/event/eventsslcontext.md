---
title: La clase EventSslContext
source_url: https://www.php.net/manual/es/class.eventsslcontext.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventsslcontext.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 20420
---

## Introducción

Representa la estructura `SSL_CTX`. Proporciona métodos y propiedades para configurar el contexto SSL.

## Sinopsis de la clase

EventSslContext

final

EventSslContext

Constantes

const

int

EventSslContext::SSLv2_CLIENT_METHOD

1

const

int

EventSslContext::SSLv3_CLIENT_METHOD

2

const

int

EventSslContext::SSLv23_CLIENT_METHOD

3

const

int

EventSslContext::TLS_CLIENT_METHOD

4

const

int

EventSslContext::SSLv2_SERVER_METHOD

5

const

int

EventSslContext::SSLv3_SERVER_METHOD

6

const

int

EventSslContext::SSLv23_SERVER_METHOD

7

const

int

EventSslContext::TLS_SERVER_METHOD

8

const

int

EventSslContext::OPT_LOCAL_CERT

1

const

int

EventSslContext::OPT_LOCAL_PK

2

const

int

EventSslContext::OPT_PASSPHRASE

3

const

int

EventSslContext::OPT_CA_FILE

4

const

int

EventSslContext::OPT_CA_PATH

5

const

int

EventSslContext::OPT_ALLOW_SELF_SIGNED

6

const

int

EventSslContext::OPT_VERIFY_PEER

7

const

int

EventSslContext::OPT_VERIFY_DEPTH

8

const

int

EventSslContext::OPT_CIPHERS

9

Propiedades

public

string

local_cert

public

string

local_pk

Métodos

## Propiedades

`local_cert`  
Ruta hacia el fichero que contiene el certificado en el sistema de ficheros. Debe ser un fichero codificado PEM que contiene los certificados. Puede, opcionalmente, contener la cadena del certificado del emisor.

`local_pk`  
Ruta hacia el fichero que contiene la clave privada local.

## Constantes predefinidas

`EventSslContext::SSLv2_CLIENT_METHOD`  
Método cliente SSLv2. Ver la página del manual sobre `SSL_CTX_new(3)`.

`EventSslContext::SSLv3_CLIENT_METHOD`  
Método cliente SSLv3. Ver la página del manual sobre `SSL_CTX_new(3)`.

`EventSslContext::SSLv23_CLIENT_METHOD`  
Método cliente SSLv23. Ver la página del manual sobre `SSL_CTX_new(3)`.

`EventSslContext::TLS_CLIENT_METHOD`  
Método cliente TLS. Ver la página del manual sobre `SSL_CTX_new(3)`.

`EventSslContext::SSLv2_SERVER_METHOD`  
Método servidor SSLv2. Ver la página del manual sobre `SSL_CTX_new(3)`.

`EventSslContext::SSLv3_SERVER_METHOD`  
Método servidor SSLv3. Ver la página del manual sobre `SSL_CTX_new(3)`.

`EventSslContext::SSLv23_SERVER_METHOD`  
Método servidor SSLv23. Ver la página del manual sobre `SSL_CTX_new(3)`.

`EventSslContext::TLS_SERVER_METHOD`  
Método servidor TLS. Ver la página del manual sobre `SSL_CTX_new(3)`.

`EventSslContext::OPT_LOCAL_CERT`  
Clave para un elemento del array que contiene las opciones, utilizado en el método EventSslContext::\_\_construct. Las opciones apuntan a la ruta del certificado local.

`EventSslContext::OPT_LOCAL_PK`  
Clave para un elemento del array que contiene las opciones, utilizado en el método EventSslContext::\_\_construct. Las opciones apuntan a la ruta de la clave privada.

`EventSslContext::OPT_PASSPHRASE`  
Clave para un elemento del array que contiene las opciones, utilizado en el método EventSslContext::\_\_construct. Representa la contraseña del certificado.

`EventSslContext::OPT_CA_FILE`  
Clave para un elemento del array que contiene las opciones, utilizado en el método EventSslContext::\_\_construct. Representa la ruta hacia el fichero de la autoridad del certificado.

`EventSslContext::OPT_CA_PATH`  
Clave para un elemento del array que contiene las opciones, utilizado en el método EventSslContext::\_\_construct. Representa la ruta en la que se debe buscar el fichero de la autoridad del certificado.

`EventSslContext::OPT_ALLOW_SELF_SIGNED`  
Clave para un elemento del array que contiene las opciones, utilizado en el método EventSslContext::\_\_construct. Representa una opción que permite los certificados autofirmados.

`EventSslContext::OPT_VERIFY_PEER`  
Clave para un elemento del array que contiene las opciones, utilizado en el método EventSslContext::\_\_construct. Representa una opción que indica a Event que verifique los pares.

`EventSslContext::OPT_VERIFY_DEPTH`  
Clave para un elemento del array que contiene las opciones, utilizado en el método EventSslContext::\_\_construct. Representa la profundidad máxima de la verificación de la cadena del certificado que debe ser permitida para el contexto SSL.

`EventSslContext::OPT_CIPHERS`  
Clave para un elemento del array que contiene las opciones, utilizado en el método EventSslContext::\_\_construct. Representa la lista de cifrados para el contexto SSL.
