---
title: openssl_pkey_new
description: Genera una nueva clave privada
source_url: https://www.php.net/manual/es/function.openssl-pkey-new.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-pkey-new.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 3b06ef4bb
order: 59430
---

openssl_pkey_new

Genera una nueva clave privada

## Descripción

```php
openssl_pkey_new([array $options]): OpenSSLAsymmetricKey
```php

`openssl_pkey_new` genera una nueva clave privada. Cómo obtener el componente público de la clave se demuestra en un ejemplo a continuación.

> [!NOTE]
> Debe existir un archivo `openssl.cnf` válido e instalado para que esta función opere correctamente. Ver las notas encontradas en la [sección concerniente a la instalación](#openssl.installation) para más información.

## Parámetros

`options`  
Es posible afinar la generación de claves (por ejemplo, especificando el número de bits o los parámetros) mediante el argumento `options`. Estas opciones pueden ser parámetros específicos del algoritmo utilizados para la generación de claves, u opciones genéricas también utilizadas para la generación de CSR si no se especifican. Consulte `openssl_csr_new` para obtener más información sobre el uso de `options` para un CSR. Entre estas opciones, solo `private_key_bits`, `private_key_type`, `curve_name`, y `config` se utilizan para la generación de claves. Las opciones específicas de un algoritmo se utilizan si el array asociativo incluye una de las claves específicas.

- Clave `"rsa"` para definir los parámetros RSA.

  | options  | type     | format         | requis | description                       |
  |----------|----------|----------------|--------|-----------------------------------|
  | `"n"`    | `string` | número binario | sí     | módulo                            |
  | `"e"`    | `string` | número binario | no     | exponente público                 |
  | `"d"`    | `string` | número binario | sí     | exponente privado                 |
  | `"p"`    | `string` | número binario | no     | primer 1                          |
  | `"q"`    | `string` | número binario | no     | primer 2                          |
  | `"dmp1"` | `string` | número binario | no     | exponent1, d mod (p-1)            |
  | `"dmq1"` | `string` | número binario | no     | exponent2, d mod (q-1)            |
  | `"iqmp"` | `string` | número binario | no     | coeficiente, (inverso de q) mod p |

- Clave `"dsa"` para definir los parámetros DSA.

  | options | type | format | requis | description |
  |----|----|----|----|----|
  | `"p"` | `string` | número binario | no | número primo (público) |
  | `"q"` | `string` | número binario | no | 160 bits sub-prime, q \| p-1 (público) |
  | `"g"` | `string` | número binario | no | generador del subgrupo (público) |
  | `"priv_key"` | `string` | clave PEM | no | clave privada x |
  | `"pub_key"` | `string` | clave PEM | no | clave pública y = g^x |

- Clave `"dh"` para los parámetros DH (intercambio de claves Diffie–Hellman).

  | Options      | Tipo     | Format         | Requis | Descripción                   |
  |--------------|----------|----------------|--------|-------------------------------|
  | `"p"`        | `string` | número binario | no     | número primo (compartido)     |
  | `"g"`        | `string` | número binario | no     | generador de Z_p (compartido) |
  | `"priv_key"` | `string` | clave PEM      | no     | valor DH privado x            |
  | `"pub_key"`  | `string` | clave PEM      | no     | valor DH público g^x          |

- Clave `"ec"` para los parámetros de curva elíptica

  | Options | Tipo | Format | Requis | Descripción |
  |----|----|----|----|----|
  | `"curve_name"` | `string` | nombre | no | nombre de la curva, ver `openssl_get_curve_names` |
  | `"p"` | `string` | número binario | no | número primo del campo para la curva sobre Fp |
  | `"a"` | `string` | número binario | no | coeficiente a de la curva para Fp : y^2 mod p = x^3 + ax + b mod p |
  | `"b"` | `string` | número binario | no | coeficiente b de la curva para Fp : y^2 mod p = x^3 + ax + b mod p |
  | `"seed"` | `string` | número binario | no | número aleatorio opcional utilizado para generar el coeficiente b |
  | `"generator"` | `string` | punto codificado en binario | no | punto generador de la curva |
  | `"g_x"` | `string` | número binario | no | coordenada x del punto generador de la curva |
  | `"g_y"` | `string` | número binario | no | coordenada y del punto generador de la curva |
  | `"cofactor"` | `string` | número binario | no | cofactor de la curva |
  | `"order"` | `string` | número binario | no | orden de la curva |
  | `"x"` | `string` | número binario | no | coordenada x (pública) |
  | `"y"` | `string` | número binario | no | coordenada y (pública) |
  | `"d"` | `string` | número binario | no | clave privada |

- Claves `"x25519"`, `"x448"`, `"ed25519"`, `"ed448"` para los parámetros Curve25519 y Curve448.

  | Options      | Tipo     | Format    | Requis | Descripción   |
  |--------------|----------|-----------|--------|---------------|
  | `"priv_key"` | `string` | clave PEM | no     | clave privada |
  | `"pub_key"`  | `string` | clave PEM | no     | clave pública |

## Valores devueltos

Devuelve una instancia de `OpenSSLAsymmetricKey` en caso de éxito, `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Se añadió el soporte para claves basadas en Curve25519 y Curve448 con la introducción de los campos `x25519`, `ed25519`, `x448`, y `ed448`. |
| 8.3.0 | Se añadió el soporte para la generación de claves EC con parámetros EC personalizados. Más específicamente, con la introducción de las opciones EC: `p`, `a`, `b`, `seed`, `generator`, `g_x`, `g_y`, `cofactor`, y `order`. |
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `OpenSSLAsymmetricKey`; anteriormente, se devolvía un `resource` de tipo `OpenSSL key`. |
| 7.1.0 | Se añadió la opción `curve_name` para permitir la creación de claves EC. |

## Ejemplos

Obtener la clave pública a partir de una clave privada

```
<?php

$private_key = openssl_pkey_new();
$public_key_pem = openssl_pkey_get_details($private_key)['key'];
echo $public_key_pem, PHP_EOL;

$public_key = openssl_pkey_get_public($public_key_pem);
var_dump($public_key);

?>

   
```php

Resultado del ejemplo anterior es similar a:

    // Resultado antes de PHP 8.0.0; note que la función devuelve un recurso
    -----BEGIN PUBLIC KEY-----
    MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwknBFEherZe74BiRjTFA
    hqwZ1SK7brwq7C/afnLXKhRR7jnrpfM0ypC46q8xz5UZswenZakJ7kd5fls+r4Bv
    3P8XsKYLTh2m1GiWQhV1g77cNIN4qNWh70PiDO3fB2446o1LBgToQYuRZS5YQRfJ
    rVD0ysgtVcCU9tjaey28HlgApOpYFTaaKPj2MBmEYpMC+kG2HhL12GfpHUi2eiXI
    dXT2WskWHWvUrmQ7fJIfI92JlDokV62DH/q1oiedLs9OPNb0rL1aAmYdzaVN6XNH
    x/o4Lh125v2vAPV9E3fZCDc/HDEUaahpjanMiCQEgEDp5Hr+CRkvERT5/ydN+p08
    5wIDAQAB
    -----END PUBLIC KEY-----
    resource(6) of type (OpenSSL key)

    // Resultado a partir de PHP 8.0.0; note que la función devuelve un objeto
    -----BEGIN PUBLIC KEY-----
    MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwknBFEherZe74BiRjTFA
    hqwZ1SK7brwq7C/afnLXKhRR7jnrpfM0ypC46q8xz5UZswenZakJ7kd5fls+r4Bv
    3P8XsKYLTh2m1GiWQhV1g77cNIN4qNWh70PiDO3fB2446o1LBgToQYuRZS5YQRfJ
    rVD0ysgtVcCU9tjaey28HlgApOpYFTaaKPj2MBmEYpMC+kG2HhL12GfpHUi2eiXI
    dXT2WskWHWvUrmQ7fJIfI92JlDokV62DH/q1oiedLs9OPNb0rL1aAmYdzaVN6XNH
    x/o4Lh125v2vAPV9E3fZCDc/HDEUaahpjanMiCQEgEDp5Hr+CRkvERT5/ydN+p08
    5wIDAQAB
    -----END PUBLIC KEY-----

    object(OpenSSLAsymmetricKey)#2 (0) {
    }

Generación de una clave RSA a partir de parámetros

```
<?php

$nhex = "BBF82F090682CE9C2338AC2B9DA871F7368D07EED41043A440D6B6F07454F51F" .
        "B8DFBAAF035C02AB61EA48CEEB6FCD4876ED520D60E1EC4619719D8A5B8B807F" .
        "AFB8E0A3DFC737723EE6B4B7D93A2584EE6A649D060953748834B2454598394E" .
        "E0AAB12D7B61A51F527A9A41F6C1687FE2537298CA2A8F5946F8E5FD091DBDCB";

$ehex = "11";
$dhex = "A5DAFC5341FAF289C4B988DB30C1CDF83F31251E0668B42784813801579641B2" .
        "9410B3C7998D6BC465745E5C392669D6870DA2C082A939E37FDCB82EC93EDAC9" .
        "7FF3AD5950ACCFBC111C76F1A9529444E56AAF68C56C092CD38DC3BEF5D20A93" .
        "9926ED4F74A13EDDFBE1A1CECC4894AF9428C2B7B8883FE4463A4BC85B1CB3C1";

$phex = "EECFAE81B1B9B3C908810B10A1B5600199EB9F44AEF4FDA493B81A9E3D84F632" .
        "124EF0236E5D1E3B7E28FAE7AA040A2D5B252176459D1F397541BA2A58FB6599";

$qhex = "C97FB1F027F453F6341233EAAAD1D9353F6C42D08866B1D05A0F2035028B9D86" .
        "9840B41666B42E92EA0DA3B43204B5CFCE3352524D0416A5A441E700AF461503";

$dphex = "11";
$dqhex = "11";
$qinvhex = "b06c4fdabb6301198d265bdbae9423b380f271f73453885093077fcd39e2119f" .
           "c98632154f5883b167a967bf402b4e9e2e0f9656e698ea3666edfb25798039f7";

$rsa= openssl_pkey_new([
    'rsa' => [
        'n' => hex2bin($nhex),
        'e' => hex2bin($ehex),
        'd' => hex2bin($dhex),
        'p' => hex2bin($phex),
        'q' => hex2bin($qhex),
        'dmp1' => hex2bin($dphex),
        'dmq1' => hex2bin($dqhex),
        'iqmp' => hex2bin($qinvhex),
    ],
]);
$details = openssl_pkey_get_details($rsa);
var_dump($details);

?>

   
```php
