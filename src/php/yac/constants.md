---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/yac.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yac/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yac
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 104260
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`YAC_VERSION` (`string`)  

`YAC_MAX_KEY_LEN` (`int`)  
La longitud máxima de una clave podría ser, es de 48 bytes.

`YAC_MAX_VALUE_RAW_LEN` (`int`)  

`YAC_MAX_RAW_COMPRESSED_LEN` (`int`)  

`YAC_SERIALIZER_PHP` (`int`)  
Usa php serialize como serializador

`YAC_SERIALIZER_JSON` (`int`)  
Usa json como serializador (requrie --enable-json)

`YAC_SERIALIZER_IGBINARY` (`int`)  
Usa igbinary como serializador (require --enable-igbinary)

`YAC_SERIALIZER_MSGPACK` (`int`)  
Usa msgpack como serializador (require --enable-msgpack)

`YAC_SERIALIZER` (`string`)  
Qué serializador está yac usando
