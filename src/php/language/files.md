---
title: $_FILES
description: Variables de subida de ficheros HTTP
source_url: https://www.php.net/manual/es/reserved.variables.files.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/variables/files.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: a6d209f4f
order: 4150
---

\$\_FILES

Variables de subida de ficheros HTTP

## Descripción

Un `array` asociativo de elementos subidos al script en curso a través del método POST. La estructura de este array se resume en la sección [Subidas con el método POST](#features.file-upload.post-method).

## Notas

> [!NOTE]
> Esto es una 'superglobal', o variable global automática. Esto significa simplemente que esta variable está disponible en todos los contextos del script. No es necesario hacer `global $variable;` para acceder a ella en las funciones o los métodos.

## Véase también

`move_uploaded_file`, [Manejo de subida de ficheros](#features.file-upload)
