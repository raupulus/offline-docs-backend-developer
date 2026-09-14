---
title: La clase CURLStringFile
source_url: https://www.php.net/manual/es/class.curlstringfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/curlstringfile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 9810
---

## Introducción

`CURLStringFile` hace posible subir un archivo directamente desde una variable. Esto es similar a `CURLFile`, pero funciona con los contenidos del archivo, no con su nombre. Esta clase o `CURLFile` deberían ser utilizadas para subir los contenidos del archivo con `CURLOPT_POSTFIELDS`.

## Sinopsis de la clase

CURLStringFile

Propiedades

public

string

data

public

string

postname

public

string

mime

Métodos

## Propiedades

`data`  
Los contenidos a ser subidos.

`postname`  
El nombre del archivo a ser utilizado en los datos subidos.

`mime`  
El tipo MIME del archivo (por defecto es `application/octet-stream`).

## Véase también

`curl_setopt`, `CURLFile`
