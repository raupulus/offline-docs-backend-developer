---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/yac.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yac/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yac
translation_status: ready
translation_reviewed: false
translation_revision: d4d5216e7
order: 104270
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [yac.compress_threshold](#ini.yac.compress-threshold) | -1 | `INI_SYSTEM` |  |
| [yac.debug](#ini.yac.debug) | 0 | `INI_ALL` |  |
| [yac.enable](#ini.yac.enable) | 1 | `INI_SYSTEM` |  |
| [yac.enable_cli](#ini.yac.enable-cli) | 0 | `INI_SYSTEM` |  |
| [yac.keys_memory_size](#ini.yac.keys-memory-size) | 4M | `INI_SYSTEM` |  |
| [yac.serializer](#ini.yac.serializer) | php | `INI_SYSTEM` |  |
| [yac.values_memory_size](#ini.yac.values-memory-size) | 64M | `INI_SYSTEM` |  |

Yac Opciones de configuración

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`yac.compress_threshold` `int`  

`yac.debug` `int`  

`yac.enable` `int`  

`yac.enable_cli` `int`  

`yac.keys_memory_size` `string`  

`yac.serializer` `string`  

`yac.values_memory_size` `string`
