---
title: parse_ini_file
description: Analiza un archivo de configuración
source_url: https://www.php.net/manual/es/function.parse-ini-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/parse-ini-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_revision: bb54309ef
order: 23890
---

parse_ini_file

Analiza un archivo de configuración

## Descripción

```php
parse_ini_file(string $filename, [bool $process_sections], [int $scanner_mode]): array
```php

`parse_ini_file` carga el archivo `filename` y devuelve las configuraciones que contiene como un array asociativo.

La estructura de los archivos de configuración leídos es similar a la de `php.ini`.

> [!WARNING]
> Esta función no debe ser utilizada con entradas no confiables, a menos que `scanner_mode` sea `INI_SCANNER_RAW`, ya que la salida analizada podría contener los valores de constantes sensibles, como constantes que contienen una contraseña de base de datos.

## Parámetros

`filename`  
El nombre del archivo de configuración a analizar. Si se utiliza una ruta relativa, se evalúa relativa a la carpeta actual, luego según el [include_path](#ini.include-path).

`process_sections`  
Al pasar el argumento `process_sections` a `true`, se obtendrá un array multidimensional con los nombres de las secciones. El valor por omisión de este argumento es `false`

`scanner_mode`  
Puede ser `INI_SCANNER_NORMAL` (por omisión) o `INI_SCANNER_RAW`. Si se proporciona `INI_SCANNER_RAW`, entonces los valores en opción no serán analizados.

A partir de PHP 5.6.1 también puede ser especificado como `INI_SCANNER_TYPED`. En este modo los booleanos, null y enteros son preservados tanto como sea posible. Las cadenas de caracteres `"true"`, `"on"` y `"yes"` son convertidas a `true`. `"false"`, `"off"`, `"no"` y `"none"` son considerados como `false`. `"null"` es convertido a `null` en este modo. Además todas las cadenas de caracteres numéricas son convertidas a entero si es posible.

## Valores devueltos

La configuración se devuelve en forma de un array asociativo en caso de éxito, y `false` si ocurre un error.

## Ejemplos

Contenido del archivo `sample.ini`

    ; Este es un archivo de configuración
    ; Los comentarios comienzan con ';', como en php.ini

    [first_section]
    one = 1
    five = 5
    animal = BIRD

    [second_section]
    path = "/usr/local/bin"
    URL = "http://www.example.com/~username"

    [third_section]
    phpversion[] = "5.0"
    phpversion[] = "5.1"
    phpversion[] = "5.2"
    phpversion[] = "5.3"

    urls[svn] = "http://svn.php.net"
    urls[git] = "http://git.php.net"

Ejemplo con `parse_ini_file`

Las [constantes](#language.constants) (pero no las "constantes mágicas" como `__FILE__`) también pueden ser utilizadas en el archivo .ini, por lo que si se define una constante antes de ejecutar `parse_ini_file`, será integrada en los resultados. Solo se evalúan los valores de configuración, y el valor debe ser simplemente la constante. Por ejemplo:

```
<?php

define('BIRD', 'Dodo bird');

// Análisis sin secciones
$ini_array = parse_ini_file("sample.ini");
print_r($ini_array);

// Análisis con secciones
$ini_array = parse_ini_file("sample.ini", true);
print_r($ini_array);

?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [one] => 1
        [five] => 5
        [animal] => Dodo bird
        [path] => /usr/local/bin
        [URL] => http://www.example.com/~username
        [phpversion] => Array
            (
                [0] => 5.0
                [1] => 5.1
                [2] => 5.2
                [3] => 5.3
            )

        [urls] => Array
            (
                [svn] => http://svn.php.net
                [git] => http://git.php.net
            )

    )
    Array
    (
        [first_section] => Array
            (
                [one] => 1
                [five] => 5
                [animal] => Dodo bird
            )

        [second_section] => Array
            (
                [path] => /usr/local/bin
                [URL] => http://www.example.com/~username
            )

        [third_section] => Array
            (
                [phpversion] => Array
                    (
                        [0] => 5.0
                        [1] => 5.1
                        [2] => 5.2
                        [3] => 5.3
                    )
                [urls] => Array
                    (
                        [svn] => http://svn.php.net
                        [git] => http://git.php.net
                    )

    )

`parse_ini_file` para analizar un archivo php.ini

```
<?php
// Una función simple para comparar los resultados a continuación
function yesno($expression)
{
    return($expression ? 'Yes' : 'No');
}

// Lee la ruta del php.ini utilizando php_ini_loaded_file()
$ini_path = php_ini_loaded_file();

// Análisis de php.ini
$ini = parse_ini_file($ini_path);

// Visualización y comparativo de los valores. Observe que get_cfg_var()
// dará los mismos resultados entre los resultados analizados y cargados
echo '(analizado) magic_quotes_gpc = ' . yesno($ini['magic_quotes_gpc']) . PHP_EOL;
echo '(cargado ) magic_quotes_gpc = ' . yesno(get_cfg_var('magic_quotes_gpc')) . PHP_EOL;
?>

    
```php

Resultado del ejemplo anterior es similar a:

    (analizado) magic_quotes_gpc = Yes
    (cargado ) magic_quotes_gpc = Yes

Interpolación de Valor

Además de evaluar las constantes, ciertos caracteres tienen un significado particular en un valor ini. Adicionalmente, las variables de entorno y opciones de configuración definidas previamente (ver `get_cfg_var`) pueden ser leídas utilizando la sintaxis `${}`.

    ; | se utiliza para OR a nivel de bits
    three = 2|3

    ; & se utiliza para AND a nivel de bits
    four = 6&5

    ; ^ se utiliza para XOR a nivel de bits
    five = 3^6

    ; ~ se utiliza para negación a nivel de bits
    negative_two = ~1

    ; () se utiliza para agrupación
    seven = (8|7)&(6|5)

    ; Interpolar la variable de entorno PATH
    path = ${PATH}

    ; Interpolar la opción de configuración 'memory_limit'
    configured_memory_limit = ${memory_limit}

Escapar Caracteres

Ciertos caracteres tienen un significado particular en las cadenas entre comillas dobles y deben ser escapados prefijándolos con un backslash. Primero, son las comillas dobles `"` como marcador de frontera, y el backslash `\` mismo (si está seguido de uno de los caracteres especiales):

    quoted = "She said \"Exactly my point\"." ; Resultados en una cadena con marcas de comillas en ella.
    hint = "Use \\\" to escape double quote" ; Resultados en: Use \" to escape double quote

        

Hay una excepción para las rutas estilo Windows: es posible no escapar el backslash final si la cadena citada es seguida directamente por un retorno de línea:

    save_path = "C:\Temp\"

        

Si se debe escapar una comilla doble seguida de un retorno de línea en un valor multilínea, es posible utilizar la concatenación de valor de la siguiente manera (hay una cadena de comillas dobles seguida directamente de otra):

    long_text = "Lorem \"ipsum\"""
     dolor" ; Resultados en: Lorem "ipsum"\n dolor

        

Otro carácter con un significado particular es `$` (el signo de dólar). Debe ser escapado si está seguido de una llave abierta:

    code = "\${test}"

        

El escape de caracteres no es soportado en el modo `INI_SCANNER_RAW` (en este modo todos los caracteres son tratados "tal cual").

Es de notar que el analizador INI no soporta las secuencias de escape estándar (`\n`, `\t`, etc.). Si es necesario, el resultado de `parse_ini_file` debe ser post-procesado con la función `stripcslashes`.

## Notas

> [!NOTE]
> Esta función no tiene nada que ver con el archivo `php.ini`. Este último ya ha sido procesado cuando se comienza a ejecutar el script. Esta función puede permitir leer sus propios archivos de configuración.

> [!NOTE]
> Si un valor del archivo ini contiene datos no-alfanuméricos, debe ser protegido colocándolo entre comillas dobles (").

> [!NOTE]
> Existen palabras reservadas que no deben ser utilizadas como claves en los archivos ini. Esto incluye: `null`, `yes`, `no`, `true`, `false`, `on` y `off`. Los valores `null`, `off`, `no` y `false` dan "" (cadena vacía). Los valores `on`, `yes` y `true` dan "1", a menos que se utilice el modo `INI_SCANNER_TYPED`. Los caracteres `?{}|&~!()^"` no deben ser utilizados en ninguna parte de la clave y tienen un significado especial en el valor.

> [!NOTE]
> Las entradas sin un signo igual serán ignoradas. Por ejemplo, "foo" será ignorado mientras que "bar =" será analizado y añadido con un valor vacío. Por ejemplo, MySQL tiene una opción de configuración "no-auto-rehash" en el archivo `my.cnf` que no toma valor, por lo tanto, será ignorada.

> [!NOTE]
> Los archivos ini son generalmente tratados como archivos de texto sin formato por los servidores web, y por lo tanto enviados al navegador si se solicita. Esto significa que para la seguridad, los archivos ini deben ser almacenados fuera de la raíz docroot, o reconfigurar el servidor web para no servirlos. El fracaso de realizar una de estas medidas puede introducir un riesgo de seguridad.

## Véase también

`parse_ini_string`
