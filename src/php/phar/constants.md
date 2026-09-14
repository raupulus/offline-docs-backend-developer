---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/phar.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: 37280533a
order: 64870
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

| Constante | Valor | Descripción |
|----|----|----|
| `Phar::NONE` (`int`) | 0x00000000 | ninguna compresión |
| `Phar::COMPRESSED` (`int`) | 0x0000F000 | máscara de bits que puede ser utilizada con los flags de fichero para determinar si se utiliza una compresión |
| `Phar::GZ` (`int`) | 0x00001000 | compresión zlib (gzip) |
| `Phar::BZ2` (`int`) | 0x00002000 | compresión bzip2 |

Las constantes de compresión Phar {#phar.constants.compression}

| Constante            | Valor | Descripción             |
|----------------------|-------|-------------------------|
| `Phar::PHAR` (`int`) | 1     | formato de fichero phar |
| `Phar::TAR` (`int`)  | 2     | formato de fichero tar  |
| `Phar::ZIP` (`int`)  | 3     | formato de fichero zip  |

Las constantes de formato de fichero Phar {#phar.constants.fileformat}

| Constante | Valor | Descripción |
|----|----|----|
| `Phar::MD5` (`int`) | 0x0001 | firma con el algoritmo md5 |
| `Phar::SHA1` (`int`) | 0x0002 | firma con el algoritmo sha1 |
| `Phar::SHA256` (`int`) | 0x0003 | firma con el algoritmo sha256 (requiere la extensión hash) |
| `Phar::SHA512` (`int`) | 0x0004 | firma con el algoritmo sha512 (requiere la extensión hash) |
| `Phar::OPENSSL` (`int`) | 0x0010 | firma con un par de claves privada/pública OpenSSL. Es una verdadera firma de clave asimétrica |
| `Phar::OPENSSL_SHA256` (`int`) |  |  |
| `Phar::OPENSSL_SHA512` (`int`) |  |  |

Las constantes de firma Phar {#phar.constants.signature}

| Constante | Valor | Descripción |
|----|----|----|
| `Phar::PHP` (`int`) | 0 | utilizada para especificar el argumento de sobrescritura mime de `Phar::webPhar` y hacer que la extensión sea analizada como un fichero PHP |
| `Phar::PHPS` (`int`) | 1 | utilizada para especificar el argumento de sobrescritura mime de `Phar::webPhar` y hacer que la extensión sea analizada como un fichero PHP mediante `highlight_file` |

Las constantes de sobrescritura de mime Phar webPhar {#phar.constants.mimeoverride}
