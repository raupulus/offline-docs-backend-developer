---
title: La clase EventDnsBase
source_url: https://www.php.net/manual/es/class.eventdnsbase.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventdnsbase.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 7cecc752c
order: 19830
---

## Introducción

Representa la estructura base DNS de Libevent. Utilizada para resolver DNS de forma asíncrona, para analizar ficheros de configuración como resolv.conf etc.

## Sinopsis de la clase

EventDnsBase

final

EventDnsBase

Constantes

const

int

EventDnsBase::OPTION_SEARCH

1

const

int

EventDnsBase::OPTION_NAMESERVERS

2

const

int

EventDnsBase::OPTION_MISC

4

const

int

EventDnsBase::OPTION_HOSTSFILE

8

const

int

EventDnsBase::OPTIONS_ALL

15

const

int

EventDnsBase::DISABLE_WHEN_INACTIVE

32768

const

int

EventDnsBase::INITIALIZE_NAMESERVERS

1

const

int

EventDnsBase::NAMESERVERS_NO_DEFAULT

65536

Métodos

## Constantes predefinidas

`EventDnsBase::OPTION_SEARCH`  
Solicita leer el dominio y buscar los campos desde el fichero `resolv.conf` y la opción `ndots`, y los utiliza para decidir qué dominio (si lo hay) debe ser utilizado para buscar los nombres de hosts que no están totalmente cualificados.

`EventDnsBase::OPTION_NAMESERVERS`  
Solicita conocer los nombres de los servidores desde el fichero `resolv.conf`.

`EventDnsBase::OPTION_MISC`  

`EventDnsBase::OPTION_HOSTSFILE`  
Solicita leer una lista de hosts desde el fichero `/etc/hosts` como parte de la carga del fichero `resolv.conf`.

`EventDnsBase::OPTIONS_ALL`  
Solicita conocer todo el contenido del fichero `resolv.conf`.

`EventDnsBase::DISABLE_WHEN_INACTIVE`  
No impide que el bucle de eventos de libevent termine cuando no se tienen peticiones DNS activas.

`EventDnsBase::INITIALIZE_NAMESERVERS`  
Procesar el fichero `resolv.conf`.

`EventDnsBase::NAMESERVERS_NO_DEFAULT`  
No añadir un servidor de nombres por omisión si no hay servidores de nombres en el fichero `resolv.conf`.
