---
title: Instalación
source_url: https://www.php.net/manual/es/pgsql.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_revision: 96c9d88ba
order: 62820
---

## Instalación

Con el fin de habilitar el soporte de PostgreSQL, `--with-pgsql[=DIR]` es requerido cuando se compila PHP. `DIR` es el directorio base donde está instalado PostgreSQL, por defecto generalmente es `/usr/local/pgsql` en sistemas linux. Si el módulo de objetos compartidos está disponible, el módulo PostgreSQL puede ser cargado usando la directiva [extension](#ini.extension) en `php.ini` o la función `dl`.
