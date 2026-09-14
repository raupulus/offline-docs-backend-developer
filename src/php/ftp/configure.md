---
title: Instalación
source_url: https://www.php.net/manual/es/ftp.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: false
translation_revision: af4324241
order: 24310
---

## Instalación

Para activar el módulo FTP en la configuración de PHP, debe utilizarse la opción `--enable-ftp`.

En Autotools, el soporte FTP SSL se activa implícitamente durante la compilación con la extensión `openssl` utilizando la opción de configuración `--with-openssl`. Durante la compilación sin la extensión `openssl`, la opción de configuración Autotools `--with-ftp-ssl` puede ser utilizada para activar explícitamente el soporte FTP SSL.

En Windows, esta extensión siempre se construye como extensión compartida, por lo que debe ser activada en el `php.ini`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | La opción de configuración Autotools `--with-openssl-dir` ha sido eliminada en favor de la nueva `--with-ftp-ssl` que activa explícitamente el soporte FTP SSL durante la compilación sin la extensión `openssl`. |
