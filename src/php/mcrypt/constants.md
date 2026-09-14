---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/mcrypt.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: f80105b4f
order: 45690
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

Mcrypt puede operar en 4 modos de cifrado (`CBC`, `OFB`, `CFB` y `ECB`). Si está vinculado contra libmcrypt-2.4.x o posterior, las funciones pueden operar asimismo en modo `nOFB` y en modo `STREAM`. A continuación se encuentra una lista con todos los modos de cifrado soportados con las constantes que están definidas para el modo de cifrado. Para una referencia más completa y discusiones, ver Applied Cryptography by Schneier (ISBN 0-471-11709-9).

- `MCRYPT_MODE_ECB` (`electronic codebook`) es un modo de cifrado por bloques que generalmente es inapropiado para la mayoría de los usos. El uso de este modo está desaconsejado.

- `MCRYPT_MODE_CBC` (`cipher block chaining`) es un modo de cifrado por bloques que es considerablemente más seguro que el modo `ECB`.

- `MCRYPT_MODE_CFB` (`cipher feedback, en modo de 8 bits`) es un modo de cifrado por flujo. Se recomienda utilizar el modo `NCFB` en lugar del modo `CFB`.

- `MCRYPT_MODE_OFB` (`output feedback, en 8 bits`) es un modo de cifrado por flujo comparable a `CFB`, pero puede ser utilizado en aplicaciones donde la propagación de errores no puede ser tolerada. Se recomienda utilizar el modo `NOFB` en lugar del modo `OFB`.

- `MCRYPT_MODE_NOFB` (`output feedback, en modo de n bits`) es comparable al modo `OFB`, pero opera sobre el tamaño de bloque completo del algoritmo.

- `MCRYPT_MODE_STREAM` es un modo adicional, para incluir algoritmos de flujo tales como `"WAKE"` o `"RC4"`.

Mcrypt soporta otros modos de operación para los cuales no hay constantes predefinidas. Pueden ser utilizados pasando un `string` en lugar de las constantes faltantes.

- `"ctr"` (`counter mode`) es un modo de cifrado por flujo.

- `"ncfb"` (`cipher feedback, en modo de n bits`) es comparable al modo `CFB`, pero opera sobre el tamaño de bloque completo del algoritmo.

A continuación se presentan algunos otros modos y métodos de compresión:

`MCRYPT_ENCRYPT` (`int`)  

`MCRYPT_DECRYPT` (`int`)  

`MCRYPT_DEV_RANDOM` (`int`)  

`MCRYPT_DEV_URANDOM` (`int`)  

`MCRYPT_RAND` (`int`)
