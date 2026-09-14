---
title: Instalación
source_url: https://www.php.net/manual/es/imap.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 86177fa03
order: 37900
---

## Instalación

## PHP 8.4

Esta extensión ha sido movida al módulo [PECL](https://pecl.php.net/) y no será integrada en PHP a partir de PHP 8.4.0

Información sobre la instalación de estas extensiones PECL puede ser encontrada en el capítulo del manual titulado [Instalación de extensiones PECL](#install.pecl). Otra información como notas sobre nuevas versiones, descargas, fuentes de ficheros, información sobre los mantenedores así como un CHANGELOG, pueden ser encontradas aquí: <https://pecl.php.net/package/imap>.

## PHP \< 8.4

Para que estas funciones operen, es necesario compilar PHP con `--with-imap[=DIR]`, donde DIR es el prefijo de instalación de c-client. En el ejemplo anterior, se utilizaría `--with-imap=/usr/local/imap-2000b`. Esta ubicación depende de dónde se haya creado este directorio, como se indica en la descripción anterior. Los usuarios de Windows pueden incluir la DLL `php_imap.dll` en `php.ini`.

> [!NOTE]
> Dependiendo de cómo se haya configurado c-client, es posible que también sea necesario añadir `--with-imap-ssl=/path/to/openssl/` y/o `--with-kerberos=/path/to/kerberos` a la línea de configuración de PHP.

> [!WARNING]
> La extensión IMAP no es thread-safe; no debe ser utilizada con builds ZTS.

> [!WARNING]
> Las extensiones [IMAP](#book.imap), [recode](#book.recode) y [YAZ](#book.yaz) no pueden ser utilizadas simultáneamente ya que utilizan un símbolo interno común. Nota: Yaz 2.0 y superior ya no sufre de este problema.
