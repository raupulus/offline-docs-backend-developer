---
title: La clase StreamBucket
source_url: https://www.php.net/manual/es/class.streambucket.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/streambucket.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_revision: 564bdc2db
order: 88300
---

## Introducción

Un cubo de flujo (stream bucket) es una parte de un flujo que puede ser extraída de las brigadas de cubos.

## Sinopsis de la clase

final

StreamBucket

Propiedades

public

readonly

resource

bucket

public

readonly

string

data

public

readonly

int

datalen

public

readonly

int

dataLength

## Propiedades

resource `bucket`  
Un recurso `userfilter.bucket`.

string `data`  
El string actual en el cubo.

int `datalen`  
La longitud del string en el cubo. Deprecado a partir de PHP 8.4 en favor de `StreamBucket::$dataLength`.

int `dataLength`  
La longitud del string en el cubo.

## Véase también

stream_bucket_new

stream_bucket_append

stream_bucket_prepend

stream_bucket_make_writeable
