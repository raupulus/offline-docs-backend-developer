---
title: proc_open
description: Ejecuta un comando y abre los punteros de ficheros para las entradas
  / salidas
source_url: https://www.php.net/manual/es/function.proc-open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/exec/functions/proc-open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: exec
translation_status: ready
translation_reviewed: false
translation_revision: f50098447
order: 20600
---

proc_open

Ejecuta un comando y abre los punteros de ficheros para las entradas / salidas

## Descripción

```php
proc_open(array $command, array $descriptor_spec, array $pipes, [string $cwd], [array $env_vars], [array $options]): resource
```php

`proc_open` es similar a `popen` pero proporciona un mayor grado de control sobre la ejecución del programa.

## Parámetros

`command`  
El comando a ejecutar como `string`. Los caracteres especiales deben ser escapados correctamente, y una aplicación correcta de las comillas debe ser aplicada.

> [!NOTE]
> En *Windows*, a menos que `bypass_shell` esté definida a `true` en `options`, `command` es pasado a `cmd.exe` (en realidad, `%ComSpec%`) con el flag `/c` como un `string` *sin comillas* (es decir, exactamente como fue proporcionado a `proc_open`). Esto puede causar `cmd.exe` para eliminar las comillas que rodean `command` (para más detalles ver la documentación de `cmd.exe`), resultando en un comportamiento inesperado, y potencialmente peligroso, ya que los mensajes de error de `cmd.exe` pueden contener (una parte de) la `command` pasada (ver ejemplo a continuación).

A partir de PHP 7.4.0, `command` puede ser pasado como un `array` de argumentos de comandos. En este caso el proceso será abierto directamente (sin pasar por un shell) y PHP se encargará de escapar los argumentos necesarios.

> [!NOTE]
> En Windows, el escape de los argumentos de los elementos del `array` asume que el procesamiento de la línea de comandos del comando ejecutado es compatible con el procesamiento de argumentos de línea de comandos realizado por el runtime VC.

`descriptor_spec`  
Un array indexado, donde las claves representan el número de descriptor y el valor el método con el cual PHP pasará este descriptor al proceso hijo. 0 es stdin, 1 es stdout, y 2 es stderr.

Cada elemento puede ser: Un array que describe el pipe a pasar al proceso. El primer elemento es el tipo del descriptor y los elementos siguientes son opciones para el tipo dado. Los tipos válidos son `pipe` (el segundo elemento es `r` para pasar el extremo de lectura del pipe al proceso, o `w` para pasar el extremo de escritura) y `file` (el segundo elemento es el nombre de fichero, y el tercer elemento es el modo de apertura del fichero, igual que `fopen`). Se debe notar que cualquier otro elemento diferente de `w` es tratado como `r`., Un recurso de flujo que representa un descriptor de fichero (por ejemplo, un fichero abierto, un socket, o bien `STDIN`).

Los números de punteros de ficheros no están limitados a 0, 1 y 2 - se puede especificar cualquier número de descriptor válido, y será pasado al proceso hijo. Esto permitirá que su script interactúe con otros scripts, y que sea ejecutado como "co-proceso". En particular, es muy práctico para pasar contraseñas a programas como PGP, GPG y openssl, con un método muy protegido. También es práctico para leer información de estado proporcionada por estos programas, en descriptores auxiliares.

`pipes`  
Debe ser definido como un array indexado de punteros de ficheros que corresponden al extremo de cualquier descriptor PHP que sean creados.

`cwd`  
El directorio inicial de trabajo del comando. Esto debe ser una ruta **absoluta** al directorio o `null` si se quiere utilizar el valor por omisión (el directorio de trabajo del proceso PHP actual)

`env_vars`  
Un array que contiene las variables de entorno para el comando que debe ser ejecutado, o `null` para utilizar el mismo entorno que el proceso PHP actual

`options`  
Permite especificar opciones adicionales. Las opciones actualmente soportadas son: `suppress_errors` (solo Windows): supresión de errores generados por esta función cuando está definida a `true`, `bypass_shell` (solo Windows): omisión del shell `cmd.exe` cuando está definida a `true`, `blocking_pipes` (solo Windows): fuerza los pipes bloqueantes cuando está definida a `true`, `create_process_group` (solo Windows): permite al proceso hijo manejar los eventos `CTRL` cuando está a `true`, `create_new_console` (solo Windows): el nuevo proceso tiene una nueva consola, en lugar de heredar la consola de su padre.

## Valores devueltos

Retorna un recurso que representa el proceso, que podrá ser utilizado por la función `proc_close` cuando ya no sea necesario. En caso de fallo, `false` será retornado.

## Errores/Excepciones

A partir de PHP 8.3.0, se lanza una excepción ValueError si `command` es un array sin al menos un elemento no vacío.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Se lanzará una excepción ValueError si `command` es un array sin al menos un elemento no vacío. |
| 7.4.4 | Se añadió la opción `create_new_console` al parámetro `options`. |
| 7.4.0 | `proc_open` ahora acepta un `array` para `command`. |
| 7.4.0 | Se añadió la opción `create_process_group` al parámetro `options`. |

## Ejemplos

Ejemplo con `proc_open`

```
<?php
$descriptorspec = array(
   0 => array("pipe", "r"),  // stdin es un pipe donde el proceso leerá
   1 => array("pipe", "w"),  // stdout es un pipe donde el proceso escribirá
   2 => array("file", "/tmp/error-output.txt", "a") // stderr es un fichero
);

$cwd = '/tmp';
$env = array('some_option' => 'aeiou');

$process = proc_open('php', $descriptorspec, $pipes, $cwd, $env);

if (is_resource($process)) {
    // $pipes se parece a:
    // 0 => fichero accesible en escritura, conectado a la entrada estándar del proceso hijo
    // 1 => fichero accesible en lectura, conectado a la salida estándar del proceso hijo
    // Cualquier error será añadido al fichero /tmp/error-output.txt

    fwrite($pipes[0], '<?php print_r($_ENV); ?>');
    fclose($pipes[0]);

    echo stream_get_contents($pipes[1]);
    fclose($pipes[1]);

    // Es importante que cierre los pipes antes de llamar
    // a proc_close para evitar un bloqueo.
    $return_value = proc_close($process);

    echo "El comando retornó $return_value\n";
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [some_option] => aeiou
        [PWD] => /tmp
        [SHLVL] => 1
        [_] => /usr/local/bin/php
    )
    El comando retornó 0

Comportamiento extraño de `proc_open` en Windows

Aunque se podría esperar que el siguiente programa busque el fichero `filename.txt` para el texto `search` y muestre los resultados, se comporta de manera diferente.

```
<?php
$descriptorspec = [STDIN, STDOUT, STDOUT];
$cmd = '"findstr" "search" "filename.txt"';
$proc = proc_open($cmd, $descriptorspec, $pipes);
proc_close($proc);
?>

    
```php

El ejemplo anterior mostrará:

    'findstr" "search" "filename.txt' no se reconoce como un comando interno o externo,
    programa ejecutable o archivo por lotes.

        

Para evitar este comportamiento, generalmente es suficiente rodear `command` con comillas adicionales:

```
$cmd = '""findstr" "search" "filename.txt""';

    
```php

## Notas

> [!NOTE]
> Compatibilidad Windows: los descriptores más allá de 2 (stderr) son accesibles al proceso hijo, en forma de punteros heredados, pero como la arquitectura Windows no asocia números a los descriptores de bajo nivel, el proceso hijo no tiene, actualmente, ningún medio para acceder a ellos. Por otro lado, stdin, stdout y stderr funcionan como de costumbre.

> [!NOTE]
> Si solo se necesita un proceso unidireccional, `popen` será más práctico, ya que es más sencillo de utilizar.

## Véase también

`popen`, `exec`, `system`, `passthru`, `stream_select`, [Las comillas invertidas](#language.operators.execution)
