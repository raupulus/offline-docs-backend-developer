---
title: Instalación
source_url: https://www.php.net/manual/es/recode.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/recode/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: recode
translation_status: ready
translation_reviewed: false
translation_revision: 72f847e07
order: 68860
---

## Instalación

## PHP 7.4

Esta extensión ha sido movida al módulo [PECL](https://pecl.php.net/) y no será integrada en PHP a partir de PHP 7.4.0

Información sobre la instalación de estas extensiones PECL puede ser encontrada en el capítulo del manual titulado [Instalación de extensiones PECL](#install.pecl). Otra información como notas sobre nuevas versiones, descargas, fuentes de ficheros, información sobre los mantenedores así como un CHANGELOG, pueden ser encontradas aquí: <https://pecl.php.net/package/recode>.

## PHP \< 7.4

Para utilizar las funciones definidas en este módulo, PHP debe ser compilado con la opción`--with-recode[=DIR]`.

> [!WARNING]
> Pueden encontrarse fallos y problemas de inicio de PHP cuando la extensión recode es cargada **después** de las extensiones [MySQL](#ref.mysql) o [imap](#ref.imap). Cargar la extensión recode antes de estas dos extensiones corrige el problema. Esto se debe a un problema técnico ya que la biblioteca c-client de IMAP y recode tienen ambas su propia función `hash_lookup()` y las extensiones mysql y recode tienen ambas su función `hash_insert`.

> [!WARNING]
> Las extensiones [IMAP](#book.imap), [recode](#book.recode) y [YAZ](#book.yaz) no pueden ser utilizadas simultáneamente ya que utilizan un símbolo interno común. Nota: Yaz 2.0 y superior ya no sufre de este problema.
