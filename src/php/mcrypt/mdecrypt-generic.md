---
title: mdecrypt_generic
description: Desencripta los datos
source_url: https://www.php.net/manual/es/function.mdecrypt-generic.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mdecrypt-generic.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 46010
---

mdecrypt_generic

Desencripta los datos

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
mdecrypt_generic(resource $td, string $data): string
```php

Desencripta los datos `data`. Tenga en cuenta que la longitud del string desencriptado puede ser más larga que el string original, ya que puede haber sido completado con caracteres.

## Parámetros

`td`  
Un descriptor de cifrado, devuelto por la función `mcrypt_module_open`

`data`  
Los datos cifrados.

## Valores devueltos

Devuelve el string desencriptado.

## Ejemplos

Ejemplo con `mdecrypt_generic`

```
<?php
/* Datos */
$key = 'Esta es una clave de cifrado muy larga, incluso demasiado larga';
$plain_text = 'Estos son datos importantes';

/* Abre el módulo y crea un VI */
$td = mcrypt_module_open('des', '', 'ecb', '');
$key = substr($key, 0, mcrypt_enc_get_key_size($td));
$iv_size = mcrypt_enc_get_iv_size($td);
$iv = mcrypt_create_iv($iv_size, MCRYPT_RAND);

/* Inicializa el módulo de cifrado */
if (mcrypt_generic_init($td, $key, $iv) != -1) {

    /* Cifra los datos */
    $c_t = mcrypt_generic($td, $plain_text);
    mcrypt_generic_deinit($td);

    /* Reinicia los buffers para el descifrado */
    mcrypt_generic_init($td, $key, $iv);
    $p_t = mdecrypt_generic($td, $c_t);

    /* Limpia */
    mcrypt_generic_deinit($td);
    mcrypt_module_close($td);
}

if (strncmp($p_t, $plain_text, strlen($plain_text)) == 0) {
    echo "ok\n";
} else {
    echo "error\n";
}
?>

   
```php

El ejemplo anterior muestra cómo verificar que los datos antes del cifrado son los mismos que después del cifrado/descifrado. Es muy importante reiniciar el buffer de cifrado con `mcrypt_generic_init` antes de descifrar los datos.

El gestor de descifrado debe ser siempre inicializado por la función `mcrypt_generic_init` con una clave y un VI antes de llamar a esta función. Cuando el cifrado está hecho, es necesario liberar los datos cifrados llamando a `mcrypt_generic_deinit`. Consulte `mcrypt_module_open` para un ejemplo.

## Véase también

mcrypt_generic

mcrypt_generic_init

mcrypt_generic_deinit
