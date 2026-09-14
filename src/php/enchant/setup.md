---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/enchant.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/enchant/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: enchant
translation_status: ready
translation_reviewed: false
translation_revision: a6b55f8de
order: 17560
---

## Instalación/Configuración

## Requisitos

Esta versión utiliza las funciones de la [biblioteca Enchant](https://rrthomas.github.io/enchant/) por Dom Lachowicz. Se debe utilizar Enchant 1.2.4 o superior. Enchant 2.0.0 o superior es únicamente soportado a partir de PHP 8.0.0.

Enchant requiere asimismo [Glib 2.6](http://ftp.gnome.org/pub/gnome/sources/glib/) o superior. Las bibliotecas Windows pre-compiladas están disponibles desde <http://ftp.gnome.org/pub/gnome/binaries/win32/glib/>.

## Tipos de recursos

Anterior a PHP 8.0.0, existen dos tipos de recursos en esta extensión. El primero es el broker (gestor de backends) y el segundo es para el diccionario.
