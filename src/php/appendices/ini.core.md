---
title: Descripción de las directivas internas del php.ini
source_url: https://www.php.net/manual/es/ini.core.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/ini.core.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: false
translation_revision: a52e3d27c
order: 120
---

## Descripción de las directivas internas del `php.ini`

Esta lista incluye las directivas internas del `php.ini` que puede definir para personalizar su configuración de PHP. Las directivas gestionadas por las extensiones se enumeran y detallan en las páginas de documentación respectivas de las extensiones; la información sobre las directivas en las sesiones, por ejemplo, se puede encontrar en la página de documentación de las [sesiones](#session.configuration).

> [!NOTE]
> Los valores predeterminados enumerados aquí se utilizarán cuando `php.ini` no se carga; los valores de los archivos `php.ini` en entornos de producción y desarrollo pueden variar.

## Opciones del lenguaje

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [short_open_tag](#ini.short-open-tag) | "1" | `INI_ALL` |  |
| [precision](#ini.precision) | "14" | `INI_ALL` |  |
| [serialize_precision](#ini.serialize-precision) | "-1" | `INI_ALL` | Antes de PHP 7.1.0, el valor predeterminado era 17. |
| [disable_functions](#ini.disable-functions) | "" | `INI_SYSTEM` solo |  |
| [disable_classes](#ini.disable-classes) | "" | `php.ini` solo | Eliminado a partir de PHP 8.5.0 |
| [exit_on_timeout](#ini.exit-on-timeout) | "" | `INI_ALL` |  |
| [expose_php](#ini.expose-php) | "1" | `php.ini` solo |  |
| [hard_timeout](#ini.hard-timeout) | "2" | `INI_SYSTEM` | Disponible a partir de 7.1.0. |
| [zend.exception_ignore_args](#ini.zend.exception-ignore-args) | "0" | `INI_ALL` | Disponible a partir de 7.4.0 |
| [zend.multibyte](#ini.zend.multibyte) | "0" | `INI_ALL` |  |
| [zend.script_encoding](#ini.zend.script-encoding) | NULL | `INI_ALL` |  |
| [zend.detect-unicode](#ini.zend.detect-unicode) | NULL | `INI_ALL` |  |
| [zend.signal_check](#ini.zend.signal-check) | "0" | `INI_SYSTEM` |  |
| [zend.assertions](#ini.zend.assertions) | "1" | `INI_ALL` con restricciones |  |
| [zend.exception_string_param_max_len](#ini.zend.exception-string-param-max-len) | "15" | `INI_ALL` | Disponible a partir de PHP 8.0.0. |

Opciones de configuración

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`short_open_tag` `bool`  
Define si las etiquetas cortas de apertura de PHP (`<? ?>`) están permitidas o no. Si desea usar PHP con XML, debe desactivar esta opción de configuración para poder usar `<?xml ?>`. De lo contrario, puede escribirlo usando PHP, por ejemplo: `<?php echo '<?xml version="1.0">'; ?>`. Si esta opción está desactivada, debe usar la versión larga de las etiquetas de apertura de PHP (`<?php ?>`).

> [!NOTE]
> Esta directiva no afecta el uso de `<?=`, que siempre está disponible.

`precision` `int`  
El número de decimales significativos que se mostrarán en los números de coma flotante. `-1` significa que se utilizará el mejor algoritmo para redondear este número.

`serialize_precision` `int`  
El número de dígitos significativos conservados al serializar números de coma flotante. `-1` significa que se utilizará el mejor algoritmo para redondear este número.

`expose_php` `bool`  
Expone a todos los clientes el hecho de que PHP está instalado en el servidor. Esto incluye la versión de PHP en los encabezados HTTP de la respuesta (X-Powered-By: PHP/5.3.7).

`disable_functions` `string`  
Esta directiva le permite deshabilitar ciertas funciones. Toma una lista de nombres de funciones separados por comas.

Solo las [funciones internas](#functions.internal) pueden deshabilitarse usando esta directiva. Las [funciones definidas por el usuario](#functions.user-defined) no se ven afectadas.

Esta directiva debe definirse en el `php.ini`. Por ejemplo, no puede definirse en el archivo `httpd.conf`.

> [!WARNING]
> Esta directiva puede ser eludida y no debe considerarse una medida de seguridad suficiente para entornos de alojamiento compartido.

`disable_classes` `string`  
Esta directiva le permite deshabilitar ciertas clases. Toma una lista de nombres de clases separados por comas.

Solo las clases internas pueden deshabilitarse usando esta directiva. Las clases definidas por el usuario no se ven afectadas.

Esta directiva debe definirse en el `php.ini`. Por ejemplo, no puede definirse en el archivo `httpd.conf`.

> [!WARNING]
> Esta directiva puede ser eludida y no debe considerarse una medida de seguridad suficiente para entornos de alojamiento compartido.

> [!WARNING]
> Esta funcionalidad ha sido *ELIMINADA* a partir de PHP 8.5.0.

`zend.assertions` `int`  
Cuando se establece en `1`, se generará el código de aserción (en modo de desarrollo). Cuando se establece en `0`, se generará el código de aserción, pero se ignorará (no se ejecutará) durante la ejecución. Cuando se establece en `-1`, el código de aserción no se generará, haciendo que las aserciones sean completamente neutrales (en modo de producción).

> [!NOTE]
> Si un proceso se inicia en modo de producción, [zend.assertions](#ini.zend.assertions) no puede cambiarse en tiempo de ejecución, ya que el código para las aserciones no se ha generado.
>
> Si un proceso se inicia en modo de desarrollo, [zend.assertions](#ini.zend.assertions) no puede establecerse en `-1` en tiempo de ejecución.

`zend.exception_string_param_max_len` `int`  
La longitud máxima de los argumentos de función de cadenas en los trazas de pila convertidos en cadenas. Debe estar en el rango entre `"0"` y `"1000000"`.

`hard_timeout` `int`  
Cuando se alcanza el tiempo de espera establecido en [max_execution_time](#ini.max-execution-time), el tiempo de ejecución de PHP destruirá los recursos de manera elegante. Si algo se bloquea cuando esto ocurre, se activará el tiempo de espera forzado durante el número de segundos establecido. Cuando se alcanza el tiempo de espera forzado, PHP saldrá de manera no elegante. Cuando se establece en 0, el tiempo de espera forzado nunca se activará.

Cuando PHP finaliza con un tiempo de espera forzado, se verá algo así:

    Fatal error: Maximum execution time of 30+2 seconds exceeded (terminated) in Unknown on line 0

            

`zend.exception_ignore_args` `bool`  
Excluye los argumentos en los trazas de pila generados desde las excepciones.

`zend.multibyte` `bool`  
Activa el análisis léxico de archivos PHP en codificaciones multibyte. Activar zend.multibyte es necesario para usar ciertas codificaciones de caracteres como SJIS, BIG5, etc., que contienen caracteres especiales en codificación multibyte. Las codificaciones compatibles con ISO-8859-1 como UTF-8, EUC, etc., no requieren esta opción.

Activar zend.multibyte requiere la extensión mbstring.

`zend.script_encoding` `string`  
Este valor se usará a menos que una directiva [declare(encoding=...)](#control-structures.declare.encoding) aparezca en la parte superior del script. Cuando se usa una codificación incompatible con ISO-8859-1, se deben usar las opciones zend.multibyte y zend.script_encoding.

Los strings se convertirán desde zend.script_encoding a mbstring.internal_encoding, como si se hubiera llamado a la función `mb_convert_encoding`.

`zend.detect_unicode` `bool`  
Verifica el BOM (Byte Order Mark) y mira si el archivo contiene caracteres multibyte válidos. Esta detección se realiza antes de que se ejecute la función `__halt_compiler`. Disponible solo en modo multibyte de Zend.

`zend.signal_check` `bool`  
Verifica si se está utilizando un manejador de señales de reemplazo al detenerse.

`exit_on_timeout` `bool`  
Esta es una directiva solo para Apache1 mod_php que fuerza a los hilos de Apache a salir si ocurre un tiempo de espera de expiración de PHP. Tal expiración produce internamente una llamada a longjmp() en Apache1 que puede dejar algunas extensiones en un estado no consistente. Al terminar el proceso, todos los bloqueos y la memoria se limpiarán.

## Límite de recursos

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [memory_limit](#ini.memory-limit) | "128M" | `INI_ALL` |  |

Opciones de configuración

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`memory_limit` `int`  
Esta opción determina la memoria límite, en bytes, que un script está permitido asignar. Esto evita que un script mal codificado use toda la memoria. Tenga en cuenta que para no tener ningún límite, debe establecer esta directiva en `-1`.

Cuando se utiliza un `int`, el valor se mide en bytes. También se puede usar la notación abreviada, como se describe en [esta FAQ](#faq.using.shorthandbytes).

Véase también: [max_execution_time](#ini.max-execution-time).

## Ajuste de rendimiento

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [realpath_cache_size](#ini.realpath-cache-size) | "4M" | `INI_SYSTEM` | Antes de PHP 7.0.16 y 7.1.2, el valor predeterminado era `"16K"` |
| [realpath_cache_ttl](#ini.realpath-cache-ttl) | "120" | `INI_SYSTEM` |  |

Ajuste de rendimiento

> [!NOTE]
> Usar [open_basedir](#ini.open-basedir) *desactivará* la caché realpath.

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`realpath_cache_size` `int`  
Determina el tamaño de la caché de realpath que usará PHP. Este valor debería aumentarse en sistemas donde PHP abre varios archivos, para reflejar la cantidad de operaciones realizadas en los archivos.

El tamaño representa el número total de bytes en la cadena almacenada del camino, más el tamaño de los datos asociados con la entrada de la caché. Esto significa que para almacenar caminos largos en la caché, el tamaño de la caché debe ser lo suficientemente grande. Este valor no controla directamente el número de caminos distintos que pueden almacenarse en caché.

El tamaño necesario para los datos de la entrada de la caché depende del sistema.

`realpath_cache_ttl` `int`  
Tiempo (en segundos) durante el cual persiste la información de la caché de realpath para un archivo o directorio dado. Para sistemas con archivos que cambian poco, considere aumentar este valor.

## Manejo de datos

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [arg_separator.output](#ini.arg-separator.output) | "&" | `INI_ALL` |  |
| [arg_separator.input](#ini.arg-separator.input) | "&" | `INI_PERDIR` |  |
| [variables_order](#ini.variables-order) | "EGPCS" | `INI_PERDIR` |  |
| [request_order](#ini.request-order) | "" | `INI_PERDIR` |  |
| [auto_globals_jit](#ini.auto-globals-jit) | "1" | `INI_PERDIR` |  |
| [register_argc_argv](#ini.register-argc-argv) | "1" | `INI_PERDIR` | Obsoleto a partir de PHP 8.5.0 |
| [enable_post_data_reading](#ini.enable-post-data-reading) | "1" | `INI_PERDIR` |  |
| [post_max_size](#ini.post-max-size) | "8M" | `INI_PERDIR` |  |
| [auto_prepend_file](#ini.auto-prepend-file) | NULL | `INI_PERDIR` |  |
| [auto_append_file](#ini.auto-append-file) | NULL | `INI_PERDIR` |  |
| [default_mimetype](#ini.default-mimetype) | "text/html" | `INI_ALL` |  |
| [default_charset](#ini.default-charset) | "UTF-8" | `INI_ALL` |  |
| [input_encoding](#ini.input-encoding) | "" | `INI_ALL` |  |
| [output_encoding](#ini.output-encoding) | "" | `INI_ALL` |  |
| [internal_encoding](#ini.internal-encoding) | "" | `INI_ALL` |  |

Opciones de configuración

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`arg_separator.output` `string`  
El separador utilizado cuando PHP genera las URL para separar los argumentos.

`arg_separator.input` `string`  
Lista de separadores utilizados por PHP para analizar las URL entrantes y deducir los valores.

> [!NOTE]
> ¡Cada carácter de esta directiva se considera un separador!

`variables_order` `string`  
Define el orden de análisis de las variables EGPCS (`E`nvironment, `G`et, `P`ost, `C`ookie y `S`erver). Por ejemplo, si variables_order se establece en `"SP"`, entonces PHP creará [superglobals](#language.variables.predefined) `$_SERVER` y `$_POST`, pero no creará `$_ENV`, `$_GET` y `$_COOKIE`. Establecer este orden en "" significa que ninguna [superglobals](#language.variables.predefined) se definirá.

> [!WARNING]
> En las SAPIs CGI y FastCGI, `$_SERVER` también se llena con valores del entorno; `S` siempre es equivalente a `ES` en lo que respecta a la posición de `E` en cualquier otro lugar en esta directiva.

> [!NOTE]
> El contenido y el orden de `$_REQUEST` también se ven afectados por esta directiva.

`request_order` `string`  
Esta directiva describe el orden en el que PHP coloca las variables GET, POST y Cookie en la matriz \_REQUEST. La colocación se realiza de izquierda a derecha, con los valores más recientes sobrescribiendo los valores más antiguos.

Si esta directiva no está definida, se utiliza [variables_order](#ini.variables-order) para el contenido de `$_REQUEST`.

Tenga en cuenta que los archivos `php.ini` de la distribución predeterminada no contienen `'C'` para las cookies, por razones de seguridad.

`auto_globals_jit` `bool`  
Cuando esta directiva está activada, las variables SERVER, REQUEST y ENV se crean cuando se usan: solo si es necesario. Si estas variables no se usan en un script, el script verá un aumento en el rendimiento.

> [!WARNING]
> El uso de las variables SERVER, REQUEST y ENV se verifica durante la compilación. Por lo tanto, usarlas con, por ejemplo, [variables dinámicas](#language.variables.variable) no provocará su inicialización.

`register_argc_argv` `bool`  
Le dice a PHP si debe declarar o no las variables argv y argc (que contendrán la información GET).

Véase también las [líneas de comando](#features.commandline).

> [!WARNING]
> Esta característica está *OBSOLETA* a partir de PHP 8.5.0. Depender de esta característica está altamente desaconsejado.

> [!NOTE]
> Derivar `$_SERVER['argc']` y `$_SERVER['argv']` desde la query string para SAPI no-CLI ha sido marcado como obsoleto. Configurar `register_argc_argv=0` y usar en su lugar `$_GET` o `$_SERVER['QUERY_STRING']` para acceder a la información, tras verificar que el uso es seguro.

`enable_post_data_reading` `bool`  
Si se desactiva esta opción, las variables `$_POST` y `$_FILES` no se *poblarán*. El cuerpo de la petición permanece sin consumir en [php://input](#wrappers.php) y puede leerse manualmente o analizarse mediante `request_parse_body`. Esto puede ser interesante para las solicitudes a través de un proxy o para analizar los datos transmitidos directamente en la memoria.

`post_max_size` `int`  
Define el tamaño máximo de los datos recibidos por el método POST. Esta opción también afecta a los archivos cargados. Para cargar archivos grandes, este valor debe ser mayor que el valor de [upload_max_filesize](#ini.upload-max-filesize).

De manera general, [memory_limit](#ini.memory-limit) debe ser mayor que `post_max_size`.

Cuando se utiliza un `int`, el valor se mide en bytes. También se puede usar la notación abreviada, como se describe en [esta FAQ](#faq.using.shorthandbytes).

Si el tamaño de los datos recibidos por el método POST es mayor que post_max_size, `$_POST` y `$_FILES` [superglobales](#language.variables.superglobals) estarán vacías. Esto se puede monitorear de diferentes formas, por ejemplo, pasando una variable `$_GET` al script que procesa los datos, es decir, `<form action="edit.php?processed=1">`, y luego verificar si `$_GET['processed']` está definido.

> [!NOTE]
> PHP permite palabras clave para los bytes, incluyendo K (kilo), M (mega) y G (giga). PHP realiza la conversión automáticamente si usa estas palabras clave. Tenga cuidado de no exceder el límite de un entero con signo de 32 bits (si usa las versiones de 32 bits), en cuyo caso su script fallará.

| Versión | Descripción |
|----|----|
| 5.3.4 | `post_max_size` = 0 no desactivará el límite cuando el tipo de contenido es application/x-www-form-urlencoded o no está registrado con PHP. |
| 5.3.2 , 5.2.12 | Permite un tamaño de envío ilimitado estableciendo `post_max_size` en 0. |

Historial para `post_max_size`

`auto_prepend_file` `string`  
Especifica el nombre de un archivo que se recorrerá automáticamente antes del archivo principal. Este archivo se incluye como si se hubiera incluido con la función `require`, por lo que se usa [include_path](#ini.include-path).

El valor especial `none` desactiva la adición automática.

`auto_append_file` `string`  
Especifica el nombre del archivo que se recorrerá automáticamente después del archivo principal. Este archivo se incluye como si se hubiera incluido con la función `require`, por lo que se usa [include_path](#ini.include-path).

El valor especial `none` desactiva la adición automática.

> [!NOTE]
> Si el script termina con la función `exit`, *no* se realizará la adición automática.

`default_mimetype` `string`  
Por defecto, PHP enviará el tipo de medio usando el encabezado Content-Type. Para desactivar esto, deje este valor vacío.

El tipo de medio predeterminado en PHP es text/html.

`default_charset` `string`  
"UTF-8" es el valor predeterminado y se usa como el conjunto de caracteres predeterminado para las funciones y módulos. PHP siempre enviará un conjunto de caracteres predeterminado para `htmlentities`, `html_entity_decode` y `htmlspecialchars` si se omite el parámetro `encoding`. El valor de `default_charset` también se usará para establecer el conjunto de caracteres predeterminado para las funciones [iconv](#book.iconv) si las opciones de configuración [`iconv.input_encoding`](#ini.iconv.input-encoding), [`iconv.output_encoding`](#ini.iconv.output-encoding) y [`iconv.internal_encoding`](#ini.iconv.internal-encoding) no están definidas, y para las funciones [mbstring](#book.mbstring) si las opciones de configuración [`mbstring.http_input`](#ini.mbstring.http-input), [`mbstring.http_output`](#ini.mbstring.http-output) y [`mbstring.internal_encoding`](#ini.mbstring.internal-encoding) no están definidas.

Todas las versiones de PHP usarán este valor como el conjunto de caracteres predeterminado en el encabezado Content-Type predeterminado enviado por PHP si el encabezado no se sobrescribe a través de una llamada a la función `header`.

No se recomienda establecer un `default_charset` en un valor vacío.

`input_encoding` `string`  
Este parámetro se usa para los módulos multibyte como mbstring e iconv. Vacío por defecto.

`output_encoding` `string`  
Este parámetro se usa para los módulos multibyte como mbstring e iconv. Vacío por defecto.

`internal_encoding` `string`  
Este parámetro se usa para los módulos multibyte como mbstring e iconv. Vacío por defecto. Si está vacío, se usa [default_charset](#ini.default-charset).

## Rutas y directorios

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [include_path](#ini.include-path) | ".;/ruta/a/php/pear" | `INI_ALL` |  |
| [open_basedir](#ini.open-basedir) | NULL | `INI_ALL` |  |
| [doc_root](#ini.doc-root) | NULL | `INI_SYSTEM` |  |
| [user_dir](#ini.user-dir) | NULL | `INI_SYSTEM` |  |
| [user_ini.cache_ttl](#ini.user-ini.cache-ttl) | "300" | `INI_SYSTEM` |  |
| [user_ini.filename](#ini.user-ini.filename) | ".user.ini" | `INI_SYSTEM` |  |
| [extension_dir](#ini.extension-dir) | "/ruta/a/php" | `INI_SYSTEM` |  |
| [extension](#ini.extension) | NULL | `php.ini` solo |  |
| [zend_extension](#ini.zend-extension) | NULL | `php.ini` solo |  |
| [cgi.check_shebang_line](#ini.cgi.check-shebang-line) | "1" | `INI_SYSTEM` |  |
| [cgi.discard_path](#ini.cgi.discard-path) | "0" | `INI_SYSTEM` |  |
| [cgi.fix_pathinfo](#ini.cgi.fix-pathinfo) | "1" | `INI_SYSTEM` |  |
| [cgi.force_redirect](#ini.cgi.force-redirect) | "1" | `INI_SYSTEM` |  |
| [cgi.nph](#ini.cgi.nph) | "0" | `INI_SYSTEM` |  |
| [cgi.redirect_status_env](#ini.cgi.redirect-status-env) | NULL | `INI_SYSTEM` |  |
| [cgi.rfc2616_headers](#ini.cgi.rfc2616-headers) | "0" | `INI_ALL` |  |
| [fastcgi.impersonate](#ini.fastcgi.impersonate) | "0" | `INI_SYSTEM` |  |
| [fastcgi.logging](#ini.fastcgi.logging) | "1" | `INI_SYSTEM` |  |

Opciones de configuración

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`include_path` `string`  
Especifica una lista de directorios donde las funciones `require`, `include`, `fopen`, `file`, `readfile` y `file_get_contents` buscarán los archivos. El formato es idéntico a la variable de entorno del sistema `PATH`: una lista de directorios separados por dos puntos en Unix o por un punto y coma en Windows.

PHP considera cada entrada del camino de inclusión por separado al buscar archivos para incluir. Verificará el primer camino y, si no encuentra el archivo, verificará el siguiente camino, hasta encontrar el archivo para incluir o devolver una alerta de tipo `E_WARNING` o de tipo `E_ERROR` usando la función `set_include_path`.

include_path en Unix

```php
include_path=".:/php/includes"

         
```

include_path en Windows

```php
include_path=".;c:\php\includes"

         
```

El uso de un punto (`.`) en el camino de inclusión le permite hacer inclusiones relativas al directorio actual. Sin embargo, es más eficiente incluir explícitamente un archivo con `include './file'` que pedirle a PHP que verifique el directorio actual en cada inclusión.

> [!NOTE]
> Las variables `ENV` también están disponibles en los archivos .ini. Por lo tanto, es posible hacer referencia al directorio home usando la sintaxis `${LOGIN}` y `${USER}`.
>
> Las variables de entorno pueden variar según las APIs del servidor, así como según los entornos.

include_path en Unix usando la variable de entorno \${USER}

```php
include_path = ".:${USER}/pear/php"

         
```

`open_basedir` `string`  
Limita los archivos que pueden ser accedidos por PHP a una estructura de directorios específica, incluyendo el archivo mismo.

Cuando un script intenta acceder a un archivo con, por ejemplo, la función `include` o la función `fopen`, la ruta al archivo se analiza. Cuando el archivo se encuentra fuera de la estructura de directorios especificada, PHP se negará a acceder a él. Todos los enlaces simbólicos se resuelven, por lo que no es posible eludir esta restricción con un enlace simbólico. Si el archivo no existe, entonces el enlace simbólico no se puede resolver y el nombre del archivo se compara con `open_basedir`.

La opción `open_basedir` puede afectar más que las funciones del sistema de archivos; por ejemplo, si `MySQL` está configurado para usar el controlador `mysqlnd`, `LOAD DATA INFILE` se verá afectado por la opción `open_basedir`. La mayoría de las extensiones de PHP usan la opción `open_basedir` de esta manera.

El valor especial `.` indica que se usará el directorio actual del script como directorio base. Sin embargo, esto es ligeramente peligroso en el sentido de que el directorio actual puede cambiarse fácilmente con la función `chdir`.

En el archivo `httpd.conf`, `open_basedir` puede desactivarse (por ejemplo, para algunos hosts virtuales) de la [misma manera](#configuration.changes.apache) que cualquier directiva de configuración con "`php_admin_value open_basedir none`".

En Windows, separe los directorios con un punto y coma. En todos los demás sistemas, separe los directorios con dos puntos. Al usar Apache como módulo, los caminos de `open_basedir` desde los directorios padres ahora se heredan automáticamente.

La restricción especificada con `open_basedir` es un nombre de directorio, no un prefijo.

De manera predeterminada, todos los archivos pueden abrirse.

> [!NOTE]
> open_basedir puede afinarse en el momento de la ejecución. Esto significa que si open_basedir se establece en `/www/` en el archivo `php.ini`, un script puede afinar la configuración en `/www/tmp/` en el momento de la ejecución usando la función `ini_set`. Al recorrer varios directorios, puede usar la constante `PATH_SEPARATOR` según el sistema operativo.
>
> A partir de PHP 8.3.0, `open_basedir` ya no acepta rutas que contengan el directorio padre (`..`) cuando se establece en tiempo de ejecución usando `ini_set`.

> [!NOTE]
> Usar open_basedir establecerá [realpath_cache_size](#ini.realpath-cache-size) a `0` y, por lo tanto, *desactivará* la caché realpath.

> [!CAUTION]
> `open_basedir` es solo una medida de protección adicional y no es de ninguna manera exhaustiva, y no debe dependerse de ella cuando se necesita seguridad.

`doc_root` `string`  
El directorio raíz de PHP en el servidor. Solo se usa si no está vacío. Si PHP no se compiló con FORCE_REDIRECT, *debe* definir el doc_root si usa PHP como CGI bajo cualquier servidor web (distinto de IIS). Alternativamente, puede usar la configuración [cgi.force_redirect](#ini.cgi.force-redirect).

`user_ini.cache_ttl` `int`  

`user_ini.filename` `string`  

`user_dir` `string`  
El nombre base del directorio usado en un directorio de usuario para los archivos PHP, por ejemplo, `public_html`.

`extension_dir` `string`  
Especifica el directorio donde PHP debe buscar extensiones externas para cargar. Se recomienda especificar una ruta absoluta. Véase también [enable_dl](#ini.enable-dl) y `dl`.

`extension` `string`  
Qué extensiones deben cargarse dinámicamente al iniciar PHP.

`zend_extension` `string`  
Nombre de la extensión Zend cargable dinámicamente (por ejemplo, XDebug) que se cargará al iniciar PHP.

`cgi.check_shebang_line` `bool`  
Controla si PHP CGI verifica la línea que comienza con `#!` (shebang) en la parte superior del script ejecutado. Esta línea es necesaria si el script está destinado a ejecutarse de forma independiente y a través de un PHP CGI. PHP en modo CGI no lee esta línea y omite su contenido si esta directiva está activa.

`cgi.discard_path` `bool`  
Si está activado, el binario PHP CGI puede colocarse fuera del árbol web de manera segura y las personas no podrán eludir la seguridad .htaccess.

`cgi.fix_pathinfo` `bool`  
Proporciona un *real* `PATH_INFO`/`PATH_TRANSLATED` para CGI. El comportamiento anterior de PHP era establecer `PATH_TRANSLATED` en `SCRIPT_FILENAME` y no llenar `PATH_INFO`. Para obtener más información sobre `PATH_INFO`, consulte las especificaciones CGI. Si se establece en `1`, PHP CGI corregirá este camino según las especificaciones. Si se establece en 0, PHP aplicará el comportamiento anterior. De manera predeterminada, esta directiva está activada. Debe modificar sus scripts para usar `SCRIPT_FILENAME` en lugar de `PATH_TRANSLATED`.

`cgi.force_redirect` `bool`  
cgi.force_redirect es necesario por razones de seguridad al usar PHP en modo CGI bajo la mayoría de los servidores web. Si no lo establece, PHP lo activará automáticamente de manera predeterminada. Puede desactivarlo *bajo su propio riesgo*.

> [!NOTE]
> Usuarios de Windows: Al usar IIS, esta opción *debe* desactivarse; lo mismo ocurre con OmniHTTPD y Xitami.

`cgi.nph` `bool`  
Si cgi.nph está activado, forzará a CGI a enviar siempre el estado: 200 con cada solicitud.

`cgi.redirect_status_env` `string`  
Si cgi.force_redirect está activado y no está ejecutando un servidor web Apache o Netscape (iPlanet), *debería* definir un nombre de variable de entorno que PHP usará para verificar si todo está correcto para continuar la ejecución.

> [!NOTE]
> Definir esta variable *puede* tener consecuencias de seguridad. *Saber lo que hace antes de hacerlo*.

`cgi.rfc2616_headers` `bool`  
Le dice a PHP qué tipo de encabezado usar al enviar el código de respuesta HTTP. Si está desactivado, PHP enviará un encabezado "Status:" ([RFC 3875](https://datatracker.ietf.org/doc/html/rfc3875)) que es compatible con Apache y otros servidores web. Cuando está activado, PHP enviará un encabezado que cumple con la especificación [RFC 2616](https://datatracker.ietf.org/doc/html/rfc2616).

Si esta opción está activada y está ejecutando PHP en un entorno CGI (por ejemplo, PHP-FPM), no debe usar los encabezados de respuesta HTTP "status" RFC 2616, sino usar el equivalente RFC 3875, es decir, en lugar del encabezado ("HTTP/1.0 404 Not found"), use ("Status: 404 Not Found").

Deje este parámetro desactivado a menos que sepa exactamente lo que está haciendo.

`fastcgi.impersonate` `bool`  
FastCGI en IIS (en sistemas operativos basados en WINNT) admite la capacidad de determinar la marca de seguridad del cliente que llama. Esto permite que IIS establezca el contexto de seguridad en el que se ejecutará la solicitud. mod_fastcgi en Apache no admite actualmente esta funcionalidad (03/17/2002). Active si se ejecuta en IIS. De manera predeterminada, está desactivado.

`fastcgi.logging` `bool`  
Activa el registro SAPI con FastCGI. Activado de manera predeterminada.

## Carga de archivos

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [file_uploads](#ini.file-uploads) | "1" | `INI_SYSTEM` |  |
| [upload_tmp_dir](#ini.upload-tmp-dir) | NULL | `INI_SYSTEM` |  |
| [max_input_nesting_level](#ini.max-input-nesting-level) | 64 | `INI_PERDIR` |  |
| [max_input_vars](#ini.max-input-vars) | 1000 | `INI_PERDIR` |  |
| [upload_max_filesize](#ini.upload-max-filesize) | "2M" | `INI_PERDIR` |  |
| [max_file_uploads](#ini.max-file-uploads) | 20 | `INI_PERDIR` |  |

Opciones de configuración

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`file_uploads` `bool`  
Permite o no la [carga de archivos](#features.file-upload) por HTTP. Véase también las directivas [upload_max_filesize](#ini.upload-max-filesize), [upload_tmp_dir](#ini.upload-tmp-dir) y [post_max_size](#ini.post-max-size).

`upload_tmp_dir` `string`  
El directorio temporal usado para almacenar archivos durante la carga. El usuario bajo el cual se ejecuta PHP debe tener permisos de escritura en este directorio. Si no se especifica, PHP usará el directorio temporal predeterminado del sistema.

Si el directorio especificado aquí no es accesible en escritura, PHP recurrirá al directorio temporal predeterminado del sistema. Si [open_basedir](#ini.open-basedir) está activado, entonces el directorio temporal predeterminado del sistema debe estar permitido para que la carga de archivos funcione.

`upload_max_filesize` `int`  
El tamaño máximo en bytes de un archivo subido.

[post_max_size](#ini.post-max-size) debe ser mayor que este valor.

Cuando se utiliza un `int`, el valor se mide en bytes. También se puede usar la notación abreviada, como se describe en [esta FAQ](#faq.using.shorthandbytes).

`max_file_uploads` `int`  
El número máximo de archivos que pueden enviarse simultáneamente. Los campos de carga que se dejan vacíos al enviar no se cuentan en el cálculo de este límite.

## SQL general

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [sql.safe_mode](#ini.sql.safe-mode) | "0" | `INI_SYSTEM` | Eliminado a partir de PHP 7.2.0 |

Opciones de configuración

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`sql.safe_mode` `bool`  
Si está activado, las funciones de conexión a la base de datos que especifican valores predeterminados usarán estos valores en lugar de los argumentos proporcionados. Para los valores predeterminados, consulte la documentación de las funciones de conexión para la base de datos correspondiente.

> [!WARNING]
> ¡Esta funcionalidad ha sido *ELIMINADA* a partir de PHP 7.2.0!

## Específico de Windows

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [windows.show_crt_warning](#ini.windows-show-crt-warning) | "0" | `INI_ALL` |  |

Opciones de configuración específicas de Windows

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`windows.show_crt_warning` `bool`  
Esta directiva muestra las advertencias de CRT de Windows cuando está activada.
