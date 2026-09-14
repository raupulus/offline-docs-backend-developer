---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/rnp.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rnp/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rnp
translation_status: ready
translation_reviewed: false
translation_revision: 8e27a4602
order: 72060
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`RNP_KEYSTORE_GPG` (`string`)  
Formato del almacén de claves "GPG".

`RNP_KEYSTORE_KBX` (`string`)  
Formato del almacén de claves "KBX". Solo para claves públicas. Una caja de claves (keybox) es un formato de fichero utilizado para almacenar claves públicas con metadatos e índices.

`RNP_KEYSTORE_G10` (`string`)  
Formato del almacén de claves "G10". Para claves privadas.

`RNP_LOAD_SAVE_PUBLIC_KEYS` (`integer`)  
Carga o guarda solo las claves públicas. Puede ser combinado con `RNP_LOAD_SAVE_SECRET_KEYS` para cargar tanto las claves públicas como privadas en el contexto FFI o guardarlas del contexto.

`RNP_LOAD_SAVE_SECRET_KEYS` (`integer`)  
Carga o guarda solo las claves secretas. Puede ser combinado con `RNP_LOAD_SAVE_PUBLIC_KEYS` para cargar tanto las claves públicas como privadas en el contexto FFI o guardarlas del contexto.

`RNP_LOAD_SAVE_PERMISSIVE` (`integer`)  
Permite ignorar los paquetes de firma/clave/subclave incorrectos durante la importación de claves.

`RNP_LOAD_SAVE_SINGLE` (`integer`)  
Si se define, solo la primera clave será cargada.

`RNP_LOAD_SAVE_BASE64` (`integer`)  
Permite la importación de claves codificadas en base64 (claves autocrypt).

`RNP_FEATURE_SYMM_ALG` (`string`)  
Lista los algoritmos de cifrado simétrico disponibles.

`RNP_FEATURE_AEAD_ALG` (`string`)  
Lista los algoritmos AEAD disponibles.

`RNP_FEATURE_PROT_MODE` (`string`)  
Lista los modos de protección disponibles.

`RNP_FEATURE_PK_ALG` (`string`)  
Lista los algoritmos de clave pública disponibles.

`RNP_FEATURE_HASH_ALG` (`string`)  
Lista los algoritmos de hash disponibles.

`RNP_FEATURE_COMP_ALG` (`string`)  
Lista los algoritmos de compresión disponibles.

`RNP_FEATURE_CURVE` (`string`)  
Lista las curvas elípticas disponibles.

`RNP_DUMP_MPI` (`integer`)  
Muestra los valores MPI (enteros multi-precisión).

`RNP_DUMP_RAW` (`integer`)  
Muestra también el contenido sin tratar del paquete.

`RNP_DUMP_GRIP` (`integer`)  
Muestra las huellas y los identificadores de clave.

`RNP_JSON_DUMP_MPI` (`integer`)  
Muestra los valores MPI (enteros multi-precisión).

`RNP_JSON_DUMP_RAW` (`integer`)  
Muestra también el contenido sin tratar del paquete.

`RNP_JSON_DUMP_GRIP` (`integer`)  
Muestra las huellas y los identificadores de clave.

`RNP_ENCRYPT_NOWRAP` (`integer`)  
Permite el cifrado del mensaje firmado. El mensaje no está envuelto en un paquete de datos literales.

`RNP_KEY_EXPORT_ARMORED` (`integer`)  
Activa la armadura ASCII de los datos exportados.

`RNP_KEY_EXPORT_PUBLIC` (`integer`)  
Exporta la clave pública.

`RNP_KEY_EXPORT_SECRET` (`integer`)  
Exporta la clave secreta.

`RNP_KEY_EXPORT_SUBKEYS` (`integer`)  
Si la clave principal es exportada, todas las subclaves lo serán también.

`RNP_KEY_EXPORT_BASE64` (`integer`)  
Exporta la clave autocrypt codificada en base64 en lugar de binaria.

`RNP_KEY_REMOVE_PUBLIC` (`integer`)  
Elimina la clave pública.

`RNP_KEY_REMOVE_SECRET` (`integer`)  
Elimina la clave secreta.

`RNP_KEY_REMOVE_SUBKEYS` (`integer`)  
Si la clave principal es eliminada, todas las subclaves lo serán también.
