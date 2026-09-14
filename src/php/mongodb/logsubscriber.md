---
title: La interfaz MongoDB\Driver\Monitoring\LogSubscriber
source_url: https://www.php.net/manual/es/class.mongodb-driver-monitoring-logsubscriber.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/logsubscriber.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50290
---

## Introducción

Las clases que implementan esta interfaz pueden ser registradas como observadores y recibir mensajes de registro de la extensión. Esto es similar al registro de depuración basado en flujos (es decir, [mongodb.debug](#ini.mongodb.debug)) excepto que los mensajes de registro de nivel trace no son *recibidos*.

Al igual que con el registro basado en flujos, solo es posible registrar un registrador globalmente utilizando `MongoDB\Driver\Monitoring\addSubscriber`. La extensión no es capaz de distinguir los mensajes de registro para objetos `MongoDB\Driver\Manager` individuales.

## Sinopsis de la interfaz

MongoDB\Driver\Monitoring\LogSubscriber

MongoDB\Driver\Monitoring\LogSubscriber

MongoDB\Driver\Monitoring\Subscriber

Constantes

const

int

MongoDB\Driver\Monitoring\LogSubscriber::LEVEL_ERROR

0

const

int

MongoDB\Driver\Monitoring\LogSubscriber::LEVEL_CRITICAL

1

const

int

MongoDB\Driver\Monitoring\LogSubscriber::LEVEL_WARNING

2

const

int

MongoDB\Driver\Monitoring\LogSubscriber::LEVEL_MESSAGE

3

const

int

MongoDB\Driver\Monitoring\LogSubscriber::LEVEL_INFO

4

const

int

MongoDB\Driver\Monitoring\LogSubscriber::LEVEL_DEBUG

5

Métodos

## Constantes predefinidas

`MongoDB\Driver\Monitoring\LogSubscriber::LEVEL_ERROR`  
El nivel de registro de error. Una condición de error que la extensión no es capaz de reportar a través de su API. Es el nivel de registro más severo de la extensión.

`MongoDB\Driver\Monitoring\LogSubscriber::LEVEL_CRITICAL`  
El nivel de registro crítico. Una condición de error con una severidad ligeramente inferior. Esta constante existe para la coherencia con libmongoc; sin embargo, la extensión es poco susceptible de utilizarla en la práctica.

`MongoDB\Driver\Monitoring\LogSubscriber::LEVEL_WARNING`  
El nivel de registro de advertencia. Indica una situación donde un comportamiento indeseable de la aplicación puede ocurrir.

`MongoDB\Driver\Monitoring\LogSubscriber::LEVEL_MESSAGE`  
El nivel de registro de mensaje o notificación. Indica un evento inusual pero no problemático.

`MongoDB\Driver\Monitoring\LogSubscriber::LEVEL_INFO`  
El nivel de registro de información. Información de alto nivel sobre el comportamiento normal del controlador.

`MongoDB\Driver\Monitoring\LogSubscriber::LEVEL_DEBUG`  
El nivel de registro de depuración. Información detallada que puede ser útil durante la depuración de una aplicación.
