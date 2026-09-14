---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/pthreads.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_revision: bf92d8bd8
order: 66680
---

## Instalación/Configuración

## Requisitos

Pthreads requiere una construcción de PHP con ZTS activado (`--enable-zts`, o en sistemas no-Windows anteriores a PHP 8.0.0, `--enable-maintainer-zts`).

> [!CAUTION]
> La seguridad de los Threads Zend (Zend Thread Safety - ZTS) no puede ser activada después de la construcción; es una opción de compilación.

pthreads debería compilar siempre que exista un encabezado Posix Threads funcional (pthread.h) así como una construcción ZTS de PHP, lo cual incluye Windows (utilizando el proyecto pthread-w32 de redhat).

## Instalación

Las versiones de pthreads están alojadas en PECL y las fuentes en [github](https://github.com/krakjoe/pthreads). El procedimiento de instalación más sencillo es el estándar de PECL: <https://pecl.php.net/package/pthreads>.

Los usuarios de Windows pueden descargar binarios preconstruidos desde el sitio de [PECL](https://pecl.php.net/package/pthreads).

> [!CAUTION]
> Los usuarios de Windows deben añadir pthreadVC2.dll (distribuido con Windows) a su `PATH`.
