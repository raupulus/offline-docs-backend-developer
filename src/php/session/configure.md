---
title: Instalación
source_url: https://www.php.net/manual/es/session.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: true
translation_revision: a7d56396b
order: 73680
---

## Instalación

Esta extensión está activada por defecto. Puede ser desactivada utilizando la opción de configuración: `--disable-session`

Para utilizar la asignación de memoria compartida (mm) para el almacenamiento de las sesiones, configure PHP `--with-mm[=DIR]`.

La versión Windows de PHP dispone del soporte automático de esta extensión. No es necesario añadir ninguna biblioteca adicional para disponer de estas funciones.

> [!NOTE]
> Por omisión, todos los datos relativos a una sesión particular serán almacenados en un fichero del directorio especificado por `session.save_path` en las opciones del archivo `php.ini`. Un fichero para cada sesión será creado. Esto se debe a que una sesión es abierta (un fichero es creado) pero ningún dato es escrito en este fichero. Tenga en cuenta que este comportamiento es un efecto de las limitaciones de uso del sistema de ficheros y es posible que un gestor de sesiones personalizado (por ejemplo, uno que utilice una base de datos) no guarde ningún registro de las sesiones donde ningún dato haya sido almacenado.
