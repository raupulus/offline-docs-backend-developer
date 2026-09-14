---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/openssl.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 3fa666ce0
order: 59690
---

## Instalación/Configuración

## Requisitos

Para poder utilizar las funciones OpenSSL, debe instalarse la biblioteca [OpenSSL](http://www.openssl.org/). PHP 7.0 requiere OpenSSL \>= 0.9.8, \< 1.2. PHP 7.1-8.0 requieren OpenSSL \>= 1.0.1, \< 3.0. PHP \>= 8.1 requiere OpenSSL \>= 1.0.2, \< 4.0. PHP \>= 8.4 requiere OpenSSL \>= 1.1.1, \< 4.0.

> [!WARNING]
> Se recomienda encarecidamente utilizar la versión mantenida de OpenSSL para evitar ciertas vulnerabilidades en el servidor web.

## Tipos de recursos

Antes de PHP 8.0.0, existían 3 tipos de recursos definidos en el módulo OpenSSL: `OpenSSL key`, `OpenSSL X.509`, `OpenSSL X.509 CSR`
