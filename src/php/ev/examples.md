---
title: Ejemplos
source_url: https://www.php.net/manual/es/ev.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: 940ea8c1b
order: 18750
---

## Ejemplos

Ejemplo de temporizadores

```php
<?php
// Crea e inicia un temporizador que se activa después de 2 segundos
$w1 = new EvTimer(2, 0, function () {
    echo "Han pasado 2 segundos\n";
});

// Crea e inicia un temporizador que se activa después de 2 segundos y se repite cada segundo
// hasta que se detenga manualmente
$w2 = new EvTimer(2, 1, function ($w) {
    echo "se llama cada segundo y se inicia después de 2 segundos\n";
    echo "iteración = ", Ev::iteration(), PHP_EOL;

    // Detiene el watcher después de 5 iteraciones
    Ev::iteration() == 5 and $w->stop();
    // Detiene el watcher si las próximas llamadas provocan más de 10 iteraciones
    Ev::iteration() >= 10 and $w->stop();
});

// Crea un temporizador detenido. Permanecerá inactivo hasta que lo iniciemos manualmente
$w_stopped = EvTimer::createStopped(10, 5, function($w) {
    echo "Función de retorno de un temporizador creado detenido\n";

    // Detiene el watcher después de 2 iteraciones
    Ev::iteration() >= 2 and $w->stop();
});

// Bucle mientras Ev::stop() no sea llamado o todos los watchers no estén detenidos
Ev::run();

// Inicia y verifica si funciona
$w_stopped->start();
echo "Ejecuta una sola iteración\n";
Ev::run(Ev::RUN_ONCE);

echo "Reinicia el segundo watcher e intenta manejar el mismo evento, pero no bloquea\n";
$w2->again();
Ev::run(Ev::RUN_NOWAIT);

$w = new EvTimer(10, 0, function() {});
echo "Ejecutando un bucle bloqueante\n";
Ev::run();
echo "FIN\n";
?>

  
```

Resultado del ejemplo anterior es similar a:

    Han pasado 2 segundos
    se llama cada segundo y se inicia después de 2 segundos
    iteración = 1
    se llama cada segundo y se inicia después de 2 segundos
    iteración = 2
    se llama cada segundo y se inicia después de 2 segundos
    iteración = 3
    se llama cada segundo y se inicia después de 2 segundos
    iteración = 4
    se llama cada segundo y se inicia después de 2 segundos
    iteración = 5
    Ejecuta una sola iteración
    Función de retorno de un temporizador creado detenido
    Reinicia el segundo watcher e intenta manejar el mismo evento, pero no bloquea
    Ejecutando un bucle bloqueante
    se llama cada segundo y se inicia después de 2 segundos
    iteración = 8
    se llama cada segundo y se inicia después de 2 segundos
    iteración = 9
    se llama cada segundo y se inicia después de 2 segundos
    iteración = 10
    FIN

Temporizador periódico. Alerta cada 10.5 segundos

```php
<?php
$w = new EvPeriodic(0., 10.5, NULL, function ($w, $revents) {
    echo time(), PHP_EOL;
});

Ev::run();
?>

  
```

Temporizador periódico. Uso de la función de retorno de reprogramación

```php
<?php
// Alerta cada 10.5 segundos

function reschedule_cb ($watcher, $now) {
    return $now + (10.5 - fmod($now, 10.5));
}

$w = new EvPeriodic(0., 0., "reschedule_cb", function ($w, $revents) {
    echo time(), PHP_EOL;
});

Ev::run();
?>

  
```

Temporizador periódico. Alerta cada 10.5 segundos, comenzando ahora

```php
<?php
// Alerta cada 10.5 segundos comenzando ahora
$w = new EvPeriodic(fmod(Ev::now(), 10.5), 10.5, NULL, function ($w, $revents) {
    echo time(), PHP_EOL;
});

Ev::run();
?>

  
```

Espera a que STDIN sea accesible para lectura

```php
<?php
// Espera a que STDIN sea accesible para lectura
$w = new EvIo(STDIN, Ev::READ, function ($watcher, $revents) {
    echo "STDIN es accesible para lectura\n";
});

Ev::run(Ev::RUN_ONCE);
?>

  
```

Uso de algunas E/S asíncronas para acceder a un socket

```php
<?php
/* Usa algunas E/S asíncronas para acceder a un socket */

// La extensión `sockets' continuará registrando alertas
// para EINPROGRESS, EAGAIN/EWOULDBLOCK etc.
error_reporting(E_ERROR);

$e_nonblocking = array (/*EAGAIN or EWOULDBLOCK*/11, /*EINPROGRESS*/115);

// Obtiene el puerto para el servicio WWW
$service_port = getservbyname('www', 'tcp');

// Obtiene la dirección IP para el host objetivo
$address = gethostbyname('google.co.uk');

// Crea un socket TCP/IP
$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
if ($socket === FALSE) {
    echo "Fallo en socket_create() : razón : "
        .socket_strerror(socket_last_error()) . "\n";
}

// Establece el flag O_NONBLOCK
socket_set_nonblock($socket);

// Se detiene una vez alcanzado el tiempo máximo de espera
$timeout_watcher = new EvTimer(10.0, 0., function () use ($socket) {
    socket_close($socket);
    Ev::stop(Ev::BREAK_ALL);
});

// Realiza una solicitud HEAD cuando el socket es accesible para escritura
$write_watcher = new EvIo($socket, Ev::WRITE, function ($w)
    use ($socket, $timeout_watcher, $e_nonblocking)
{
    // Detiene el watcher timeout
    $timeout_watcher->stop();
    // Detiene el watcher write
    $w->stop();

    $in = "HEAD / HTTP/1.1\r\n";
    $in .= "Host: google.co.uk\r\n";
    $in .= "Connection: Close\r\n\r\n";

    if (!socket_write($socket, $in, strlen($in))) {
        trigger_error("Fallo al escribir $in en el socket", E_USER_ERROR);
    }

    $read_watcher = new EvIo($socket, Ev::READ, function ($w, $re)
        use ($socket, $e_nonblocking)
    {
        // El socket es accesible para lectura. recv() recibió 20 bytes usando el modo no bloqueante
        $ret = socket_recv($socket, $out, 20, MSG_DONTWAIT);

        if ($ret) {
            echo $out;
        } elseif ($ret === 0) {
            // Todo ha sido leído
            $w->stop();
            socket_close($socket);
            return;
        }

        // Se capturan EINPROGRESS, EAGAIN, o EWOULDBLOCK
        if (in_array(socket_last_error(), $e_nonblocking)) {
            return;
        }

        $w->stop();
        socket_close($socket);
    });

    Ev::run();
});

$result = socket_connect($socket, $address, $service_port);

Ev::run();
?>

  
```

Resultado del ejemplo anterior es similar a:

    HTTP/1.1 301 Moved Permanently
    Location: http://www.google.co.uk/
    Content-Type: text/html; charset=UTF-8
    Date: Sun, 23 Dec 2012 16:08:27 GMT
    Expires: Tue, 22 Jan 2013 16:08:27 GMT
    Cache-Control: public, max-age=2592000
    Server: gws
    Content-Length: 221
    X-XSS-Protection: 1; mode=block
    X-Frame-Options: SAMEORIGIN
    Connection: close

Encapsula un bucle dentro de otro

```php
<?php
/*
* Intenta obtener un bucle de eventos encapsulable y lo encapsula en
* un bucle de eventos por defecto. Si es posible, se usa el bucle
* por defecto. El bucle por defecto se almacena en $loop_hi, mientras que el bucle
* encapsulable se almacena en $loop_lo (que es $loop_hi en el caso de
* que no se pueda usar ningún bucle encapsulable).
*
* Ejemplo traducido a PHP de:
* http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#Examples_CONTENT-9
*/
$loop_hi = EvLoop::defaultLoop();
$loop_lo = NULL;
$embed   = NULL;

/*
* Verifica si hay posibilidad de obtener uno que funcione
* (un valor de flag a 0 significa autodetección)
*/
$loop_lo = Ev::embeddableBackends() & Ev::recommendedBackends()
    ? new EvLoop(Ev::embeddableBackends() & Ev::recommendedBackends())
    : 0;

if ($loop_lo) {
    $embed = new EvEmbed($loop_lo, function () {});
} else {
    $loop_lo = $loop_hi;
}
?>

  
```

Encapsula un bucle creado con el backend kqueue en el bucle por defecto

```php
<?php
/*
* Verifica si kqueue está disponible pero no recomendado, y crea un backend kqueue
* para usarlo con sockets (lo cual funciona con todas las implementaciones kqueue).
* Almacena el bucle de eventos kqueue/solo-socket en loop_socket. (También se puede
* usar EVFLAG_NOENV)
*
* Ejemplo tomado de:
* http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#Examples_CONTENT-9
*/
$loop        = EvLoop::defaultLoop();
$socket_loop = NULL;
$embed       = NULL;

if (Ev::supportedBackends() & ~Ev::recommendedBackends() & Ev::BACKEND_KQUEUE) {
    if (($socket_loop = new EvLoop(Ev::BACKEND_KQUEUE))) {
        $embed = new EvEmbed($loop);
    }
}

if (!$socket_loop) {
    $socket_loop = $loop;
}

// Ahora se puede usar $socket_loop para todos los sockets, y $loop para todo lo demás
?>

  
```

Manejo de la señal SIGTERM

```php
<?php
$w = new EvSignal(SIGTERM, function ($watcher) {
    echo "Se recibe un SIGTERM\n";
    $watcher->stop();
});

Ev::run();
?>

  
```

Monitoreo de cambios en /var/log/messages

```php
<?php
// Uso de un intervalo de actualización de 10 segundos.
$w = new EvStat("/var/log/messages", 8, function ($w) {
    echo "Cambio en /var/log/messages\n";

    $attr = $w->attr();

    if ($attr['nlink']) {
        printf("Tamaño actual: %ld\n", $attr['size']);
        printf("atime actual: %ld\n", $attr['atime']);
        printf("mtime actual: %ld\n", $attr['mtime']);
    } else {
        fprintf(STDERR, "¡El fichero `messages` ya no está aquí!");
        $w->stop();
    }
});

Ev::run();
?>

  
```

Monitoreo de cambios en /var/log/messages. Se observan cambios con un segundo de retraso

```php
<?php
$timer = EvTimer::createStopped(0., 1.02, function ($w) {
    $w->stop();

    $stat = $w->data;

    // 1 segundo después de la última modificación de un fichero
    printf("Tamaño actual: %ld\n", $stat->attr()['size']);
});

$stat = new EvStat("/var/log/messages", 0., function () use ($timer) {
    // Reinicia el watcher timer
    $timer->again();
});

$timer->data = $stat;

Ev::run();
?>

  
```

Cambio de estado de un proceso

```php
<?php
$pid = pcntl_fork();

if ($pid == -1) {
    fprintf(STDERR, "pcntl_fork ha fallado\n");
} elseif ($pid) {
    $w = new EvChild($pid, FALSE, function ($w, $revents) {
        $w->stop();

        printf("El proceso %d ha salido con estado %d\n", $w->rpid, $w->rstatus);
    });

    Ev::run();

    // Protección contra Zombies
    pcntl_wait($status);
} else {
    // Se bifurca el hijo
    exit(2);
}
?>

  
```
