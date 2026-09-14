---
title: Ejemplos
source_url: https://www.php.net/manual/es/eio.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_reviewed: false
translation_revision: 3ae6fd023
order: 16670
---

## Ejemplos

Cancelar una petición

```php
 <?php
 /* Es llamada cuando finaliza eio_nop() */
 function mi_llamada_retorno_nop($datos, $resultado) {
  echo "mi_nop ", $datos, "\n";
 }

// Esta llamada a eio_nop() será cancelada
$petición = eio_nop(EIO_PRI_DEFAULT, "mi_llamada_retorno_nop", "1");
var_dump($petición);
eio_cancel($petición);

// Esta vez eio_nop() será procesada
eio_nop(EIO_PRI_DEFAULT, "mi_llamada_retorno_nop", "2");

// Procesar las peticiones
eio_event_loop();
?>

  
```

Resultado del ejemplo anterior es similar a:

    resource(4) of type (EIO Request Descriptor)
    mi_nop 2

Llamar a `eio_chmod`

```php
<?php
$nombre_fichero_temp = dirname(__FILE__) ."eio-fichero-temp.tmp";
touch($nombre_fichero_temp);

/* Es llamada cuando finaliza eio_chmod() */
function mi_llamada_retorno_chmod($datos, $resultado) {
    global $nombre_fichero_temp;

    if ($resultado == 0 && !is_readable($nombre_fichero_temp) && is_writable($nombre_fichero_temp)) {
        echo "eio_chmod_ok";
    }

    @unlink($nombre_fichero_temp);
}

eio_chmod($nombre_fichero_temp, 0200, EIO_PRI_DEFAULT, "mi_llamada_retorno_chmod");
eio_event_loop();
?>

  
```

Resultado del ejemplo anterior es similar a:

    eio_chmod_ok

Realizar una petición personalizada

```php
<?php
/* Llamada de retorno para la llamada de retorno personalizada */
function mi_llamada_retorno_personalizada($datos, $resultado) {
    var_dump($datos);
    var_dump(count($resultado));
    var_dump($resultado['data_modified']);
    var_dump($resultado['result']);
}

/* La petición personalizada */
function mi_personalizada($datos) {
    var_dump($datos);

    $resultado = array(
        'result'        => 1001,
        'data_modified' => "mis datos personalizados",
    );

    return $resultado;
}

$datos = "mis_datos_personalizados";
$petición = eio_custom("mi_personalizada", EIO_PRI_DEFAULT, "mi_llamada_retorno_personalizada", $datos);
var_dump($petición);
eio_event_loop();
?>

  
```

Resultado del ejemplo anterior es similar a:

    resource(4) of type (EIO Request Descriptor)
    string(24) "mis_datos_personalizados"
    string(24) "mis_datos_personalizados"
    int(2)
    string(24) "mis datos personalizados"
    int(1001)

Agrupar peticiones

```php
<?php
/*
 * Crear un grupo de peticiones para abrir, leer y cerrar un fichero
 */

$nombre_fichero_temp = dirname(__FILE__) ."/eio-file.tmp";
$fp = fopen($nombre_fichero_temp, "w");
fwrite($fp, "algunos datos");
fclose($fp);

/* Es llamada cuando el grupo de peticiones está hecho */
function mi_grupo_hecho($datos, $resultado) {
 global $nombre_fichero_temp;
 var_dump($resultado == 0);
 @unlink($nombre_fichero_temp);
}

/* Es llamada cuando eio_open() termina */
function mi_grupo_llamada_retorno_fichero_abierto($datos, $resultado) {
 global $mi_df_fichero, $grupo;

 $mi_df_fichero = $resultado;

 var_dump($resultado > 0);

 // Crear una petición eio_read() y añadirla al grupo
 $petición = eio_read($mi_df_fichero, 4, 0, EIO_PRI_DEFAULT, "mi_grupo_llamada_retorno_fichero_leído");
 eio_grp_add($grupo, $petición);
}

/* Se llama cuando eio_read() termina */
function mi_grupo_llamada_retorno_fichero_leído($datos, $resultado) {
 global $mi_df_fichero, $grupo;

 var_dump($resultado);

 // Crear una petición eio_close() y añadirla al grupo
 $petición = eio_close($mi_df_fichero);
 eio_grp_add($grupo, $petición);
}

$grupo = eio_grp("mi_grupo_hecho", "mis_datos_grupo");

// Crear una petición eio_open() y añadirla al grupo
$petición = eio_open($nombre_fichero_temp, EIO_O_RDWR | EIO_O_APPEND , NULL,
  EIO_PRI_DEFAULT, "mi_grupo_llamada_retorno_fichero_abierto", NULL);
eio_grp_add($grupo, $petición);
var_dump($grupo);

eio_event_loop();
?>

   
```

Resultado del ejemplo anterior es similar a:

    resource(6) of type (EIO Group Descriptor)
    bool(true)
    string(7) "algunos"
    bool(true)

Emplear eio con la extensión libevent

```php
<?php
function mi_eio_poll($df, $eventos, $argumentos) {
    /* Algunas regulaciones de libevent podrían ir aquí .. */
    if (eio_nreqs()) {
        eio_poll();
    }
    /* .. y aquí */
}

function mi_llamada_retorno_nop($d, $r) {
    var_dump($r); var_dump($d);
}

$base = event_base_new();
$evento = event_new();

$df = eio_get_event_stream();
var_dump($df);

eio_nop(EIO_PRI_DEFAULT, "mi_llamada_retorno_nop", "nop data");
eio_mkdir("/tmp/abc-eio-temp", 0750, EIO_PRI_DEFAULT, "mi_llamada_retorno_nop", "nop data");
/* algunas llamadas eio_* aquí ... */

// establecer las banderas del evento
event_set($evento, $df, EV_READ /*| EV_PERSIST*/, "my_eio_poll", array($evento, $base));

// Establecer la base del evento
event_base_set($evento, $base);

// habilitar el evento
event_add($evento);

// iniciar el bucle de eventos
event_base_loop($base);

/* Lo mismo estará disponible mediante interfaz libevent con buffer */
?>
```

Resultado del ejemplo anterior es similar a:

    int(3)
    int(0)
    string(8) "nop data"
    int(0)
    string(10) "mkdir data"

Emplear eio con la extensión event

```php
<?php
$base = new EventBase();

// Recuperar el flujo de sondeo de eio.
// Observe, esta variable debería permanecer viva mientras se ejecute el bucle.
$eio_stream = eio_get_event_stream();

// Vincular el flujo de sondeo de eio al bucle de evento.
$poll_event = new Event($base, $eio_stream, Event::READ, function () {
  if (eio_nreqs()) {
    eio_poll();
  }
});
$poll_event->add();

// Añadir trabajos de eio
eio_nop(EIO_PRI_DEFAULT, function () {
  echo "eio_nop\n";
});

// Añadir eventos
$timer = Event::timer($base, function () {
  echo "2 segundos transcurridos\n";
});
$timer->add(2);

// Despachar eventos.
$base->dispatch();
?>
```

Resultado del ejemplo anterior es similar a:

    eio_nop
    2 segundos transcurridos
