---
title: streamWrapper::dir_readdir
description: Lee un archivo en un directorio
source_url: https://www.php.net/manual/es/streamwrapper.dir-readdir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/streamwrapper/dir-readdir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: true
translation_revision: 525aa5f19
order: 88350
---

streamWrapper::dir_readdir

Lee un archivo en un directorio

## Descripción

```php
public streamWrapper::dir_readdir(): string
```php

Este método se llama en respuesta a `readdir`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Debe devolver una `string` que representa el próximo nombre de archivo, o `false` si no hay más archivos.

> [!WARNING]
> Devolver `true` o `false` tendrá el mismo efecto de señalar que no hay un siguiente fichero. Sin embargo, devolver `true` está desaconsejado y `false` debe ser utilizado para señalar esta condición en su lugar.

> [!NOTE]
> Un valor de retorno no booleano se convertirá en `string`.

## Errores/Excepciones

Emite una advertencia `E_WARNING` si la llamada a este método falla (i.e. no implementado).

## Ejemplos

Lista de archivos de un archivo tar

```
<?php
class streamWrapper {
    protected $fp;

    public function dir_opendir($path, $options) {
        $url = parse_url($path);

        $path = $url["host"] . $url["path"];

        if (!is_readable($path)) {
            trigger_error("$path no es legible para mí", E_USER_NOTICE);
            return false;
        }
        if (!is_file($path)) {
            trigger_error("$path no es un archivo", E_USER_NOTICE);
            return false;
        }

        $this->fp = fopen($path, "rb");
        return true;
    }

    public function dir_readdir() {
        // Extrae el encabezado para esta entrada
        $header      = fread($this->fp, 512);
        $data = unpack("a100filename/a8mode/a8uid/a8gid/a12size/a12mtime/a8checksum/a1filetype/a100link/a100linkedfile", $header);

        // Recorta el nombre del archivo y el tamaño del archivo
        $filename    = trim($data["filename"]);

        // No hay archivo, estamos al final del archivo
        if (!$filename) {
            return false;
        }

        $octal_bytes = trim($data["size"]);
        // El tamaño del archivo está definido en octetos
        $bytes       = octdec($octal_bytes);

        // tar redondea los tamaños de archivos al múltiplo de 512 siguiente
        $rest        = $bytes % 512;
        if ($rest > 0) {
            $bytes      += 512 - $rest;
        }

        // Lectura del archivo
        fseek($this->fp, $bytes, SEEK_CUR);

        return $filename;
    }

    public function dir_closedir() {
        return fclose($this->fp);
    }

    public function dir_rewinddir() {
        return fseek($this->fp, 0, SEEK_SET);
    }
}

stream_wrapper_register("tar", "streamWrapper");
$handle = opendir("tar://example.tar");
while (false !== ($file = readdir($handle))) {
    var_dump($file);
}

echo "Reinicio...\n";
rewind($handle);
var_dump(readdir($handle));

closedir($handle);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    string(13) "construct.xml"
    string(16) "dir-closedir.xml"
    string(15) "dir-opendir.xml"
    string(15) "dir-readdir.xml"
    string(17) "dir-rewinddir.xml"
    string(9) "mkdir.xml"
    string(10) "rename.xml"
    string(9) "rmdir.xml"
    string(15) "stream-cast.xml"
    string(16) "stream-close.xml"
    string(14) "stream-eof.xml"
    string(16) "stream-flush.xml"
    string(15) "stream-lock.xml"
    string(15) "stream-open.xml"
    string(15) "stream-read.xml"
    string(15) "stream-seek.xml"
    string(21) "stream-set-option.xml"
    string(15) "stream-stat.xml"
    string(15) "stream-tell.xml"
    string(16) "stream-write.xml"
    string(10) "unlink.xml"
    string(12) "url-stat.xml"
    Reinicio...
    string(13) "construct.xml"

## Véase también

`readdir`
