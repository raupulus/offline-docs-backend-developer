---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/win32service.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/win32service/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: win32service
translation_status: ready
translation_revision: b655c9df2
order: 101570
---

## Instalación/Configuración

## Requisitos

Las versiones de Windows soportadas son las mismas que el paquete redistribuible Visual C++ utilizado para construir PHP.

## Instalación

Información sobre la instalación de estas extensiones PECL puede ser encontrada en el capítulo del manual titulado [Instalación de extensiones PECL](#install.pecl). Otra información como notas sobre nuevas versiones, descargas, fuentes de ficheros, información sobre los mantenedores así como un CHANGELOG, pueden ser encontradas aquí: <https://pecl.php.net/package/win32service>

## Consideraciones de seguridad

Esta extensión requiere privilegios de administrador para ciertas acciones tales como [create](#function.win32-create-service), [delete](#function.win32-delete-service), [start](#function.win32-start-service), [stop](#function.win32-stop-service), [pause](#function.win32-pause-service) y [continue](#function.win32-continue-service). Esta exigencia puede causar una elevación de privilegios si el control de servicio está disponible desde la interfaz Web o el control remoto.

La ACL del servicio puede ser definida después de su adición en el SCM para delegar las tareas de administración actuales a una cuenta no administrador o a una cuenta de servicio.

A partir de Win32Service 1.1.0, los derechos de servicio pueden ser gestionados con PHP. Los ACL actuales pueden ser leídos con `win32_read_all_rights_access_service`, un derecho de acceso o de denegación puede ser añadido con `win32_add_right_access_service`, o un derecho de acceso puede ser eliminado con `win32_remove_right_access_service`.

Se recomienda actualizar a Win32Service 1.1.0. Para instrucciones adicionales sobre la gestión de derechos sin la extensión (o con una versión anterior a 1.1.0), consulte la [Base de conocimientos de Microsoft](https://www.betaarchive.com/wiki/index.php?title=Microsoft_KB_Archive/914392).
