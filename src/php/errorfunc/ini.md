---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/errorfunc.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/errorfunc/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: errorfunc
translation_status: ready
translation_reviewed: false
translation_revision: c7b445ec8
order: 17730
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [error_reporting](#ini.error-reporting) | NULL | `INI_ALL` |  |
| [fatal_error_backtraces](#ini.fatal-error-backtraces) | "1" | `INI_ALL` | Disponible a partir de PHP 8.5.0 |
| [display_errors](#ini.display-errors) | "1" | `INI_ALL` |  |
| [display_startup_errors](#ini.display-startup-errors) | "1" | `INI_ALL` | Anterior a PHP 8.0.0, el valor por omisión era `"0"`. |
| [log_errors](#ini.log-errors) | "0" | `INI_ALL` |  |
| [log_errors_max_len](#ini.log-errors-max-len) | "1024" | `INI_ALL` | Sin efecto a partir de PHP 8.0.0, eliminado a partir de PHP 8.1.0. |
| [ignore_repeated_errors](#ini.ignore-repeated-errors) | "0" | `INI_ALL` |  |
| [ignore_repeated_source](#ini.ignore-repeated-source) | "0" | `INI_ALL` |  |
| [report_memleaks](#ini.report-memleaks) | "1" | `INI_ALL` | Obsoleto a partir de PHP 8.5.0 |
| [track_errors](#ini.track-errors) | "0" | `INI_ALL` | Deprecado a partir de PHP 7.2.0, eliminado a partir de PHP 8.0.0. |
| [html_errors](#ini.html-errors) | "1" | `INI_ALL` |  |
| [xmlrpc_errors](#ini.xmlrpc-errors) | "0" | `INI_SYSTEM` |  |
| [xmlrpc_error_number](#ini.xmlrpc-error-number) | "0" | `INI_ALL` |  |
| [docref_root](#ini.docref-root) | "" | `INI_ALL` |  |
| [docref_ext](#ini.docref-ext) | "" | `INI_ALL` |  |
| [error_prepend_string](#ini.error-prepend-string) | NULL | `INI_ALL` |  |
| [error_append_string](#ini.error-append-string) | NULL | `INI_ALL` |  |
| [error_log](#ini.error-log) | NULL | `INI_ALL` |  |
| [error_log_mode](#ini.error-log-mode) | 0o644 | `INI_ALL` | Disponible a partir de PHP 8.2.0. |
| [syslog.facility](#ini.syslog.facility) | "LOG_USER" | `INI_SYSTEM` | Disponible a partir de PHP 7.3.0. |
| [syslog.filter](#ini.syslog.filter) | "no-ctrl" | `INI_ALL` | Disponible a partir de PHP 7.3.0. |
| [syslog.ident](#ini.syslog.ident) | "php" | `INI_SYSTEM` | Disponible a partir de PHP 7.3.0. |

Opciones de configuración para la gestión de errores

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`error_reporting` `int`  
Establece el nivel de error. Este parámetro es un entero, representando un campo de bits. Añada los valores siguientes para elegir el nivel que desee, tal como se describe en la sección [Constantes predefinidas](#errorfunc.constants), y en el archivo `php.ini`. Para modificar esta configuración durante la ejecución del script, utilice la función `error_reporting`. Consulte también la directiva [display_errors](#ini.display-errors).

El valor por omisión es `E_ALL`.

Anterior a PHP 8.0.0, el valor por omisión era : `E_ALL & ~E_NOTICE & ~E_STRICT & ~E_DEPRECATED`. Esto significa que los diagnósticos de nivel `E_NOTICE`, `E_STRICT` y `E_DEPRECATED` no eran mostrados.

> [!NOTE]
> El uso de las constantes PHP fuera de PHP, como en el archivo `httpd.conf`, no tiene significado útil excepto en los casos donde se necesitan valores enteros. Y desde que los niveles de errores fueron añadidos, el valor máximo (para `E_ALL`) debería cambiar. Por lo tanto, en lugar de `E_ALL`, utilice un valor más grande para cubrir todos los bits, un valor numérico como `2147483647` (incluyendo todos los errores, y no solo los errores de tipo `E_ALL`).

`fatal_error_backtraces` `bool`  
Controla si los errores fatales deben incluir un seguimiento de pila. Los errores fatales son `E_ERROR`, `E_CORE_ERROR`, `E_COMPILE_ERROR`, `E_USER_ERROR`, `E_RECOVERABLE_ERROR`, y `E_PARSE`.

`display_errors` `string`  
Esta directiva determina si los errores deben ser mostrados en pantalla o no.

- `Off` : no mostrar ningún error.

- `On` o `stdout` : mostrar los errores a `stdout`. Es el valor por omisión.

- `stderr` : mostrar los errores a `stderr`. Solamente efectivo en las SAPIs `CLI`, `phpdbg` y `CGI`.

El `php.ini-development` empaquetado lo define en `On`; `php.ini-production` lo define en `Off`.

> [!NOTE]
> Es una directiva necesaria en desarrollo, pero que nunca debe ser utilizada en un sistema en producción. (ej. sistemas conectados a Internet).

> [!NOTE]
> Aunque display_errors puede ser definido durante la ejecución (con la función `ini_set`), no tendrá efecto si el script tiene errores fatales, ya que la acción deseada en el momento de la ejecución no será ejecutada.

`display_startup_errors` `bool`  
Aunque display_errors esté activado, pueden ocurrir errores durante la secuencia de inicio de PHP, y estos errores son ocultados. Con esta opción, puede mostrarlos, lo cual es recomendado para el depurado. Fuera de este caso, se recomienda encarecidamente dejar display_startup_errors en off.

`log_errors` `bool`  
Indica si los mensajes de error generados por los scripts deben ser registrados en el registro de errores del servidor o en [error_log](#ini.error-log). Esta función es específica del servidor.

> [!NOTE]
> Se recomienda utilizar el historial de errores, en lugar de mostrar los errores en los sitios de producción.

`log_errors_max_len` `int`  
Configura la longitud máxima de los errores que serán registrados en el historial, en kilobytes. En las informaciones de [error_log](#ini.error-log), se añade el origen. El valor por omisión es de 1024. 0 significa que no hay límite de longitud. Esta longitud se aplica para registrar en el historial los errores, mostrar los errores y también a `$php_errormsg` pero no para las llamadas explícitas a funciones como `error_log`.

Cuando se utiliza un `int`, el valor se mide en bytes. También se puede usar la notación abreviada, como se describe en [esta FAQ](#faq.using.shorthandbytes).

`ignore_repeated_errors` `bool`  
No registrar mensajes repetitivos. Los errores repetidos deben ocurrir en el mismo momento, en la misma línea y desde el mismo archivo de script, a menos que [ignore_repeated_source](#ini.ignore-repeated-source) esté definido a `true`.

`ignore_repeated_source` `bool`  
Ignora la fuente del mensaje en los mensajes repetidos. Cuando se ha configurado esta opción a On, no se registrarán los errores repetidos provenientes de archivos y líneas de código diferentes.

`report_memleaks` `bool`  
Si este parámetro está definido a On (por omisión), mostrará un informe de fuga de memoria detectada por el gestor de memoria Zend. Este informe será enviado a stderr en las plataformas Posix. En Windows, será enviado al depurador utilizando OutputDebugString() y podrá ser leído con herramientas como [DbgView](http://technet.microsoft.com/en-us/sysinternals/bb896647). Este parámetro solo tiene efecto durante una compilación de depuración, y si error_reporting incluye `E_WARNING` en su lista autorizada.

> [!WARNING]
> Esta característica está *OBSOLETA* a partir de PHP 8.5.0. Depender de esta característica está altamente desaconsejado.

`track_errors` `bool`  
Si esta opción está activada, el último mensaje de error será colocado en la variable `$php_errormsg`.

`html_errors` `bool`  
Si está activado, los mensajes de error incluirán etiquetas HTML. El formato de los errores HTML producirá mensajes clicables que redirigirán al usuario hacia una página describiendo el error o la función que causó el error. Estas referencias son afectadas por [docref_root](#ini.docref-root) y [docref_ext](#ini.docref-ext).

Si está desactivado, el mensaje de error será mostrado en texto plano.

`xmlrpc_errors` `bool`  
Si está activado, desactiva el informe normal de error y formatea los errores como mensajes de error XML-RPC.

`xmlrpc_error_number` `int`  
Utilizado como valor del elemento XML-RPC faultcode.

`docref_root` `string`  
El nuevo formato de error contiene una referencia a una página describiendo el error, o la función que causó el error. Para el manual, puede descargar este último en su idioma, y configurar esta opción para que apunte a él. Si su copia del manual es accesible a `"/manual/"`, puede simplemente utilizar `docref_root=/manual/`. Además, debe configurar `docref_ext` para que corresponda a las extensiones de su manual. `docref_ext=.html`. Es posible utilizar referencias externas. Por ejemplo, puede utilizar `docref_root=http://manual/en/` o `docref_root="http://landonize.it/?how=url&theme=classic&filter=Landon&url=http%3A%2F%2Fwww.php.net%2F"`

La mayoría de las veces, se utiliza la opción docref_root con una barra al final (`"/"`). Pero no es obligatorio, como muestra el segundo ejemplo anterior.

> [!NOTE]
> Esta directiva está destinada a ayudar en el desarrollo haciendo fácil la consulta de la descripción de una función. Nunca debe ser utilizada en un sistema de producción (ej. sistema conectado a Internet).

`docref_ext` `string`  
Consulte también [docref_root](#ini.docref-root).

> [!NOTE]
> El valor de docref_ext debe comenzar con un punto `"."`.

`error_prepend_string` `string`  
La cadena a colocar antes de los mensajes de error. Solo utilizado cuando el mensaje de error es mostrado en pantalla. El uso principal es poder añadir etiquetado HTML adicional antes del mensaje de error.

`error_append_string` `string`  
La cadena a colocar después de los mensajes de error. Solo utilizado cuando el mensaje de error es mostrado en pantalla. El uso principal es poder añadir etiquetado HTML adicional después del mensaje de error.

`error_log` `string`  
Nombre del archivo donde serán registrados los errores. El archivo debe ser accesible en escritura por el usuario ejecutando el servidor web. Si el valor especial `syslog` es utilizado, los errores serán enviados al sistema de registro del servidor. En Unix, esto corresponde a syslog(3) y en Windows al registro de eventos. Consulte también: `syslog`. Si esta directiva no está fijada, los errores son enviados al registro de errores SAPI. Por ejemplo, si es un registro de errores en Apache o `stderr` en CLI. Consulte también la función `error_log`.

`error_log_mode` `int`  
Modo de archivo para el archivo definido para [error_log](#ini.error-log).

`syslog.facility` `string`  
Especifica el tipo de programa que registra el mensaje. Solo efectivo si [error_log](#ini.error-log) está definido como "syslog".

`syslog.filter` `string`  
Especifica el tipo de filtro para filtrar los mensajes registrados. Los caracteres permitidos son pasados sin modificación; todos los demás son escritos en su representación hexadecimal prefijada con `\x`.

- `all` – la cadena registrada será separada en caracteres de retorno de línea, y todos los caracteres son transmitidos sin alteraciones

- `ascii` – la cadena registrada será separada en caracteres de retorno de línea, y todo carácter 7-bit ASCII no imprimible será escapado

- `no-ctrl` – la cadena registrada será separada en caracteres de retorno de línea, y los caracteres no imprimibles serán escapados

- `raw` – todos los caracteres son pasados al sistema de registro sin alteraciones, sin separaciones en los retornos de línea (idéntico a PHP anterior a 7.3)

Este parámetro afectará el registro a través de [error_log](#ini.error-log) definido como "syslog" y las llamadas a `syslog`.

> [!NOTE]
> El tipo de filtro `raw` está disponible a partir de PHP 7.3.8 y PHP 7.4.0.

Esta directiva no es soportada en Windows.

`syslog.ident` `string`  
Especifica la cadena de identidad que es añadida a cada mensaje. Solo efectivo si [error_log](#ini.error-log) está definido como "syslog".
