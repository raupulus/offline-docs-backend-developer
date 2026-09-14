---
title: La clase Yaf_Request_Http
source_url: https://www.php.net/manual/es/class.yaf-request-http.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf-request-http.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 4d17b7b49
order: 104740
---

## Introducción

Cualquier petición de un cliente se inicializa como un `Yaf_Request_Http`. Se puede obtener la información de la petición, como la consulta de URI y los parámetros de POST, mediante los métodos de esta clase.

> [!NOTE]
> Por seguridad, \$\_GET/\$\_POST son de solo lectura en Yaf, lo que significa que si se establece un valor en esta variables globales, este no se podrá obtener desde Yaf_Request_Http::getQuery o Yaf_Request_Http::getPost.
>
> Aunque si fuera necesaria tal característica, como en las pruebas unitarias, Yaf se puede construir con --enable-yaf-debug, la cual permite a Yaf leer el valor establecido por el usuario mediante script.
>
> En tal caso, Yaf lanzará un aviso E_STRICT para recordarlo: Strict Standards: you are running yaf in debug mode

## Sinopsis de la clase

Yaf_Request_Http

Yaf_Request_Http

extends

Yaf_Request_Abstract

Propiedades

Métodos

Métodos heredados

## Propiedades

`module`  

`controller`  

`action`  

`method`  

`params`  

`language`  

`_exception`  

`_base_uri`  

`uri`  

`dispatched`  

`routed`
