---
title: Instalación
source_url: https://www.php.net/manual/es/fileinfo.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fileinfo/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fileinfo
translation_status: ready
translation_reviewed: false
translation_revision: 82ddd2ec8
order: 23120
---

## Instalación

Esta extensión está activada por omisión.

Los usuarios de Windows deben incluir la biblioteca DLL proporcionada `php_fileinfo.dll` en su `php.ini` para activar esta extensión.

La biblioteca libmagic se proporciona con PHP, pero incluye cambios específicos para PHP. Un parche de libmagic denominado `libmagic.patch` se mantiene y puede ser encontrado en el código fuente de la extensión fileinfo de PHP.
