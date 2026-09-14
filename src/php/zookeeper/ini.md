---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/zookeeper.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zookeeper/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zookeeper
translation_status: ready
translation_reviewed: false
translation_revision: 940ea8c1b
order: 109530
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [zookeeper.recv_timeout](#ini.zookeeper.recv_timeout) | 10000 | `INI_ALL` |  |
| [zookeeper.session_lock](#ini.zookeeper.session_lock) | 1 | `INI_SYSTEM` |  |
| [zookeeper.sess_lock_wait](#ini.zookeeper.sess_lock_wait) | 150000 | `INI_ALL` |  |

Zookeeper Opciones de configuración

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`zookeeper.recv_timeout` `int`  
Tiempo máximo de espera predeterminado para todas las sesiones de ZooKeeper.

`zookeeper.session_lock` `int`  
Permite el bloqueo de sesiones PHP.

`zookeeper.sess_lock_wait` `int`  
Tiempo de espera en microsegundos para los intentos de bloqueo de la sesión PHP. Se debe tener precaución al definir este valor. Los valores válidos son enteros, donde 0 se interpreta como el valor predeterminado. Los valores negativos provocan un bloqueo reducido a un intento de bloqueo.
