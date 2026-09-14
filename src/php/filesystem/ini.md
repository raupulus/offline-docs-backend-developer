---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/filesystem.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_revision: d4d5216e7
order: 24100
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [allow_url_fopen](#ini.allow-url-fopen) | "1" | `INI_SYSTEM` |  |
| [allow_url_include](#ini.allow-url-include) | "0" | `INI_SYSTEM` | Obsoleto a partir de PHP 7.4.0. |
| [user_agent](#ini.user-agent) | NULL | `INI_ALL` |  |
| [default_socket_timeout](#ini.default-socket-timeout) | "60" | `INI_ALL` |  |
| [from](#ini.from) | "" | `INI_ALL` |  |
| [auto_detect_line_endings](#ini.auto-detect-line-endings) | "0" | `INI_ALL` | Obsoleto a partir de PHP 8.1.0. |
| [sys_temp_dir](#ini.sys-temp-dir) | "" | `INI_SYSTEM` |  |

Opciones de configuración del sistema de ficheros y flujos

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`allow_url_fopen` `bool`  
Esta opción habilita las envolturas fopen de tipo URL que permiten el acceso a objetos URL como ficheros. Las envolturas predeterminadas están proporcionads para el acceso de [ficheros remotos](#features.remote-files) usando los protocolos ftp o http, algunas extensiones como [zlib](#ref.zlib) pueden registrar envolturas adicionales.

`allow_url_include` `bool`  
Esta opción permite es uso de envolturas fopen de tipo URL con las siguientes funciones: `include`, `include_once`, `require`, `require_once`.

> [!NOTE]
> Esta opción requiere allow_url_fopen para ser activada.

`user_agent` `string`  
Define el agente de usuario de PHP para el envío.

`default_socket_timeout` `int`  
Tiempo de espera predeterminado (en segundos) para sockets basados en flujos. Especificar un valor negativo significa tiempo de espera infinito.

`from` `string`  
La dirección de email a usar en conexiones FTP no autenticadas y como valor de la cabecera From de conexiones HTTP, al usar las envolturas ftp y http, respectivamente.

`auto_detect_line_endings` `bool`  
Cuando se activa, PHP examinará la información leída por `fgets` y `file` para ver si se está usando las convenciones de final de línea de Unix, MS-Dos o Macintosh.

Esto permite a PHP inter-operar con los sistemas Macintosh, pero por defecto está en Off, ya que hay una pérdida muy pequeña de rendimiento cuando se detectan las convenciones de EOL para la primera línea, y también porque la gente que usa retornos de carro como elementos serparadores bajo sistemas Unix podrían experimentar un comportamiento que no es compatible con versiones anteriores.

`sys_temp_dir` `string`
