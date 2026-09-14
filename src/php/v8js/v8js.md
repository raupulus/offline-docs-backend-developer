---
title: La clase V8Js
source_url: https://www.php.net/manual/es/class.v8js.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/v8js/v8js.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: v8js
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 100380
---

## Introducción

Esta es la clase principal para la extensión de V8Js. Cada instancia creada a partir de esta clase tiene su propio contexto en el que todo el Javascript es compilado y ejecutado.

Véase `V8Js::__construct` para más información.

## Sinopsis de la clase

V8Js

V8Js

Constantes

const

string

V8Js::V8_VERSION

const

int

V8Js::FLAG_NONE

1

const

int

V8Js::FLAG_FORCE_ARRAY

2

Métodos

## Constantes predefinidas

`V8Js::V8_VERSION`  
La versión del motor de Javascript V8.

`V8Js::FLAG_NONE`  
Ningún flag.

`V8Js::FLAG_FORCE_ARRAY`  
Obliga a todos los objetos JS a ser arrays asociativos en PHP.
