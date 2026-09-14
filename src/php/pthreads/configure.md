---
title: Instalación
source_url: https://www.php.net/manual/es/pthreads.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_revision: bf92d8bd8
order: 66590
---

## Instalación

Utilizar `--enable-maintainer-zts` durante la compilación de PHP.

Los usuarios de Windows deben incluir `php_pthreads.dll` en el `php.ini`

> [!NOTE]
> Los usuarios de Windows deben asegurarse asimismo de que `pthreadVC2.dll` (incluido en la distribución) esté presente en una de las carpetas especificadas en la variable de entorno `PATH`.
