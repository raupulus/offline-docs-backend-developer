---
title: Las Superglobales
description: Variables internas siempre disponibles, independientemente del contexto
source_url: https://www.php.net/manual/es/language.variables.superglobals.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/variables/superglobals.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: a6d209f4f
order: 4240
---

Las Superglobales

Variables internas siempre disponibles, independientemente del contexto

## Descripción

Varios arrays predefinidos en PHP son "superglobales", lo que significa que están disponibles independientemente del contexto del script. No es necesario utilizar `global $variable;` antes de acceder a ellas en funciones o métodos.

Las variables superglobales son: `$GLOBALS`, `$_SERVER`, `$_GET`, `$_POST`, `$_FILES`, `$_COOKIE`, `$_SESSION`, `$_REQUEST`, `$_ENV`

## Notas

> [!NOTE]
> Por omisión, todas las superglobales están disponibles, y solo las directivas de configuración pueden hacerlas no disponibles. Para más información, consulte la documentación sobre el [orden de las variables](#ini.variables-order).

> [!NOTE]
> Las superglobales no pueden ser utilizadas como [variables dinámicas](#language.variables.variable) en una función o método de una clase.

## Véase también

El [ámbito de las variables](#language.variables.scope), La directiva [variables_order](#ini.variables-order), [La extensión sobre los filtros](#book.filter)
