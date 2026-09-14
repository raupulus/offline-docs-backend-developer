---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/pthreads.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: 1f3517218
order: 66600
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`PTHREADS_INHERIT_ALL` (`int`)  
Las opciones por omisión para todos los hilos, haciendo que los pthreads copien los entornos cuando los nuevos hilos son iniciados

`PTHREADS_INHERIT_NONE` (`int`)  
No hereda nada cuando los nuevos hilos son iniciados

`PTHREADS_INHERIT_INI` (`int`)  
Hereda las entradas INI cuando los nuevos hilos son iniciados

`PTHREADS_INHERIT_CONSTANTS` (`int`)  
Hereda las constantes declaradas por el usuario cuando los nuevos hilos son iniciados

`PTHREADS_INHERIT_CLASSES` (`int`)  
Hereda las clases declaradas por el usuario cuando los nuevos hilos son iniciados

`PTHREADS_INHERIT_FUNCTIONS` (`int`)  
Hereda las funciones declaradas por el usuario cuando los nuevos hilos son iniciados

`PTHREADS_INHERIT_INCLUDES` (`int`)  
La herencia incluye la información de fichero cuando los nuevos hilos son iniciados

`PTHREADS_INHERIT_COMMENTS` (`int`)  
Hereda todos los comentarios cuando los nuevos hilos son iniciados

`PTHREADS_ALLOW_HEADERS` (`int`)  
Permite que los nuevos hilos envíen los encabezados a la salida estándar (normalmente no permitido)
