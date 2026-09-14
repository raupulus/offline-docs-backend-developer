---
title: Instalación
source_url: https://www.php.net/manual/es/xml.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xml/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xml
translation_status: ready
translation_reviewed: true
translation_revision: cdab70215
order: 102610
---

## Instalación

Esta extensión está activada por defecto. Puede ser desactivada utilizando la opción de configuración: `--disable-xml`

Estas funciones están activadas por omisión y utilizan la biblioteca expat proporcionada con la distribución. El soporte de XML puede ser desactivado utilizando la opción de compilación `--disable-xml`. Si se compila PHP como módulo para Apache 1.3.9 o superior, PHP utilizará automáticamente la biblioteca expat proporcionada por Apache. Si no se desea utilizar la biblioteca expat integrada, es necesario compilar PHP con la opción `--with-expat-dir=DIR`, donde DIR es el directorio de instalación de la biblioteca expat.

La versión Windows de PHP dispone del soporte automático de esta extensión. No es necesario añadir ninguna biblioteca adicional para disponer de estas funciones.
