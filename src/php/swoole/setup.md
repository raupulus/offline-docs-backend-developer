---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/swoole.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_reviewed: true
translation_revision: d4854f421
order: 90680
---

## Instalación/Configuración

## Requisitos

Swoole requiere la biblioteca libbrotli.

La activación de la opción --enable-swoole-curl requiere la biblioteca libcurl, y PHP así como Swoole deben estar vinculados a la misma biblioteca compartida libcurl y a los mismos encabezados, a fin de evitar un comportamiento indefinido.

La activación de la opción --enable-iouring requiere la biblioteca liburing (versión ≥ 2.0) y un núcleo Linux (versión ≥ 5.12).

La activación de la opción --enable-swoole-thread requiere que PHP sea compilado en modo ZTS (Zend Thread Safety).

La activación de la opción --enable-cares requiere la biblioteca libc-ares.

La activación de la opción --enable-zstd requiere la biblioteca libzstd (versión ≥ 1.4.0).

La activación de la opción --enable-swoole-sqlite requiere la biblioteca libsqlite.

La activación de la opción --enable-swoole-pgsql requiere la biblioteca libpq.

La activación de la opción --with-swoole-odbc requiere la biblioteca unixodbc-dev.

La activación de la opción --with-swoole-oracle requiere las bibliotecas Oracle Instant Client.
