---
title: Progresión de una subida (upload) en sesión
source_url: https://www.php.net/manual/es/session.upload-progress.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/upload-progress.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: false
translation_revision: 184f3f7bd
order: 74170
---

## Progresión de una subida (upload) en sesión

Cuando la opción de configuración [session.upload_progress.enabled](#ini.session.upload-progress.enabled) está activa, PHP será capaz de rastrear la progresión de un fichero en curso de subida (upload). Esta información no es particularmente útil para la petición de subida en sí, pero durante la subida, una aplicación puede enviar una petición POST separada (por ejemplo, mediante XHR) para verificar el estado de esta subida.

La progresión de la subida estará disponible en la variable superglobal `$_SESSION` cuando la subida está en curso, y durante un envío en método POST de una variable con el mismo nombre que el definido en la opción de configuración INI [session.upload_progress.name](#ini.session.upload-progress.name). Cuando PHP detecta una petición POST de este tipo, llenará un array en `$_SESSION`, donde el índice es un valor concatenado de las opciones de configuración [session.upload_progress.prefix](#ini.session.upload-progress.prefix) y [session.upload_progress.name](#ini.session.upload-progress.name). La clave se recupera típicamente leyendo estas configuraciones INI, es decir:

```php
<?php
$key = ini_get("session.upload_progress.prefix") . $_POST[ini_get("session.upload_progress.name")];
var_dump($_SESSION[$key]);
?>

   
```

Asimismo, es posible *cancelar* la subida actual definiendo la clave `$_SESSION[$key]["cancel_upload"]` al valor `true`. Durante la subida de varios ficheros en la misma petición, esta acción solo cancelará el fichero actualmente en curso de subida, así como aquellos en espera de subida, pero no cancelará las subidas terminadas con éxito. Cuando una subida es cancelada utilizando este método, la clave `error` del array `$_FILES` será definida a `UPLOAD_ERR_EXTENSION`.

Las opciones de configuración INI [session.upload_progress.freq](#ini.session.upload-progress.freq) y [session.upload_progress.min_freq](#ini.session.upload-progress.min-freq) controlan la frecuencia de actualización de las informaciones de progresión de subida. Con una configuración razonable de estas 2 opciones, el sobrecoste en términos de carga es casi nulo.

Ejemplo

Ejemplo de estructura del array que contiene las informaciones de subida.

```php
<form action="upload.php" method="POST" enctype="multipart/form-data">
 <input type="hidden" name="<?php echo ini_get("session.upload_progress.name"); ?>" value="123" />
 <input type="file" name="file1" />
 <input type="file" name="file2" />
 <input type="submit" />
</form>

   
```

Los datos almacenados en sesión se asemejarán a:

```php
<?php
$_SESSION["upload_progress_123"] = array(
 "start_time" => 1234567890,   // La hora de la petición
 "content_length" => 57343257, // Longitud del contenido POST
 "bytes_processed" => 453489,  // Cantidad de bytes recibidos y procesados
 "done" => false,              // true cuando el manejador POST ha terminado, con éxito o no
 "files" => array(
  0 => array(
   "field_name" => "file1",       // Nombre del campo <input/>
   // Los 3 elementos siguientes son equivalentes a los en $_FILES
   "name" => "foo.avi",
   "tmp_name" => "/tmp/phpxxxxxx",
   "error" => 0,
   "done" => true,                // True cuando el manejador POST ha terminado de manejar este fichero
   "start_time" => 1234567890,    // La hora de inicio de petición
   "bytes_processed" => 57343250, // Cantidad de bytes recibidos y procesados para este fichero
  ),
  // Otro fichero, en curso de subida, en la misma petición
  1 => array(
   "field_name" => "file2",
   "name" => "bar.avi",
   "tmp_name" => NULL,
   "error" => 0,
   "done" => false,
   "start_time" => 1234567899,
   "bytes_processed" => 54554,
  ),
 )
);

   
```

> [!WARNING]
> El almacenamiento en búfer de la petición del servidor web debe estar desactivado para el buen funcionamiento de esta funcionalidad, de lo contrario PHP solo verá el fichero una vez que esté completamente subido. Los servidores como Nginx son conocidos por almacenar en búfer grandes peticiones.

> [!CAUTION]
> Las informaciones de progresión de la subida son escritas en sesión antes de que un script sea ejecutado. Por consecuencia, cambiar el nombre de sesión mediante `ini_set` o `session_name` dará una sesión sin las informaciones de progresión de la subida.
