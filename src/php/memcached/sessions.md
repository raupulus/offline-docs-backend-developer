---
title: Soporte para sesiones
source_url: https://www.php.net/manual/es/memcached.sessions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/sessions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_revision: af4410a7e
order: 46880
---

## Soporte para sesiones

Memcached proporciona un controlador personalizado de sesiones que puede emplearse para almacenar sesiones de usuario en memcache. Utiliza internamente una instancia diferente para este propósito, por lo que se puede utilizar una agrupación de servidores diferente si fuera necesario. Las claves de sesiones se almacenan bajo el prefijo `memc.sess.key.`, por lo que hay que considerar esto si se utiliza la misma agrupación de servidores para caché de sesiones y caché genérica.

`session.save_handler` `string`  
Establecer a `memcached` para activar el soporte para sesiones.

`session.save_path` `string`  
Define entradas `nombre_host:puerto` separadas por comas para utilizarlas en agrupaciones de servidores de sesiones, por ejemplo `"sess1:11211, sess2:11211"`.
