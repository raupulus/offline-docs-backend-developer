---
title: mcrypt_module_open
description: Abre el módulo del algoritmo y del modo a utilizar
source_url: https://www.php.net/manual/es/function.mcrypt-module-open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mcrypt-module-open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 45990
---

mcrypt_module_open

Abre el módulo del algoritmo y del modo a utilizar

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
mcrypt_module_open(string $algorithm, string $algorithm_directory, string $mode, string $mode_directory): resource
```php

`mcrypt_module_open` abre el módulo del algoritmo y del modo a utilizar. El nombre del algoritmo se especifica mediante el parámetro `algorithm` (por ejemplo: `"twofish"`), o bien una de las constantes `MCRYPT_ciphername`. La biblioteca se cierra al llamar a `mcrypt_module_close`.

## Parámetros

`algorithm`  
Una de las constantes `MCRYPT_ciphername`, o el nombre del algoritmo como cadena.

`algorithm_directory`  
El parámetro `algorithm_directory` se utiliza para localizar el módulo de cifrado. Cuando se especifica un nombre de directorio, se utilizará. Si se especifica una cadena vacía (`""`), se utilizará el valor definido en la directiva `mcrypt.algorithms_dir` del fichero `php.ini`. Cuando no está definida, el directorio por omisión utilizado será aquel en el que se encuentre la biblioteca libmcrypt (habitualmente, `/usr/local/lib/libmcrypt`).

`mode`  
Una de las constantes `MCRYPT_MODE_modename`, o una de las siguientes cadenas: "ecb", "cbc", "cfb", "ofb", "nofb" o "stream".

`mode_directory`  
El parámetro `mode_directory` se utiliza para localizar el módulo de cifrado. Si se especifica un nombre de directorio, se utilizará. Cuando se especifica una cadena vacía (`""`), se utilizará el valor de la directiva `mcrypt.modes_dir` del fichero `php.ini`. Si no está definida, el directorio por omisión utilizado será aquel en el que se encuentre la biblioteca libmcrypt (habitualmente `/usr/local/lib/libmcrypt`).

## Valores devueltos

Normalmente, esta función devuelve un descriptor de cifrado, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `mcrypt_module_open`

```
<?php
$td = mcrypt_module_open(MCRYPT_DES, '',
    MCRYPT_MODE_ECB, '/usr/lib/mcrypt-modes');

$td = mcrypt_module_open('rijndael-256', '', 'ofb', '');
?>

   
```php

La primera línea del ejemplo anterior intentará abrir el cifrado `DES`, en el directorio por omisión, y el modo `ECB` en el directorio `/usr/lib/mcrypt-modes`. El segundo ejemplo utiliza las cadenas como nombre para el cifrado y el modo. Esto solo funciona si la extensión está compilada con libmcrypt 2.4.x o 2.5.x.

Utilización de `mcrypt_module_open` para cifrar

```
<?php
/* Carga un cifrado */
$td = mcrypt_module_open('rijndael-256', '', 'ofb', '');

/* Crea el VI y determina el tamaño de la clave */
$iv = mcrypt_create_iv(mcrypt_enc_get_iv_size($td), MCRYPT_DEV_RANDOM);
$ks = mcrypt_enc_get_key_size($td);

/* Crea la clave (ejemplo únicamente: MD5 no es un buen algoritmo de hash para esto) */
$key = substr(hash('md5', 'very secret key'), 0, $ks);

/* Inicializa el cifrado */
mcrypt_generic_init($td, $key, $iv);

/* Cifra los datos */
$encrypted = mcrypt_generic($td, 'This is very important data');

/* Libera el gestor de cifrado */
mcrypt_generic_deinit($td);

/* Inicializa el módulo de cifrado para el descifrado */
mcrypt_generic_init($td, $key, $iv);

/* Descifra los datos */
$decrypted = mdecrypt_generic($td, $encrypted);

/* Libera el gestor de descifrado y cierra el módulo */
mcrypt_generic_deinit($td);
mcrypt_module_close($td);

/* Muestra la cadena */
echo trim($decrypted)."\n";
?>

   
```php

## Véase también

mcrypt_module_close

mcrypt_generic

mdecrypt_generic

mcrypt_generic_init

mcrypt_generic_deinit
