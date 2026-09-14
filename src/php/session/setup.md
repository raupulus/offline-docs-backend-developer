---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/session.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: true
translation_revision: 48ce43fe7
order: 74160
---

## Instalación/Configuración

## Requisitos

No se requiere ninguna biblioteca externa para compilar esta extensión.

> [!NOTE]
> Opcionalmente, puede utilizarse la asignación de memoria compartida (mm), desarrollada por Ralf S.Engelschall, para almacenar las sesiones. Es necesario descargar [mm](http://www.ossp.org/pkg/lib/mm/) e instalarlo. Esta opción no está disponible para los entornos Windows. Tenga en cuenta que el módulo de almacenamiento de sesiones mm no garantiza los bloqueos de sesiones en caso de acceso múltiple a la misma sesión. Puede ser más adecuado utilizar un sistema de archivos basado en memoria compartida (como tmpfs en Solaris/Linux o `/dev/md` en BSD) para almacenar las sesiones en archivos, ya que estos serán bloqueados correctamente. Los datos de sesión se almacenan en memoria, por lo que serán borrados al reiniciar el servidor web.
