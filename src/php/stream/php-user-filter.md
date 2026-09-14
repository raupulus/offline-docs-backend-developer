---
title: La clase php_user_filter
source_url: https://www.php.net/manual/es/class.php-user-filter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/php-user-filter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 88250
---

## Introducción

Los hijos de esta clase se pasan a la función `stream_filter_register`. Cabe señalar que el método [\_\_construct](#object.construct) no es llamado; en su lugar, php_user_filter::onCreate debería ser utilizado para la inicialización.

## Sinopsis de la clase

php_user_filter

Propiedades

public

string

filtername

""

public

mixed

params

""

public

resource

null

stream

null

Métodos

## Propiedades

`filtername`  
Nombre del filtro a registrar por la función `stream_filter_append`.

`params`  

`stream`
