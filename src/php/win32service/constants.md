---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/win32service.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/win32service/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: win32service
translation_status: ready
translation_revision: 1a5886130
order: 101270
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

| Constante | Valor | Descripción |
|----|----|----|
| `WIN32_SERVICE_WIN32_OWN_PROCESS` | `0x00000010` | El servicio se ejecuta en su propio proceso. |
| `WIN32_SERVICE_INTERACTIVE_PROCESS` | `0x00000100` | El servicio puede interactuar con el escritorio. Esta opción no está disponible en Windows Vista o versiones posteriores. |
| `WIN32_SERVICE_WIN32_OWN_PROCESS_INTERACTIVE` | `0x00000110` | El servicio se ejecuta en su propio proceso y puede interactuar con el escritorio. Esta opción no está disponible en Windows Vista y siguientes. |

Mascara binaria de tipo de Servicio de Win32Service {#win32service.constants.servicetype}

| Constante | Valor | Descripción |
|----|----|----|
| `WIN32_SERVICE_CONTINUE_PENDING` | `0x00000005` | La continuación del servicio está en espera. |
| `WIN32_SERVICE_PAUSE_PENDING` | `0x00000006` | La pausa del servicio está en espera. |
| `WIN32_SERVICE_PAUSED` | `0x00000004` | El servicio está en pausa. |
| `WIN32_SERVICE_RUNNING` | `0x00000004` | El servicio está en curso de ejecución. |
| `WIN32_SERVICE_START_PENDING` | `0x00000002` | El servicio está en curso de inicio. |
| `WIN32_SERVICE_STOP_PENDING` | `0x00000003` | El servicio está en curso de parada. |
| `WIN32_SERVICE_STOPPED` | `0x00000001` | El servicio está parado. |

Constantes de Estado del Servicio de Win32Service {#win32service.constants.servicestatus}

| Constante | Valor | Descripción |
|----|----|----|
| `WIN32_SERVICE_CONTROL_CONTINUE` | `0x00000003` | Avisa a un servicio suspendido que debe reanudarse. |
| `WIN32_SERVICE_CONTROL_DEVICEEVENT` | `0x0000000B` |  |
| `WIN32_SERVICE_CONTROL_HARDWAREPROFILECHANGE` | `0x0000000C` |  |
| `WIN32_SERVICE_CONTROL_INTERROGATE` | `0x00000004` | Avisa a un servicio que debe informar sobre su estado actual al controlador de servicio. |
| `WIN32_SERVICE_CONTROL_NETBINDADD` | `0x00000007` | Avisa a un servicio de red que existe un nuevo componente para la conexión. |
| `WIN32_SERVICE_CONTROL_NETBINDDISABLE` | `0x0000000A` | Avisa a un servicio de red que una de sus conexiones ha sido desactivada. |
| `WIN32_SERVICE_CONTROL_NETBINDENABLE` | `0x00000009` | Avisa a un servicio de red que una conexión desactivada ha sido activada. |
| `WIN32_SERVICE_CONTROL_NETBINDREMOVE` | `0x00000008` | Avisa a un servicio de red que un componente para la conexión ha sido eliminado. |
| `WIN32_SERVICE_CONTROL_PARAMCHANGE` | `0x00000006` | Avisa a un servicio que sus parámetros de inicio han cambiado. |
| `WIN32_SERVICE_CONTROL_PAUSE` | `0x00000002` | Avisa a un servicio que debe ponerse en pausa. |
| `WIN32_SERVICE_CONTROL_POWEREVENT` | `0x0000000D` |  |
| `WIN32_SERVICE_CONTROL_PRESHUTDOWN` | `0x0000000F` | Avisa a un servicio que el sistema va a apagarse. Un servicio que maneja esta notificación bloquea el apagado del sistema hasta que el servicio se detenga o hasta que expire el tiempo de preapagado. Este valor no es soportado por Windows Server 2003 y Windows XP/2000. |
| `WIN32_SERVICE_CONTROL_SESSIONCHANGE` | `0x0000000E` |  |
| `WIN32_SERVICE_CONTROL_SHUTDOWN` | `0x00000005` | Avisa a un servicio que el sistema se está apagando y que el servicio puede realizar tareas de limpieza. Si un servicio acepta este código de control, debe detenerse tan pronto como complete sus tareas de limpieza. Después de enviar este código de control por el ACM, ningún otro código de control será enviado al servicio. |
| `WIN32_SERVICE_CONTROL_STOP` | `0x00000001` | Avisa a un servicio que debe detenerse. |

Constantes del Servicio de Control de Mensaje de Win32Service {#win32service.constants.servicecontrol}

| Constante | Valor | Descripción |
|----|----|----|
| `WIN32_SERVICE_ACCEPT_HARDWAREPROFILECHANGE` | `0x00000020` | El servicio es notificado cuando el perfil de hardware del ordenador ha cambiado. Esto permite al sistema enviar notificaciones `WIN32_SERVICE_CONTROL_HARDWAREPROFILECHANGE` al servicio. |
| `WIN32_SERVICE_ACCEPT_NETBINDCHANGE` | `0x00000010` | El servicio es un componente de red que puede aceptar cambios en su conexión sin ser detenido y reiniciado. Este código de control permite al servicio recibir las notificaciones `WIN32_SERVICE_CONTROL_NETBINDADD`, `WIN32_SERVICE_CONTROL_NETBINDREMOVE`, `WIN32_SERVICE_CONTROL_NETBINDENABLE`, y `WIN32_SERVICE_CONTROL_NETBINDDISABLE`. |
| `WIN32_SERVICE_ACCEPT_PARAMCHANGE` | `0x00000008` | El servicio puede releer sus parámetros de inicio sin ser detenido y reiniciado. Este código de control permite al servicio recibir notificaciones `WIN32_SERVICE_CONTROL_PARAMCHANGE`. |
| `WIN32_SERVICE_ACCEPT_PAUSE_CONTINUE` | `0x00000002` | El servicio puede ser puesto en pausa y continuado. Este código de control permite al servicio recibir las notificaciones `WIN32_SERVICE_CONTROL_PAUSE` y `WIN32_SERVICE_CONTROL_CONTINUE`. |
| `WIN32_SERVICE_ACCEPT_POWEREVENT` | `0x00000040` | El servicio es notificado cuando el estado de alimentación del ordenador ha cambiado. Esto permite al sistema enviar notificaciones `WIN32_SERVICE_CONTROL_POWEREVENT` al servicio. |
| `WIN32_SERVICE_ACCEPT_PRESHUTDOWN` | `0x00000100` | El servicio puede realizar tareas antes del apagado. Este código de control permite al servicio recibir la notificación `WIN32_SERVICE_CONTROL_PRESHUTDOWN`. Este valor no es soportado por Windows Server 2003 y Windows XP/2000. |
| `WIN32_SERVICE_ACCEPT_SESSIONCHANGE` | `0x00000080` | El servicio es notificado cuando el estado de sesión del ordenador ha cambiado. Esto permite al sistema enviar notificaciones `WIN32_SERVICE_CONTROL_SESSIONCHANGE` al servicio. Windows 2000: este valor no es soportado. |
| `WIN32_SERVICE_ACCEPT_SHUTDOWN` | `0x00000004` | El servicio es informado cuando ocurre el apagado del sistema. Este código de control permite al servicio recibir la notificación `WIN32_SERVICE_CONTROL_SHUTDOWN`. |
| `WIN32_SERVICE_ACCEPT_STOP` | `0x00000001` | El servicio puede ser detenido. Este control permite al servicio recibir la notificación `WIN32_SERVICE_CONTROL_STOP`. |
| `WIN32_SERVICE_ACCEPT_TIMECHANGE` | `0x00000200` | El servicio es notificado cuando la hora del sistema ha cambiado. Esto permite al sistema enviar notificaciones `WIN32_SERVICE_CONTROL_TIMECHANGE` al servicio. Windows Server 2008, Windows Vista, Windows Server 2003 y Windows XP/2000: este código de control no es soportado. |
| `WIN32_SERVICE_ACCEPT_TRIGGEREVENT` | `0x00000400` | El servicio es notificado cuando ocurre un evento para el cual el servicio se ha registrado. Esto permite al sistema enviar notificaciones `WIN32_SERVICE_CONTROL_TRIGGEREVENT` al servicio. Windows Server 2008, Windows Vista, Windows Server 2003 y Windows XP/2000: este código de control no es soportado. |

Máscara binaria de Mensaje de Control de Servicio de Win32Service {#win32service.constants.controlsaccepted}

| Constante | Valor | Descripción |
|----|----|----|
| `WIN32_SERVICE_BOOT_START` | `0x00000000` | Un controlador de dispositivo iniciado por el cargador del sistema. Este valor es válido únicamente para los servicios de controlador. |
| `WIN32_SERVICE_SYSTEM_START` | `0x00000001` | Un controlador de dispositivo iniciado por la función IoInitSystem. Este valor es válido únicamente para los servicios de controlador. |
| `WIN32_SERVICE_AUTO_START` | `0x00000002` | Un servicio lanzado automáticamente por el controlador de servicio al inicio del sistema. |
| `WIN32_SERVICE_DEMAND_START` | `0x00000003` | Un servicio iniciado por el controlador de servicio cuando un proceso llama a la función StartService. |
| `WIN32_SERVICE_DISABLED` | `0x00000004` | Un servicio que no puede ser iniciado. Los intentos para iniciar devuelven un código de error `WIN32_ERROR_SERVICE_DISABLED`. |

Constantes de Tipo de Inicio del Servicio de Win32Service {#win32service.constants.servicestarttype}

| Constante | Valor | Descripción |
|----|----|----|
| `WIN32_SERVICE_ERROR_IGNORE` | `0x00000000` | El programa de inicio ignora el error y continúa la operación de inicio. |
| `WIN32_SERVICE_ERROR_NORMAL` | `0x00000001` | El programa de inicio registra el error en el registro de eventos, pero continúa la operación de inicio. |
| `WIN32_SERVICE_ERROR_SEVERE` | `0x00000002` | El programa de inicio consigna el error en el registro de eventos. Si la última configuración conocida es lanzada, la operación de inicio se continúa. De lo contrario, el sistema se reinicia con la última configuración conocida-bueno. |
| `WIN32_SERVICE_ERROR_CRITICAL` | `0x00000003` | El programa de inicio consigna el error en el registro de eventos, si es posible. Si la última configuración conocida es lanzada, la operación de inicio falla. De lo contrario, el sistema se reinicia con la última configuración conocida-bueno. |

Constantes de Control de Error de Win32Service {#win32service.constants.errorcontrol}

| Constante | Valor | Descripción |
|----|----|----|
| `WIN32_SERVICE_RUNS_IN_SYSTEM_PROCESS` | `0x00000001` | El servicio se ejecuta en un proceso del sistema que debe estar siempre en ejecución. |

Constantes de Flag de Servicio de Win32Service {#win32service.constants.serviceflag}

> [!NOTE]
> Estas constantes ya no se utilizan a partir de Win32Service 1.0.0.

| Constante | Valor | Descripción |
|----|----|----|
| `WIN32_ERROR_ACCESS_DENIED` | `0x00000005` | El controlador de la base de datos SMC no dispone de los derechos de acceso apropiados. |
| `WIN32_ERROR_CIRCULAR_DEPENDENCY` | `0x00000423` | Una dependencia circular de servicio está especificada. |
| `WIN32_ERROR_DATABASE_DOES_NOT_EXIST` | `0x00000429` | La base de datos especificada no existe. |
| `WIN32_ERROR_DEPENDENT_SERVICES_RUNNING` | `0x0000041B` | El servicio no puede ser detenido porque otros servicios en ejecución dependen de él. |
| `WIN32_ERROR_DUPLICATE_SERVICE_NAME` | `0x00000436` | El nombre de visualización ya existe en la base de datos del controlador de servicio como nombre de servicio o como nombre de visualización. |
| `WIN32_ERROR_FAILED_SERVICE_CONTROLLER_CONNECT` | `0x00000427` | Este error es devuelto si el programa es ejecutado en aplicación de consola en lugar de como servicio. Si el programa es ejecutado en aplicación de consola para propósitos de depuración, debe ser estructurado de manera que el código específico del servicio nunca sea llamado. |
| `WIN32_ERROR_INSUFFICIENT_BUFFER` | `0x0000007A` | El buffer es demasiado pequeño para la estructura de estado del servicio. Nada ha sido escrito en la estructura. |
| `WIN32_ERROR_INVALID_DATA` | `0x0000000D` | La estructura de estado del servicio indicada no es válida. |
| `WIN32_ERROR_INVALID_HANDLE` | `0x00000006` | El manejador para el controlador de servicio especificado es inválido. |
| `WIN32_ERROR_INVALID_LEVEL` | `0x0000007C` | El parámetro InfoLevel contiene un valor no soportado. |
| `WIN32_ERROR_INVALID_NAME` | `0x0000007B` | El nombre de servicio especificado no es válido. |
| `WIN32_ERROR_INVALID_PARAMETER` | `0x00000057` | Un parámetro especificado no es válido. |
| `WIN32_ERROR_INVALID_SERVICE_ACCOUNT` | `0x00000421` | El nombre de usuario especificado en el parámetro `user` no existe. Ver `win32_create_service`. |
| `WIN32_ERROR_INVALID_SERVICE_CONTROL` | `0x0000041C` | El código de control solicitado no es válido, o es inaceptable para el servicio. |
| `WIN32_ERROR_PATH_NOT_FOUND` | `0x00000003` | El fichero binario del servicio no ha podido ser encontrado. |
| `WIN32_ERROR_SERVICE_ALREADY_RUNNING` | `0x00000420` | Una instancia del servicio ya está en ejecución. |
| `WIN32_ERROR_SERVICE_CANNOT_ACCEPT_CTRL` | `0x00000425` | El código de control solicitado no puede ser enviado al servicio porque el estado del servicio es `WIN32_SERVICE_STOPPED`, `WIN32_SERVICE_START_PENDING` o `WIN32_SERVICE_STOP_PENDING`. |
| `WIN32_ERROR_SERVICE_DATABASE_LOCKED` | `0x0000041F` | La base de datos está bloqueada. |
| `WIN32_ERROR_SERVICE_DEPENDENCY_DELETED` | `0x00000433` | El servicio depende de un servicio que no existe o que ha sido marcado para eliminación. |
| `WIN32_ERROR_SERVICE_DEPENDENCY_FAIL` | `0x0000042C` | Este servicio depende de otro servicio que no ha podido iniciar. |
| `WIN32_ERROR_SERVICE_DISABLED` | `0x00000422` | El servicio ha sido desactivado. |
| `WIN32_ERROR_SERVICE_DOES_NOT_EXIST` | `0x00000424` | El servicio especificado no existe como servicio instalado. |
| `WIN32_ERROR_SERVICE_EXISTS` | `0x00000431` | El servicio especificado ya existe en la base de datos. |
| `WIN32_ERROR_SERVICE_LOGON_FAILED` | `0x0000042D` | El servicio no ha iniciado debido a un fallo de conexión. Este error ocurre si el servicio está configurado para ejecutarse bajo un cuenta que no tiene los derechos "conectar como servicio". |
| `WIN32_ERROR_SERVICE_MARKED_FOR_DELETE` | `0x00000430` | El servicio especificado ya ha sido marcado para eliminación. |
| `WIN32_ERROR_SERVICE_NO_THREAD` | `0x0000041E` | Un thread no ha podido ser creado para el servicio. |
| `WIN32_ERROR_SERVICE_NOT_ACTIVE` | `0x00000426` | El servicio no ha sido iniciado. |
| `WIN32_ERROR_SERVICE_REQUEST_TIMEOUT` | `0x0000041D` | El proceso del servicio ha sido iniciado, pero no ha llamado StartServiceCtrlDispatcher, o el thread que ha llamado StartServiceCtrlDispatcher puede estar bloqueado en una función del controlador de control. |
| `WIN32_ERROR_SHUTDOWN_IN_PROGRESS` | `0x0000045B` | El sistema se está apagando, esta función no puede ser llamada. |
| `WIN32_ERROR_SERVICE_SPECIFIC_ERROR` | `0x0000042A` | El servicio ha devuelto un código de error específico del servicio. |
| `WIN32_NO_ERROR` | `0x00000000` | Ningún error. |

Códigos de Error Win32 {#win32service.constants.errors}

| Constante | Valor | Descripción |
|----|----|----|
| `WIN32_ABOVE_NORMAL_PRIORITY_CLASS` | `0x00008000` | Proceso con una prioridad superior a WIN32_NORMAL_PRIORITY_CLASS pero inferior a WIN32_HIGH_PRIORITY_CLASS. |
| `WIN32_BELOW_NORMAL_PRIORITY_CLASS` | `0x00004000` | Proceso con una prioridad superior a WIN32_IDLE_PRIORITY_CLASS pero inferior a WIN32_NORMAL_PRIORITY_CLASS. |
| `WIN32_HIGH_PRIORITY_CLASS` | `0x00000080` | Proceso que ejecuta tareas críticas en el tiempo que deben ser ejecutadas inmediatamente. El thread del proceso precede a los threads de prioridad normal o en reposo. Un ejemplo es la lista de tareas, que debe responder rápidamente cuando es llamada por el usuario, independientemente de la carga del sistema. Sea extremadamente cuidadoso cuando se utiliza la clase de alta prioridad, ya que una aplicación de clase de alta prioridad puede utilizar casi todo el tiempo CPU disponible. |
| `WIN32_IDLE_PRIORITY_CLASS` | `0x00000040` | Proceso cuyo threads solo se ejecutan cuando el sistema está inactivo. Los threads del proceso son precedidos por los threads de cualquier proceso en curso con una clase de mayor prioridad. Un ejemplo es un protector de pantalla. Esta clase es heredada por los procesos hijos. |
| `WIN32_NORMAL_PRIORITY_CLASS` | `0x00000020` | Proceso sin necesidades específicas de planificación. |
| `WIN32_REALTIME_PRIORITY_CLASS` | `0x00000100` | Proceso con la mayor prioridad posible. Los threads del proceso preceden a los threads de cualquier otro proceso, incluyendo los procesos del sistema operativo ejecutando tareas importantes. Por ejemplo, un proceso en tiempo real que se ejecuta un poco demasiado lento puede causar pérdidas de escritura del buffer en el disco o impedir a la ratón de responder. |

Clases de Prioridad de Base Win32 {#win32service.constants.basepriorities}

| Constante                     | Valor        | Descripción            |
|-------------------------------|--------------|------------------------|
| `WIN32_SC_ACTION_NONE`        | `0x00000000` | Ninguna acción.        |
| `WIN32_SC_ACTION_RESTART`     | `0x00000001` | Reiniciar el servicio. |
| `WIN32_SC_ACTION_REBOOT`      | `0x00000002` | Reiniciar el servidor. |
| `WIN32_SC_ACTION_RUN_COMMAND` | `0x00000003` | Ejecutar un programa.  |

Acciones de Recuperación Win32 {#win32service.constants.recovery-action}

| Constante                          | Valor                   | Descripción |
|------------------------------------|-------------------------|-------------|
| `WIN32_INFO_SERVICE`               | "service"               |             |
| `WIN32_INFO_DISPLAY`               | "display"               |             |
| `WIN32_INFO_USER`                  | "user"                  |             |
| `WIN32_INFO_PASSWORD`              | "password"              |             |
| `WIN32_INFO_PATH`                  | "path"                  |             |
| `WIN32_INFO_PARAMS`                | "params"                |             |
| `WIN32_INFO_DESCRIPTION`           | "description"           |             |
| `WIN32_INFO_START_TYPE`            | "start_type"            |             |
| `WIN32_INFO_LOAD_ORDER`            | "load_order"            |             |
| `WIN32_INFO_SVC_TYPE`              | "svc_type"              |             |
| `WIN32_INFO_ERROR_CONTROL`         | "error_control"         |             |
| `WIN32_INFO_DELAYED_START`         | "delayed_start"         |             |
| `WIN32_INFO_BASE_PRIORITY`         | "base_priority"         |             |
| `WIN32_INFO_DEPENDENCIES`          | "dependencies"          |             |
| `WIN32_INFO_RECOVERY_DELAY`        | "recovery_delay"        |             |
| `WIN32_INFO_RECOVERY_ACTION_1`     | "recovery_action_1"     |             |
| `WIN32_INFO_RECOVERY_ACTION_2`     | "recovery_action_2"     |             |
| `WIN32_INFO_RECOVERY_ACTION_3`     | "recovery_action_3"     |             |
| `WIN32_INFO_RECOVERY_RESET_PERIOD` | "recovery_reset_period" |             |
| `WIN32_INFO_RECOVERY_ENABLED`      | "recovery_enabled"      |             |
| `WIN32_INFO_RECOVERY_REBOOT_MSG`   | "recovery_reboot_msg"   |             |
| `WIN32_INFO_RECOVERY_COMMAND`      | "recovery_command"      |             |

Informaciones de Servicio Win32 {#win32service.constants.serviceinfos}

| Constante | Valor | Descripción |
|----|----|----|
| `WIN32_SERVICE_ALL_ACCESS` | `0x000F003F` |  |
| `WIN32_SERVICE_CHANGE_CONFIG` | `0x00000002` |  |
| `WIN32_SERVICE_ENUMERATE_DEPENDENTS` | `0x00000008` |  |
| `WIN32_SERVICE_INTERROGATE` | `0x00000080` |  |
| `WIN32_SERVICE_PAUSE_CONTINUE` | `0x00000040` |  |
| `WIN32_SERVICE_QUERY_CONFIG` | `0x00000001` |  |
| `WIN32_SERVICE_QUERY_STATUS` | `0x00000004` |  |
| `WIN32_SERVICE_START` | `0x00000010` |  |
| `WIN32_SERVICE_STOP` | `0x00000020` |  |
| `WIN32_SERVICE_USER_DEFINED_CONTROL` | `0x00000100` |  |
| `WIN32_ACCESS_SYSTEM_SECURITY` | `0x00001000` |  |
| `WIN32_DELETE` | `0x00010000` |  |
| `WIN32_READ_CONTROL` | `0x00020000` |  |
| `WIN32_WRITE_DAC` | `0x00040000` |  |
| `WIN32_WRITE_OWNER` | `0x00080000` |  |
| `WIN32_GENERIC_READ` | Incluye los permisos: `WIN32_STANDARD_RIGHTS_READ`, `WIN32_SERVICE_QUERY_CONFIG`, `WIN32_SERVICE_QUERY_STATUS`, `WIN32_SERVICE_INTERROGATE`, `WIN32_SERVICE_ENUMERATE_DEPENDENTS` |  |
| `WIN32_GENERIC_WRITE` | Incluye los permisos: `WIN32_STANDARD_RIGHTS_WRITE`, `WIN32_SERVICE_CHANGE_CONFIG` |  |
| `WIN32_GENERIC_EXECUTE` | Incluye los permisos: `WIN32_STANDARD_RIGHTS_EXECUTE`, `WIN32_SERVICE_START`, `WIN32_SERVICE_STOP`, `WIN32_SERVICE_PAUSE_CONTINUE`, `WIN32_SERVICE_USER_DEFINED_CONTROL` |  |

Permisos de Servicio Win32 {#win32service.constants.rights}
