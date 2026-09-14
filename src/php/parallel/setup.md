---
title: Instalación
source_url: https://www.php.net/manual/es/parallel.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 60360
---

## Instalación

## Requisitos

parallel requiere una compilación de PHP con ZTS (Zend Thread Safety) activado (`--enable-zts`, o en sistemas no-Windows antes de PHP 8.0.0, `--enable-maintainer-zts`)

> [!CAUTION]
> Zend Thread Safety no puede ser activado después de la compilación; es una opción de configuración de compilación.

parallel debería compilarse en cualquier lugar donde haya un encabezado Posix Threads funcional (pthread.h) y una compilación ZTS de PHP, incluyendo Windows (utilizando el proyecto pthread-w32 de redhat).

## Instalación

Las versiones de parallel son alojadas por PECL y el código fuente por [github](https://github.com/krakjoe/parallel), el método de instalación más simple es la ruta PECL normal: <https://pecl.php.net/package/parallel>.

Los usuarios de Windows pueden descargar binarios de versiones precompiladas desde el sitio [PECL](https://pecl.php.net/package/parallel).

> [!CAUTION]
> Los usuarios de Windows deben tomar la medida adicional de añadir `pthreadVC?.dll` (distribuido con las versiones de Windows) a su `PATH`.
