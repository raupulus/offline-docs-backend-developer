---
title: Gestión de las conexiones
source_url: https://www.php.net/manual/es/features.connection-handling.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: features/connection-handling.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: features
translation_status: ready
translation_reviewed: false
translation_revision: dc0f955be
order: 1530
---

## Gestión de las conexiones

El estado de las conexiones se conserva internamente por PHP. Hay cuatro estados posibles:

- 0 - NORMAL (normal)

- 1 - ABORTED (anulado)

- 2 - TIMEOUT (caducado)

- 3 - ABORTED and TIMEOUT (anulado y caducado)

Cuando un script PHP está en ejecución, el estado es NORMAL. Si el cliente remoto se desconecta, el estado se convierte en ABORTED. Una desconexión del cliente remoto generalmente es causada por los usuarios presionando su botón STOP. Si se supera el tiempo máximo de ejecución de PHP, (ver `set_time_limit`), el script adopta el estado TIMEOUT.

Asimismo, se puede decidir si se desea que la desconexión de un cliente provoque la interrupción del script. A veces es práctico que los scripts continúen ejecutándose hasta el final, incluso si el cliente ya no está presente para recibir la información. Sin embargo, por omisión, el script se detendrá tan pronto como el cliente se desconecte. Este comportamiento puede ser modificado con la directiva `ignore_user_abort` en el fichero `php.ini` o bien con la directiva Apache `php_value ignore_user_abort` del fichero Apache `httpd.conf` o con la función `ignore_user_abort`. Si no se solicita a PHP que ignore la desconexión, y el usuario se desconecta, el script será terminado. La única excepción es si se ha registrado una función de cierre, con `register_shutdown_function`. Con tal función, cuando el usuario interrumpe su solicitud, en la próxima ejecución del script, PHP se dará cuenta de que el último script no ha sido terminado, y desencadenará la función de cierre. Esta función también será llamada al final del script, si este termina normalmente. Para poder tener un comportamiento diferente según el estado del script al finalizar, se pueden ejecutar comandos específicos a la desconexión gracias a la función `connection_aborted`. Esta función devolverá `true` si la conexión ha sido anulada.

El script también puede ser interrumpido automáticamente después de un cierto tiempo. Por omisión, el tiempo límite es de 30 segundos. Este valor puede ser cambiado utilizando la directiva PHP `max_execution_time` en el fichero `php.ini` o con la directiva `php_value max_execution_time`, en el fichero Apache `httpd.conf` o también con la función `set_time_limit`. Cuando el tiempo límite expira, el script es terminado, y como en la desconexión del cliente, una función de terminación será llamada. En esta función, se puede saber si es el tiempo límite el que ha causado el fin del script, llamando a la función `connection_status`. Esta función devolverá `2` si el tiempo límite ha sido superado.

Una cosa a tener en cuenta es que los dos casos ABORTED y TIMEOUT pueden ser llamados al mismo tiempo. Esto es posible si se solicita a PHP que ignore las desconexiones de los usuarios. PHP aún así notará el hecho de que el usuario se ha desconectado, pero el script continuará. Luego, cuando alcance el límite de tiempo, el script caducará. En ese momento, la función `connection_status` devolverá `3`.
