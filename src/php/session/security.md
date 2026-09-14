---
title: Sesiones y Seguridad
source_url: https://www.php.net/manual/es/session.security.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/security.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: false
translation_revision: 55e0481a2
order: 73950
---

## Sesiones y Seguridad

Enlace externo: [Fijación de sesión](https://acrossecurity.com/papers/session_fixation.pdf)

La gestión de las sesiones HTTP representa el núcleo de la seguridad en la web. Medidas de mitigación *deben* ser consideradas para asegurar la seguridad de las sesiones. Los desarrolladores deben activar/utilizar los parámetros de seguridad apropiados.

## Gestión básica de sesiones

### Seguridad de sesiones

El módulo de sesión no puede garantizar que la información almacenada en una sesión sea vista únicamente por el usuario que ha creado la sesión. Medidas adicionales son necesarias para proteger la confidencialidad de la sesión, según el valor que se le asigne.

La importancia de los datos almacenados en una sesión debe ser evaluada y protecciones adicionales pueden ser desplegadas; esto tiene obligatoriamente un costo como ser menos práctico para el usuario. Por ejemplo, para proteger a los usuarios de una táctica simple, la directiva [session.use_only_cookies](#ini.session.use-only-cookies) debe ser activada. En este caso, las cookies deben ser activadas obligatoriamente lado-cliente sino las sesiones no funcionarán.

Existen varias formas de divulgar identificadores de sesión a terceros. Por ejemplo, inyecciones Javascript, identificadores de sesión en las URLs, sniffing de paquetes, acceso físico al dispositivo, etc. Un identificador de sesión divulgado permite a un tercero acceder a todos los recursos asociados con dicho identificador. Primero, las URLs que contienen los identificadores de sesión. Si hay enlaces a sitios o recursos externos, la URL que incluye el identificador de sesión debe ser almacenada en los logs referrer del sitio externo. Si estos datos no están cifrados, los identificadores de sesión serán transmitidos en texto plano por la red. La solución aquí es implementar SSL/TLS en el servidor y hacerlo obligatorio para los usuarios. HSTS debe ser utilizado para mejorar también la seguridad.

> [!NOTE]
> Incluso HTTPS no puede proteger la confidencialidad de los datos en todos los casos. Por ejemplo, las vulnerabilidades CRIME y BEAST permiten a un atacante leer los datos. Además, note que algunas redes utilizan proxys HTTPS MITM para auditorías. Los atacantes también pueden establecer este tipo de proxy.

### Gestión de sesiones no adaptativas

El gestor de sesiones de PHP es adaptativo, por defecto. Un gestor de sesiones adaptativo introduce riesgos adicionales.

Cuando [session.use_strict_mode](#ini.session.use-strict-mode) está activado, y el gestor de guardado de sesiones lo soporta, un identificador de sesión no inicializado es rechazado, y uno nuevo es creado. Esto previene un ataque que fuerza a los usuarios a utilizar un identificador de sesión conocido. Un atacante puede pasar enlaces o enviar emails que contienen el identificador de sesión. Por ejemplo: `http://example.com/page.php?PHPSESSID=123456789` si [session.use_trans_sid](#ini.session.use-trans-sid) está activado, la víctima iniciará una sesión utilizando el identificador de sesión proporcionado por el atacante. [session.use_strict_mode](#ini.session.use-strict-mode) permite anular este tipo de riesgo.

> [!WARNING]
> Los gestores de guardado definidos por el usuario también pueden soportar el modo de sesión estricto implementando la validación de identificadores de sesión. Todos los gestores de guardado definidos por el usuario deben implementar la validación de identificadores de sesión.

La cookie de identificador de sesión puede ser definida con los atributos domain, path, httponly, secure y, desde PHP 7.3, SameSite. Existe una prioridad definida por los navegadores. Utilizando las prioridades, un atacante puede definir el identificador de sesión que puede ser utilizado permanentemente. El uso de la directiva [session.use_only_cookies](#ini.session.use-only-cookies) no permite resolver este problema. [session.use_strict_mode](#ini.session.use-strict-mode) permite mitigar este riesgo. Con la directiva [session.use_strict_mode](#ini.session.use-strict-mode)=On, el identificador de sesión no inicializado será rechazado.

> [!NOTE]
> Aunque la directiva [session.use_strict_mode](#ini.session.use-strict-mode) limita los riesgos concernientes al gestor adaptativo de sesión, un atacante puede forzar a los usuarios a utilizar un identificador de sesión no inicializado que ha sido creado por el atacante, por ejemplo, mediante inyecciones Javascript. Este tipo de ataque puede ser limitado utilizando las recomendaciones de este manual.
>
> Siguiendo este manual, los desarrolladores deben activar la directiva [session.use_strict_mode](#ini.session.use-strict-mode), utilizar timestamps basados en el gestor de sesión, y regenerar los identificadores de sesión utilizando la función `session_regenerate_id` con los procedimientos recomendados. Si los desarrolladores siguen estas instrucciones, un identificador de sesión generado por un atacante será normalmente eliminado.
>
> Cuando ocurre un acceso a una sesión obsoleta, los desarrolladores deben guardar todas las datos de la sesión activa del usuario; estas informaciones serán útiles para futuras investigaciones. El usuario debe ser forzado a desconectarse de todas las sesiones, por ejemplo, forzándolo a identificarse de nuevo. Esto permite contrarrestar ataques utilizando sesiones robadas.

> [!WARNING]
> El acceso a una sesión obsoleta no significa necesariamente que se trate de una ataque. Una red inestable y/o la eliminación inmediata de la sesión activa hará que usuarios legítimos utilicen sesiones obsoletas.

Desde 7.1.0, la función `session_create_id` ha sido añadida. Esta función permite acceder a todas las sesiones activas de un usuario prefijando los identificadores de sesión con el identificador del usuario. La activación de la directiva [session.use_strict_mode](#ini.session.use-strict-mode) es vital en esta configuración. De lo contrario, los usuarios maliciosos pueden definir identificadores de sesiones para otros usuarios.

> [!NOTE]
> Los usuarios de versiones anteriores a PHP 7.1.0 *deben* utilizar CSPRNG, por ejemplo, `/dev/urandom`, o la función `random_bytes` y las funciones de hash para generar un nuevo identificador de sesión. La función `session_create_id` posee mecanismos de detección de colisiones, y genera un identificador de sesión siguiendo las configuraciones INI de las sesiones. El uso de la función `session_create_id` es recomendado.

### Regeneración de un identificador de sesión

La directiva [session.use_strict_mode](#ini.session.use-strict-mode) es un buen compromiso pero no es suficiente. Los desarrolladores deben también utilizar la función `session_regenerate_id` para la seguridad de las sesiones.

La regeneración de un identificador de sesión reduce el riesgo de robo de identificadores de sesión, por lo que la función `session_regenerate_id` debe ser utilizada periódicamente; por ejemplo, regenerar el identificador de sesión cada 15 minutos para asegurar contenido sensible. Incluso en el caso de que un identificador de sesión sea robado, tanto el usuario legítimo como el atacante tendrán su sesión que expirará. En otras palabras, el acceso al contenido por el usuario o el atacante generará un error de acceso a una sesión obsoleta.

Los identificadores de sesión *deben* ser regenerados cuando los privilegios del usuario son elevados, como después de una autenticación. La función `session_regenerate_id` debe ser llamada antes de almacenar las informaciones de autenticación en `$_SESSION`. (la función `session_regenerate_id` guarda los datos de sesión actuales automáticamente para guardar timestamps/etc... en la sesión actual.) Asegúrese de que la nueva sesión contenga la bandera de autenticación.

Los desarrolladores *no deben* basarse en la expiración del identificador de sesión definida por la directiva [session.gc_maxlifetime](#ini.session.gc-maxlifetime). Los atacantes pueden acceder al identificador de sesión de la víctima de forma periódica para evitar su expiración, y permitir su explotación incluyendo con sesiones autenticadas.

En su lugar, los desarrolladores deben implementar un timestamp basado en la gestión de datos de sesión.

> [!WARNING]
> Aunque el gestor de sesión puede manejar los timestamps de forma transparente, esta funcionalidad no está implementada. Los datos de las sesiones antiguas deben ser conservados hasta que el recuperador de memoria no haya pasado. Simultáneamente, los desarrolladores deben asegurarse ellos mismos de que los datos de sesión obsoleta sean efectivamente borrados. Sin embargo, los desarrolladores no deben borrar los datos de sesión activa demasiado rápido. Por ejemplo, `session_regenerate_id(true);` y `session_destroy` nunca deben ser llamados al mismo tiempo para una sesión activa. Esto puede parecer contradictorio, pero es un requisito del mandante.

`session_regenerate_id` *no borrará* las sesiones antiguas por defecto. Las sesiones autenticadas obsoletas pueden estar presentes para ser utilizadas. Los desarrolladores deben asegurarse de que las sesiones antiguas no sean utilizadas por nadie. Deben prohibir el acceso a los datos de sesión obsoleta utilizando ellos mismos timestamps.

> [!WARNING]
> La eliminación repentina de una sesión activa produce efectos secundarios indeseables. Las sesiones pueden desaparecer cuando hay conexiones concurrentes en la aplicación web y/o cuando la red es inestable.
>
> Los accesos potencialmente maliciosos son indetectables con la eliminación repentina de una sesión.
>
> En lugar de eliminar las sesiones obsoletas inmediatamente, los desarrolladores deben definir un corto tiempo de expiración (timestamp) en `$_SESSION`, y prohibir el acceso a los datos de sesión.
>
> Los desarrolladores no deben prohibir el acceso a los datos de las sesiones antiguas inmediatamente después de la ejecución de la función `session_regenerate_id`. El acceso debe ser prohibido en una etapa posterior; por ejemplo, unos segundos después para redes estables, como una red cableada y unos minutos después para redes inestables como teléfonos móviles o redes Wi-Fi.
>
> Si un usuario accede a una sesión obsoleta (sesión expirada), el acceso a esta sesión debe ser rechazado. También es recomendado borrar el estado de autenticación de todas las sesiones de usuario, ya que esto puede representar un eje de ataque.

El uso de la directiva [session.use_only_cookies](#ini.session.use-only-cookies) y de la función `session_regenerate_id` pueden causar un DoS personal con cookies no eliminadas definidas por los atacantes. En este caso, los desarrolladores pueden invitar a los usuarios a eliminar las cookies y advertirles que pueden encontrar un problema de seguridad. Los atacantes pueden definir cookies maliciosas mediante una aplicación web vulnerable, un plugin de navegador expuesto o viciado, un dispositivo físico comprometido, etc...

> [!WARNING]
> No se confunda sobre el riesgo DoS. [session.use_strict_mode](#ini.session.use-strict-mode)=On es obligatorio para la seguridad de los identificadores de sesión ! Todos los sitios son animados a activar la directiva [session.use_strict_mode](#ini.session.use-strict-mode).
>
> DoS solo puede ocurrir cuando la cuenta sufre un ataque. Una inyección Javascript en una aplicación representa la mayoría de los ejes de ataque.

### Eliminación de datos de sesión

Los datos de sesiones obsoletas deben ser inaccesibles y deben ser eliminados. El módulo actual de sesión no soporta este aspecto.

Los datos de sesiones obsoletas deben ser eliminados tan pronto como sea posible. Sin embargo, las sesiones activas no deben ser eliminadas instantáneamente. Para satisfacer estas recomendaciones, los desarrolladores mismos deben implementar un gestor de datos de sesión basado en timestamp.

Defina y gestione la expiración del timestamp en la variable global \$\_SESSION. Prohíba el acceso a los datos de sesiones caducadas. Cuando se detecte un acceso a datos de sesión obsoleta, debe eliminarse todo el estado autenticado de las sesiones de usuario y forzar a los usuarios a autenticarse de nuevo. El acceso a datos de sesiones obsoletas puede representar un ataque. Para lograr esto, los desarrolladores deben seguir todas las sesiones activas de todos los usuarios.

> [!NOTE]
> El acceso a una sesión obsoleta también puede ocurrir debido a una red inestable y/o un acceso concurrente a un sitio web, por ejemplo, el servidor intenta definir un nuevo identificador de sesión mediante una cookie, pero el paquete Set-Cookie nunca llegó al cliente debido a una pérdida de conexión. Una conexión puede crear un nuevo identificador de sesión mediante la función `session_regenerate_id`, pero otra conexión concurrente puede no haber recibido aún el identificador de sesión. Sin embargo, los desarrolladores deben prohibir el acceso a una sesión obsoleta en un momento más lejano. Por ejemplo, la gestión de sesiones basada en timestamp es obligatoria.

En resumen, los datos de sesiones no deben ser destruidos con la función `session_regenerate_id`, ni con la función `session_destroy`, pero los timestamps deben ser utilizados para controlar el acceso a los datos de sesión. Deje que la función `session_gc` elimine los datos obsoletos desde el almacenamiento de datos de sesiones.

### Sesión y Bloqueo

Los datos de sesión están bloqueados por defecto para evitar los accesos concurrentes. El bloqueo es obligatorio para mantener una consistencia de los datos de sesión a través de las peticiones.

Sin embargo, el bloqueo de sesión puede ser utilizado por los atacantes para realizar ataques DoS. Para minimizar el riesgo de un ataque DoS por bloqueo de sesión, debe minimizarse el uso de bloqueos. Utilice datos en modo solo lectura cuando los datos de sesión no necesiten ser actualizados. Utilice la opción 'read_and_close' con la función `session_start`. `session_start(['read_and_close'=>1]);` cerrará la sesión tan pronto como sea posible después de actualizar la variable global \$\_SESSION utilizando la función `session_commit`.

El módulo de sesión actual *no detecta* todas las modificaciones de la variable \$\_SESSION cuando la sesión está inactiva. Es responsabilidad del desarrollador no modificar la variable \$\_SESSION cuando la sesión está inactiva.

### Sesiones activas

Los desarrolladores deben mantener un registro de todas las sesiones activas de cada usuario, y notificarles el número de sesiones activas, desde qué dirección IP, desde cuándo, etc. PHP no mantiene registros de estas informaciones. Los desarrolladores están supuestos a hacerlo ellos mismos.

Existen diferentes formas de hacerlo. Una implementación posible es definir una base de datos que mantenga un registro de los datos necesarios, y almacenar todas las informaciones pertinentes. Dado que los datos de sesión son GCed, los desarrolladores deben tener cuidado con los datos GCed para mantener la base de datos de sesiones activas consistente.

Una de las implementaciones simples es "el identificador de usuario prefijando el identificador de sesión" y almacenar las informaciones necesarias en la variable \$\_SESSION. La mayoría de las bases de datos son relativamente eficientes para seleccionar un prefijo en forma de `string`. Los desarrolladores DEBEN utilizar la función `session_regenerate_id` así como la función `session_create_id` para esto.

> [!WARNING]
> Nunca utilice datos confidenciales como prefijo. Si el identificador de usuario es confidencial, debería utilizar la función `hash_hmac`.

> [!WARNING]
> La activación de la directiva [session.use_strict_mode](#ini.session.use-strict-mode) es obligatoria para este tipo de configuración. Asegúrese de que esté activada. De lo contrario, la base de datos de sesiones activas puede ser comprometida.

El gestor de sesión basado en timestamp es obligatorio para detectar el acceso a sesiones obsoletas. Cuando se detecte el acceso a una sesión obsoleta, la bandera de autenticación debe ser eliminada de todas las sesiones activas del usuario. Esto permite evitar que los atacantes continúen explotando las sesiones robadas.

### Sesión y auto-identificación

Los desarrolladores no deben utilizar identificadores de sesión con una larga duración para la auto-identificación, ya que esto aumenta el riesgo de utilizar sesiones robadas. Una funcionalidad de auto-identificación debe ser implementada por el desarrollador.

Utilice una clave de hash segura de un solo uso como clave de auto-identificación utilizando la función `setcookie`. Utilice un hash seguro más fuerte que SHA-2. Por ejemplo, SHA-256 o superior con datos aleatorios desde la función `random_bytes` o mediante `/dev/urandom`.

Si el usuario no está autenticado, verifique si la clave de auto-identificación de un solo uso es válida o no. En el caso de que sea válida, autentifique al usuario y defina una nueva clave de hash segura de un solo uso. Una clave de auto-identificación solo debe ser utilizada una vez, por ejemplo, nunca utilice una clave de auto-identificación, y siempre regénela.

Una clave de auto-identificación es una clave de autenticación con una larga duración, debe ser protegida tanto como sea posible. Utilice los atributos de cookie path/httponly/secure/SameSite para protegerla. Por ejemplo, nunca transmita la clave de auto-identificación a menos que sea necesario.

Los desarrolladores deben implementar las funcionalidades que desactivan la auto-identificación, y eliminan las cookies que contienen las claves de auto-identificación no necesarias.

### Ataques CSRF (Cross-Site Request Forgeries)

Las sesiones y las autenticaciones no protegen contra los ataques CSRF. Los desarrolladores deben implementar protecciones CSRF ellos mismos.

La función `output_add_rewrite_var` puede ser utilizada para la protección CSRF. Consulte las páginas del manual para más detalles.

> [!NOTE]
> PHP, antes de su versión 7.2.0, utiliza el mismo buffer de salida y las mismas configuraciones INI que la configuración trans-sid. Sin embargo, el uso de la función `output_add_rewrite_var` con versiones de PHP anteriores a 7.2.0 no es recomendado.

La mayoría de los frameworks de aplicaciones web soportan la protección CSRF. Consulte el manual de su framework de aplicación web para más detalles.

Desde PHP 7.3, el atributo SameSite de la cookie de sesión puede ser definido. Esto es una medida adicional que puede minimizar las vulnerabilidades CSRF.

## Seguridad de las configuraciones INI de sesión

Al asegurar las configuraciones INI de sesiones, los desarrolladores pueden experimentar la seguridad de las sesiones. Muchas configuraciones INI no tienen una configuración recomendada. Los desarrolladores son responsables de la correcta configuración de las sesiones.

- [session.cookie_lifetime](#ini.session.cookie-lifetime)=0

  El valor `0` tiene un significado importante. Informa a los navegadores de no almacenar la cookie en un espacio de almacenamiento permanente. También, cuando el navegador se cierra, la cookie de identificación de sesión es eliminada inmediatamente. Si los desarrolladores definen un valor diferente de 0, permite a otros usuarios utilizar el identificador de sesión. La mayoría de las aplicaciones deben utilizar "`0`" como valor.

  Si se desea una funcionalidad de auto-identificación, los desarrolladores deben implementar su propio sistema de auto-identificación seguro. No utilice identificadores de sesión de larga duración para esto. Para más información, consulte la sección adecuada de esta documentación.

- [session.use_cookies](#ini.session.use-cookies)=On

  [session.use_only_cookies](#ini.session.use-only-cookies)=On

  Aunque las cookies HTTP sufren de problemas técnicos, siguen siendo la forma preferida de gestionar los identificadores de sesiones. Utilice solo cookies para la gestión de identificadores de sesiones cuando sea posible. La mayoría de las aplicaciones deben utilizar una cookie para el identificador de sesión.

  Si [session.use_only_cookies](#ini.session.use-only-cookies)=Off, el módulo de sesión utilizará los valores del identificador de sesión definidos por las variables GET o POST proporcionadas, y la cookie del identificador de sesión no será inicializada.

- [session.use_strict_mode](#ini.session.use-strict-mode)=On

  Aunque la activación de [session.use_strict_mode](#ini.session.use-strict-mode) es obligatoria para la seguridad de las sesiones, esta directiva está desactivada por defecto.

  Este modo evita que el módulo de sesión utilice un identificador de sesión no inicializado. Dicho de otra forma, el módulo de sesión solo va a aceptar identificadores de sesiones válidos generados por el módulo de sesión. Rechazará todos los identificadores de sesión proporcionados por los usuarios.

  Debido a la especificación de cookies, los atacantes son capaces de colocar cookies que contienen identificadores de sesiones configurando localmente una base de datos de cookies o mediante inyecciones Javascript. [session.use_strict_mode](#ini.session.use-strict-mode) puede evitar que un atacante inicialice un identificador de sesión.

  > [!NOTE]
  > Los atacantes pueden inicializar un identificador de sesión con su propio dispositivo, y pueden definir el identificador de sesión de su víctima. Deben entonces mantener el identificador de sesión activo para poder abusar de él. Los atacantes deben pasar por muchos otros pasos para tener éxito en su ataque en este escenario. También, el uso de la directiva [session.use_strict_mode](#ini.session.use-strict-mode) permite limitar los riesgos.

- [session.cookie_httponly](#ini.session.cookie-httponly)=On

  Permite rechazar el acceso a una cookie de sesión desde javascript. Esta configuración evita que una cookie sea corrompida por una inyección Javascript.

  Es posible utilizar un identificador de sesión como token CSRF, pero no es recomendado. Por ejemplo, fuentes HTML pueden ser guardadas y enviadas a otros usuarios. Los desarrolladores no deben escribir los identificadores de sesión en las páginas web por razones de seguridad. Todas las aplicaciones web deben utilizar el atributo httponly para la cookie que contiene el identificador de sesión.

  > [!NOTE]
  > El token CSRF debe ser renovado periódicamente, al igual que el identificador de sesión.

- [session.cookie_secure](#ini.session.cookie-secure)=On

  Permite acceder a la cookie de identificador de sesión únicamente cuando el protocolo es HTTPS. Si un sitio web solo es accesible por HTTPS, esta directiva debe ser activada.

  HSTS debe ser utilizado para los sitios web accesibles solo por HTTPS.

- [session.cookie_samesite](#ini.session.cookie-samesite)="Lax" o [session.cookie_samesite](#ini.session.cookie-samesite)="Strict"

  Desde PHP 7.3, el atributo `"SameSite"` puede ser definido para la cookie de identificador de sesión. Este atributo es una forma de mitigar los ataques CSRF (Cross Site Request Forgery).

  La diferencia entre Lax y Strict es la accesibilidad de la cookie en las peticiones originadas de otros dominios empleando el método HTTP GET. Las cookies utilizando Lax serán accesibles mediante una petición GET originada de otro dominio, mientras que las cookies utilizando Strict no lo serán.

- [session.gc_maxlifetime](#ini.session.gc-maxlifetime)=\[elija el más pequeño posible\]

  [session.gc_maxlifetime](#ini.session.gc-maxlifetime) es una configuración para eliminar el identificador de sesión obsoleto. Confiar completamente en esta configuración *no es* recomendado. Los desarrolladores deben gestionar la duración de las sesiones con un timestamp por ellos mismos.

  La GC de sesiones (recolección de basura) es mejor realizada utilizando la función `session_gc`. La función `session_gc` debe ser ejecutada por un gestor de tareas; por ejemplo, un cron en los sistemas Unix.

  GC es ejecutado por probabilidad, por defecto. Esta configuración *no garantiza* que las sesiones antiguas sean eliminadas. Aunque los desarrolladores no deben basarse en este parámetro, se recomienda definirlo con el valor más pequeño posible. Debe ajustarse las directivas [session.gc_probability](#ini.session.gc-probability) y [session.gc_divisor](#ini.session.gc-divisor) de modo que las sesiones obsoletas sean eliminadas con la frecuencia apropiada. Si la funcionalidad de auto-identificación es necesaria, los desarrolladores deben implementar su propia funcionalidad de auto-identificación segura; consulte a continuación para más información. Nunca utilice el identificador de sesión de larga duración para realizar este tipo de funcionalidad.

  > [!NOTE]
  > Algunos módulos de gestión de guardado de sesiones no utilizan esta funcionalidad basada en expiración y probabilidad; por ejemplo, memcached, memcache. Consulte la documentación de estos gestores de guardado de sesiones para más detalles.

- [session.use_trans_sid](#ini.session.use-trans-sid)=Off

  El uso de un gestor de identificadores de sesiones transparente no está prohibido. Los desarrolladores deben emplearlo cuando sea necesario. Sin embargo, la desactivación de la gestión de identificadores de sesión de forma transparente permite asegurar un poco más los identificadores de sesión eliminando la posibilidad de una inyección de identificador de sesión o fuga de este identificador.

  > [!NOTE]
  > El identificador de sesión puede filtrarse desde URLs guardadas, URLs en emails, una fuente HTML guardada, etc...

- [session.trans_sid_tags](#ini.session.trans-sid-tags)=\[banderas limitadas\]

  (PHP 7.1.0 \>=) Los desarrolladores no deben reescribir banderas HTML innecesarias. El valor por defecto debe ser suficiente para la mayoría de los usos. Para versiones de PHP más antiguas, utilice en su lugar [url_rewriter.tags](#ini.url-rewriter.tags).

- [session.trans_sid_hosts](#ini.session.trans-sid-hosts)=\[hosts limitados\]

  (PHP 7.1.0 \>=) Este parámetro define una lista blanca de hosts que están autorizados a reescribir los identificadores de sesión transparentes. ¡Nunca añada hosts que no sean de confianza! El módulo de sesión solo autoriza `$_SERVER['HTTP_HOST']` cuando este parámetro está vacío.

- [session.referer_check](#ini.session.referer-check)=\[URL de origen\]

  Cuando el parámetro [session.use_trans_sid](#ini.session.use-trans-sid) está activo. Este parámetro reduce los riesgos de inyección de identificador de sesión. Si un sitio web es `http://example.com/`, defina como valor para este parámetro `http://example.com/`. Tenga en cuenta que los navegadores HTTPS no envían el encabezado referrer. Los navegadores pueden no enviar el encabezado referrer debido a su propia configuración. Por lo tanto, este parámetro no puede ser considerado como una medida fiable de seguridad. A pesar de todo, su uso es recomendado.

- [session.cache_limiter](#ini.session.cache-limiter)=nocache

  Asegura que el contenido HTTP no sea almacenado en caché para las sesiones autenticadas. Permite el almacenamiento en caché solo para los contenidos que no son privados. De lo contrario, el contenido será expuesto. El valor `"private"` debe ser empleado si el contenido HTTP no incluye datos sensibles desde un punto de vista de seguridad. Tenga en cuenta que `"private"` puede transmitir datos privados almacenados en caché para los clientes compartidos. `"public"` solo debe ser utilizado cuando el contenido HTML no contiene ningún dato privado.

- [session.hash_function](#ini.session.hash-function)="sha256"

  (PHP 7.1.0 \<) Una función de hash fuerte generará un identificador de sesión fuerte. Aunque una colisión de hash es poco probable con algoritmos de hash MD5, los desarrolladores deben utilizar SHA-2 o un algoritmo de hash más fuerte como sha384 y sha512. Los desarrolladores deben asegurarse de una longitud suficiente de la [entropía](#ini.session.entropy-length) para la función de hash utilizada.

- [session.save_path](#ini.session.save-path)=\[directorio no legible por todos\]

  Si este parámetro está definido a un directorio accesible en lectura por todos, como `/tmp` (por defecto), otros usuarios del servidor serán capaces de recuperar las sesiones listando los archivos presentes en este directorio.
