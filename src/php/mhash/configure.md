---
title: Instalación
source_url: https://www.php.net/manual/es/mhash.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mhash/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mhash
translation_status: ready
translation_reviewed: false
translation_revision: a2e72b2b3
order: 46900
---

## Instalación

Será necesario compilar PHP con la opción `--with-mhash[=DIR]` para activar esta extensión. DIR es la ruta del directorio de instalación de la biblioteca MHASH.

Desde PHP 5.3.0, la extensión mhash es emulada a través de la extensión [Hash](#ref.hash). Asimismo, la opción que permite especificar el directorio de instalación de mhash ya no tiene efecto, y esta extensión requiere la instalación de la extensión hash para funcionar.
