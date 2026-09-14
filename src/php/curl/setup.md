---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/curl.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_reviewed: true
translation_revision: 85de4c262
order: 10170
---

## Instalación/Configuración

## Requisitos

Para poder utilizar las funciones cURL en PHP, debe instalarse el paquete [libcurl](http://curl.haxx.se/). PHP requiere libcurl versión 7.10.5 o superior. A partir de PHP 7.3.0, se requiere la versión 7.15.5 o posterior. A partir de PHP 8.0.0, se requiere la versión 7.29.0 o posterior. A partir de PHP 8.4.0, se requiere la versión 7.61.0 o superior.

## Tipos de recursos

Antes de PHP 8.0.0, esta extensión definía tres tipos de recursos: un manejador `curl`, un manejador `curl_multi` y un manejador `curl_share`.
