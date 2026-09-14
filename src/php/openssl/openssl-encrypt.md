---
title: openssl_encrypt
description: Cifra los datos
source_url: https://www.php.net/manual/es/function.openssl-encrypt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-encrypt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 7a016103e
order: 59150
---

openssl_encrypt

Cifra los datos

## Descripción

```php
#[\SensitiveParameter] #[\SensitiveParameter] openssl_encrypt(string $data, string $cipher_algo, string $passphrase, [int $options], [string $iv], [string $tag], [string $aad], [int $tag_length]): string
```php

Cifra los datos pasados con el método y la frase de contraseña especificados. Devuelve un `string` bruto o codificado en base64.

## Parámetros

`data`  
Los datos del mensaje en texto bruto a cifrar.

`cipher_algo`  
El método de cifrado. Para una lista de los métodos de cifrado disponibles, utilizar `openssl_get_cipher_methods`.

`passphrase`  
La frase de contraseña. Si la frase de contraseña es más corta de lo esperado, se rellena silenciosamente con caracteres `NUL`; si la frase de contraseña es más larga de lo esperado, se trunca silenciosamente.

> [!CAUTION]
> No se utiliza ninguna función de derivación de clave para el parámetro `passphrase` como su nombre podría sugerir. La única operación utilizada es el relleno con caracteres `NUL` o la truncación si la longitud es diferente de la esperada.

`options`  
`options` es una disyunción a nivel de bits de los flags `OPENSSL_RAW_DATA` y `OPENSSL_ZERO_PADDING` o `OPENSSL_DONT_ZERO_PAD_KEY`.

`iv`  
Un vector de inicialización no-`null`. Si el IV es más corto de lo esperado, se completa con caracteres `NUL` y se emite un aviso; si la frase de contraseña es más larga de lo esperado, se trunca y se emite un aviso.

`tag`  
La etiqueta de autenticación pasada por referencia al utilizar el modo de cifrado AEAD (GCM o CCM).

`aad`  
Datos adicionales autenticados.

`tag_length`  
La longitud de la `tag` de autenticación. Su valor puede estar entre 4 y 16 para el modo GCM.

## Valores devueltos

Devuelve la cadena cifrada en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Emite un error de nivel `E_WARNING` si se pasa un algoritmo de cifrado desconocido como parámetro `cipher_algo`.

Emite un error de nivel `E_WARNING` si se pasa un valor vacío como parámetro `iv`.

## Historial de cambios

| Versión | Descripción                                              |
|---------|----------------------------------------------------------|
| 7.1.0   | Se añadieron los parámetros `tag`, `aad` y `tag_length`. |

## Ejemplos

Ejemplo de cifrado autenticado AES en modo GCM para PHP 7.1+

```
<?php
//$key debería ser generado previamente de manera criptográfica, tal como openssl_random_pseudo_bytes
$plaintext = "message to be encrypted";
$cipher = "aes-128-gcm";
if (in_array($cipher, openssl_get_cipher_methods()))
{
    $ivlen = openssl_cipher_iv_length($cipher);
    $iv = openssl_random_pseudo_bytes($ivlen);
    $ciphertext = openssl_encrypt($plaintext, $cipher, $key, $options=0, $iv, $tag);
    //guardar $cipher, $iv, y $tag para el descifrado posterior
    $original_plaintext = openssl_decrypt($ciphertext, $cipher, $key, $options=0, $iv, $tag);
    echo $original_plaintext."\n";
}
?>

    
```php

Ejemplo de cifrado autenticado AES en modo GCM anterior a PHP 7.1

```
<?php
//$key debería ser generado previamente de manera criptográfica, tal como openssl_random_pseudo_bytes
$plaintext = "message to be encrypted";
$ivlen = openssl_cipher_iv_length($cipher="AES-128-CBC");
$iv = openssl_random_pseudo_bytes($ivlen);
$ciphertext_raw = openssl_encrypt($plaintext, $cipher, $key, $options=OPENSSL_RAW_DATA, $iv);
$hmac = hash_hmac('sha256', $ciphertext_raw, $key, $as_binary=true);
$ciphertext = base64_encode( $iv.$hmac.$ciphertext_raw );

// descifrar más tarde ...
$c = base64_decode($ciphertext);
$ivlen = openssl_cipher_iv_length($cipher="AES-128-CBC");
$iv = substr($c, 0, $ivlen);
$hmac = substr($c, $ivlen, $sha2len=32);
$ciphertext_raw = substr($c, $ivlen+$sha2len);
$original_plaintext = openssl_decrypt($ciphertext_raw, $cipher, $key, $options=OPENSSL_RAW_DATA, $iv);
$calcmac = hash_hmac('sha256', $ciphertext_raw, $key, $as_binary=true);
if (hash_equals($hmac, $calcmac))// comparación segura contra ataques de tiempo
{
    echo $original_plaintext."\n";
}
?>

    
```php

## Véase también

`openssl_decrypt`
