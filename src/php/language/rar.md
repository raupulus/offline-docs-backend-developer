---
title: rar://
description: RAR
source_url: https://www.php.net/manual/es/wrappers.rar.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/wrappers/rar.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 8bc832a46
order: 4700
---

rar://

RAR

## Descripción

Esta envoltura toma la ruta codificada URL hacia el archivo RAR (relativo o absoluto), luego, opcionalmente, un asterisco (`*`), opcionalmente seguido de un signo de número (`#`), y, siempre opcionalmente, un nombre de entrada codificado URL, tal como se almacena en el archivo. La especificación de un nombre de entrada requiere la presencia del signo de número; la presencia de una barra al inicio del nombre de la entrada es opcional.

Esta envoltura puede abrir tanto ficheros como directorios. Al abrir directorios, el asterisco fuerza a que los nombres de los directorios sean devueltos sin codificar. Si no se especifica, serán devueltos en forma codificada URL - esto permite que la envoltura sea utilizada correctamente con funcionalidades internas como `RecursiveDirectoryIterator` en presencia de nombres de ficheros que parecen estar codificados URL.

Si el signo de número y el nombre de la entrada no están incluidos, se mostrará la raíz del archivo. Esta visualización es diferente de los directorios regulares en el sentido de que el flujo resultante no contendrá información como la fecha y hora de modificación, ya que la raíz del directorio no se almacena como una entrada individual en el archivo. El uso de esta envoltura con `RecursiveDirectoryIterator` requiere la presencia del signo de número en la URL al acceder a la raíz, para construir correctamente las URLs de los hijos.

> [!NOTE]
> Para utilizar la envoltura `rar://`, la extensión [rar](https://pecl.php.net/package/rar) disponible en [PECL](https://pecl.php.net/) debe estar instalada.

`rar://` está disponible a partir de PECL rar 3.0.0

## Uso

- `rar://<nombre de archivo codificado URL>[*][#<nombre de entrada codificado URL>]]`

## Opciones

| Atributo                                                    | Soportado |
|-------------------------------------------------------------|-----------|
| Restringido por [allow_url_fopen](#ini.allow-url-fopen)     | No        |
| Restringido por [allow_url_include](#ini.allow-url-include) | No        |
| Permite la lectura                                          | Sí        |
| Permite la escritura                                        | No        |
| Permite la adición                                          | No        |
| Permite la lectura y escritura simultáneamente              | No        |
| Soporte de la función `stat`                                | Sí        |
| Soporte de la función `unlink`                              | No        |
| Soporte de la función `rename`                              | No        |
| Soporte de la función `mkdir`                               | No        |
| Soporte de la función `rmdir`                               | No        |

Resumen de la envoltura {role="stream_wrapper"}

| Nombre | Uso | Por omisión |
|----|----|----|
| `open_password` | La contraseña utilizada para cifrar los encabezados del archivo, si los hay. WinRAR cifrará todos los ficheros con la misma contraseña que los encabezados cuando esta esté presente, por lo tanto, para archivos con encabezados cifrados, `file_password` será ignorado. |  |
| `file_password` | La contraseña utilizada para cifrar un fichero, si la hay. Si los encabezados también están cifrados, esta opción será ignorada y se privilegiará la contraseña de la opción `open_password`. La razón por la que hay 2 opciones es el deseo de poder cubrir la posibilidad de soportar archivos con diferentes contraseñas para los encabezados y los ficheros. Tenga en cuenta que si el encabezado del archivo no está cifrado, la opción `open_password` será ignorada y esta opción debe ser utilizada en su lugar. |  |
| `volume_callback` | Una función de devolución de llamada para determinar la ruta de los volúmenes faltantes. Consulte el método RarArchive::open para obtener más información. |  |

Opciones de contexto {role="stream_wrapper"}

## Ejemplos

Recorrido de un archivo RAR

```php
<?php

class MyRecDirIt extends RecursiveDirectoryIterator {
    function current() {
        return rawurldecode($this->getSubPathName()) .
            (is_dir(parent::current())?" [DIR]":"");
    }
}

$f = "rar://" . rawurlencode(dirname(__FILE__)) .
    DIRECTORY_SEPARATOR . 'dirs_and_extra_headers.rar#';

$it = new RecursiveTreeIterator(new MyRecDirIt($f));

foreach ($it as $s) {
    echo $s, "\n";
}
?>

   
```

Resultado del ejemplo anterior es similar a:

    |-allow_everyone_ni [DIR]
    |-file1.txt
    |-file2_אּ.txt
    |-with_streams.txt
    \-אּ [DIR]
      |-אּ\%2Fempty%2E [DIR]
      | \-אּ\%2Fempty%2E\file7.txt
      |-אּ\empty [DIR]
      |-אּ\file3.txt
      |-אּ\file4_אּ.txt
      \-אּ\אּ_2 [DIR]
        |-אּ\אּ_2\file5.txt
        \-אּ\אּ_2\file6_אּ.txt

Apertura de un fichero cifrado (encabezado cifrado)

```php
<?php
$stream = fopen("rar://" .
    rawurlencode(dirname(__FILE__)) . DIRECTORY_SEPARATOR .
    'encrypted_headers.rar' . '#encfile1.txt', "r", false,
    stream_context_create(
        array(
            'rar' =>
                array(
                    'open_password' => 'samplepassword'
                )
            )
        )
    );
var_dump(stream_get_contents($stream));
/* Las fechas de creación y último acceso son opcionales con WinRAR,
 * lo que explica que la mayoría de los ficheros no las tengan */
var_dump(fstat($stream));
?>

   
```

Resultado del ejemplo anterior es similar a:

    string(26) "Encrypted file 1 contents."
    Array
    (
        [0] => 0
        [1] => 0
        [2] => 33206
        [3] => 1
        [4] => 0
        [5] => 0
        [6] => 0
        [7] => 26
        [8] => 0
        [9] => 1259550052
        [10] => 0
        [11] => -1
        [12] => -1
        [dev] => 0
        [ino] => 0
        [mode] => 33206
        [nlink] => 1
        [uid] => 0
        [gid] => 0
        [rdev] => 0
        [size] => 26
        [atime] => 0
        [mtime] => 1259550052
        [ctime] => 0
        [blksize] => -1
        [blocks] => -1
    )
