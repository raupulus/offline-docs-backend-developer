---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/imagick.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: d4d5216e7
order: 37880
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [imagick.locale_fix](#ini.imagick.locale-fix) | `false` | `INI_ALL` | Disponible a partir de 2.1.0 |
| [imagick.progress_monitor](#ini.imagick.progress-monitor) | `false` | `INI_SYSTEM` | Disponible a partir de Imagick 2.2.2 |
| [imagick.skip_version_check](#ini.imagick.skip-version-check) | `false` | `INI_SYSTEM` | Disponible a partir de Imagick 3.3.0 |

Opciones de configuración de Imagick

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`imagick.locale_fix` `bool`  
Corrige un error en el dibujo cuando las configuraciones locales utilizan el carácter '`,`' como separadores.

`imagick.progress_monitor` `bool`  
Se utiliza para activar la supervisión de la progresión de la imagen.

`imagick.skip_version_check` `bool`  
Cuando Imagick se carga, se verifica el número de versión de ImageMagick utilizado durante la compilación, y se compara con el número de versión actualmente utilizado; se emite una alerta si las dos versiones no coinciden. Esta alerta puede ser eliminada activando esta opción de configuración.

El uso de una versión de Imagick diferente a la versión de ImageMagick no es recomendado. Aunque esto puede funcionar, puede resultar en errores aleatorios o comportamientos no definidos.
