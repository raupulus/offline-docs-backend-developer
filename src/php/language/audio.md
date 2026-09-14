---
title: ogg://
description: Flujos de audio
source_url: https://www.php.net/manual/es/wrappers.audio.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/wrappers/audio.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 8bc832a46
order: 4600
---

ogg://

Flujos de audio

## Descripción

Los ficheros que se abran para lectura usando la envoltura `ogg://` se utilizan como codificaciones de audio comprimido usando el códec `OGG/Vorbis`. De forma similar, los ficheros abiertos para escritura o para añadir contenido usando la envoltura `ogg://` se escriben como datos de audio comprimidos. Cuando se use la función `stream_get_meta_data` con un fichero `OGG/Vorbis` abierto para lectura, se devolverán diversos detalles del flujo, incluyendo la etiqueta `vendor`, cualquier `comments` que se haya añadido, el número de canales `channels`, el `ratio` de muestreo, y el rango del ratio de codificación descrito por: `bitrate_lower`, `bitrate_upper`, `bitrate_nominal`, y `bitrate_window`.

`ogg://` (PECL)

> [!NOTE]
> Para usar la envoltura `ogg://` es necesario instalar la extensión [OGG/Vorbis](https://pecl.php.net/package/oggvorbis) disponible en [PECL](https://pecl.php.net/).

## Uso

- `ogg://soundfile.ogg`

- `ogg:///path/to/soundfile.ogg`

- `ogg://http://www.example.com/path/to/soundstream.ogg`

## Opciones

| Atributo                                                | Permitido |
|---------------------------------------------------------|-----------|
| Restringido por [allow_url_fopen](#ini.allow-url-fopen) | No        |
| Permite Lecturas                                        | Sí        |
| Permite Escrituras                                      | Sí        |
| Permite Añadir contenido                                | Sí        |
| Permite Lecturas y Escrituras Simultánea                | No        |
| Permite usar la función `stat`                          | No        |
| Permite usar la función `unlink`                        | No        |
| Permite usar la función `rename`                        | No        |
| Permite usar la función `mkdir`                         | No        |
| Permite usar la función `rmdir`                         | No        |

Resumen de la Envoltura {role="stream_wrapper"}

| Nombre | Uso | Valor por omisión | Modo |
|----|----|----|----|
| `pcm_mode` | codificación PCM que se aplicará en las lecturas, de entre: `OGGVORBIS_PCM_U8`, `OGGVORBIS_PCM_S8`, `OGGVORBIS_PCM_U16_BE`, `OGGVORBIS_PCM_S16_BE`, `OGGVORBIS_PCM_U16_LE`, y `OGGVORBIS_PCM_S16_LE`. (8 o 16 bit, con o sin signo, big o little `endian`) | OGGVORBIS_PCM_S16_LE | Lectura |
| `rate` | Ratio de muestreo en datos de entradas, expresado en Hz | 44100 | Escritura/Adición |
| `bitrate` | Si es un entero, definirá el bitrate fijo al que se codificará. (de 16000 a 131072) Si es un real, definirá la calidad del bitrate variable a usar. (de -1.0 a 1.0) | 128000 | Escritura/Adición |
| `channels` | El número de canales de audio a codificar, normalmente 1 (mono), o 2 (estéreo). Puede llegar a 16. | 2 | Escritura/Adición |
| `comments` | Un array de strings a codificar en la cabecera de la pista. |  | Escritura/Adición |

Opciones de contexto {role="stream_wrapper"}
