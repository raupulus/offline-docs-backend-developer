---
title: Instalación
source_url: https://www.php.net/manual/es/lzf.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/lzf/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: lzf
translation_status: ready
translation_reviewed: true
translation_revision: b274da1f1
order: 44200
---

## Instalación

Esta extensión [PECL](https://pecl.php.net/) no está integrada en PHP. Información sobre la instalación de estas extensiones PECL puede ser encontrada en el capítulo del manual titulado [Instalación de extensiones PECL](#install.pecl). Otra información como notas sobre nuevas versiones, descargas, fuentes de ficheros, información sobre los mantenedores así como un CHANGELOG, pueden ser encontradas aquí: <https://pecl.php.net/package/lzf>.

Para utilizar estas funciones, PHP debe ser compilado con soporte para LZF mediante la opción de configuración `--with-lzf[=DIR]`. Asimismo, puede especificarse la opción `--enable-lzf-better-compression` para optimizar LZF en términos de espacio, aunque esto puede afectar negativamente a la velocidad.

Los usuarios de Windows deben activar la biblioteca `php_lzf.dll` en el `php.ini` para poder utilizar estas funciones.
