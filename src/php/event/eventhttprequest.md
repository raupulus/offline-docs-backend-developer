---
title: La clase EventHttpRequest
source_url: https://www.php.net/manual/es/class.eventhttprequest.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventhttprequest.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 20320
---

## Introducción

Representa una petición HTTP.

## Sinopsis de la clase

EventHttpRequest

EventHttpRequest

Constantes

const

int

EventHttpRequest::CMD_GET

1

const

int

EventHttpRequest::CMD_POST

2

const

int

EventHttpRequest::CMD_HEAD

4

const

int

EventHttpRequest::CMD_PUT

8

const

int

EventHttpRequest::CMD_DELETE

16

const

int

EventHttpRequest::CMD_OPTIONS

32

const

int

EventHttpRequest::CMD_TRACE

64

const

int

EventHttpRequest::CMD_CONNECT

128

const

int

EventHttpRequest::CMD_PATCH

256

const

int

EventHttpRequest::INPUT_HEADER

1

const

int

EventHttpRequest::OUTPUT_HEADER

2

Métodos

## Constantes predefinidas

`EventHttpRequest::CMD_GET`  
método GET (comando)

`EventHttpRequest::CMD_POST`  
método POST (comando)

`EventHttpRequest::CMD_HEAD`  
método HEAD (comando)

`EventHttpRequest::CMD_PUT`  
método PUT (comando)

`EventHttpRequest::CMD_DELETE`  
comando DELETE (método)

`EventHttpRequest::CMD_OPTIONS`  
método OPTIONS (comando)

`EventHttpRequest::CMD_TRACE`  
método TRACE (comando)

`EventHttpRequest::CMD_CONNECT`  
método CONNECT (comando)

`EventHttpRequest::CMD_PATCH`  
método PATCH (comando)

`EventHttpRequest::INPUT_HEADER`  
Solicita el tipo de encabezado de entrada.

`EventHttpRequest::OUTPUT_HEADER`  
Solicita el tipo de encabezado de salida.
