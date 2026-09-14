---
title: Rastreo dinámico de DTrace
source_url: https://www.php.net/manual/es/features.dtrace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: features/dtrace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: features
translation_status: ready
translation_revision: 7c966c94f
order: 1550
---

## Rastreo dinámico de DTrace

## Introducción a PHP y DTrace

DTrace es un framework de rastreo siempre disponible, a bajo costo, disponible en varias plataformas, incluyendo Solaris, macOS, Oracle Linux y BSD. DTrace puede rastrear el comportamiento del sistema operativo y la ejecución de programas de usuario. Puede mostrar los valores de los argumentos y ser utilizado para deducir estadísticas de rendimiento. Las sondas son controladas por scripts creados por el usuario y escritos en el lenguaje de script DTrace D. Esto permite un análisis eficiente de los puntos de datos.

Las sondas PHP que no son activamente monitoreadas por el script DTrace D del usuario no contienen código instrumentado, por lo que no hay degradación del rendimiento durante la ejecución normal de la aplicación. Las sondas que son monitoreadas tienen un costo de funcionamiento bastante bajo para generalmente permitir la supervisión de DTrace en sistemas de producción.

PHP incorpora sondas de "Rastreo Estático Definido por el Usuario" (USDT) que se disparan en el momento de la ejecución. Por ejemplo, cuando un script D monitorea la sonda `function-entry` de PHP, entonces, cada vez que se llama a una función del script PHP, esta sonda se dispara y el código de acción del script D asociado se ejecuta. Este código de acción podría, por ejemplo, imprimir los argumentos de la sonda como la ubicación del fichero fuente de la función PHP. La acción también puede agrupar datos como el número de veces que se llama a cada función.

Solo se describen aquí las sondas PHP USDT. Consulte la documentación externa general y específica del sistema operativo para ver cómo DTrace puede ser utilizado para trazar funciones arbitrarias, y cómo puede ser utilizado para trazar el comportamiento del sistema operativo. Tenga en cuenta que no todas las funcionalidades de DTrace están disponibles en todas las implementaciones de DTrace.

Las sondas DTrace estáticas en PHP pueden alternativamente ser utilizadas con la función SystemTap en ciertas distribuciones Linux.

## Usar PHP y DTrace

PHP puede ser configurado con las sondas estáticas DTrace en las plataformas que soportan el rastreo dinámico DTrace.

### Configurar PHP para las sondas estáticas de DTrace

Consulte la documentación específica de la plataforma externa para habilitar el soporte de DTrace del sistema operativo. Por ejemplo, en Oracle Linux inicie un núcleo UEK3 y haga:

```php
## modprobe fasttrap
## chmod 666 /dev/dtrace/helper

     
```

En lugar de usar `chmod`, puede usar una regla de paquetado ACL para limitar el acceso al dispositivo a un usuario específico.

Construir PHP con el parámetro de configuración `--enable-dtrace`:

```php
## ./configure --enable-dtrace ...
## make
## make install

     
```

Esto hace que las sondas estáticas estén disponibles en el núcleo de PHP. Todas las extensiones PHP que proporcionen sus propias sondas deben ser construidas por separado como extensiones compartidas.

Para habilitar las sondas, definir la variable de entorno `USE_ZEND_DTRACE=1` a los procesos PHP objetivo.

### Sondas estáticas DTrace en el núcleo de PHP

| Nombre de la sonda | Descripción de la sonda | Argumentos de la sonda |
|----|----|----|
| `request-startup` | Se dispara cuando una petición comienza. | char \*`file`, char \*`request_uri`, char \*`request_method` |
| `request-shutdown` | Se dispara cuando una petición se detiene. | char \*`file`, char \*`request_uri`, char \*`request_method` |
| `compile-file-entry` | Se dispara cuando comienza la compilación de un script. | char \*`compile_file`, char \*`compile_file_translated` |
| `compile-file-return` | Se dispara cuando termina la compilación de un script. | char \*`compile_file`, char \*`compile_file_translated` |
| `execute-entry` | Se dispara cuando un array de opcodes debe ser ejecutado. Por ejemplo, se dispara en llamadas de función, inclusiones y reanudaciones de generador. | char \*`request_file`, int `lineno` |
| `execute-return` | Se dispara después de la ejecución de un array de opcodes. | char \*`request_file`, int `lineno` |
| `function-entry` | Se dispara cuando el motor de PHP entra en una función PHP o una llamada de método. | char \*`function_name`, char \*`request_file`, int `lineno`, char \*`classname`, char \*`scope` |
| `function-return` | Se dispara cuando el motor PHP regresa de una función PHP o una llamada de método. | char \*`function_name`, char \*`request_file`, int `lineno`, char \*`classname`, char \*`scope` |
| `exception-thrown` | Se dispara cuando se lanza una excepción. | char \*`classname` |
| `exception-caught` | Se dispara cuando se captura una excepción. | char \*`classname` |
| `error` | Se dispara cuando ocurre un error, independientemente del nivel de [error_reporting](#ini.error-reporting). | char \*`errormsg`, char \*`request_file`, int `lineno` |

Las siguientes sondas estáticas están disponibles en PHP

Las extensiones PHP también pueden disponer de sondas estáticas adicionales.

### Lista de sondas estáticas DTrace de PHP

Para listar las sondas disponibles, inicie un proceso PHP y luego ejecute:

    # dtrace -l

El resultado será similar al siguiente:

       ID   PROVIDER            MODULE                          FUNCTION NAME
       [ . . . ]
        4   php15271               php               dtrace_compile_file compile-file-entry
        5   php15271               php               dtrace_compile_file compile-file-return
        6   php15271               php                        zend_error error
        7   php15271               php  ZEND_CATCH_SPEC_CONST_CV_HANDLER exception-caught
        8   php15271               php     zend_throw_exception_internal exception-thrown
        9   php15271               php                 dtrace_execute_ex execute-entry
       10   php15271               php           dtrace_execute_internal execute-entry
       11   php15271               php                 dtrace_execute_ex execute-return
       12   php15271               php           dtrace_execute_internal execute-return
       13   php15271               php                 dtrace_execute_ex function-entry
       14   php15271               php                 dtrace_execute_ex function-return
       15   php15271               php              php_request_shutdown request-shutdown
       16   php15271               php               php_request_startup request-startup

Los valores de la columna Provider son `php` y el identificador del proceso PHP en ejecución.

Si el servidor web Apache está en ejecución, el nombre del módulo podría ser, por ejemplo, `libphp5.so`, y habría varios bloques de listas, uno por cada proceso Apache en ejecución.

La columna Función hace referencia a la implementación interna en C de PHP, donde se encuentra cada proveedor.

Si no hay un proceso PHP en ejecución, no se mostrará ninguna sonda PHP.

### DTrace con un ejemplo PHP

Este ejemplo muestra los fundamentos del lenguaje de script DTrace D.

`all_probes.d` para trazar todas las sondas estáticas PHP con DTrace

    #!/usr/sbin/dtrace -Zs

    #pragma D option quiet

    php*:::compile-file-entry
    {
        printf("PHP compile-file-entry\n");
        printf("  compile_file              %s\n", copyinstr(arg0));
        printf("  compile_file_translated   %s\n", copyinstr(arg1));
    }

    php*:::compile-file-return
    {
        printf("PHP compile-file-return\n");
        printf("  compile_file              %s\n", copyinstr(arg0));
        printf("  compile_file_translated   %s\n", copyinstr(arg1));
    }

    php*:::error
    {
        printf("PHP error\n");
        printf("  errormsg                  %s\n", copyinstr(arg0));
        printf("  request_file              %s\n", copyinstr(arg1));
        printf("  lineno                    %d\n", (int)arg2);
    }

    php*:::exception-caught
    {
        printf("PHP exception-caught\n");
        printf("  classname                 %s\n", copyinstr(arg0));
    }

    php*:::exception-thrown
    {
        printf("PHP exception-thrown\n");
        printf("  classname                 %s\n", copyinstr(arg0));
    }

    php*:::execute-entry
    {
        printf("PHP execute-entry\n");
        printf("  request_file              %s\n", copyinstr(arg0));
        printf("  lineno                    %d\n", (int)arg1);
    }

    php*:::execute-return
    {
        printf("PHP execute-return\n");
        printf("  request_file              %s\n", copyinstr(arg0));
        printf("  lineno                    %d\n", (int)arg1);
    }

    php*:::function-entry
    {
        printf("PHP function-entry\n");
        printf("  function_name             %s\n", copyinstr(arg0));
        printf("  request_file              %s\n", copyinstr(arg1));
        printf("  lineno                    %d\n", (int)arg2);
        printf("  classname                 %s\n", copyinstr(arg3));
        printf("  scope                     %s\n", copyinstr(arg4));
    }

    php*:::function-return
    {
        printf("PHP function-return\n");
        printf("  function_name             %s\n", copyinstr(arg0));
        printf("  request_file              %s\n", copyinstr(arg1));
        printf("  lineno                    %d\n", (int)arg2);
        printf("  classname                 %s\n", copyinstr(arg3));
        printf("  scope                     %s\n", copyinstr(arg4));
    }

    php*:::request-shutdown
    {
        printf("PHP request-shutdown\n");
        printf("  file                      %s\n", copyinstr(arg0));
        printf("  request_uri               %s\n", copyinstr(arg1));
        printf("  request_method            %s\n", copyinstr(arg2));
    }

    php*:::request-startup
    {
        printf("PHP request-startup\n");
        printf("  file                      %s\n", copyinstr(arg0));
        printf("  request_uri               %s\n", copyinstr(arg1));
        printf("  request_method            %s\n", copyinstr(arg2));
    }

Este script utiliza la opción `-Z` de `dtrace`, lo que le permite ejecutarse cuando no hay ningún proceso PHP en ejecución. Si se omitiera esta opción, el script terminaría inmediatamente porque sabe que ninguna de las sondas a monitorear existe.

El script traza todos los puntos de sondeo estáticos de PHP durante la duración de un script PHP en ejecución. Ejecute el script D:

    # ./all_probes.d

Ejecute un script o una aplicación PHP. El script D de monitoreo mostrará los argumentos de cada sonda a medida que se dispare.

Cuando el monitoreo haya terminado, el script D puede ser interrumpido con un <span class="keycombo">CTRL+C</span>

En máquinas multi-CPU, el orden de las sondas puede no ser secuencial. Esto depende del CPU que ha procesado las sondas, y de cómo los hilos migran de un CPU a otro. La visualización de los timestamps de las sondas permite reducir la confusión, por ejemplo :

    php*:::function-entry
    {
          printf("%lld: PHP function-entry ", walltimestamp);
          [ . . .]
    }

### Véase también

OCI8 y el rastreo dinámico DTrace

## Usar SystemTap con las sondas estáticas DTrace de PHP

En ciertas distribuciones Linux, la utilidad de rastreo SystemTap puede ser utilizada para trazar las sondas estáticas DTrace de PHP. Esto está disponible con PHP 5.4.20 y PHP 5.5.

### Instalar PHP con SystemTap

Instale el paquete de desarrollo SDT de SystemTap:

```php
## yum install systemtap-sdt-devel

     
```

Instalar PHP con las sondas DTrace habilitadas:

```php
## ./configure --enable-dtrace ...
## make

     
```

### Lista de sondas estáticas con SystemTap

Las sondas estáticas en PHP pueden ser listadas utilizando `stap`:

    # stap -l 'process.provider("php").mark("*")' -c 'sapi/cli/php -i'

Esto produce:

    process("sapi/cli/php").provider("php").mark("compile__file__entry")
    process("sapi/cli/php").provider("php").mark("compile__file__return")
    process("sapi/cli/php").provider("php").mark("error")
    process("sapi/cli/php").provider("php").mark("exception__caught")
    process("sapi/cli/php").provider("php").mark("exception__thrown")
    process("sapi/cli/php").provider("php").mark("execute__entry")
    process("sapi/cli/php").provider("php").mark("execute__return")
    process("sapi/cli/php").provider("php").mark("function__entry")
    process("sapi/cli/php").provider("php").mark("function__return")
    process("sapi/cli/php").provider("php").mark("request__shutdown")
    process("sapi/cli/php").provider("php").mark("request__startup")

### SystemTap con un Ejemplo PHP

`all_probes.stp` para trazar todas las sondas estáticas PHP con SystemTap

```php
probe process("sapi/cli/php").provider("php").mark("compile__file__entry") {
    printf("Probe compile__file__entry\n");
    printf("  compile_file %s\n", user_string($arg1));
    printf("  compile_file_translated %s\n", user_string($arg2));
}
probe process("sapi/cli/php").provider("php").mark("compile__file__return") {
    printf("Probe compile__file__return\n");
    printf("  compile_file %s\n", user_string($arg1));
    printf("  compile_file_translated %s\n", user_string($arg2));
}
probe process("sapi/cli/php").provider("php").mark("error") {
    printf("Probe error\n");
    printf("  errormsg %s\n", user_string($arg1));
    printf("  request_file %s\n", user_string($arg2));
    printf("  lineno %d\n", $arg3);
}
probe process("sapi/cli/php").provider("php").mark("exception__caught") {
    printf("Probe exception__caught\n");
    printf("  classname %s\n", user_string($arg1));
}
probe process("sapi/cli/php").provider("php").mark("exception__thrown") {
    printf("Probe exception__thrown\n");
    printf("  classname %s\n", user_string($arg1));
}
probe process("sapi/cli/php").provider("php").mark("execute__entry") {
    printf("Probe execute__entry\n");
    printf("  request_file %s\n", user_string($arg1));
    printf("  lineno %d\n", $arg2);
}
probe process("sapi/cli/php").provider("php").mark("execute__return") {
    printf("Probe execute__return\n");
    printf("  request_file %s\n", user_string($arg1));
    printf("  lineno %d\n", $arg2);
}
probe process("sapi/cli/php").provider("php").mark("function__entry") {
    printf("Probe function__entry\n");
    printf("  function_name %s\n", user_string($arg1));
    printf("  request_file %s\n", user_string($arg2));
    printf("  lineno %d\n", $arg3);
    printf("  classname %s\n", user_string($arg4));
    printf("  scope %s\n", user_string($arg5));
}
probe process("sapi/cli/php").provider("php").mark("function__return") {
    printf("Probe function__return: %s\n", user_string($arg1));
    printf(" function_name %s\n", user_string($arg1));
    printf("  request_file %s\n", user_string($arg2));
    printf("  lineno %d\n", $arg3);
    printf("  classname %s\n", user_string($arg4));
    printf("  scope %s\n", user_string($arg5));
}
probe process("sapi/cli/php").provider("php").mark("request__shutdown") {
    printf("Probe request__shutdown\n");
    printf("  file %s\n", user_string($arg1));
    printf("  request_uri %s\n", user_string($arg2));
    printf("  request_method %s\n", user_string($arg3));
}
probe process("sapi/cli/php").provider("php").mark("request__startup") {
    printf("Probe request__startup\n");
    printf("  file %s\n", user_string($arg1));
    printf("  request_uri %s\n", user_string($arg2));
    printf("  request_method %s\n", user_string($arg3));
}

     
```

El script anterior trazará todos los puntos de sondeo estáticos de PHP durante toda la duración de la ejecución de un script PHP:

    # stap -c 'sapi/cli/php test.php' all_probes.stp

## Usar bpftrace con las sondas estáticas DTrace de PHP

En las distribuciones Linux con un núcleo que soporta eBPF, la utilidad bpftrace puede conectarse directamente a las sondas USDT de DTrace de PHP, sin necesidad de SystemTap.

### Instalar bpftrace

Instale bpftrace utilizando el gestor de paquetes de la distribución. Por ejemplo, en Oracle Linux, RHEL o Fedora:

```php
## dnf install bpftrace

     
```

O bien, en Debian o Ubuntu:

```php
## apt install bpftrace

     
```

Los ejemplos siguientes asumen que el binario PHP objetivo está instalado en `/usr/bin/php`.

Las mismas sondas USDT también son expuestas por otros SAPIs construidos a partir del mismo árbol de fuentes, por lo que el objetivo de la sonda puede ser en su lugar el módulo de Apache (`libphp.so`) o el binario del FastCGI Process Manager (`php-fpm`); sustituya la ruta apropiada o conéctese por PID con `-p` según sea necesario.

Asegúrese de que el binario objetivo esté construido con DTrace y de que la variable de entorno esté configurada correctamente. Consulte [Configurar PHP para las sondas estáticas de DTrace](#features.dtrace.install) para más detalles.

Las sondas estáticas en PHP pueden ser listadas utilizando `bpftrace`:

    # bpftrace -l 'usdt:/usr/bin/php:php:*'

Esto produce:

    usdt:/usr/bin/php:php:compile__file__entry
    usdt:/usr/bin/php:php:compile__file__return
    usdt:/usr/bin/php:php:error
    usdt:/usr/bin/php:php:exception__caught
    usdt:/usr/bin/php:php:exception__thrown
    usdt:/usr/bin/php:php:execute__entry
    usdt:/usr/bin/php:php:execute__return
    usdt:/usr/bin/php:php:function__entry
    usdt:/usr/bin/php:php:function__return
    usdt:/usr/bin/php:php:request__shutdown
    usdt:/usr/bin/php:php:request__startup

`all_probes.bt` para trazar todas las sondas estáticas PHP con bpftrace

```php
#!/usr/bin/env bpftrace

usdt:/usr/bin/php:php:compile__file__entry
{
    printf("Probe compile__file__entry\n");
    printf("  compile_file %s\n", str(arg0));
    printf("  compile_file_translated %s\n", str(arg1));
}
usdt:/usr/bin/php:php:compile__file__return
{
    printf("Probe compile__file__return\n");
    printf("  compile_file %s\n", str(arg0));
    printf("  compile_file_translated %s\n", str(arg1));
}
usdt:/usr/bin/php:php:error
{
    printf("Probe error\n");
    printf("  errormsg %s\n", str(arg0));
    printf("  request_file %s\n", str(arg1));
    printf("  lineno %d\n", (int32)arg2);
}
usdt:/usr/bin/php:php:exception__caught
{
    printf("Probe exception__caught\n");
    printf("  classname %s\n", str(arg0));
}
usdt:/usr/bin/php:php:exception__thrown
{
    printf("Probe exception__thrown\n");
    printf("  classname %s\n", str(arg0));
}
usdt:/usr/bin/php:php:execute__entry
{
    printf("Probe execute__entry\n");
    printf("  request_file %s\n", str(arg0));
    printf("  lineno %d\n", (int32)arg1);
}
usdt:/usr/bin/php:php:execute__return
{
    printf("Probe execute__return\n");
    printf("  request_file %s\n", str(arg0));
    printf("  lineno %d\n", (int32)arg1);
}
usdt:/usr/bin/php:php:function__entry
{
    printf("Probe function__entry\n");
    printf("  function_name %s\n", str(arg0));
    printf("  request_file %s\n", str(arg1));
    printf("  lineno %d\n", (int32)arg2);
    printf("  classname %s\n", str(arg3));
    printf("  scope %s\n", str(arg4));
}
usdt:/usr/bin/php:php:function__return
{
    printf("Probe function__return\n");
    printf("  function_name %s\n", str(arg0));
    printf("  request_file %s\n", str(arg1));
    printf("  lineno %d\n", (int32)arg2);
    printf("  classname %s\n", str(arg3));
    printf("  scope %s\n", str(arg4));
}
usdt:/usr/bin/php:php:request__shutdown
{
    printf("Probe request__shutdown\n");
    printf("  file %s\n", str(arg0));
    printf("  request_uri %s\n", str(arg1));
    printf("  request_method %s\n", str(arg2));
}
usdt:/usr/bin/php:php:request__startup
{
    printf("Probe request__startup\n");
    printf("  file %s\n", str(arg0));
    printf("  request_uri %s\n", str(arg1));
    printf("  request_method %s\n", str(arg2));
}

     
```

El script anterior trazará todos los puntos de sondeo estáticos del núcleo de PHP durante toda la duración de la ejecución de un script PHP. bpftrace requiere privilegios de root:

    # USE_ZEND_DTRACE=1 bpftrace -c '/usr/bin/php test.php' all_probes.bt

Para trazar un proceso PHP que ya está en ejecución (por ejemplo, un worker de `php-fpm` o un proceso Apache que carga `libphp.so`), conéctese por PID:

    # bpftrace -p $PID all_probes.bt

La ruta del objetivo `usdt:` en el script debe coincidir con el binario del proceso en ejecución; ajuste `usdt:/usr/bin/php` al binario de `php-fpm` o a `libphp.so` según corresponda.
