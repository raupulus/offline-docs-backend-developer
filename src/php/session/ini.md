---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/session.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_revision: 7f1b75ed3
order: 73940
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [session.save_path](#ini.session.save-path) | "" | `INI_ALL` |  |
| [session.name](#ini.session.name) | "PHPSESSID" | `INI_ALL` |  |
| [session.save_handler](#ini.session.save-handler) | "files" | `INI_ALL` |  |
| [session.auto_start](#ini.session.auto-start) | "0" | `INI_PERDIR` |  |
| [session.gc_probability](#ini.session.gc-probability) | "1" | `INI_ALL` |  |
| [session.gc_divisor](#ini.session.gc-divisor) | "100" | `INI_ALL` |  |
| [session.gc_maxlifetime](#ini.session.gc-maxlifetime) | "1440" | `INI_ALL` |  |
| [session.serialize_handler](#ini.session.serialize-handler) | "php" | `INI_ALL` |  |
| [session.cookie_lifetime](#ini.session.cookie-lifetime) | "0" | `INI_ALL` |  |
| [session.cookie_path](#ini.session.cookie-path) | "/" | `INI_ALL` |  |
| [session.cookie_domain](#ini.session.cookie-domain) | "" | `INI_ALL` |  |
| [session.cookie_secure](#ini.session.cookie-secure) | "0" | `INI_ALL` | Anterior a PHP 7.2.0, el valor por omisión era `""`. |
| [session.cookie_httponly](#ini.session.cookie-httponly) | "0" | `INI_ALL` | Anterior a PHP 7.2.0, el valor por omisión era `""`. |
| [session.cookie_samesite](#ini.session.cookie-samesite) | "" | `INI_ALL` | Disponible a partir de PHP 7.3.0. |
| [session.use_strict_mode](#ini.session.use-strict-mode) | "0" | `INI_ALL` |  |
| [session.use_cookies](#ini.session.use-cookies) | "1" | `INI_ALL` |  |
| [session.use_only_cookies](#ini.session.use-only-cookies) | "1" | `INI_ALL` |  |
| [session.referer_check](#ini.session.referer-check) | "" | `INI_ALL` |  |
| [session.cache_limiter](#ini.session.cache-limiter) | "nocache" | `INI_ALL` |  |
| [session.cache_expire](#ini.session.cache-expire) | "180" | `INI_ALL` |  |
| [session.use_trans_sid](#ini.session.use-trans-sid) | "0" | `INI_ALL` |  |
| [session.trans_sid_tags](#ini.session.trans-sid-tags) | "a=href,area=href,frame=src,form=" | `INI_ALL` | Disponible a partir de PHP 7.1.0. |
| [session.trans_sid_hosts](#ini.session.trans-sid-hosts) | `$_SERVER['HTTP_HOST']` | `INI_ALL` | Disponible a partir de PHP 7.1.0. |
| [session.sid_length](#ini.session.sid-length) | "32" | `INI_ALL` | Disponible a partir de PHP 7.1.0. Obsoleto a partir de PHP 8.4.0. |
| [session.sid_bits_per_character](#ini.session.sid-bits-per-character) | "4" | `INI_ALL` | Disponible a partir de PHP 7.1.0. Obsoleto a partir de PHP 8.4.0. |
| [session.upload_progress.enabled](#ini.session.upload-progress.enabled) | "1" | `INI_PERDIR` |  |
| [session.upload_progress.cleanup](#ini.session.upload-progress.cleanup) | "1" | `INI_PERDIR` |  |
| [session.upload_progress.prefix](#ini.session.upload-progress.prefix) | "upload_progress\_" | `INI_PERDIR` |  |
| [session.upload_progress.name](#ini.session.upload-progress.name) | "PHP_SESSION_UPLOAD_PROGRESS" | `INI_PERDIR` |  |
| [session.upload_progress.freq](#ini.session.upload-progress.freq) | "1%" | `INI_PERDIR` |  |
| [session.upload_progress.min_freq](#ini.session.upload-progress.min-freq) | "1" | `INI_PERDIR` |  |
| [session.lazy_write](#ini.session.lazy-write) | "1" | `INI_ALL` |  |
| [session.hash_function](#ini.session.hash-function) | "0" | `INI_ALL` | Eliminado a partir de PHP 7.1.0 |
| [session.hash_bits_per_character](#ini.session.hash-bits-per-character) | "4" | `INI_ALL` | Eliminado a partir de PHP 7.1.0 |
| [session.entropy_file](#ini.session.entropy-file) | "" | `INI_ALL` | Eliminado a partir de PHP 7.1.0. |
| [session.entropy_length](#ini.session.entropy-length) | "0" | `INI_ALL` | Eliminado a partir de PHP 7.1.0. |

Opciones de configuración para las sesiones

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

El sistema de sesiones dispone de un gran número de directivas en el archivo `php.ini`. A continuación se presenta una descripción:

`session.save_handler` `string`  
Define el nombre del controlador de sesiones que se utiliza para almacenar y leer los datos. Por omisión, es el sistema integrado por archivos: `files`. Tenga en cuenta que las extensiones individuales deben registrar sus propios controladores de sesiones. Consulte también `session_set_save_handler`.

`session.save_path` `string`  
Define la ruta que debe pasarse al controlador de guardado. Si decide elegir el controlador por omisión (por archivos), este argumento se utilizará como carpeta de guardado de las sesiones. Consulte también `session_save_path`.

Existe un argumento opcional `N` para esta directiva que determina la profundidad de directorios donde su archivo de sesión será almacenado. Por ejemplo, si define `'5;/tmp'`, su archivo estará ubicado en `/tmp/4/b/1/e/3/sess_4b1e384ad74619bd212e236e52a5a174If`. Si desea utilizar `N`, debe crear todos estos directorios antes de usarlos. Existe un pequeño script shell en `ext/session` para realizar estas creaciones y se denomina `mod_files.sh`, y su versión Windows lleva el nombre `mod_files.bat`. Tenga en cuenta también que si `N` se utiliza y es superior a 0, entonces la rutina automática gc (recolección de basura) no se ejecutará; consulte una copia de `php.ini` para más información. Asimismo, si utiliza `N`, asegúrese de rodear `session.save_path` con "comillas dobles" ya que el separador (`;`) también se utiliza para los comentarios en `php.ini`.

El módulo de almacenamiento de archivos crea archivos utilizando el modo 600 por omisión. Este modo por omisión puede modificarse utilizando el argumento opcional `MODE`: `N;MODE;/path` donde `MODE` es la representación octal del modo. El hecho de definir el argumento `MODE` no afecta al proceso umask.

> [!WARNING]
> Si esta opción se configura con una carpeta accesible en lectura para todos, como `/tmp` (por omisión), otros usuarios podrán explotar estas sesiones obteniendo la lista de archivos en esta carpeta.

> [!CAUTION]
> Al utilizar el argumento opcional `N` que determina la profundidad de directorios, como se indicó anteriormente, tenga en cuenta que el uso de un valor superior a 1 o 2 no es apropiado para la mayoría de los sitios debido al número de directorios requeridos: por ejemplo, un valor de 3 implica que `(2 ** session.sid_bits_per_character) ** 3` directorios existen en el sistema de archivos lo que implica potencialmente un gran número de espacios y inodos desperdiciados.
>
> No utilice un valor de `N` superior a 2 a menos que esté seguro de que es necesario para su sitio.

`session.name` `string`  
Especifica el nombre de la sesión, que se utilizará como nombre de cookie. Solo debe contener caracteres alfanuméricos. Por omisión, es `PHPSESSID`. Consulte también `session_name`.

`session.auto_start` `bool`  
Especifica si el módulo de sesiones debe iniciarse automáticamente al comienzo de cada script PHP. Por omisión, es `0` (desactivado).

`session.serialize_handler` `string`  
Define el nombre del controlador que se utiliza para serializar y deserializar los datos. El formato de serialización PHP (llamado `php_serialize`), los formatos internos a PHP (llamados `php` y `php_binary`) y WDDX (llamado `wddx`) son soportados. WDDX solo está disponible, si PHP ha sido compilado con la opción [WDDX](#ref.wddx). `php_serialize` utiliza las funciones de serialización/deserialización en interno, y no tiene las limitaciones que `php` y `php_binary` tienen. Los antiguos controladores de serialización no pueden almacenar índices numéricos, ni índices en forma de cadenas que contengan caracteres especiales (`|` y `!`) en \$\_SESSION. Utilice `php_serialize` para evitar este tipo de error al final del script. Por omisión, es `php`.

`session.gc_probability` `int`  
Especifica la probabilidad, expresada en porcentaje, en conjunción de `session.gc_divisor`, que la rutina gc (`garbage collection`) se inicie en cada solicitud. El valor por omisión es `1`. Debe ser superior o igual a `0`. Consulte [session.gc_divisor](#ini.session.gc-divisor) para más detalles.

`session.gc_divisor` `int`  
`session.gc_divisor` en conjunción con `session.gc_probability` define la probabilidad que la rutina gc (`garbage collection`) se inicie en cada inicio de sesión. La probabilidad se calcula utilizando gc_probability/gc_divisor, por ejemplo 1/100 significa que hay un 1% de probabilidad de que la rutina gc se inicie en cada solicitud. El valor por omisión es `100`. Debe ser superior o igual a `0`.

`session.gc_maxlifetime` `int`  
Especifica la duración de vida de los datos en el servidor, en número de segundos. Después de este tiempo, los datos serán considerados obsoletos, y pueden potencialmente ser eliminados. Los datos pueden volverse obsoletos al inicio de la sesión (siguiendo [session.gc_probability](#ini.session.gc-probability) y [session.gc_divisor](#ini.session.gc-divisor)). El valor por omisión es `1440` (24 minutos).

> [!NOTE]
> Si diferentes scripts tienen valores diferentes de `session.gc_maxlifetime` pero comparten el mismo lugar para almacenar los datos de sesión, entonces, el script con el valor más pequeño borrará los datos. En este caso, utilice esta directiva conjuntamente con [session.save_path](#ini.session.save-path).

`session.referer_check` `int`  
Contiene una subcadena que desea encontrar en todos los encabezados HTTP Referer. Si este encabezado ha sido enviado por el cliente y la subcadena no ha sido encontrada, el identificador de sesión será considerado inválido. Por omisión, esta opción es una cadena vacía.

`session.entropy_file` `string`  
Es un camino hasta una fuente externa (un archivo), que será utilizada como fuente adicional de entropía para la creación del identificador de sesión. Ejemplos válidos son `/dev/random` y `/dev/urandom`, que están disponibles en todos los sistemas Unix.

Esta funcionalidad es soportada en Windows. El hecho de definir `session.entropy_length` a un valor diferente de cero hará que PHP utilice la API aleatoria de Windows como fuente de entropía.

> [!NOTE]
> Eliminado en PHP 7.1.0.
>
> `session.entropy_file` vale por omisión `/dev/urandom` o `/dev/arandom` si está disponible.

`session.entropy_length` `int`  
Especifica el número de bytes que serán leídos en el archivo definido anteriormente. Por omisión `32`.

Eliminado en PHP 7.1.0.

`session.use_strict_mode` `bool`  
`session.use_strict_mode` especifica si el módulo debe utilizar el modo de identificador de sesión estricto. Si este modo está activado, el módulo no aceptará identificadores de sesión no inicializados. Si un identificador de sesión no inicializado es enviado desde el navegador, un nuevo identificador de sesión será enviado al navegador. Las aplicaciones están protegidas de la fijación de sesiones mediante el uso del modo estricto de sesiones. Por omisión, vale `0` (desactivado).

> [!NOTE]
> Activar `session.use_strict_mode` es obligatorio para la seguridad general de las sesiones. Se recomienda activarlo para todos los sitios. Consulte el ejemplo de código de `session_create_id` para más detalles.

> [!WARNING]
> Si un controlador de sesiones registrado mediante la función `session_set_save_handler` no implementa SessionUpdateTimestampHandlerInterface::validateId, ni proporciona la función de devolución de llamada `validate_sid`, respectivamente, el modo de identificador de sesión estricto estará efectivamente desactivado, siguiendo el valor de esta directiva. Tenga en cuenta que `SessionHandler` *no implementa* el método SessionHandler::validateId.

`session.use_cookies` `bool`  
Especifica si el módulo utilizará cookies para almacenar el id de sesión en el lado del cliente. Por omisión, vale `1`, es decir, activo.

`session.use_only_cookies` `bool`  
Especifica si el módulo debe utilizar **solo** cookies para almacenar los identificadores de sesiones en el lado del navegador. Al activarlo, evitará ataques que utilicen identificadores de sesiones en las URL. Por omisión, vale `1` (activado).

`session.cookie_lifetime` `int`  
Especifica la duración de vida de la cookie en segundos. El valor de `0` significa: "Hasta que el navegador se apague". El valor por omisión es `0`. Consulte también `session_get_cookie_params` y `session_set_cookie_params`.

> [!NOTE]
> El timestamp que representa la duración de vida de la cookie se define en relación con el tiempo del servidor, que no es necesariamente el mismo que el tiempo del navegador.

`session.cookie_path` `string`  
Especifica el camino utilizado al crear la cookie. Por omisión, vale `/`. Consulte también `session_get_cookie_params` y `session_set_cookie_params`.

`session.cookie_domain` `string`  
Especifica el dominio utilizado al crear la cookie. Por omisión, no vale nada, lo que significa que es el nombre del host del servidor que genera la cookie de acuerdo con las especificaciones sobre cookies. Consulte también `session_get_cookie_params` y `session_set_cookie_params`.

`session.cookie_secure` `bool`  
Especifica que las cookies solo deben emitirse en conexiones seguras. Con esta opción definida en `on`, las sesiones solo funcionan con conexiones HTTPS. Si está definida en `off`, entonces las sesiones funcionan con las conexiones HTTP y HTTPS. Por omisión, está definida en `off`. Consulte también `session_get_cookie_params` y `session_set_cookie_params`.

`session.cookie_httponly` `bool`  
Marca la cookie para que solo sea accesible a través del protocolo HTTP. Esto significa que la cookie no será accesible por los lenguajes de script, como Javascript. Esta configuración permite limitar ataques como los ataques XSS (aunque no es soportado por todos los navegadores).

`session.cookie_samesite` `string`  
Permite que una cookie no sea enviada por el servidor con solicitudes entre sitios (cross-site). Esta afirmación permite a los agentes de usuario mitigar los riesgos de fuga de información de origen del sitio (cross-origin), y proporciona protección contra las ataques de falsificación de solicitudes entre sitios (cross-site request forgery). Tenga en cuenta que esto no es soportado por todos los navegadores. Un valor vacío significa que ningún atributo SameSite será definido. `Lax` y `Strict` significa que la cookie no será enviada para solicitudes POST entre dominios; `Lax` enviará la cookie para solicitudes GET entre dominios, mientras que `Strict` no lo hará.

`session.cache_limiter` `string`  
Especifica el tipo de control de caché utilizado para las páginas con sesiones. Los valores posibles son : `nocache`, `private`, `private_no_expire`, `public`. Por omisión, vale `nocache`. Consulte también `session_cache_limiter` para conocer el significado de estos valores.

`session.cache_expire` `int`  
Especifica la duración de vida de los datos de sesiones, en minutos. Esta opción no tiene ninguna consecuencia en el control de caché. Por omisión, vale `180` (3 horas). Consulte también `session_cache_expire`.

`session.use_trans_sid` `bool`  
Especifica si el soporte del SID es transparente o no. Por omisión vale `0` (desactivado).

> [!NOTE]
> El sistema de gestión de sesiones por URL representa un riesgo adicional de seguridad: un usuario puede enviar su URL con el identificador de sesión por correo electrónico a un amigo, o bien ponerla en sus marcadores. Esto difundirá entonces el identificador de sesión.
>
> Desde PHP 7.1.0, la URL completa, por ejemplo https://php.net/, es gestionada por la funcionalidad. Anteriormente, PHP gestionaba solo el camino relativo únicamente. El host objetivo de la reescritura está definido por [session.trans_sid_hosts](#ini.session.trans-sid-hosts).

`session.trans_sid_tags` `string`  
`session.trans_sid_tags` especifica las etiquetas HTML que son reescritas para incluir el ID de sesión cuando el soporte del SID transparente está activado. Por omisión `a=href,area=href,frame=src,input=src,form=`

`form` es una etiqueta especial. La variable de formulario `<input hidden="session_id" name="session_name">` es añadida.

> [!NOTE]
> Antes de PHP 7.1.0, [url_rewriter.tags](#ini.url-rewriter.tags) era utilizado para este propósito. Desde PHP 7.1.0, `fieldset` ya no es considerado como una etiqueta especial.

`session.trans_sid_hosts` `string`  
`session.trans_sid_hosts` especifica los hosts que son reescritos para incluir el ID de sesión cuando el soporte del SID transparente está activado. Por omisión `$_SERVER['HTTP_HOST']`. Varios hosts pueden ser especificados separados por ",", ningún espacio está permitido entre los hosts. Por ejemplo: `php.net,wiki.php.net,bugs.php.net`

`session.sid_length` `int`  
`session.sid_length` permite especificar la longitud de la cadena de ID de sesión. La longitud del ID de sesión puede ser comprendida entre 22 y 256.

El valor por omisión es 32. Si necesita compatibilidad, puede especificar 32, 40, etc. El ID de sesión más largo es más difícil de adivinar. Al menos 32 caracteres son recomendados.

> [!TIP]
> Nota de compatibilidad: utilizar 32 en lugar de `session.hash_function`=0 (MD5) y `session.hash_bits_per_character`=4, `session.hash_function`=1 (SHA1) y `session.hash_bits_per_character`=6. Utilizar 26 en lugar de `session.hash_function`=0 (MD5) y `session.hash_bits_per_character`=5. Utilizar 22 en lugar de `session.hash_function`=0 (MD5) y `session.hash_bits_per_character`=6. Debe configurar los valores INI para que haya 128 bits en el ID de sesión. No olvide definir el valor apropiado a `session.sid_bits_per_character`, de lo contrario tendrá ID de sesión más débiles.

> [!NOTE]
> Disponible a partir de PHP 7.1.0.

`session.sid_bits_per_character` `int`  
`session.sid_bits_per_character` permite especificar el número de bits en el carácter codificado en el ID de sesión. Los valores posibles son '4' (0-9, a-f), '5' (0-9, a-v), y '6' (0-9, a-z, A-Z, "-", ",").

El valor por omisión es 4. Más bits resultan en un ID de sesión más fuerte. 5 es el valor recomendado para la mayoría de los entornos.

> [!NOTE]
> Disponible a partir de PHP 7.1.0.

`session.hash_function` mixed  
`session.hash_function` permite especificar la función de hash a utilizar para generar los identificadores de sesión. '0' significa MD5 (128 bits) y '1' significa SHA-1 (160 bits).

También es posible especificar cualquier algoritmo proporcionado por la [extensión hash](#ref.hash) (si está disponible), como `sha512` o `whirlpool`. Una lista completa de algoritmos puede ser obtenida con la función `hash_algos`.

> [!NOTE]
> Eliminado en PHP 7.1.0.

`session.hash_bits_per_character` `int`  
`session.hash_bits_per_character` permite definir el número de bits utilizados para cada carácter durante las conversiones de los datos binarios en elementos legibles. Los valores posibles son '4' (0-9, a-f), '5' (0-9, a-v), y '6' (0-9, a-z, A-Z, "-", ",").

> [!NOTE]
> Eliminado en PHP 7.1.0.

`session.upload_progress.enabled` `bool`  
Activa la supervisión de la progresión de una subida, poblando la variable `$_SESSION`. Por omisión, vale 1 (activado).

`session.upload_progress.cleanup` `bool`  
Limpia las informaciones de progresión tan pronto como todos los datos POST han sido leídos (es decir, la subida ha terminado). Por omisión, vale 1 (activado).

> [!NOTE]
> Se recomienda encarecidamente mantener activa esta funcionalidad.

`session.upload_progress.prefix` `string`  
Un prefijo utilizado para la clave relativa a la progresión de la subida en el array `$_SESSION`. Esta clave será concatenada con el valor de `$_POST[ini_get("session.upload_progress.name")]` para proporcionar un índice único.

Por omisión, vale "upload_progress\_".

`session.upload_progress.name` `string`  
El nombre de la clave a utilizar en el array `$_SESSION` para almacenar las informaciones de progresión. Consulte también [session.upload_progress.prefix](#ini.session.upload-progress.prefix).

Si `$_POST[ini_get("session.upload_progress.name")]` no es proporcionado o disponible, la progresión de una subida no será registrada.

Por omisión, vale "PHP_SESSION_UPLOAD_PROGRESS".

`session.upload_progress.freq` `mixed`  
Define el número de veces que las informaciones de progresión de subida deben ser actualizadas. Puede ser definido en bytes (es decir, "actualizar las informaciones de progresión de subida cada 100 bytes), o en porcentaje (es decir, "actualizar las informaciones de progresión de subida cada 1% de recepción del peso total del archivo").

Por omisión, vale "1%".

`session.upload_progress.min_freq` `int`  
El retraso mínimo entre las actualizaciones, en segundos. Por omisión, vale "1" (un segundo).

`session.lazy_write` `bool`  
`session.lazy_write`, cuando está definido a 1, significa que los datos de sesión solo serán reescritos si estos cambian. Por omisión 1, activado.

La progresión de subida no será registrada a menos que session.upload_progress.enabled esté activo, y que la variable \$\_POST\[ini_get("session.upload_progress.name")\] esté definida. Consulte la [progresión de subida de sesión](#session.upload-progress) para más información sobre esta funcionalidad.
