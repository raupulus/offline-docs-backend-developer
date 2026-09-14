---
title: openssl_csr_new
description: Genera una CSR
source_url: https://www.php.net/manual/es/function.openssl-csr-new.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-csr-new.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: f0d11929d
order: 59100
---

openssl_csr_new

Genera una

CSR

## Descripción

```php
#[\SensitiveParameter] openssl_csr_new(array $distinguished_names, OpenSSLAsymmetricKey $private_key, [array $options], [array $extra_attributes]): OpenSSLCertificateSigningRequest
```php

`openssl_csr_new` genera una nueva CSR (requisición de firma de certificado), basada en la información proporcionada por `distinguished_names`.

> [!NOTE]
> Debe existir un archivo `openssl.cnf` válido e instalado para que esta función opere correctamente. Ver las notas encontradas en la [sección concerniente a la instalación](#openssl.installation) para más información.

## Parámetros

`distinguished_names`  
El nombre distintivo (Distinguished Name) o los campos del sujeto a incluir en el certificado. El `distinguished_names` es un array asociativo cuyas claves representan los nombres de atributos de los Distinguished Names, y los valores pueden ser cadenas (para un valor único) o arrays (si se deben definir varios valores).

`private_key`  
`private_key` debe ser una clave privada que haya sido generada por `openssl_pkey_new` (u obtenida de otro modo mediante alguna de las funciones de la familia openssl_pkey), o la variable `null`. Si su valor es una variable `null`, se genera una nueva clave privada según las `options` proporcionadas y se asigna a la variable suministrada. La parte pública correspondiente de la clave se utilizará para firmar la CSR.

`options`  
Por omisión, se utiliza el archivo `openssl.conf` del sistema para inicializar la requisición; puede especificarse una sección del archivo de configuración configurando la clave `config_section_section` en `options`. También puede especificarse un archivo de configuración alternativo de OpenSSL configurando el valor de `config` con la ruta del archivo a utilizar. Si las claves siguientes están presentes en `options`, se comportan como sus equivalentes en `openssl.conf`, según la lista siguiente.

| `options` | tipo | Equivalente de `openssl.conf` | descripción |
|----|----|----|----|
| digest_alg | `string` | default_md | Método de digest o firma de hash, generalmente uno de `openssl_get_md_methods` |
| x509_extensions | `string` | x509_extensions | Selecciona qué extensión utilizar al crear un certificado x509 |
| req_extensions | `string` | req_extensions | Selecciona qué extensión utilizar al crear una CSR |
| private_key_bits | `int` | default_bits | Especifica la longitud en bits de la clave privada |
| private_key_type | `int` | none | Especifica el tipo de clave privada a crear. Puede ser uno de `OPENSSL_KEYTYPE_DSA`, `OPENSSL_KEYTYPE_DH`, `OPENSSL_KEYTYPE_RSA` o `OPENSSL_KEYTYPE_EC`. El valor por omisión es `OPENSSL_KEYTYPE_RSA`. |
| encrypt_key | `bool` | encrypt_key | ¿Debe estar cifrada la clave (con contraseña) exportada? |
| encrypt_key_cipher | `int` | none | Una de las [constantes cipher](#openssl.ciphers). |
| curve_name | `string` | none | Uno de `openssl_get_curve_names`. |
| config | `string` | N/A | Ruta hacia su archivo openssl.conf alternativo. |

Sobrescribir configuración

`extra_attributes`  
`extra_attributes` se utiliza para especificar atributos adicionales para la CSR. Se trata de un array asociativo cuyas claves se convierten en OID y se aplican como atributos de CSR.

## Valores devueltos

Devuelve la CSR en caso de éxito, `true` si la creación de la CSR tiene éxito pero falla la firma o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | El array asociativo `distinguished_names` ahora admite arrays como valores, permitiendo especificar varios valores para un mismo atributo. |
| 8.4.0 | El parámetro `extra_attributes` ahora define correctamente los atributos del CSR, en lugar de modificar el nombre distintivo del sujeto como hacía anteriormente de forma incorrecta. |
| 8.0.0 | `csr` ahora acepta una instancia de `OpenSSLCertificateSigningRequest` ; anteriormente, se aceptaba un `resource` de tipo `OpenSSL X.509 CSR`. |
| 8.0.0 | En caso de éxito, esta función ahora devuelve una instancia de `OpenSSLAsymmetricKey` ; anteriormente se devolvía una `resource` de tipo `OpenSSL key`. |
| 7.1.0 | `options` ahora admite `curve_name`. |

## Ejemplos

Creación de un certificado autosignado

```
<?php
// para certificados SSL de servidor, el commonName es el nombre de dominio a proteger
// para certificados de correo electrónico S/MIME el commonName es el propietario de la dirección de correo
// los campos de ubicación e identificación hacen referencia al propietario del dominio o al objeto del correo a proteger
$dn = array(
    "countryName" => "GB",
    "stateOrProvinceName" => "Somerset",
    "localityName" => "Glastonbury",
    "organizationName" => "The Brain Room Limited",
    "organizationalUnitName" => "PHP Documentation Team",
    "commonName" => "Wez Furlong",
    "emailAddress" => "wez@example.com"
);

// Genera un nuevo par de claves privada (y pública)
$privkey = openssl_pkey_new(array(
    "private_key_bits" => 2048,
    "private_key_type" => OPENSSL_KEYTYPE_RSA,
));

// Genera una requisición de firma de certificado
$csr = openssl_csr_new($dn, $privkey, array('digest_alg' => 'sha256'));

// Genera un certificado autosignado, válido durante 365 días
$x509 = openssl_csr_sign($csr, null, $privkey, $days=365, array('digest_alg' => 'sha256'));

// Guarde su clave privada, CSR y certificado autosignado para uso posterior
openssl_csr_export($csr, $csrout) and var_dump($csrout);
openssl_x509_export($x509, $certout) and var_dump($certout);
openssl_pkey_export($privkey, $pkeyout, "mypassword") and var_dump($pkeyout);

// Muestra los errores que han ocurrido
while (($e = openssl_error_string()) !== false) {
    echo $e . "\n";
}
?>

    
```php

Crear un certificado ECC autosignado (a partir de PHP 7.1.0)

```
<?php
$subject = array(
    "commonName" => "docs.php.net",
);

// Genera un nuevo par de claves privada (y pública)
$private_key = openssl_pkey_new(array(
    "private_key_type" => OPENSSL_KEYTYPE_EC,
    "curve_name" => 'prime256v1',
));

// Genera una requisición de firma de certificado
$csr = openssl_csr_new($subject, $private_key, array('digest_alg' => 'sha384'));

// Genera un certificado EC autosignado
$x509 = openssl_csr_sign($csr, null, $private_key, $days=365, array('digest_alg' => 'sha384'));
openssl_x509_export_to_file($x509, 'ecc-cert.pem');
openssl_pkey_export_to_file($private_key, 'ecc-private.key');
?>

    
```php

## Véase también

`openssl_csr_sign`
