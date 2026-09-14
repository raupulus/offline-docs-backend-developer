---
title: La clase CURLFile
source_url: https://www.php.net/manual/es/class.curlfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/curlfile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_reviewed: true
translation_revision: 4d17b7b49
order: 9750
---

## Introducción

Esta clase o `CURLStringFile` debe ser utilizada para transferir un fichero con las constantes `CURLOPT_POSTFIELDS`.

La deserialización de las instancias `CURLFile` no está permitida. A partir de PHP 7.4.0, la serialización está prohibida en primer lugar.

## Sinopsis de la clase

CURLFile

Propiedades

public

string

name

""

public

string

mime

""

public

string

postname

""

Métodos

## Propiedades

`name`  
Nombre del fichero a descargar.

`mime`  
Tipo MIME del fichero (por omisión, `application/octet-stream`).

`postname`  
El nombre del fichero en los datos descargados (por omisión, la propiedad `name`).

## Véase también

`curl_setopt`, `CURLStringFile`
