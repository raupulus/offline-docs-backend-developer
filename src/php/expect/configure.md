---
title: Instalación
source_url: https://www.php.net/manual/es/expect.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/expect/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: expect
translation_status: ready
translation_revision: ca6054f60
order: 20740
---

## Instalación

Esta extensión [PECL](https://pecl.php.net/) no está integrada en PHP. Información sobre la instalación de estas extensiones PECL puede ser encontrada en el capítulo del manual titulado [Instalación de extensiones PECL](#install.pecl). Otra información como notas sobre nuevas versiones, descargas, fuentes de ficheros, información sobre los mantenedores así como un CHANGELOG, pueden ser encontradas aquí: <https://pecl.php.net/package/expect>.

Para poder utilizar estas funciones, se debe compilar PHP con soporte para expect utilizando la opción de configuración `--with-expect[=DIR]`.

Los usuarios de Windows deben habilitar `php_expect.dll` dentro del fichero `php.ini` para poder utilizar estas funciones. No hay biblioteca DLL para esta extensión PECL actualmente disponible. Consulte la sección [Compilación en Windows](#install.windows.building) .
