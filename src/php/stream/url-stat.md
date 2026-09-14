---
title: streamWrapper::url_stat
description: Lee la información sobre un fichero
source_url: https://www.php.net/manual/es/streamwrapper.url-stat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/streamwrapper/url-stat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: false
translation_revision: 525aa5f19
order: 88550
---

streamWrapper::url_stat

Lee la información sobre un fichero

## Descripción

```php
public streamWrapper::url_stat(string $path, int $flags): array
```php

Este método es llamado en respuesta a todas las funciones relacionadas con `stat`, tales como: `copy`, `fileperms`, `fileinode`, `filesize`, `fileowner`, `filegroup`, `fileatime`, `filemtime`, `filectime`, `filetype`, `is_writable`, `is_readable`, `is_executable`, `is_file`, `is_dir`, `is_link`, `file_exists`, `lstat`, `stat`, SplFileInfo::getPerms, SplFileInfo::getInode, SplFileInfo::getSize, SplFileInfo::getOwner, SplFileInfo::getGroup, SplFileInfo::getATime, SplFileInfo::getMTime, SplFileInfo::getCTime, SplFileInfo::getType, SplFileInfo::isWritable, SplFileInfo::isReadable, SplFileInfo::isExecutable, SplFileInfo::isFile, SplFileInfo::isDir, SplFileInfo::isLink, RecursiveDirectoryIterator::hasChildren

## Parámetros

`path`  
La ruta de acceso del fichero o la URL a analizar. Se debe tener en cuenta que en el caso de las URLs, deben estar delimitadas por ://. Cualquier otro formato no es soportado.

`flags`  
Las opciones adicionales activadas por la API de flujos. Puede contener una o más de las constantes siguientes, combinadas por OR:

| Opción | Descripción |
|----|----|
| STREAM_URL_STAT_LINK | Para los recursos que tienen la capacidad de enlazarse a otros recursos (como una redirección HTTP o un enlace simbólico). Esta opción indica que la información leída debe concernir al enlace en sí mismo, y no al recurso apuntado por el enlace. Esta opción es activada en respuesta a una llamada a `lstat`, `is_link` o `filetype`. |
| STREAM_URL_STAT_QUIET | Si esta opción está activada, el gestor no debe emitir errores. Si esta opción no está activada, se es responsable del informe de errores, llamando a la función `trigger_error` durante el análisis de la ruta de acceso. |

## Valores devueltos

Debe retornar un `array` con tantos elementos como `stat` retorna. Los valores desconocidos o no disponibles deben tomar un valor razonable (generalmente, `0`). Se debe prestar especial atención a `mode` como está documentado bajo `stat`. Debe retornar `false` en caso de fallo.

## Errores/Excepciones

Emite una advertencia `E_WARNING` si la llamada a este método falla (i.e. no implementado).

## Notas

> [!NOTE]
> La propiedad `streamWrapper::$context` es actualizada si un contexto válido es pasado a la función.

## Véase también

`stat`, streamwrapper::stream_stat
