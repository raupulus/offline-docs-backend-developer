---
title: Instalación
source_url: https://www.php.net/manual/es/wddx.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wddx/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wddx
translation_status: ready
translation_revision: 2d84d3e00
order: 101180
---

## Instalación

## PHP 7.4

Esta extensión ha sido movida al módulo [PECL](https://pecl.php.net/) y no será integrada en PHP a partir de PHP 7.4.0

Información sobre la instalación de estas extensiones PECL puede ser encontrada en el capítulo del manual titulado [Instalación de extensiones PECL](#install.pecl). Otra información como notas sobre nuevas versiones, descargas, fuentes de ficheros, información sobre los mantenedores así como un CHANGELOG, pueden ser encontradas aquí: <https://pecl.php.net/package/wddx>.

## PHP \< 7.4

Después de instalar la librería requerida Expat, compile PHP con `--enable-wddx` y utilice `--with-libexpat-dir` para Expat.

La versión Windows de PHP dispone del soporte automático de esta extensión. No es necesario añadir ninguna biblioteca adicional para disponer de estas funciones.
