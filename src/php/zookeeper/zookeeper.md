---
title: La clase Zookeeper
source_url: https://www.php.net/manual/es/class.zookeeper.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zookeeper/zookeeper.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zookeeper
translation_status: ready
translation_reviewed: false
translation_revision: 7cecc752c
order: 109760
---

## Introducción

Representa la sesión de ZooKeeper.

## Sinopsis de la clase

Zookeeper

Zookeeper

Métodos

Constantes

const

int

PERM_READ

1

const

int

PERM_WRITE

2

const

int

PERM_CREATE

4

const

int

PERM_DELETE

8

const

int

PERM_ADMIN

16

const

int

PERM_ALL

31

const

int

EPHEMERAL

1

const

int

SEQUENCE

2

const

int

LOG_LEVEL_ERROR

1

const

int

LOG_LEVEL_WARN

2

const

int

LOG_LEVEL_INFO

3

const

int

LOG_LEVEL_DEBUG

4

const

int

EXPIRED_SESSION_STATE

-112

const

int

AUTH_FAILED_STATE

-113

const

int

CONNECTING_STATE

1

const

int

ASSOCIATING_STATE

2

const

int

CONNECTED_STATE

3

const

int

READONLY_STATE

5

const

int

NOTCONNECTED_STATE

999

const

int

CREATED_EVENT

1

const

int

DELETED_EVENT

2

const

int

CHANGED_EVENT

3

const

int

CHILD_EVENT

4

const

int

SESSION_EVENT

-1

const

int

NOTWATCHING_EVENT

-2

const

int

SYSTEMERROR

-1

const

int

RUNTIMEINCONSISTENCY

-2

const

int

DATAINCONSISTENCY

-3

const

int

CONNECTIONLOSS

-4

const

int

MARSHALLINGERROR

-5

const

int

UNIMPLEMENTED

-6

const

int

OPERATIONTIMEOUT

-7

const

int

BADARGUMENTS

-8

const

int

INVALIDSTATE

-9

const

int

NEWCONFIGNOQUORUM

-13

const

int

RECONFIGINPROGRESS

-14

const

int

OK

0

const

int

APIERROR

-100

const

int

NONODE

-101

const

int

NOAUTH

-102

const

int

BADVERSION

-103

const

int

NOCHILDRENFOREPHEMERALS

-108

const

int

NODEEXISTS

-110

const

int

NOTEMPTY

-111

const

int

SESSIONEXPIRED

-112

const

int

INVALIDCALLBACK

-113

const

int

INVALIDACL

-114

const

int

AUTHFAILED

-115

const

int

CLOSING

-116

const

int

NOTHING

-117

const

int

SESSIONMOVED

-118

const

int

NOTREADONLY

-119

const

int

EPHEMERALONLOCALSESSION

-120

const

int

NOWATCHER

-121

const

int

RECONFIGDISABLED

-122

## Constantes predefinidas

## Permisos ZooKeeper

`Zookeeper::PERM_READ`  
Puede leer el valor de los nodos y enumerar sus hijos

`Zookeeper::PERM_WRITE`  
Puede establecer el valor de los nodos

`Zookeeper::PERM_CREATE`  
Puede crear hijos

`Zookeeper::PERM_DELETE`  
Puede eliminar hijos

`Zookeeper::PERM_ADMIN`  
Puede ejecutar set_acl()

`Zookeeper::PERM_ALL`  
Todas las flags anteriores combinadas con OR

## Flags de creación de ZooKeeper

`Zookeeper::EPHEMERAL`  
Si la flag Zookeeper::EPHEMERAL es establecida, el nodo se eliminará automáticamente si la sesión del cliente desaparece.

`Zookeeper::SEQUENCE`  
Si la flag Zookeeper::SEQUENCE flag es establecida, un número de secuencia ascendente único se añade al nombre de la ruta. El número de secuencia es siempre de longitud fija de 10 dígitos, 0 relleno.

## Niveles de log de ZooKeeper

`Zookeeper::LOG_LEVEL_ERROR`  
Emite sólo mensajes de error

`Zookeeper::LOG_LEVEL_WARN`  
Emite errores/advertencias

`Zookeeper::LOG_LEVEL_INFO`  
Emite grandes mensajes de acción además de errores/advertencias

`Zookeeper::LOG_LEVEL_DEBUG`  
Emite todo

## Estados de ZooKeeper

`Zookeeper::EXPIRED_SESSION_STATE`  
Conectado pero la sesión expiró

`Zookeeper::AUTH_FAILED_STATE`  
Conectado pero la autentificación falló

`Zookeeper::CONNECTING_STATE`  
Conectando

`Zookeeper::ASSOCIATING_STATE`  
Asociando

`Zookeeper::CONNECTED_STATE`  
Conectado

`Zookeeper::READONLY_STATE`  
TODO: Ayúdanos a mejorar esta extensión.

`Zookeeper::NOTCONNECTED_STATE`  
La conexión falló

## Tipos de relojes ZooKeeper

`Zookeeper::CREATED_EVENT`  
Se ha creado un nodo

Esto sólo se genera por los relojes en nodos inexistentes. Estos relojes se ajustan usando Zookeeper::exists.

`Zookeeper::DELETED_EVENT`  
Se ha eliminado un nodo

Esto sólo se genera por los relojes de los nodos. Estos relojes se ajustan usando Zookeeper::exists y Zookeeper::get.

`Zookeeper::CHANGED_EVENT`  
Un nodo ha cambiado

Esto sólo lo generan los relojes de los nodos. Estos relojes se ajustan usando Zookeeper::exists y Zookeeper::get.

`Zookeeper::CHILD_EVENT`  
Un cambio como el ocurrido en la lista de hijos

Esto sólo se genera por los relojes en la lista de hijos de un nodo. Estos relojes se ajustan usando Zookeeper::getChildren.

`Zookeeper::SESSION_EVENT`  
Se ha perdido una sesión

Esto se genera cuando un cliente pierde el contacto o se reconecta con un servidor.

`Zookeeper::NOTWATCHING_EVENT`  
Se ha quitado un reloj

Esto se genera cuando el servidor, por alguna razón, probablemente una limitación de recursos, ya no vigila un nodo para un cliente.

## Errores del sistema y del servidor ZooKeeper

`Zookeeper::SYSTEMERROR`  
Esto nunca es lanzado por el servidor, no debe ser usado más que para indicar un rango. Específicamente códigos de error mayores que este valor, pero menores que Zookeeper::APIERROR, son errores del sistema.

`Zookeeper::RUNTIMEINCONSISTENCY`  
Se encontró una inconsistencia en el tiempo de ejecución.

`Zookeeper::DATAINCONSISTENCY`  
Se encontró una inconsistencia en los datos.

`Zookeeper::CONNECTIONLOSS`  
Se ha perdido la conexión con el servidor.

`Zookeeper::MARSHALLINGERROR`  
Error al ordenar o desordenar los datos.

`Zookeeper::UNIMPLEMENTED`  
La operación no se ha llevado a cabo.

`Zookeeper::OPERATIONTIMEOUT`  
Tiempo de espera de la operación.

`Zookeeper::BADARGUMENTS`  
Argumentos inválidos.

`Zookeeper::INVALIDSTATE`  
Estado de zhandle inválido.

`Zookeeper::NEWCONFIGNOQUORUM`  
Ningún grupo de nueva configuración está conectado y actualizado con el líder de la última configuración realizada. - intente invocar la reconfiguración después de que los nuevos servidores estén conectados y sincronizados.

Disponible a partir de ZooKeeper 3.5.0

`Zookeeper::RECONFIGINPROGRESS`  
Se solicita una reconfiguración mientras se está llevando a cabo otra reconfiguración. Esto no se soporta actualmente. Por favor, vuelva a intentarlo..

Disponible a partir de ZooKeeper 3.5.0

## Errores de la API ZooKeeper

`Zookeeper::OK`  
Todo está bien.

`Zookeeper::APIERROR`  
Esto nunca es lanzado por el servidor, no debe usarse más que para indicar un rango. Específicamente los códigos de error mayores que este valor son errores de la API (mientras que los valores inferiores a éste indican una Zookeeper::SYSTEMERROR).

`Zookeeper::NONODE`  
El nodo no existe.

`Zookeeper::NOAUTH`  
No está autentificado.

`Zookeeper::BADVERSION`  
Conflicto de versiones.

`Zookeeper::NOCHILDRENFOREPHEMERALS`  
Los nodos efímeros pueden no tener hijos.

`Zookeeper::NODEEXISTS`  
El nodo ya existe.

`Zookeeper::NOTEMPTY`  
El nodo tiene hijos.

`Zookeeper::SESSIONEXPIRED`  
La sesión ha expirado por el servidor.

`Zookeeper::INVALIDCALLBACK`  
Se especificó una devolución de llamada inválida.

`Zookeeper::INVALIDACL`  
Se especificó un LCA inválido.

`Zookeeper::AUTHFAILED`  
La autentificación del cliente falló.

`Zookeeper::CLOSING`  
ZooKeeper está cerrando.

`Zookeeper::NOTHING`  
(no error) No hay respuestas del servidor al proceso.

`Zookeeper::SESSIONMOVED`  
La sesión se movió a otro servidor, así que la operación es ignorada.

`Zookeeper::NOTREADONLY`  
La solicitud de cambio de estado se pasa al servidor de sólo lectura.

`Zookeeper::EPHEMERALONLOCALSESSION`  
Intentar crear un nodo efímero en una sesión local.

`Zookeeper::NOWATCHER`  
El observador no pudo ser encontrado.

`Zookeeper::RECONFIGDISABLED`  
Intentar realizar una operación de reconfiguración cuando la función de reconfiguración está desactivada.
