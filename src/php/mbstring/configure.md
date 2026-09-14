---
title: Instalación
source_url: https://www.php.net/manual/es/mbstring.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: false
translation_revision: 4df3260b8
order: 44920
---

## Instalación

`mbstring` es una extensión PHP. La extensión debe ser activada con la opción `configure`. Ver la sección [instalación](#install) para más detalles.

Las siguientes opciones de configuración están relacionadas con la extensión `mbstring`.

- `--enable-mbstring` : Activa las funciones `mbstring`. Esta opción es necesaria para utilizar las funciones `mbstring`.

  libmbfl es necesario para `mbstring`. libmbfl está incluido con `mbstring`. Anterior a PHP 7.3.0, si libmbfl ya está instalado en el sistema, `--with-libmbfl[=DIR]` puede ser especificado para utilizar la biblioteca instalada.

- `--disable-mbregex` : Desactiva las funciones de expresión regular con soporte para caracteres multioctetos.

  Oniguruma es necesario para las funciones de expresión regular con soporte para caracteres multioctetos. A partir de PHP 7.4.0, pkg-config es utilizado para detectar la biblioteca libonig. Anterior a PHP 7.4.0, Oniguruma estaba incluido con `mbstring`, pero era posible compilar contra una versión de libonig ya instalada pasando `--with-onig[=DIR]`.

  Es posible desactivar la verificación del backtrack (retroceso) de las regex multioctetos especificando `--disable-mbregex-backtrack`.
