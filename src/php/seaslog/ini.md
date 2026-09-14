---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/seaslog.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/seaslog/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: seaslog
translation_status: ready
translation_reviewed: false
translation_revision: 60f4ad429
order: 73120
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [seaslog.appender](#ini.seaslog.appender) | 1 | `INI_SYSTEM` |  |
| [seaslog.appender_retry](#ini.seaslog.appender-retry) | 0 | `INI_ALL` |  |
| [seaslog.level](#ini.seaslog.level) | 8 | `INI_ALL` |  |
| [seaslog.remote_host](#ini.seaslog.remote-host) | 127.0.0.1 | `INI_ALL` |  |
| [seaslog.remote_port](#ini.seaslog.remote-port) | 514 | `INI_ALL` |  |
| [seaslog.remote_timeout](#ini.seaslog.remote-timeout) | 1 | `INI_SYSTEM` |  |
| [seaslog.default_basepath](#ini.seaslog.default-basepath) | /var/log/www | `INI_SYSTEM` |  |
| [seaslog.default_logger](#ini.seaslog.default-logger) | default | `INI_SYSTEM` |  |
| [seaslog.default_template](#ini.seaslog.default-template) | %T \| %L \| %P \| %Q \| %t \| %M | `INI_SYSTEM` |  |
| [seaslog.default_datetime_format](#ini.seaslog.default-datetime-format) | Y-m-d H:i:s | `INI_SYSTEM` |  |
| [seaslog.trace_error](#ini.seaslog.trace-error) | 1 | `INI_ALL` |  |
| [seaslog.trace_exception](#ini.seaslog.trace-exception) | 0 | `INI_SYSTEM` |  |
| [seaslog.trace_notice](#ini.seaslog.trace-notice) | 0 | `INI_ALL` |  |
| [seaslog.trace_warning](#ini.seaslog.trace-warning) | 0 | `INI_ALL` |  |
| [seaslog.use_buffer](#ini.seaslog.use-buffer) | 0 | `INI_SYSTEM` |  |
| [seaslog.buffer_size](#ini.seaslog.buffer-size) | 0 | `INI_ALL` |  |
| [seaslog.buffer_disabled_in_cli](#ini.seaslog.buffer-disabled-in-cli) | 0 | `INI_SYSTEM` |  |
| [seaslog.disting_type](#ini.seaslog.disting-type) | 0 | `INI_SYSTEM` |  |
| [seaslog.disting_folder](#ini.seaslog.disting-folder) | 1 | `INI_SYSTEM` |  |
| [seaslog.disting_by_hour](#ini.seaslog.disting-by-hour) | 0 | `INI_SYSTEM` |  |
| [seaslog.recall_depth](#ini.seaslog.recall-depth) | 0 | `INI_ALL` |  |
| [seaslog.trim_wrap](#ini.seaslog.trim-wrap) | 0 | `INI_ALL` |  |
| [seaslog.ignore_warning](#ini.seaslog.ignore-warning) | 1 | `INI_ALL` |  |
| [seaslog.throw_exception](#ini.seaslog.throw-exception) | 1 | `INI_ALL` |  |

Opciones de configuración de Seaslog

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`seaslog.appender` `int`  
Cambia el almacén de datos del registro. 1Fichero 2TCP 3UDP (Cambiar por omisión 1)

Seaslog enviará el registro al servidor tcp://remote_host:remote_port o udp://remote_host:remote_port, cuando *seaslog.appender* está configurado a `2 (TCP)` o `3 (UDP)`.

Cuando *SeasLog* envía un registro a TCP/UDP, el estilo sigue la RFC5424. El `{logInfo}` es afectado por *seaslog.default_template*.

       
    The log style finally formatted such as:
    <15>1 2017-08-27T01:24:59+08:00 vagrant-ubuntu-trusty test/logger[27171]: 2016-06-25 00:59:43 | DEBUG | 21423 | 599157af4e937 | 1466787583.322 | this is a neeke debug
    <14>1 2017-08-27T01:24:59+08:00 vagrant-ubuntu-trusty test/logger[27171]: 2016-06-25 00:59:43 | INFO | 21423 | 599157af4e937 | 1466787583.323 | this is a info log
    <13>1 2017-08-27T01:24:59+08:00 vagrant-ubuntu-trusty test/logger[27171]: 2016-06-25 00:59:43 | NOTICE | 21423 | 599157af4e937 | 1466787583.324 | this is a notice log
        
         

`seaslog.appender_retry` `int`  
El conteo de reintentos del registro. 0 (No reintentar)

`seaslog.buffer_disabled_in_cli` `int`  
Desactiva el búfer en el CLI. 1-Y 0-N (Por omisión)

Activar el conmutador buffer_disabled_in_cli. El conmutador buffer_disabled_in_cli por omisión está desactivado. Si el conmutador buffer_disabled_in_cli está activado y se ejecuta en CLI, el parámetro seaslog.use_buffer será ignorado, Seaslog escribirá INMEDIATAMENTE en el almacén de datos.

`seaslog.buffer_size` `int`  
Configura el tamaño del búfer con 100. El tamaño del búfer por omisión 0, esto significa no usar búfer. Si buffer_size \> 0, SeasLog reescribirá hacia abajo en el almacén de datos cuando el registro pregrabado en memoria es \>= a este buffer_size, luego refrescará el grupo de memoria.

`seaslog.default_basepath` `string`  
La ruta base del registro por omisión. Por omisión "/var/log/www".

`seaslog.default_datetime_format` `string`  
El formato de la fecha y la hora. Por omisión "Y-m-d H:i:s".

`seaslog.default_logger` `string`  
La ruta del registro por omisión. Por omisión "default".

`seaslog.disting_by_hour` `int`  
El conmutador usa el registro con la hora. 1-Y 0-N (Por omisión)

> [!NOTE]
> *seaslog.disting_by_hour = 1* El conmutador usa Logger DisTing por hora. Esto significa que SeasLog creará el fichero cada hora.

`seaslog.disting_folder` `int`  
El conmutador usa el registro con la carpeta. 1-Y (Por omisión) 0-N

> [!NOTE]
> *seaslog.disting_folder = 1* El conmutador usa Logger DisTing por carpeta. Esto significa que SeasLog creará el fichero deistic por carpeta, y cuando esta configuración está desactivada, SeasLog creará el fichero utilice el conector de subrayado Logger y Time como default_20180211.log.

`seaslog.disting_type` `int`  
El conmutador usa el registro con el tipo. 1-Y 0-N (Por omisión)

> [!NOTE]
> *seaslog.disting_type = 1* El conmutador usa Logger DisTing por tipo, esto significa que SeasLog creará el fichero deistic info\warn\error y otro tipo.

`seaslog.ignore_warning` `int`  
El conmutador ignora las advertencias de SeasLog. 1-On (Por omisión) 0-Off

> [!NOTE]
> *seaslog.ignore_warning = 1* Abrir una advertencia para ignorar SeasLog mismo. Cuando los permisos de directorio o los puertos del servidor de recepción están bloqueados, son ignorados; cuando están cerrados, se lanza una advertencia.

`seaslog.level` `int`  
El nivel de registro. Por omisión 8 (Todos). 0-EMERGENCY 1-ALERT 2-CRITICAL 3-ERROR 4-WARNING 5-NOTICE 6-INFO 7-DEBUG 8-TODOS

> [!NOTE]
> Consejo: El elemento de configuración ha cambiado desde la versión 1.7.0. Antes de la versión 1.7.0, cuanto más pequeño es el valor, más registros se toman según el nivel: 0-todos 1-depuración 2-info 3-avisos 4-advertencia 5-error 6-crítico 7-alerta 8-emergencia Antes de la versión 1.7.0, por omisión 0 (Todos).

`seaslog.recall_depth` `int`  
La profundidad de llamada de la función. Esto afectará la variable `LineNo` en `%F`. Por omisión 0

`seaslog.remote_host` `string`  
Si se utiliza Record TCP o UDP, configure este host remoto. Por omisión "127.0.0.1"

`seaslog.remote_port` `int`  
Si se utiliza Record TCP o UDP, configure este puerto remoto. Por omisión 514

`seaslog.remote_timeout` `int`  
Si se utiliza Record TCP o UDP, configure este tiempo de espera remoto. Por omisión 1 segundo

`seaslog.throw_exception` `int`  
El conmutador lanza la excepción SeasLog. 1-On (Por omisión) 0-Off

> [!NOTE]
> *seaslog.throw_exception = 1* Abrir una excepción que lanza el SeasLog para lanzarse a sí mismo. Cuando los permisos de directorio o los puertos del servidor de recepción están bloqueados, lance una excepción; no lance una excepción cuando están cerrados.

`seaslog.trace_error` `int`  
Registrar automáticamente el error final con el registro por omisión. 1-Y (Por omisión) 0-N

`seaslog.trace_exception` `int`  
Registrar automáticamente la excepción con el registro por omisión. 1-Y 0-N (Por omisión)

`seaslog.trace_notice` `int`  
Registrar automáticamente el aviso con el registro por omisión. 1-Y 0-N (Por omisión)

`seaslog.trace_warning` `int`  
Registrar automáticamente la advertencia con el registro por omisión. 1-Y 0-N (Por omisión)

`seaslog.trim_wrap` `int`  
Recortar los \n y \r en el mensaje del registro. 1-On 0-Off (Por omisión)

`seaslog.use_buffer` `int`  
El conmutador usa el búfer del registro con la memoria. 1-Y 0-N (Por omisión)

> [!NOTE]
> *seaslog.use_buffer = 1* Activa el conmutador use_buffer. El conmutador use_buffer por omisión está desactivado. Si el conmutador use_buffer está activado, SeasLog pregraba el registro con la memoria, y serán reescritos en el almacén de datos por solicitud de parada o salida del proceso php (PHP RSHUTDOWN o PHP MSHUTDOWN).

`seaslog.default_template` `string`  
La plantilla de registro por omisión. Por omisión "%T \| %L \| %P \| %Q \| %t \| %M".

> [!NOTE]
> Las siguientes variables por omisión se proporcionan, que pueden ser usadas directamente en la plantilla de registro y reemplazadas por un valor correspondiente cuando el registro es finalmente generado.
>
> La plantilla de registro por omisión es: `seaslog.default_template = "%T | %L | %P | %Q | %t | %M"`, esto significa que el estilo de registro por omisión es: `{dateTime} | {level} | {pid} | {uniqid} | {timeStamp} | {logInfo}`
>
> Si se tiene una plantilla de registro personalizada, como: `seaslog.default_template = "[%T]:%L %P %Q %t %M"`, esto significará que el estilo de registro ha sido personalizado como: `[{dateTime}]:{level} {pid} {uniqid} {timeStamp} {logInfo}`
>
> | Nombre de variable | Descripción |
> |----|----|
> | %L | Nivel. |
> | %M | Mensaje. |
> | %T | Fecha y hora. Como `2017-08-16 19:15:02`, afectado por `seaslog.default_datetime_format`. |
> | %t | Marca de tiempo. Como `1502882102.862`, preciso a la milésima de segundo. |
> | %Q | El identificador de solicitud. Para distinguir una sola solicitud, no invocar la función `SeasLog::setRequestId($string)`, el valor único generado por la función integrada `static char *get_uniqid()` cuando la solicitud es inicializada es usado. |
> | %H | El nombre de host. |
> | %P | El identificador del proceso. |
> | %D | Dominio:Puerto. Como `www.cloudwise.com:80`; Con la Cli, como `cli`. |
> | %R | El URI de la solicitud. Como `/app/user/signin`; Con la Cli, es el script de índice, como `CliIndex.php`. |
> | %m | El método de la solicitud. Como `Get`; Con la Cli, es el script de comando, como `/bin/bash`. |
> | %I | La IP del Cliente; Con la Cli es `local`. El valor de prioridad: HTTP_X_REAL_IP \> HTTP_X_FORWARDED_FOR \> REMOTE_ADDR |
> | %F | Nombre del Fichero:Número de línea. Como `UserService.php:118`. |
> | %U | Uso de la memoria. byte. Llamada `zend_memory_usage`. |
> | %u | Uso máximo de la memoria. byte. Llamada `zend_memory_peak_usage`. |
> | %C | `TODO` Clase::Acción. Como `UserService::getUserInfo` |
>
> Tabla de variables por omisión de Seaslog
