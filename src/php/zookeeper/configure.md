---
title: Instalación
source_url: https://www.php.net/manual/es/zookeeper.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zookeeper/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zookeeper
translation_status: ready
translation_reviewed: false
translation_revision: e9366ee45
order: 109510
---

## Instalación

Esta extensión [PECL](https://pecl.php.net/) no está integrada en PHP.

Información sobre la instalación de estas extensiones PECL puede ser encontrada en el capítulo del manual titulado [Instalación de extensiones PECL](#install.pecl). Otra información como notas sobre nuevas versiones, descargas, fuentes de ficheros, información sobre los mantenedores así como un CHANGELOG, pueden ser encontradas aquí: <https://pecl.php.net/package/zookeeper>.

Para habilitar el soporte de zookeeper, configure con `--with-libzookeeper-dir=DIR`. DIR es el prefijo de instalación de ZooKeeper C Binding, que debe contener el `include/zookeeper/zookeeper.h`

No hay biblioteca DLL para esta extensión PECL actualmente disponible. Consulte la sección [Compilación en Windows](#install.windows.building) .
