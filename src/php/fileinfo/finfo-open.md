---
title: finfo_open
description: Crea una nueva instancia finfo
source_url: https://www.php.net/manual/es/function.finfo-open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fileinfo/functions/finfo-open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fileinfo
translation_status: ready
translation_reviewed: false
translation_revision: 82ddd2ec8
order: 23220
---

finfo_open

finfo::\_\_construct

Crea una nueva instancia finfo

## Descripción

Estilo procedimental

```php
finfo_open([int $flags], [string $magic_database]): finfo
```php

Estilo orientado a objetos (constructor):

```php
public finfo::__construct([int $flags], [string $magic_database])
```

Esta función abre una base de datos mágica y devuelve su instancia.

## Parámetros

`flags`  
Una o una unión de varias [constantes Fileinfo](#fileinfo.constants).

`magic_database`  
Nombre de fichero de una base de datos mágica, normalmente algo como `/path/to/magic.mime`. Si no se especifica, se utiliza la variable de entorno `MAGIC`. Si la variable de entorno no está definida, se utilizará la base de datos mágica integrada en PHP.

Pasar `null` o un `string` vacío equivale a utilizar el valor por omisión.

## Valores devueltos

(Únicamente en modo procedimental) Devuelve una instancia de `finfo` en caso de éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Ahora devuelve una instancia de `finfo` ; anteriormente, se esperaba una `resource`. |
| 8.0.3 | `magic_database` ahora es nullable. |

## Ejemplos

Estilo orientado a objetos

```php
<?php
$finfo = new finfo(FILEINFO_MIME, "/usr/share/misc/magic"); // Devuelve el tipo mime

/* Obtiene el mime-type de un fichero específico */
$filename = "/usr/local/something.txt";
echo $finfo->file($filename);

?>

   
```

Estilo procedimental

```php
<?php
$finfo = finfo_open(FILEINFO_MIME, "/usr/share/misc/magic"); // Devuelve el tipo mime

if (!$finfo) {
    echo "Fallo al abrir la base de datos fileinfo";
    exit();
}

/* Obtiene el mime-type de un fichero específico */
$filename = "/usr/local/something.txt";
echo finfo_file($finfo, $filename);

/* Cierre de la conexión */
finfo_close($finfo);
?>

   
```

El ejemplo anterior mostrará:

    text/plain; charset=us-ascii

      

## Notas

> [!NOTE]
> Generalmente, el uso de la base de datos mágica integrada (dejando las variables de entorno `magic_database` y `MAGIC` no definidas) es la mejor solución a menos que se necesite una base de datos mágica específica.

## Véase también

finfo_close
