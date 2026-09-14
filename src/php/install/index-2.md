---
title: FastCGI Process Manager (FPM)
source_url: https://www.php.net/manual/es/install.fpm.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: install/fpm/index.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: install
translation_status: ready
translation_revision: 04210d535
order: 1680
---

## FastCGI Process Manager (FPM)

FPM (FastCGI Process Manager, gestor de procesos FastCGI) es una implementación de PHP FastCGI que contiene algunas características (principalmente) útiles para sitios con mucha carga.

Estas funcionalidades incluyen :

- Gestión avanzada de procesos con parada/arranque suave (graceful) ;

- Pools que permiten iniciar trabajadores con diferentes uid/gid/chroot/entorno, escuchando en diferentes puertos y utilizando diferentes php.ini (reemplaza el modo seguro) ;

- Registro configurable stdout y stderr ;

- Reinicio de emergencia en caso de destrucción accidental del caché opcode ;

- Soporte de carga acelerada ;

- "slowlog" - registro de scripts (no solo sus nombres, sino también su backtrace PHP, utilizando ptrace o equivalente para leer el proceso remoto) que se ejecutan anormalmente lento ;

- `fastcgi_finish_request` - función especial para terminar la petición y volcar todas las datos mientras se continúa ejecutando una tarea consumidora (conversión de video por ejemplo) ;

- Nacimiento de procesos hijos dinámicos/bajo demanda/estáticos ;

- Información de estado básica y extendida (similar a mod_status de Apache) con diferentes formatos soportados como json, xml y openmetrics ;

- Fichero de configuración basado en php.ini
