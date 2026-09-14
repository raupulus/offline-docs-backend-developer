---
title: Instalación
source_url: https://www.php.net/manual/es/mailparse.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mailparse/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mailparse
translation_status: ready
translation_reviewed: false
translation_revision: 01bd007b0
order: 44290
---

## Instalación

Esta extensión [PECL](https://pecl.php.net/) no está integrada en PHP. Información sobre la instalación de estas extensiones PECL puede ser encontrada en el capítulo del manual titulado [Instalación de extensiones PECL](#install.pecl). Otra información como notas sobre nuevas versiones, descargas, fuentes de ficheros, información sobre los mantenedores así como un CHANGELOG, pueden ser encontradas aquí: <https://pecl.php.net/package/mailparse>.

Para poder utilizar estas funciones se debe compilar PHP con soporte para mailparse mediante la opción de configuración `--enable-mailparse`.

Los usuarios de windows deben habilitar `php_mailparse.dll` en el fichero `php.ini` con el fin de usar estas funciones. Los binarios Windows (los ficheros DLL) para esta extensión PECL están disponibles en el sitio web PECL.

Es necesario que la extensión [mbstring](#ref.mbstring) esté cargada antes que mailparse.
