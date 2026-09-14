---
title: Instalación
source_url: https://www.php.net/manual/es/mqseries.configure.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mqseries/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mqseries
translation_status: ready
translation_reviewed: false
translation_revision: b5efbef2d
order: 51800
---

## Instalación

Esta extensión [PECL](https://pecl.php.net/) no está integrada en PHP.

Información sobre la instalación de estas extensiones PECL puede ser encontrada en el capítulo del manual titulado [Instalación de extensiones PECL](#install.pecl). Otra información como notas sobre nuevas versiones, descargas, fuentes de ficheros, información sobre los mantenedores así como un CHANGELOG, pueden ser encontradas aquí: <https://pecl.php.net/package/mqseries>.

> [!NOTE]
> El nombre oficial de esta extensión es *mqseries*.

Existen dos formas de conectarse al gestor de colas. Dependen de cómo se haya compilado la extensión.

- En primer lugar, y también por omisión, se encuentra la biblioteca mqic. Al compilar y enlazar la extensión con las bibliotecas IBM WebSphere MQSeries, es posible conectarse al gestor de colas mediante la interfaz cliente. Las conexiones remotas también son posibles de esta manera.

- La otra forma es compilar y enlazar las bibliotecas mqm. Al utilizar estas bibliotecas, es posible emplear el gestor de transacciones del servidor de colas.

Actualmente, la selección de estas bibliotecas se realiza modificando el fichero `config.m4`.
