---
title: Gestión de cargas de ficheros
source_url: https://www.php.net/manual/es/features.file-upload.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: features/file-upload.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: features
translation_status: ready
translation_reviewed: false
translation_revision: 3944dc633
order: 1560
---

## Gestión de cargas de ficheros

## Cargas de ficheros por método POST

Esta funcionalidad permite a las personas subir tanto texto como ficheros binarios. Con las funciones de identificación y manipulación de ficheros de PHP, se tiene el control total para definir quién tiene derecho a subir, pero también qué se hará con el fichero una vez que se haya subido.

PHP es capaz de recibir ficheros emitidos por un navegador conforme a la norma RFC-1867.

> [!NOTE]
> Véase también las directivas [file_uploads](#ini.file-uploads), [upload_max_filesize](#ini.upload-max-filesize), [upload_tmp_dir](#ini.upload-tmp-dir), [post_max_size](#ini.post-max-size) y [max_input_time](#ini.max-input-time) en `php.ini`

PHP también soporta la carga por el método PUT como en el navegador Netscape Composer y Amaya del W3C. Consulte el capítulo sobre el [soporte del método PUT](#features.file-upload.put-method).

Formulario de carga de fichero

Un formulario de carga de ficheros puede ser construido creando un formulario específico como este:

```php
<!-- El tipo de codificación de datos, enctype, DEBE ser especificado como se indica a continuación -->
<form enctype="multipart/form-data" action="_URL_" method="post">
  <!-- MAX_FILE_SIZE debe preceder al campo input de tipo file -->
  <input type="hidden" name="MAX_FILE_SIZE" value="30000" />
  <!-- El nombre del elemento input determina el nombre en el array $_FILES -->
  Envíe este fichero: <input name="userfile" type="file" />
  <input type="submit" value="Enviar el fichero" />
</form>

    
```

`_URL_` en el ejemplo anterior debe ser reemplazado y apuntar a un fichero PHP.

El campo oculto `MAX_FILE_SIZE` (medido en bytes) debe preceder al campo input de tipo file y su valor representa el tamaño máximo aceptado del fichero por PHP. Este elemento de formulario debe ser siempre utilizado, ya que permite informar al usuario que la transferencia deseada es demasiado grande antes de llegar al final de la carga. Tenga en cuenta que este parámetro puede ser "engañado" fácilmente desde el lado del navegador, por lo que no se debe confiar en él, tratándose finalmente de una funcionalidad de conveniencia del lado del cliente. El parámetro PHP (del lado del servidor) sobre el tamaño máximo de un fichero cargado, no puede ser engañado.

> [!NOTE]
> Asegúrese de que su formulario de carga de fichero contenga `enctype="multipart/form-data"`, de lo contrario, el fichero no será cargado.

La variable global `$_FILES` contendrá toda la información sobre el fichero cargado. Su contenido se detalla en nuestro ejemplo a continuación. Tenga en cuenta que se supone que el nombre de la variable del fichero cargado es *userfile*, tal como se define en el formulario anterior, pero puede ser cualquier nombre.

`$_FILES['userfile']['name']`  
El nombre original del fichero, tal como en la máquina del cliente web.

`$_FILES['userfile']['type']`  
El tipo MIME del fichero, si el navegador ha proporcionado esta información. Por ejemplo, esto podría ser `"image/gif"`. Este tipo mime no es verificado por PHP y, por lo tanto, no se debe tomar su valor para sincronizarse.

`$_FILES['userfile']['size']`  
El tamaño, en bytes, del fichero cargado.

`$_FILES['userfile']['tmp_name']`  
El nombre temporal del fichero que será cargado en la máquina servidor.

`$_FILES['userfile']['error']`  
El [código de error](#features.file-upload.errors) asociado a la carga del fichero.

`$_FILES['userfile']['full_path']`  
La ruta completa tal como se envía por el navegador. Este valor no contiene siempre una verdadera jerarquía de carpetas, y no se debe confiar en él. Disponible a partir de PHP 8.1.0.

El fichero cargado será almacenado temporalmente en el directorio temporal del sistema, a menos que se proporcione otro directorio con la directiva [upload_tmp_dir](#ini.upload-tmp-dir) del `php.ini`. El directorio por defecto del servidor puede ser cambiado en el entorno a través de la variable `TMPDIR`. Modificar el valor de esta variable con la función `putenv` en un script PHP será sin efecto. Esta variable de entorno también puede ser utilizada para asegurarse de que otras operaciones funcionen también en los ficheros cargados.

Validación de carga de ficheros

Véase también las funciones `is_uploaded_file` y `move_uploaded_file` para más información. El siguiente ejemplo cargará un fichero desde un formulario.

```php
<?php
$uploaddir = '/var/www/uploads/';
$uploadfile = $uploaddir . basename($_FILES['userfile']['name']);

echo '<pre>';
if (move_uploaded_file($_FILES['userfile']['tmp_name'], $uploadfile)) {
    echo "El fichero es válido, y ha sido cargado con éxito. Aquí hay más información :\n";
} else {
    echo "Ataque potencial por carga de ficheros. Aquí hay más información :\n";
}

echo 'Aquí hay algunas informaciones de depuración :';
print_r($_FILES);

echo '</pre>';

?>

    
```

El script PHP que recibe el fichero cargado debe poder gestionar el fichero de manera apropiada. Se puede utilizar la variable `$_FILES['userfile']['size']` para recalar todos los ficheros que son demasiado grandes o demasiado pequeños. Se puede utilizar la variable `$_FILES['userfile']['type']` para descartar los ficheros que no tienen el tipo correcto, pero utilizarla únicamente para una serie de verificaciones, ya que este valor está completamente bajo el control del cliente y no es verificado por PHP. Se puede utilizar la información en `$_FILES['userfile']['error']` y adaptar su política en función de los [códigos de error](#features.file-upload.errors). Sea cual sea su política, se debe borrar el fichero del directorio temporal o moverlo.

Si no se selecciona ningún fichero en el formulario, PHP devolverá `0` en `$_FILES['userfile']['size']` y nada en `$_FILES['userfile']['tmp_name']`.

El fichero será borrado automáticamente del directorio temporal al final del script, si no ha sido movido o renombrado.

Envío de un array de ficheros

PHP soporta los [arrays en HTML](#faq.html.arrays) así como con los ficheros.

```php
<form action="" method="post" enctype="multipart/form-data">
<p>Imágenes:
<input type="file" name="pictures[]" />
<input type="file" name="pictures[]" />
<input type="file" name="pictures[]" />
<input type="submit" value="Enviar" />
</p>
</form>

   
```

```php
<?php
foreach ($_FILES["pictures"]["error"] as $key => $error) {
    if ($error == UPLOAD_ERR_OK) {
        $tmp_name = $_FILES["pictures"]["tmp_name"][$key];
        // basename() puede prevenir los ataques "filesystem traversal";
        // otra validación/limpieza del nombre de fichero puede ser apropiada
        $name = basename($_FILES["pictures"]["name"][$key]);
        move_uploaded_file($tmp_name, "data/$name");
    }
}
?>

   
```

La barra de progreso de carga puede ser implementada utilizando [la progresión de la carga a través de las sesiones](#session.upload-progress).

## Explicación sobre los mensajes de errores de carga de ficheros

PHP devuelve un código de error apropiado en el array de ficheros. Este código de error es accesible en el índice `['error']` del array, que es creado durante la carga por PHP. En otras palabras, el mensaje de error es accesible en la variable `$_FILES['userfile']['error']`.

El valor de este código de error es una de las constantes `UPLOAD_ERR_*`.

## Errores clásicos

La variable `MAX_FILE_SIZE` no puede especificar un tamaño de fichero mayor que el tamaño que ha sido fijado por [upload_max_filesize](#ini.upload-max-filesize), en el `php.ini`. El valor por defecto es 2 megaoctetos.

Si se activa un límite de memoria, puede ser necesario un valor mayor de [memory_limit](#ini.memory-limit). Asegúrese de haber definido un valor para [memory_limit](#ini.memory-limit) lo suficientemente grande.

Si el valor de [max_execution_time](#ini.max-execution-time) es demasiado pequeño, el tiempo de ejecución del script puede exceder este valor. Asegúrese de haber definido un valor para `max_execution_time` lo suficientemente grande.

> [!NOTE]
> [max_execution_time](#ini.max-execution-time) afecta únicamente al tiempo de ejecución del script. El tiempo pasado en la actividad que aparece fuera de la ejecución del script como las llamadas al sistema con la función `system`, la función `sleep`, las consultas a las bases de datos, el tiempo empleado para realizar la carga del fichero, etc. no está incluido en el cálculo del tiempo máximo de ejecución del script.

> [!WARNING]
> [max_input_time](#ini.max-input-time) define el tiempo máximo, en segundos, para que el script reciba los datos; esto incluye la carga del fichero. Para múltiples ficheros, o ficheros grandes, o incluso para usuarios en conexiones lentas, el valor por defecto de `60` segundos puede ser superado.

Si [post_max_size](#ini.post-max-size) está definido de manera demasiado baja, los ficheros grandes no podrán ser cargados. Asegúrese de definir `post_max_size` con un tamaño suficiente.

La configuración de [max_file_uploads](#ini.max-file-uploads) controla el número máximo de ficheros que pueden ser enviados en una solicitud. Si el número de ficheros enviados supera este límite, entonces `$_FILES` dejará de recibir. Por ejemplo, si [max_file_uploads](#ini.max-file-uploads) vale `10`, entonces `$_FILES` nunca contendrá más de 10 entidades.

No validar los ficheros que se manipulan puede dar acceso a los usuarios a ficheros sensibles en otras carpetas.

Debido a la gran diversidad de sistemas, no se puede garantizar que los ficheros con nombres exóticos (por ejemplo, aquellos que contienen espacios) sean tratados correctamente.

El desarrollador no debe mezclar los campos `input` normales y los campos de carga en una misma variable (utilizando un nombre de `input` como `foo[]`).

## Cargar múltiples ficheros simultáneamente

La carga de múltiples ficheros es posible utilizando diferentes nombres en el atributo `name` de la etiqueta `input`.

También es posible cargar múltiples ficheros simultáneamente y obtener la información en forma de array. Para ello, se debe utilizar la sintaxis de array en los nombres de las etiquetas HTML, como se ha hecho con las selecciones múltiples y las casillas de verificación.

Cargar múltiples ficheros simultáneamente

```php
<form action="file-upload.php" method="post" enctype="multipart/form-data">
  Envíe múltiples ficheros: <br />
  <input name="userfile[]" type="file" /><br />
  <input name="userfile[]" type="file" /><br />
  <input type="submit" value="Enviar los ficheros" />
</form>

    
```

Cuando el formulario anterior ha sido enviado, los arrays `$_FILES['userfile']`, `$_FILES['userfile']['name']`, y `$_FILES['userfile']['size']` serán inicializados.

Por ejemplo, supongamos que los ficheros `/home/test/review.html` y `/home/test/xwp.out` han sido cargados. En este caso, `$_FILES['userfile']['name'][0]` contiene `review.html` y `$_FILES['userfile']['name'][1]` contiene `xwp.out`. De manera similar, `$_FILES['userfile']['size'][0]` contendrá el tamaño del fichero `review.html`, etc.

`$_FILES['userfile']['name'][0]`, `$_FILES['userfile']['tmp_name'][0]`, `$_FILES['userfile']['size'][0]` y `$_FILES['userfile']['type'][0]` también son creados.

> [!WARNING]
> El parámetro [max_file_uploads](#ini.max-file-uploads) limita el número de ficheros que pueden ser enviados en una solicitud. Se debe verificar que su formulario no intente enviar más ficheros en la solicitud de lo que permite este límite.

Cargar un directorio entero

En los campos de carga de fichero HTML, es posible cargar un directorio entero con el atributo `webkitdirectory`. Esta funcionalidad es soportada en la mayoría de los navegadores modernos.

Con la información `full_path`, es posible almacenar las rutas relativas o reconstruir la misma jerarquía de directorios en el directorio.

```php
<form action="file-upload.php" method="post" enctype="multipart/form-data">
  Envíe este directorio:<br />
  <input name="userfile[]" type="file" webkitdirectory multiple />
  <input type="submit" value="Enviar ficheros" />
</form>

    
```

> [!WARNING]
> El atributo `webkitdirectory` no es estándar y no está actualmente en proceso de estandarización. Esto no debe ser utilizado en sitios de producción orientados al Web: no funcionará para todos los usuarios. Puede haber grandes incompatibilidades entre las implementaciones y el comportamiento puede cambiar en el futuro.
>
> PHP analiza únicamente la información de las rutas relativas enviadas por el navegador/user-agent y transmite la información en el array `$_FILES`. No hay garantías de que los valores en el array `full_path` contengan una verdadera estructura de directorios y la aplicación PHP no debe confiar en esta información.

## Carga por método PUT

PHP soporta el método HTTP PUT utilizado por los navegadores para almacenar ficheros en un servidor. Las solicitudes de tipo PUT son mucho más simples que las cargas de ficheros utilizando el tipo POST, y se parecen a:

```php
PUT /path/filename.html HTTP/1.1

    
```

Normalmente, esto significa que el servidor remoto guardará los datos que siguen en el fichero: `/path/filename.html` de su disco. Esto no es, por supuesto, muy seguro permitir que Apache o PHP sobrescriban cualquier fichero de la arborescencia. Para evitar esto, primero se debe indicar al servidor que se desea que un script PHP dado gestione la solicitud. Con Apache, hay una directiva para ello: *Script*. Puede ser colocada en cualquier lugar del fichero de configuración de Apache. En general, los webmasters la colocan en el bloque `<Directory>`, o tal vez en el bloque `<VirtualHost>`. La siguiente línea hará muy bien el trabajo:

    Script PUT /put.php

Indica a Apache que debe enviar las solicitudes de carga por método PUT al script `put.php`. Por supuesto, esto presupone que se ha activado PHP para que maneje los ficheros de tipo `.php`, y que PHP está activo. El recurso de destino para todas las solicitudes PUT de este script debe ser el script mismo, y no el nombre del fichero que el fichero cargado debe tener.

Con PHP, se querría hacer algo como lo siguiente en su put.php. Esto copiará el contenido del fichero cargado en el fichero `myputfile.ext` en el servidor. Probablemente se querrá realizar algunas verificaciones y/o identificar al usuario antes de realizar esta copia de fichero.

Guardado de ficheros HTTP PUT

```php
<?php
/* Los datos PUT llegan del flujo */
$putdata = fopen("php://input", "r");

/* Abre un fichero para escritura */
$fp = fopen("myputfile.ext", "w");

/* Lectura de los datos, 1 Ko a la vez y escritura en el fichero */
while ($data = fread($putdata, 1024))
fwrite($fp, $data);

/* Cierre del flujo */
fclose($fp);
fclose($putdata);
?>

    
```

## Véase también

[Seguridad de los ficheros](#security.filesystem)
