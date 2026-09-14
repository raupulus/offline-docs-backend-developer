---
title: $_SESSION
description: Variables de sesión
source_url: https://www.php.net/manual/es/reserved.variables.session.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/variables/session.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: a6d209f4f
order: 4230
---

\$\_SESSION

Variables de sesión

## Descripción

Es un array asociativo que contiene variables de sesión disponibles para el script actual. Ver la documentación de [Funciones de sesión](#ref.session) para más información sobre su uso.

## Notas

> [!NOTE]
> Esto es una 'superglobal', o variable global automática. Esto significa simplemente que esta variable está disponible en todos los contextos del script. No es necesario hacer `global $variable;` para acceder a ella en las funciones o los métodos.

## Véase también

`session_start`
