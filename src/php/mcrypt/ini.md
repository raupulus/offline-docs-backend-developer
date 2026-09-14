---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/mcrypt.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 46020
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [mcrypt.algorithms_dir](#ini.mcrypt.algorithms-dir) | `null` | `INI_ALL` |  |
| [mcrypt.modes_dir](#ini.mcrypt.modes-dir) | `null` | `INI_ALL` |  |

Opciones de configuración mcrypt

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`mcrypt.algorithms_dir` `string`  
El directorio que contiene los algoritmos. Por omisión es el directorio indicado durante la compilación de libmcrypt, típicamente se trata de */usr/local/lib/libmcrypt*. Consulte `mcrypt_list_algorithms` para más detalles.

`mcrypt.modes_dir` `string`  
El directorio que contiene los modos. Por omisión es el directorio indicado durante la compilación de libmcrypt, típicamente se trata de */usr/local/lib/libmcrypt*. Consulte `mcrypt_list_modes` para más detalles.
