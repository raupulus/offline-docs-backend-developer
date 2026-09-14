---
title: $_REQUEST
description: Variables HTTP Request
source_url: https://www.php.net/manual/es/reserved.variables.request.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/variables/request.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: a6d209f4f
order: 4210
---

\$\_REQUEST

Variables HTTP Request

## Descripción

Un `array` asociativo que por defecto contiene el contenido de `$_GET`, `$_POST` y `$_COOKIE`.

## Notas

> [!NOTE]
> Esto es una 'superglobal', o variable global automática. Esto significa simplemente que esta variable está disponible en todos los contextos del script. No es necesario hacer `global $variable;` para acceder a ella en las funciones o los métodos.

> [!NOTE]
> Cuando se ejecuta en la [línea de comandos ](#features.commandline), *no* se incluirán las entradas [argv](#reserved.variables.argv) y [argc](#reserved.variables.argc); ya que están presentes en el `$_SERVER` `array`.

> [!NOTE]
> Las variables en `$_REQUEST` se proporcionan al script a través de los mecanismos de entrada GET, POST, y COOKIE y por lo tanto pueden ser manipulados por el usuario remoto y no debe confiar en el contenido. La presencia y el orden de las variables listadas en este array se definen según la directiva de configuración PHP [request_order](#ini.request-order), y [variables_order](#ini.variables-order).

## Véase también

Tratando con variables externas

La extensión filter
