---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/pspell.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pspell/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pspell
translation_status: ready
translation_reviewed: true
translation_revision: 765b2d6ee
order: 66560
---

## Instalación/Configuración

## Requisitos

Para compilar PHP con el soporte pspell, será necesario contar con la biblioteca aspell, disponible en <http://aspell.net/>.

## Tipos de recursos

Antes de PHP 8.1.0, existían dos tipos de `resource` en esta extensión. El primero era el identificador de enlace al diccionario, el segundo es un recurso que contiene la configuración pspell.
