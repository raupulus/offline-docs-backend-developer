---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/sodium.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 77060
---

## Instalación/Configuración

## Requisitos

Esta extensión requiere [libsodium](https://libsodium.org/) ≥ 1.0.8.

## Instalación

A partir de PHP 7.2.0 esta extensión se proporciona con PHP. Para las versiones de PHP más antiguas esta extensión está disponible a través de PECL.

### Sistemas Linux

Para poder utilizar esta extensión se debe compilar PHP con el soporte de sodium utilizando la opción de configuración `--with-sodium[=DIR]`.

### Windows

Para poder utilizar esta extensión se debe añadir `extension=php_sodium.dll` al `php.ini`.

### Instalación a través de PECL

Información sobre la instalación de estas extensiones PECL puede ser encontrada en el capítulo del manual titulado [Instalación de extensiones PECL](#install.pecl). Otra información como notas sobre nuevas versiones, descargas, fuentes de ficheros, información sobre los mantenedores así como un CHANGELOG, pueden ser encontradas aquí: <https://pecl.php.net/package/libsodium>
