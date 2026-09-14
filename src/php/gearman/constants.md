---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/gearman.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 24860
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

Valores de retorno. Siempre se debe buscar una cadena de caracteres de error en GearmanClient::error o GearmanWorker ya que pueden estar disponibles más detalles:

`GEARMAN_SUCCESS` (`int`)  
Cualquier acción realizada ha sido exitosa.

`GEARMAN_IO_WAIT` (`int`)  
En modo no bloqueante, se ha alcanzado un evento que habría sido bloqueante.

`GEARMAN_ERRNO` (`int`)  
Un error del sistema. Se debe buscar en GearmanClient::errno o GearmanWorker::errno el código de error del sistema que se ha devuelto.

`GEARMAN_NO_ACTIVE_FDS` (`int`)  
GearmanClient::wait o GearmanWorker ha sido llamado sin conexión.

`GEARMAN_UNEXPECTED_PACKET` (`int`)  
Indica que algo grave ha ocurrido en gearmand. Solo se aplica a `GearmanWorker`.

`GEARMAN_GETADDRINFO` (`int`)  
La resolución DNS ha fallado (host o puerto inválido, etc).

`GEARMAN_NO_SERVERS` (`int`)  
No se ha realizado ninguna llamada a GearmanClient::addServer antes de enviar una tarea.

`GEARMAN_LOST_CONNECTION` (`int`)  
Se ha perdido la conexión durante una solicitud.

`GEARMAN_MEMORY_ALLOCATION_FAILURE` (`int`)  
La asignación de memoria ha fallado (no hay memoria disponible).

`GEARMAN_SERVER_ERROR` (`int`)  
Algo ha salido mal con el servidor Gearman que no ha podido procesar la solicitud como debería.

`GEARMAN_WORK_DATA` (`int`)  
Un código de error de notificación obtenido con GearmanClient::returnCode al utilizar GearmanClient::do. Se envía para actualizar al cliente con los datos de la tarea actual. Un agente lo utiliza cuando necesita enviar actualizaciones, enviar resultados parciales o vaciar datos durante tareas largas.

`GEARMAN_WORK_WARNING` (`int`)  
Un código de error de notificación obtenido con GearmanClient::returnCode al utilizar GearmanClient::do. Actualiza al cliente con un aviso. El comportamiento es el mismo que con `GEARMAN_WORK_DATA`, excepto que debería ser tratado como un aviso en lugar de los datos de una respuesta normal.

`GEARMAN_WORK_STATUS` (`int`)  
Un código de error de notificación obtenido con GearmanClient::returnCode al utilizar GearmanClient::do. Se envía para actualizar el estado de una tarea larga. Utilice GearmanClient::doStatus para obtener el porcentaje de completación de la tarea.

`GEARMAN_WORK_EXCEPTION` (`int`)  
Un código de error de notificación obtenido con GearmanClient::returnCode al utilizar GearmanClient::do. Indica que una tarea ha fallado al lanzar una excepción dada.

`GEARMAN_WORK_FAIL` (`int`)  
Un código de error de notificación obtenido con GearmanClient::returnCode al utilizar GearmanClient::do. Indica que una tarea ha fallado.

`GEARMAN_COULD_NOT_CONNECT` (`int`)  
Fallo al conectar con los servidores.

`GEARMAN_INVALID_FUNCTION_NAME` (`int`)  
Intento de referencia a una función con un nombre NULL o uso de la interfaz de devolución de llamada sin especificar las devoluciones de llamada.

`GEARMAN_INVALID_WORKER_FUNCTION` (`int`)  
Intento de referencia a una función con una función de devolución de llamada NULL.

`GEARMAN_NO_REGISTERED_FUNCTIONS` (`int`)  
Cuando un agente recibe una tarea para una función que no ha referenciado.

`GEARMAN_NO_JOBS` (`int`)  
Para un agente no bloqueante, cuando GearmanWorker::work no tiene ninguna tarea activa.

`GEARMAN_ECHO_DATA_CORRUPTION` (`int`)  
Después de GearmanClient::echo o GearmanWorker::echo, los datos devueltos no coinciden con los datos enviados.

`GEARMAN_NEED_WORKLOAD_FN` (`int`)  
Cuando el cliente ha optado por distribuir la carga de trabajo en una tarea, pero no ha especificado una función de retorno de la carga de trabajo.

`GEARMAN_PAUSE` (`int`)  
Para la interfaz de tarea cliente no bloqueante, puede ser devuelto desde el retorno de la tarea para "pausar" la llamada y el retorno de GearmanClient::runTasks. Llame de nuevo a GearmanClient::runTasks para continuar.

`GEARMAN_UNKNOWN_STATE` (`int`)  
Error de estado interno del cliente/agente.

`GEARMAN_SEND_BUFFER_TOO_SMALL` (`int`)  
Error interno: intentó vaciar más datos de los posibles en un paquete atómico, debido a tamaños de búfer codificados en el código.

`GEARMAN_TIMEOUT` (`int`)  
Se ha alcanzado el límite de tiempo del agente/cliente.

Las opciones `GearmanClient`:

`GEARMAN_CLIENT_GENERATE_UNIQUE` (`int`)  
Genera un identificador único (UUID) para cada tarea.

`GEARMAN_CLIENT_NON_BLOCKING` (`int`)  
Inicia el cliente en modo no bloqueante.

`GEARMAN_CLIENT_UNBUFFERED_RESULT` (`int`)  
Permite al cliente leer los datos por paquetes en lugar de que la biblioteca los almacene en búfer y los transmita.

`GEARMAN_CLIENT_FREE_TASKS` (`int`)  
Libera automáticamente los objetos de las tareas una vez que estas se han completado. Es la configuración por defecto de esta extensión para evitar fugas de memoria.

Las opciones `GearmanWorker`:

`GEARMAN_WORKER_NON_BLOCKING` (`int`)  
Inicia el agente en modo no bloqueante.

`GEARMAN_WORKER_GRAB_UNIQ` (`int`)  
Devuelve el identificador único asignado al cliente además del descriptor de tarea.

Configuración base de Gearman:

`GEARMAN_DEFAULT_TCP_HOST` (`string`)  

`GEARMAN_DEFAULT_TCP_PORT` (`int`)  

`GEARMAN_DEFAULT_SOCKET_TIMEOUT` (`int`)  

`GEARMAN_DEFAULT_SOCKET_SEND_SIZE` (`int`)  

`GEARMAN_DEFAULT_SOCKET_RECV_SIZE` (`int`)  

`GEARMAN_MAX_ERROR_SIZE` (`int`)  

`GEARMAN_PACKET_HEADER_SIZE` (`int`)  

`GEARMAN_JOB_HANDLE_SIZE` (`int`)  

`GEARMAN_OPTION_SIZE` (`int`)  

`GEARMAN_UNIQUE_SIZE` (`int`)  

`GEARMAN_MAX_COMMAND_ARGS` (`int`)  

`GEARMAN_ARGS_BUFFER_SIZE` (`int`)  

`GEARMAN_SEND_BUFFER_SIZE` (`int`)  

`GEARMAN_RECV_BUFFER_SIZE` (`int`)  

`GEARMAN_WORKER_WAIT_TIMEOUT` (`int`)
