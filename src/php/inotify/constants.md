---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/inotify.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/inotify/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: inotify
translation_status: ready
translation_revision: 86e6094e8
order: 39290
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`IN_ACCESS` (`int`)  
El fichero fue accedido (lectura) (\*)

`IN_MODIFY` (`int`)  
El fichero fue modificado (\*)

`IN_ATTRIB` (`int`)  
Metadatos cambiados (por ejemplo: permisos, mtime, etc) (\*)

`IN_CLOSE_WRITE` (`int`)  
El fichero, previamente abierto para escritura, fue cerrado (\*)

`IN_CLOSE_NOWRITE` (`int`)  
El fichero, no abierto para escritura, fue cerrado (\*)

`IN_OPEN` (`int`)  
El fichero fue abierto (\*)

`IN_MOVED_TO` (`int`)  
Un fichero fue movido dentro del directorio observado (\*)

`IN_MOVED_FROM` (`int`)  
Un fichero fue movido fuera del directorio observado (\*)

`IN_CREATE` (`int`)  
Un fichero o directorio fue creado en el directorio observado (\*)

`IN_DELETE` (`int`)  
Fichero o directorio borrado en el directorio observado (\*)

`IN_DELETE_SELF` (`int`)  
El fichero o directorio observado fue borrado

`IN_MOVE_SELF` (`int`)  
El fichero o directorio observado fue movido

`IN_CLOSE` (`int`)  
Similar a IN_CLOSE_WRITE \| IN_CLOSE_NOWRITE

`IN_MOVE` (`int`)  
Similar a IN_MOVED_FROM \| IN_MOVED_TO

`IN_ALL_EVENTS` (`int`)  
Máscara de bits de todas las constantes anteriores

`IN_UNMOUNT` (`int`)  
Sistema de ficheros que contiene objetos observados fue desmontado

`IN_Q_OVERFLOW` (`int`)  
Cola de eventos desbordada (wd es -1 para este evento)

`IN_IGNORED` (`int`)  
Seguimiento borrado (explicitamente indicado por `inotify_rm_watch` o debido a que el fichero fue eliminado o el sistema de ficheros desmontado)

`IN_ISDIR` (`int`)  
El sujeto del evento es un directorio

`IN_ONLYDIR` (`int`)  
Observar la ruta solamente si se trata de un directorio (A partir de Linux 2.6.15)

`IN_DONT_FOLLOW` (`int`)  
No eliminar la ruta de referencia si es un enlace simbólico (A partir de Linux 2.6.15).

`IN_MASK_ADD` (`int`)  
Agregar eventos para observar la máscara de esta ruta de acceso si ya existe (en lugar de reemplazar la máscara).

`IN_ONESHOT` (`int`)  
Monitorea una ruta para un evento, a continuación elimina de la lista de vigilancia.

> [!NOTE]
> Los eventos más arriba marcados con un asterisco (\*) pueden producirse para ficheros en directorios observados.
