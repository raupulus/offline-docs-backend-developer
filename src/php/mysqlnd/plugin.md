---
title: API del plugin del controlador nativo MySQL
source_url: https://www.php.net/manual/es/mysqlnd.plugin.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqlnd/plugin.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqlnd
translation_status: ready
translation_reviewed: false
translation_revision: 9598935f2
order: 56190
---

## API del plugin del controlador nativo MySQL

La API del plugin del controlador nativo MySQL es una funcionalidad del controlador nativo MySQL, o `mysqlnd`. El plugin `Mysqlnd` opera en la capa entre las aplicaciones PHP y el servidor MySQL. Es comparable a un proxy MySQL. Un proxy MySQL opera en una capa entre todas las aplicaciones cliente MySQL, por ejemplo, una aplicación PHP y un servidor MySQL. El plugin `Mysqlnd` puede realizar tareas típicas de proxy MySQL como el equilibrio de carga, así como el seguimiento y la optimización de las prestaciones. Debido a una arquitectura y una localización diferente, el plugin `mysqlnd` no tiene todos los inconvenientes de un proxy MySQL. Por ejemplo, con el plugin, no hay un único punto de fallo, no hay un servidor proxy dedicado que desplegar, y no hay un nuevo lenguaje que aprender (Lua).

Un plugin `mysqlnd` puede ejecutarse como una extensión a `mysqlnd`. Un plugin puede interceptar la mayoría de las funciones `mysqlnd`. Las funciones `mysqlnd` son llamadas por la extensión PHP MySQL como `ext/mysql`, `ext/mysqli`, y `PDO_MYSQL`. Como resultado, es posible para un plugin `mysqlnd` interceptar todas las llamadas realizadas por estas extensiones desde una aplicación cliente.

Las llamadas a las funciones internas `mysqlnd` pueden también ser interceptadas o reemplazadas. No hay ninguna restricción sobre la manipulación de las tablas de funciones internas `mysqlnd`. Es posible definir acciones para que cuando ciertas funciones `mysqlnd` sean llamadas por la extensión que utiliza `mysqlnd`, la llamada sea redirigida hacia la función apropiada del plugin `mysqlnd`. La posibilidad de manipular las tablas de funciones internas `mysqlnd` de este modo permite un máximo de flexibilidad.

El plugin `Mysqlnd` es, en realidad, una extensión PHP, escrita en C, que utiliza la API del plugin `mysqlnd` (que está compilada en el controlador nativo MySQL, `mysqlnd`). El plugin puede ser 100% transparente para las aplicaciones PHP. No se requiere ninguna modificación a las aplicaciones ya que el plugin opera en una capa diferente. El plugin `mysqlnd` puede ser utilizado en una capa por debajo de `mysqlnd`.

La lista siguiente representa algunas aplicaciones posibles del plugin `mysqlnd`.

- El equilibrio de carga.

  - Separación de lecturas y escrituras. Un ejemplo de esta funcionalidad es la extensión PECL/mysqlnd_ms (Maestro/esclavo). Esta extensión separa las consultas de lectura y escritura para una configuración de replicación.

  - Conmutación por error

  - Round-Robin, el menos cargado

- Supervisión

  - Registro de consultas

  - Análisis de consultas

  - Auditoría de consultas. Un ejemplo de esto es la extensión PECL/mysqlnd_sip (Protección contra Inyección SQL). Esta extensión inspecciona las consultas y ejecuta únicamente aquellas que son permitidas siguiendo conjuntos de reglas.

- Rendimiento

  - La caché. Un ejemplo de esto es la extensión PECL/mysqlnd_qc (Query Cache).

  - Limitación

  - Fragmentación. Un ejemplo de esto es la extensión PECL/mysqlnd_mc (Multi Connect). Esta extensión intenta separar una consulta SELECT en n partes, utilizando consultas del tipo SELECT ... LIMIT part_1, SELECT LIMIT part_n. La extensión envía las consultas a servidores MySQL distintos y luego fusiona el resultado hacia el cliente.

**Plugins del controlador nativo MySQL disponibles**

Ya hay varios plugins mysqlnd disponibles.

- **PECL/mysqlnd_mc** - Plugin Multi Conexión.

- **PECL/mysqlnd_ms** - Plugin Maestro Esclavo.

- **PECL/mysqlnd_qc** - Plugin de caché de consultas.

- **PECL/mysqlnd_pscache** - Plugin de caché de gestor de consultas preparadas.

- **PECL/mysqlnd_sip** - Plugin que permite la protección contra inyecciones SQL.

- **PECL/mysqlnd_uh** - Plugin de gestor de usuarios.

## Comparación de los plugins mysqlnd con proxy MySQL

Los plugins `Mysqlnd` y el proxy MySQL son tecnologías diferentes que utilizan diferentes enfoques. Ambos son herramientas válidas para resolver muchas tareas clásicas, como el equilibrio de carga, la supervisión, y la mejora de las prestaciones. Una diferencia importante es que el proxy MySQL funciona con todos los clientes MySQL mientras que los plugins `mysqlnd` son específicos para las aplicaciones PHP.

Como una extensión PHP, un plugin `mysqlnd` debe ser instalado en el servidor de aplicaciones PHP, además del resto de PHP. Un proxy MySQL puede funcionar tanto en el servidor de aplicaciones PHP como ser instalado en una máquina dedicada para gestionar varios servidores de aplicaciones PHP.

El despliegue de un proxy MySQL en un servidor de aplicaciones tiene 2 ventajas:

1.  No hay un único punto de fallo

2.  Fácil de escalar (escalado horizontal, escalado por el cliente)

Un proxy MySQL (y los plugins `mysqlnd`) puede resolver problemas fácilmente, que de otro modo habrían requerido modificaciones a las aplicaciones existentes.

Sin embargo, un proxy MySQL tiene algunos inconvenientes:

- Un proxy MySQL es un nuevo componente, una nueva tecnología a aplicar al maestro y desplegar.

- Un proxy MySQL requiere el conocimiento del lenguaje de script Lua.

Un proxy MySQL puede ser personalizado utilizando los lenguajes de programación C y Lua. Lua es el lenguaje preferido para un proxy MySQL. Para la mayoría de los expertos PHP, Lua es un nuevo lenguaje a aprender. Un plugin `mysqlnd` puede ser escrito en C. También es posible escribir un plugin en PHP utilizando [PECL/mysqlnd_uh](https://pecl.php.net/package/mysqlnd_uh).

Un proxy MySQL funciona como un demonio - un proceso en segundo plano. Un proxy MySQL puede recordar decisiones tomadas anteriormente, ya que todos los estados pueden ser conservados. Sin embargo, un plugin `mysqlnd` está ligado al ciclo de vida de una consulta PHP. Un proxy MySQL puede compartir también resultados calculados una sola vez entre varios servidores de aplicaciones. Un plugin `mysqlnd` puede necesitar almacenar datos en un medio persistente. Otro demonio puede ser utilizado con este propósito, como por ejemplo, Memcache. Este mecanismo da una ventaja al proxy MySQL.

Un proxy MySQL funciona por encima de la capa física. Con un proxy MySQL, debe analizar y realizar ingeniería inversa del protocolo cliente-servidor MySQL. Las acciones están limitadas a las que pueden ser realizadas mediante la manipulación del protocolo de comunicación. Si la capa física cambia (lo que ocurre muy raramente), los scripts del proxy MySQL pueden necesitar ser adaptados.

Los plugins `Mysqlnd` funcionan por encima de la API C, reflejando así las APIs cliente `libmysqlclient`. Esta API C es esencialmente una envoltura del protocolo Servidor Cliente MySQL, o de la capa física, ya que es llamada algunas veces. Puede interceptar todas las llamadas a la API C. PHP utiliza la API C, sin embargo, puede conectar todas las llamadas PHP, sin necesidad de programar a nivel de la capa física.

`Mysqlnd` implementa la capa física. Los plugins pueden analizar, realizar ingeniería inversa, manipular y siempre reemplazar el protocolo de comunicación. Sin embargo, esto no es generalmente necesario.

Dado que los plugins permiten crear implementaciones que utilizan los 2 niveles (API C y capa física), tienen más flexibilidad que el proxy MySQL. Si un plugin `mysqlnd` es implementado utilizando la API C, todos los cambios posteriores a la capa física no requerirán modificaciones al plugin en sí.

## Obtener la API del plugin mysqlnd

La API del plugin `mysqlnd` es simplemente una parte de la extensión del controlador PHP Nativo MySQL, `ext/mysqlnd`. El desarrollo de la API del plugin `mysqlnd` comenzó en Diciembre de 2009. Se desarrolla como parte del repositorio fuente de PHP, y por lo tanto, está disponible desde el repositorio público Git, o desde la descarga de las fuentes.

Los desarrolladores de plugins pueden determinar la versión de `mysqlnd` a través de la variable `MYSQLND_VERSION`, en el formato “mysqlnd 8.3.17”, o a través de `MYSQLND_VERSION_ID`, que es un entero como por ejemplo 50007. Los desarrolladores pueden calcular el número de versión de la siguiente manera:

| Versión (parte)    | Ejemplo          |
|--------------------|------------------|
| Mayor\*10000       | 5\*10000 = 50000 |
| Menor\*100         | 0\*100 = 0       |
| Parche             | 7 = 7            |
| MYSQLND_VERSION_ID | 50007            |

Tabla de cálculo de MYSQLND_VERSION_ID {#mysqlnd.plugin.version-id}

Durante el desarrollo, los desarrolladores deben referirse al número de versión `mysqlnd` para pruebas de compatibilidad y de versión, sabiendo que varias versiones de `mysqlnd` pueden ocurrir durante un ciclo de vida de la rama de desarrollo de PHP.

## Arquitectura del plugin del controlador nativo

Esta sección proporciona una visión general de la arquitectura del plugin `mysqlnd`.

**Visión general del controlador nativo MySQL**

Antes de desarrollar plugins `mysqlnd`, es útil tener un conocimiento mínimo sobre la organización de `mysqlnd`. `Mysqlnd` está compuesto por los siguientes módulos:

| Módulos de estadísticas            | mysqlnd_statistics.c   |
|------------------------------------|------------------------|
| Conexión                           | mysqlnd.c              |
| Juego de resultados                | mysqlnd_result.c       |
| Datos méta del juego de resultados | mysqlnd_result_meta.c  |
| Consulta                           | mysqlnd_ps.c           |
| Red                                | mysqlnd_net.c          |
| Capa física                        | mysqlnd_wireprotocol.c |

Esquema de la organización mysqlnd, por módulo {#mysqlnd.plugin.orgchart}

**Objeto C orientado a paradigma**

A nivel de código, `mysqlnd` utiliza una máscara C para implementar la orientación al objeto.

En C, se utiliza una estructura (`struct`) para representar un objeto. Los miembros de esta estructura representan las propiedades del objeto. Los miembros de la estructura que apuntan hacia funciones representan los métodos.

A diferencia de otros lenguajes como C++ o Java, no hay reglas fijas sobre la herencia en los objetos C orientados a paradigma. Sin embargo, hay algunas convenciones que deben seguirse que serán abordadas posteriormente.

**El ciclo de vida PHP**

El ciclo de vida de PHP consta de 2 ciclos básicos:

- El ciclo de inicio y parada del motor PHP

- El ciclo de una petición

Cuando el motor PHP se inicia, llama a la función de inicialización del módulo (MINIT) de cada extensión registrada. Esto permite a cada módulo definir las variables y asignar los recursos que deben existir durante la vida del proceso correspondiente al motor PHP. Cuando el motor PHP se detiene, llama a la función de parada del módulo (MSHUTDOWN) para cada extensión.

Durante la vida del motor PHP, recibirá peticiones. Cada petición constituye otro ciclo de vida. Para cada petición, el motor PHP llamará a la función de inicialización de cada extensión. La extensión puede realizar todas las definiciones de variables así como las asignaciones de recursos necesarias para procesar la petición. Cuando el ciclo de la petición termina, el motor llama a la función de parada (RSHUTDOWN) para cada extensión, por lo que la extensión puede lanzar toda la limpieza necesaria.

**Cómo funciona un plugin**

Un plugin `mysqlnd` funciona interceptando las llamadas realizadas a `mysqlnd` por las extensiones que utilizan `mysqlnd`. Esto es posible obteniendo la tabla de función `mysqlnd`, guardándola, y reemplazándola por una tabla de función personalizada, que llama a las funciones del plugin.

El código siguiente muestra cómo se reemplaza la tabla de función `mysqlnd`:

    /* un lugar para almacenar la tabla de función original */
    struct st_mysqlnd_conn_methods org_methods;

    void minit_register_hooks(TSRMLS_D) {
      /* tabla de función activa */
      struct st_mysqlnd_conn_methods * current_methods
        = mysqlnd_conn_get_methods();

      /* guardar la tabla de función original */
      memcpy(&org_methods, current_methods,
        sizeof(struct st_mysqlnd_conn_methods));

      /* instalación de las nuevas métodos */
      current_methods->query = MYSQLND_METHOD(my_conn_class, query);
    }

      

Las manipulaciones de la tabla de función de conexión deben realizarse durante la inicialización del módulo (MINIT). La tabla de función es un recurso global compartido. En un entorno multihilo, con una compilación TSRM, la manipulación de un recurso global compartido durante un proceso de petición generalmente resultará en conflictos.

> [!NOTE]
> No utilice ninguna lógica de tamaño fijo al manipular la tabla de función `mysqlnd`: las nuevas funciones pueden ser añadidas al final de la tabla de función. La tabla de función puede ser modificada en cualquier momento después.

**Llamada a métodos padres**

Si la tabla de función original se guarda, siempre es posible llamar a las entradas de la tabla de función original - los métodos padres.

En este caso, al igual que `Connection::stmt_init()`, es vital llamar al método padre antes de cualquier otra actividad en el método derivado.

    MYSQLND_METHOD(my_conn_class, query)(MYSQLND *conn,
      const char *query, unsigned int query_len TSRMLS_DC) {

      php_printf("my_conn_class::query(query = %s)\n", query);

      query = "SELECT 'query rewritten' FROM DUAL";
      query_len = strlen(query);

      return org_methods.query(conn, query, query_len); /* retorno con llamada al padre */
    }

      

**Extender propiedades**

Un objeto `mysqlnd` está representado por una estructura C. No es posible añadir un miembro a una estructura C en tiempo de ejecución. Los usuarios de objetos `mysqlnd` no pueden simplemente añadir propiedades a los objetos.

Datos arbitrarios (propiedades) pueden ser añadidos a los objetos `mysqlnd` utilizando una función apropiada de la familia `mysqlnd_plugin_get_plugin_<object>_data()`. Durante la asignación de un objeto, `mysqlnd` reserva un espacio al final del objeto para alojar un puntero `void *` hacia datos arbitrarios. `mysqlnd` reserva un espacio para un puntero `void *` por plugin.

La tabla siguiente muestra cómo calcular la posición de un puntero para un plugin específico:

| Dirección de memoria | Contenido |
|----|----|
| 0 | Inicio de la estructura C del objeto mysqlnd |
| n | Fin de la estructura C del objeto mysqlnd |
| n + (m x sizeof(void\*)) | void\* hacia los datos del objeto del plugin m-ésimo |

Cálculo de punteros para mysqlnd {#mysqlnd.plugin.pointercalc}

Si planea hacer subclases de los constructores de los objetos `mysqlnd`, lo cual está permitido, debe tener esto en cuenta.

El código siguiente muestra cómo se extienden propiedades:

    /* todos los datos que queremos asociar */
    typedef struct my_conn_properties {
      unsigned long query_counter;
    } MY_CONN_PROPERTIES;

    /* id del plugin */
    unsigned int my_plugin_id;

    void minit_register_hooks(TSRMLS_D) {
      /* obtenemos un ID único para el plugin */
      my_plugin_id = mysqlnd_plugin_register();
      /* snip - ver la extensión de la conexión: métodos */
    }

    static MY_CONN_PROPERTIES** get_conn_properties(const MYSQLND *conn TSRMLS_DC) {
      MY_CONN_PROPERTIES** props;
      props = (MY_CONN_PROPERTIES**)mysqlnd_plugin_get_plugin_connection_data(
        conn, my_plugin_id);
      if (!props || !(*props)) {
        *props = mnd_pecalloc(1, sizeof(MY_CONN_PROPERTIES), conn->persistent);
        (*props)->query_counter = 0;
      }
      return props;
    }

      

El desarrollador del plugin es responsable de la gestión de la memoria asociada a los datos del plugin.

Se recomienda el uso del asignador de memoria `mysqlnd` para los datos del plugin. Estas funciones son nombradas utilizando la siguiente convención: `mnd_*loc()`. El asignador `mysqlnd` tiene algunas características muy útiles, como la posibilidad de utilizar un asignador de depuración en una compilación no depurada.

|  | ¿Cuándo hacer una subclase? | ¿Cada instancia tiene su propia tabla de funciones privada? | ¿Cómo hacer una subclase? |
|----|----|----|----|
| Conexión (MYSQLND) | MINIT | No | mysqlnd_conn_get_methods() |
| Juego de resultados (MYSQLND_RES) | MINIT o después | Sí | mysqlnd_result_get_methods() o método del objeto de manipulación de la tabla de funciones |
| Meta del juego de resultados (MYSQLND_RES_METADATA) | MINIT | No | mysqlnd_result_metadata_get_methods() |
| Consulta (MYSQLND_STMT) | MINIT | No | mysqlnd_stmt_get_methods() |
| Red (MYSQLND_NET) | MINIT o después | Sí | mysqlnd_net_get_methods() o método del objeto de manipulación de la tabla de funciones |
| Capa física (MYSQLND_PROTOCOL) | MINIT o después | Sí | mysqlnd_protocol_get_methods() o método del objeto de manipulación de la tabla de funciones |

Cuándo y cómo hacer una subclase {#mysqlnd.plugin.subclass}

No debe manipular las tablas de funciones después de MINIT si no está permitido según la tabla anterior.

Algunas clases contienen un puntero hacia un método de la tabla de funciones. Todas las instancias de una clase de este tipo compartirán la misma tabla de funciones. Para evitar el caos, en particular en entornos multihilo, este tipo de tablas de funciones solo debe ser manipulado durante el MINIT.

Las otras clases utilizan una copia de la tabla de funciones global compartida. Esta copia se crea al mismo tiempo que el objeto. Cada objeto utiliza su propia tabla de funciones. Esto le da 2 opciones: puede manipular la tabla de funciones por defecto de un objeto durante el MINIT, y también puede afinar métodos de un objeto sin afectar a las otras instancias de la misma clase.

La ventaja del enfoque con una tabla de funciones compartida es el rendimiento. No es necesario copiar una tabla de funciones para cada objeto.

<table id="mysqlnd.plugin.constatus">
<caption>Estado del constructor</caption>
<thead>
<tr>
<th>Tipo</th>
<th>Asignación, construcción, reinicialización</th>
<th>¿Puede ser modificado?</th>
<th>Llamante</th>
</tr>
</thead>
<tbody>
<tr>
<td>Conexión (MYSQLND)</td>
<td>mysqlnd_init()</td>
<td>No</td>
<td>mysqlnd_connect()</td>
</tr>
<tr>
<td>Juego de resultados (MYSQLND_RES)</td>
<td><p>Asignación:</p>
<ul>
<li><p>Connection::result_init()</p></li>
</ul>
<p>Reinicio y reinicialización durante:</p>
<ul>
<li><p>Result::use_result()</p></li>
<li><p>Result::store_result</p></li>
</ul></td>
<td>Sí, pero llamada al padre.</td>
<td><ul>
<li><p>Connection::list_fields()</p></li>
<li><p>Statement::get_result()</p></li>
<li><p>Statement::prepare() (Meta-datos únicamente)</p></li>
<li><p>Statement::resultMetaData()</p></li>
</ul></td>
</tr>
<tr>
<td>Meta del juego de resultados (MYSQLND_RES_METADATA)</td>
<td>Connection::result_meta_init()</td>
<td>Sí, pero llamada al padre.</td>
<td>Result::read_result_metadata()</td>
</tr>
<tr>
<td>Consulta (MYSQLND_STMT)</td>
<td>Connection::stmt_init()</td>
<td>Sí, pero llamada al padre.</td>
<td>Connection::stmt_init()</td>
</tr>
<tr>
<td>Red (MYSQLND_NET)</td>
<td>mysqlnd_net_init()</td>
<td>No</td>
<td>Connection::init()</td>
</tr>
<tr>
<td>Capa física (MYSQLND_PROTOCOL)</td>
<td>mysqlnd_protocol_init()</td>
<td>No</td>
<td>Connection::init()</td>
</tr>
</tbody>
</table>

Se recomienda encarecidamente no reemplazar completamente un constructor. Los constructores realizan asignaciones de memoria. Las asignaciones de memoria son vitales para la API del plugin `mysqlnd` así como para la lógica del objeto `mysqlnd`. Si no se preocupa por las advertencias e insiste en reemplazar los constructores, debería al menos llamar al constructor padre antes de hacer cualquier cosa en su constructor.

A nivel de todas las advertencias, puede ser útil hacer subclases de los constructores. Los constructores son los lugares perfectos para modificar las tablas de funciones de los objetos con tablas de objetos no compartidas, como los juegos de resultados, la red o la capa física.

| Tipo | ¿El método derivado debe llamar al padre? | Destructor |
|----|----|----|
| Conexión | Sí, después de la ejecución del método | free_contents(), end_psession() |
| Juego de resultados | Sí, después de la ejecución del método | free_result() |
| Meta del juego de resultados | Sí, después de la ejecución del método | free() |
| Consulta | Sí, después de la ejecución del método | dtor(), free_stmt_content() |
| Red | Sí, después de la ejecución del método | free() |
| Capa física | Sí, después de la ejecución del método | free() |

Estado del destructor {#mysqlnd.plugin.deststatus}

Los destructores son los lugares perfectos para liberar propiedades, `mysqlnd_plugin_get_plugin_<object>_data()`.

Los destructores listados pueden no ser los equivalentes a los métodos actuales `mysqlnd` que liberan el objeto mismo. Sin embargo, son los mejores lugares para liberar los datos de su plugin. Al igual que los constructores, puede reemplazar métodos completos pero no se recomienda. Si varios métodos están listados en la tabla anterior, debe modificar todos los métodos listados y liberar los datos de su plugin en el método llamado primero por `mysqlnd`.

El método recomendado para los plugins es simplemente modificar los métodos, liberar su memoria y llamar a la implementación del padre inmediatamente después.

## La API del plugin mysqlnd

A continuación se presenta la lista de funciones proporcionadas en la API plugin `mysqlnd`:

- mysqlnd_plugin_register()

- mysqlnd_plugin_count()

- mysqlnd_plugin_get_plugin_connection_data()

- mysqlnd_plugin_get_plugin_result_data()

- mysqlnd_plugin_get_plugin_stmt_data()

- mysqlnd_plugin_get_plugin_net_data()

- mysqlnd_plugin_get_plugin_protocol_data()

- mysqlnd_conn_get_methods()

- mysqlnd_result_get_methods()

- mysqlnd_result_meta_get_methods()

- mysqlnd_stmt_get_methods()

- mysqlnd_net_get_methods()

- mysqlnd_protocol_get_methods()

No hay una definición formal de qué es un plugin ni de cómo funciona un plugin.

Los componentes más frecuentemente encontrados en los mecanismos de plugin son:

- Un gestor de plugin

- Una API del plugin

- Los servicios aplicativos (o módulos)

- Las APIs de los servicios aplicativos (o APIs del módulo)

El concepto de un plugin `mysqlnd` utiliza estas características, así como otras joyas de arquitectura abierta.

**Sin restricciones**

Un plugin tiene acceso total a los trabajos internos de `mysqlnd`. No hay límites de seguridad ni restricciones. Todo puede ser sobrescrito para implementar algoritmos útiles o hostiles. Se recomienda desplegar solo plugins desde fuentes de confianza.

Tal como se ha discutido anteriormente, los plugins pueden utilizar libremente punteros. Estos punteros no están restringidos de ninguna manera, por lo que puede apuntar hacia los datos de otro plugin. Una simple posición aritmética puede ser utilizada para leer los datos de otro plugin.

Se recomienda escribir plugins cooperativos, y por lo tanto, siempre llamar al método padre. Los plugins deben cooperar siempre con `mysqlnd`.

<table id="mysqlnd.plugin.chaining">
<caption>Problemas: un ejemplo de encadenamiento y cooperación</caption>
<thead>
<tr>
<th>Extensión</th>
<th>Puntero mysqlnd.query()</th>
<th>Pila de llamadas si se llama al padre</th>
</tr>
</thead>
<tbody>
<tr>
<td>ext/mysqlnd</td>
<td>mysqlnd.query()</td>
<td>mysqlnd.query</td>
</tr>
<tr>
<td>ext/mysqlnd_cache</td>
<td>mysqlnd_cache.query()</td>
<td><ol type="1">
<li><p>mysqlnd_cache.query()</p></li>
<li><p>mysqlnd.query</p></li>
</ol></td>
</tr>
<tr>
<td>ext/mysqlnd_monitor</td>
<td>mysqlnd_monitor.query()</td>
<td><ol type="1">
<li><p>mysqlnd_monitor.query()</p></li>
<li><p>mysqlnd_cache.query()</p></li>
<li><p>mysqlnd.query</p></li>
</ol></td>
</tr>
</tbody>
</table>

En este escenario, un plugin de caché (`ext/mysqlnd_cache`) y un plugin de supervisión (`ext/mysqlnd_monitor`) están cargados. Ambos tienen una subclase de `Connection::query()`. El registro del plugin ocurre durante el `MINIT` utilizando la lógica mencionada anteriormente. PHP llama a las extensiones en un orden alfabético por defecto. Los plugins no están al tanto unos de otros y no pueden fijar dependencias.

Por defecto, los plugins llaman a la implementación del padre de la función de consulta en su versión de la función derivada.

**Resumen de la extensión PHP**

A continuación se presenta un resumen de lo que ocurre al utilizar un plugin de ejemplo, `ext/mysqlnd_plugin`, que expone la API C del plugin `mysqlnd` a PHP:

- Todas las aplicaciones PHP MySQL intentan establecer una conexión a la dirección 192.168.2.29

- La aplicación PHP utilizará `ext/mysql`, `ext/mysqli` o `PDO_MYSQL`. Estas 3 extensiones PHP MySQL utilizan `mysqlnd` para establecer la conexión a la dirección 192.168.2.29.

- `Mysqlnd` llama a su método de conexión, que ha sido subclaseado por `ext/mysqlnd_plugin`.

- `ext/mysqlnd_plugin` llama al método del espacio de usuario `proxy::connect()` registrado por el usuario.

- El espacio de usuario modifica el host de conexión de 192.168.2.29 a 127.0.0.1 y devuelve la conexión establecida por `parent::connect()`.

- `ext/mysqlnd_plugin` ejecuta el equivalente de `parent::connect(127.0.0.1)` llamando al método original de `mysqlnd` para establecer una conexión.

- `ext/mysqlnd` establece una conexión y devuelve el control a `ext/mysqlnd_plugin`. `ext/mysqlnd_plugin` también devuelve.

- Cualquier extensión PHP MySQL utilizada por la aplicación, recibe una conexión a 127.0.0.1. La extensión PHP MySQL devuelve el control a la aplicación PHP. El ciclo está cerrado.

## Cómo comenzar a compilar un plugin mysqlnd

Es importante recordar que un plugin `mysqlnd` es en sí mismo una extensión PHP.

El código siguiente muestra la estructura básica de una función MINIT utilizada en un plugin típico `mysqlnd`:

    /* my_php_mysqlnd_plugin.c */

     static PHP_MINIT_FUNCTION(mysqlnd_plugin) {
      /* globales, entradas ini, recursos, clases */

      /* registro del plugin mysqlnd */
      mysqlnd_plugin_id = mysqlnd_plugin_register();

      conn_m = mysqlnd_get_conn_methods();
      memcpy(org_conn_m, conn_m,
        sizeof(struct st_mysqlnd_conn_methods));

      conn_m->query = MYSQLND_METHOD(mysqlnd_plugin_conn, query);
      conn_m->connect = MYSQLND_METHOD(mysqlnd_plugin_conn, connect);
    }

      

    /* my_mysqlnd_plugin.c */

     enum_func_status MYSQLND_METHOD(mysqlnd_plugin_conn, query)(/* ... */) {
      /* ... */
    }
    enum_func_status MYSQLND_METHOD(mysqlnd_plugin_conn, connect)(/* ... */) {
      /* ... */
    }

      

**Tarea de análisis: desde C hacia el espacio de usuario**

     class proxy extends mysqlnd_plugin_connection {
      public function connect($host, ...) { .. }
    }
    mysqlnd_plugin_set_conn_proxy(new proxy());

      

Proceso:

1.  PHP: el usuario registra una función de devolución de llamada para el plugin

2.  PHP: el usuario llama a un método de la API PHP MySQL para conectarse a MySQL

3.  C: ext/\*mysql\* llama al método mysqlnd

4.  C: mysqlnd termina en ext/mysqlnd_plugin

5.  C: ext/mysqlnd_plugin

    1.  Llamada a la función de devolución de llamada del espacio de usuario

    2.  O la función original `mysqlnd`, si el espacio de usuario no ha definido una función de devolución de llamada

Debe realizar las siguientes operaciones:

1.  Escribir una clase "mysqlnd_plugin_connection" en C

2.  Aceptar y registrar el objeto proxy a través de "mysqlnd_plugin_set_conn_proxy()"

3.  Llamar a los métodos de proxy del espacio de usuario desde C (optimización - zend_interfaces.h)

Los métodos del objeto del espacio de usuario pueden ser llamados utilizando `call_user_function()`, o puede operar a un nivel por debajo del motor Zend y utilizar `zend_call_method()`.

**Optimización: llamada a métodos desde C utilizando zend_call_method**

El código siguiente muestra un prototipo para la función `zend_call_method`, obtenido de `zend_interfaces.h`.

     ZEND_API zval* zend_call_method(
      zval **object_pp, zend_class_entry *obj_ce,
      zend_function **fn_proxy, char *function_name,
      int function_name_len, zval **retval_ptr_ptr,
      int param_count, zval* arg1, zval* arg2 TSRMLS_DC
    );

      

La API Zend soporta 2 argumentos. Puede necesitar más, por ejemplo:

     enum_func_status (*func_mysqlnd_conn__connect)(
      MYSQLND *conn, const char *host,
      const char * user, const char * passwd,
      unsigned int passwd_len, const char * db,
      unsigned int db_len, unsigned int port,
      const char * socket, unsigned int mysql_flags TSRMLS_DC
    );

      

Para solucionar este problema, deberá hacer una copia de `zend_call_method()` y añadir funcionalidad para añadir parámetros. Puede lograr esto creando un conjunto de macros `MY_ZEND_CALL_METHOD_WRAPPER`.

**Llamada al espacio de usuario PHP**

El código siguiente muestra el método optimizado para realizar una llamada a una función del espacio de usuario desde C:

      /* my_mysqlnd_plugin.c */

    MYSQLND_METHOD(my_conn_class,connect)(
      MYSQLND *conn, const char *host /* ... */ TSRMLS_DC) {
      enum_func_status ret = FAIL;
      zval * global_user_conn_proxy = fetch_userspace_proxy();
      if (global_user_conn_proxy) {
        /* llamada al proxy del espacio de usuario */
        ret = MY_ZEND_CALL_METHOD_WRAPPER(global_user_conn_proxy, host, /*...*/);
      } else {
        /* o el método original mysqlnd = no hacer nada, ser transparente */
        ret = org_methods.connect(conn, host, user, passwd,
              passwd_len, db, db_len, port,
              socket, mysql_flags TSRMLS_CC);
      }
      return ret;
    }

      

**Llamada al espacio de usuario: argumentos simples**

    /* my_mysqlnd_plugin.c */

     MYSQLND_METHOD(my_conn_class,connect)(
      /* ... */, const char *host, /* ...*/) {
      /* ... */
      if (global_user_conn_proxy) {
        /* ... */
        zval* zv_host;
        MAKE_STD_ZVAL(zv_host);
        ZVAL_STRING(zv_host, host, 1);
        MY_ZEND_CALL_METHOD_WRAPPER(global_user_conn_proxy, zv_retval, zv_host /*, ...*/);
        zval_ptr_dtor(&zv_host);
        /* ... */
      }
      /* ... */
    }

      

**Llamada al espacio de usuario: estructuras como argumentos**

    /* my_mysqlnd_plugin.c */

    MYSQLND_METHOD(my_conn_class, connect)(
      MYSQLND *conn, /* ...*/) {
      /* ... */
      if (global_user_conn_proxy) {
        /* ... */
        zval* zv_conn;
        ZEND_REGISTER_RESOURCE(zv_conn, (void *)conn, le_mysqlnd_plugin_conn);
        MY_ZEND_CALL_METHOD_WRAPPER(global_user_conn_proxy, zv_retval, zv_conn, zv_host /*, ...*/);
        zval_ptr_dtor(&zv_conn);
        /* ... */
      }
      /* ... */
    }

      

El primer argumento de todas las funciones `mysqlnd` es un objeto C. Por ejemplo, el primer argumento de la función connect() es un puntero hacia `MYSQLND`. La estructura MYSQLND representa un objeto de conexión `mysqlnd`.

El puntero del objeto de conexión `mysqlnd` puede ser comparado a un puntero de archivo estándar I/O. Al igual que un puntero de archivo estándar I/O, un objeto de conexión `mysqlnd` debe ser vinculado al espacio de usuario utilizando una variable PHP de tipo recurso.

**Desde C hacia el espacio de usuario, y luego de vuelta**

     class proxy extends mysqlnd_plugin_connection {
      public function connect($conn, $host, ...) {
        /* "pre" hook */
        printf("Conexión al host = '%s'\n", $host);
        debug_print_backtrace();
        return parent::connect($conn);
      }

      public function query($conn, $query) {
        /* "post" hook */
        $ret = parent::query($conn, $query);
        printf("Consulta = '%s'\n", $query);
        return $ret;
      }
    }
    mysqlnd_plugin_set_conn_proxy(new proxy());

      

Los usuarios PHP deben poder llamar a la implementación del padre de un método sobrescrito.

Como resultado de una subclase, es posible redefinir únicamente los métodos seleccionados, y puede elegir tener acciones "pre" o "post".

**Construcción de una clase: mysqlnd_plugin_connection::connect()**

    /*  my_mysqlnd_plugin_classes.c */

     PHP_METHOD("mysqlnd_plugin_connection", connect) {
      /* ... simplificado! ... */
      zval* mysqlnd_rsrc;
      MYSQLND* conn;
      char* host; int host_len;
      if (zend_parse_parameters(ZEND_NUM_ARGS() TSRMLS_CC, "rs",
        &mysqlnd_rsrc, &host, &host_len) == FAILURE) {
        RETURN_NULL();
      }
      ZEND_FETCH_RESOURCE(conn, MYSQLND* conn, &mysqlnd_rsrc, -1,
        "Mysqlnd Connection", le_mysqlnd_plugin_conn);
      if (PASS == org_methods.connect(conn, host, /* simplificado! */ TSRMLS_CC))
        RETVAL_TRUE;
      else
        RETVAL_FALSE;
    }
