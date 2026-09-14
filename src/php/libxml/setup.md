---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/libxml.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/libxml/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: libxml
translation_status: ready
translation_reviewed: false
translation_revision: b8cefce03
order: 43740
---

## Instalación/Configuración

## Requisitos

Esta extensión requiere [libxml](https://gitlab.gnome.org/GNOME/libxml2/-/wikis/home) \>= 2.9.4 a partir de PHP 8.4.0, libxml \>= 2.9.0 a partir de PHP 8.0.0. Anterior a PHP 8.0, libxml debe ser \>= 2.6.0.

## Instalación para las versiones de PHP \>= 7.4

La extensión libxml está activada por omisión, aunque puede ser desactivada con la opción `--without-libxml`.

PHP utiliza `pkg-config` para seleccionar el archivo de biblioteca correcto, los archivos de encabezado y los indicadores de compilación a utilizar para libxml2. Para asegurarse de que la versión deseada de libxml2 sea seleccionada, la variable de entorno `PKG_CONFIG_PATH` puede ser utilizada para controlar el camino de búsqueda de `pkg-config` antes de ejecutar el script de configuración : PKG_CONFIG_PATH="/ruta/hacia/prefijo/libxml2/lib/pkgconfig:/lib/pkgconfig"

## Instalación para las versiones de PHP \< 7.4

La extensión libxml está activada por omisión, y puede ser desactivada con la opción `--disable-libxml`.

La directiva opcional `--with-libxml-dir` se utiliza para especificar la carpeta donde `libxml` se encuentra en el sistema donde PHP es compilado. En caso de no utilizar esta opción, las carpetas por omisión serán analizadas. El proceso `configure` verifica las carpetas donde se encuentra libxml (específicamente, `xml2-config`), en este orden :

1.  La carpeta (\[DIR\]) especificada con la opción `--with-libxml-dir` (\[DIR\]=`/bin/xml2-config`)

2.  `/usr/local/bin/xml2-config`

3.  `/usr/bin/xml2-config`

Si el proceso `configure` no puede encontrar el archivo `xml2-config` en la carpeta especificada por la opción `--with-libxml-dir`, entonces, continuará y analizará las carpetas por omisión.
