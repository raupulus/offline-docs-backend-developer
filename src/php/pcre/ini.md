---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/pcre.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcre/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcre
translation_status: ready
translation_revision: d4d5216e7
order: 61680
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [pcre.backtrack_limit](#ini.pcre.backtrack-limit) | "1000000" | `INI_ALL` |  |
| [pcre.recursion_limit](#ini.pcre.recursion-limit) | "100000" | `INI_ALL` |  |
| [pcre.jit](#ini.pcre.jit) | "1" | `INI_ALL` |  |

Opciones de configuración de PCRE

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`pcre.backtrack_limit` `integer`  
Límite de retroceso de PCRE. Por defecto es 100000 para PHP \< 5.3.7.

`pcre.recursion_limit` `integer`  
Límite de recursividad de PCRE. Por favor, observe que si establece este valor con un número alto se podría consumir toda la pila de procesos disponible y provocar finalmente el malfuncionamiento de PHP (a causa de alcanzar el límite del tamaño de la pila impuesto por el sistema operativo).

`pcre.jit` `bool`  
Si se va a utilizar la compilacion «just-in-time» de PCRE.
