---
title: RarArchive::open
description: Abre un archivo RAR
source_url: https://www.php.net/manual/es/rararchive.open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rar/rararchive/open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rar
translation_status: ready
translation_revision: ee741f54f
order: 68460
---

RarArchive::open

rar_open

Abre un archivo RAR

## Descripción

Estilo orientado a objetos (método):

```php
public static RarArchive::open(string $filename, [string $password], [callable $volume_callback]): RarArchive
```php

Estilo procedimental:

```php
rar_open(string $filename, [string $password], [callable $volume_callback]): RarArchive
```

Abre un archivo RAR especificado y devuelve la instancia `RarArchive` que lo representa.

> [!NOTE]
> Si el archivo a abrir esta dividido en volúmenes, se deberá pasar la ruta del primer volúmen como parámetro de la función. De lo contrario, no todos los archivos se mostraran.

## Parámetros

`filename`  
Ruta del archivo Rar.

`password`  
Contraseña en texto plano, si fuera necesario descifrar la cabecera del archivo. También se utilizará por defecto si hay archivos encriptados encontrados. Tenga en cuenta que los archivos pueden poseer diferentes contraseñas en cuanto a las cabeceras y entre ellos.

`volume_callback`  
Una función que recibe como parámetro la ruta del volúmen que no fue encontrado y retorna una cadena con la ruta correcta para dicho archivo o `null` si el volúmen no existe o no es conocido. El programador debería asegurar que la función pasada no cause bucles, ya que esta función es llamada repetidas veces si la ruta devuelta en una llamada previa no corresponde con el volúmen solicitado. Especificando este parámetro se omite la notice que se emitiría cuando un volúmen no es encontrado; una implementación que solo devuelva `null` puede, por lo tanto, utilizarce para omitir dichos notices.

> [!WARNING]
> En versiones menores a 2.0.0 de PHP, ­esta función no manejaria rutas relativas correctamente. Use `realpath` como una solución.

## Valores devueltos

Devuelve una instancia del `RarArchive` solicitado o `false` si ocurre un error.

## Historial de cambios

| Versión        | Descripción                     |
|----------------|---------------------------------|
| PECL rar 3.0.0 | `volume_callback` fue agregada. |

## Ejemplos

Estilo orientado a objetos

```php
<?php
$rar_arch = RarArchive::open('encrypted_headers.rar', 'samplepassword');
if ($rar_arch === FALSE)
    die("Failed opening file");

$entries = $rar_arch->getEntries();
if ($entries === FALSE)
    die("Failed fetching entries");

echo "Found " . count($entries) . " files.\n";

if (empty($entries))
    die("No valid entries found.");

$stream = reset($entries)->getStream();
if ($stream === FALSE)
    die("Failed opening first file");

$rar_arch->close();

echo "Content of first one follows:\n";
echo stream_get_contents($stream);

fclose($stream);
?>

   
```

Resultado del ejemplo anterior es similar a:

    Found 2 files.
    Content of first one follows:
    Encrypted file 1 contents.

Estilo procedimental

```php
<?php
$rar_arch = rar_open('encrypted_headers.rar', 'samplepassword');
if ($rar_arch === FALSE)
    die("Failed opening file");

$entries = rar_list($rar_arch);
if ($entries === FALSE)
    die("Failed fetching entries");

echo "Found " . count($entries) . " files.\n";

if (empty($entries))
    die("No valid entries found.");

$stream = reset($entries)->getStream();
if ($stream === FALSE)
    die("Failed opening first file");

rar_close($rar_arch);

echo "Content of first one follows:\n";
echo stream_get_contents($stream);

fclose($stream);
?>

   
```

Volume Callback

```php
<?php
/* En este ejemplo, hay un volúmen llamdo multi_broken.part1.rar
 * cuyo próximo volúmen es llamado multi.part2.rar */
function resolve($vol) {
    if (preg_match('/_broken/', $vol))
        return str_replace('_broken', '', $vol);
    else
        return null;
}
$rar_file1 = rar_open(dirname(__FILE__).'/multi_broken.part1.rar', null, 'resolve');
$entry = $rar_file1->getEntry('file2.txt');
$entry->extract(null, dirname(__FILE__) . "/temp_file2.txt");
?>

   
```

## Véase también

rar://

wrapper
