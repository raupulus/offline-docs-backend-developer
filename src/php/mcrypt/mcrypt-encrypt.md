---
title: mcrypt_encrypt
description: Cifra un texto
source_url: https://www.php.net/manual/es/function.mcrypt-encrypt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mcrypt-encrypt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: false
translation_revision: e849a6c42
order: 45820
---

mcrypt_encrypt

Cifra un texto

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
mcrypt_encrypt(string $cipher, string $key, string $data, string $mode, [string $iv]): string
```php

`mcrypt_encrypt` cifra los datos y devuelve los datos cifrados.

## Parámetros

`cipher`  
Una de las constantes `MCRYPT_ciphername`, o el nombre del algoritmo como cadena.

`key`  
La clave con la que se cifrarán los datos. Si el tamaño de la clave proporcionada no es compatible con el cipher, la función emitirá una advertencia y devolverá `false`

`data`  
Los datos que se cifrarán, con el `cipher` y el `mode` indicado. Si el tamaño de los datos no es un múltiplo del tamaño de bloque, los datos se rellenarán con caracteres '`\0`', según sea necesario.

El texto cifrado devuelto puede ser más largo que el tamaño de los datos pasados como argumento a través de `data`.

`mode`  
Una de las constantes `MCRYPT_MODE_modename`, o una de las siguientes cadenas: "ecb", "cbc", "cfb", "ofb", "nofb" o "stream".

`iv`  
Utilizado para la inicialización en los modos CBC, CFB, OFB, y en algunos algoritmos en modo STREAM. Si el tamaño del IV proporcionado no es soportado por el modo de encadenamiento o no se proporcionó un IV, pero el modo de encadenamiento requiere uno, la función emitirá una advertencia y devolverá `false`.

## Valores devueltos

Devuelve los datos cifrados, como `string` o `false` si ocurre un error.

## Ejemplos

Ejemplo con `mcrypt_encrypt`

```
<?php
    # --- CIFRADO ---

    # la clave debería ser un binario aleatorio, utilice la función scrypt, bcrypt
    # o PBKDF2 para convertir una cadena de caracteres en una clave.
    # La clave se especifica utilizando notación hexadecimal.
    $key = pack('H*', "bcb04b7e103a0cd8b54763051cef08bc55abe029fdebae5e1d417e2ffb2a00a3");

    # Muestra el tamaño de la clave utilizada; claves de 16, 24 o 32 bytes para
    # AES-128, 192 y 256 respectivamente.
    $key_size =  strlen($key);
    echo "Tamaño de la clave: " . $key_size . "\n";

    $plaintext = "Esta cadena de caracteres ha sido cifrada en AES-256 / CBC / ZeroBytePadding.";

    # Crea un IV aleatorio para usar con el cifrado CBC
    $iv_size = mcrypt_get_iv_size(MCRYPT_RIJNDAEL_128, MCRYPT_MODE_CBC);
    $iv = mcrypt_create_iv($iv_size, MCRYPT_RAND);

    # Crea un texto cifrado compatible con AES (Rijndael block size = 128)
    # para mantener el texto confidencial.
    # Solo aplicable para entradas codificadas que nunca terminan
    # con el valor 00h (debido a la eliminación predeterminada de ceros finales)
    $ciphertext = mcrypt_encrypt(MCRYPT_RIJNDAEL_128, $key,
                                 $plaintext, MCRYPT_MODE_CBC, $iv);

    # Se añade el IV al inicio del texto cifrado para hacerlo disponible para el descifrado
    $ciphertext = $iv . $ciphertext;

    # Codifica el texto cifrado resultante para que pueda ser representado por una cadena de caracteres
    $ciphertext_base64 = base64_encode($ciphertext);

    echo  $ciphertext_base64 . "\n";

    # === ADVERTENCIA ===

    # El texto cifrado resultante no contiene integridad ni autenticación
    # y no está protegido contra ataques de tipo "oracle padding".

    # --- DESCIFRADO ---

    $ciphertext_dec = base64_decode($ciphertext_base64);

    # Obtiene el IV, iv_size debe haber sido creado utilizando la función
    # mcrypt_get_iv_size()
    $iv_dec = substr($ciphertext_dec, 0, $iv_size);

    # Obtiene el texto del cipher (todo, excepto $iv_size del inicio)
    $ciphertext_dec = substr($ciphertext_dec, $iv_size);

    # Se deben eliminar los caracteres de valor 00h del final del texto plano
    $plaintext_dec = mcrypt_decrypt(MCRYPT_RIJNDAEL_128, $key,
                                    $ciphertext_dec, MCRYPT_MODE_CBC, $iv_dec);

    echo  $plaintext_dec . "\n";
?>

   
```php

El ejemplo anterior mostrará:

    Tamaño de la clave: 32
    ENJW8mS2KaJoNB5E5CoSAAu0xARgsR1bdzFWpEn+poYw45q+73az5kYi4j+0haevext1dGrcW8Qi59txfCBV8BBj3bzRP3dFCp3CPQSJ8eU=
    Esta cadena de caracteres ha sido cifrada en AES-256 / CBC / ZeroBytePadding.

## Véase también

mcrypt_decrypt

mcrypt_module_open
