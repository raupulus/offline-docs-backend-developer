---
title: Instalación
source_url: https://www.php.net/manual/es/zip.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108000
---

## Instalación

## Sistemas Linux

Para usar estas funciones, PHP debe compilarse con soporte ZIP utilizando la opción de configuración `--with-zip`.

Antes de PHP 7.4.0, libzip estaba incluida con PHP, y para compilar la extensión se necesitaba usar la opción de configuración `--enable-zip`. Compilar contra la libzip incluida estaba desaconsejado a partir de PHP 7.3.0, pero aún era posible usando la opción de configuración `--without-libzip`.

Se ha añadido una opción de configuración `--with-libzip=DIR` para usar una instalación de libzip del sistema. Se requiere la versión 0.11 de libzip, recomendándose la 0.11.2 o superior.

## Windows

A partir de PHP 8.2.0, el archivo `php_zip.dll` DLL debe ser [habilitado](#install.pecl.windows.loading) en `php.ini`. Anteriormente, esta extensión estaba integrada.

## Instalación mediante PECL

Información sobre la instalación de estas extensiones PECL puede ser encontrada en el capítulo del manual titulado [Instalación de extensiones PECL](#install.pecl). Otra información como notas sobre nuevas versiones, descargas, fuentes de ficheros, información sobre los mantenedores así como un CHANGELOG, pueden ser encontradas aquí: <https://pecl.php.net/package/zip>.
