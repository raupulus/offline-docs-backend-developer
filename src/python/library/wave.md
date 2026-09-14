---
title: '"wave" --- Read and write WAV files'
source_url: https://docs.python.org/es/3
source_path: library/wave.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4490
---

# "wave" --- Read and write WAV files

**Código fuente:** Lib/wave.py

======================================================================

The "wave" module provides a convenient interface to the Waveform
Audio "WAVE" (or "WAV") file format. Only uncompressed PCM encoded
wave files are supported.

Distinto en la versión 3.12: Support for "WAVE_FORMAT_EXTENSIBLE"
headers was added, provided that the extended format is
"KSDATAFORMAT_SUBTYPE_PCM".

The "wave" module defines the following function and exception:

wave.open(file, mode=None)

   Si *file* es una cadena, abra el archivo con ese nombre, de lo
   contrario trátelo como un objeto similar a un archivo.  *mode*
   puede ser:

   "'rb'"
      Modo de solo lectura.

   "'wb'"
      Modo de solo escritura.

   Tenga en cuenta que no permite archivos WAV de lectura/escritura.

   Un *mode* de "'rb'" retorna un objeto "Wave_read", mientras que un
   *mode* de "'wb'" retorna un objeto "Wave_write".  Si se omite
   *mode* y se pasa un objeto similar a un archivo como *file*,
   "file.mode" se usa como el valor predeterminado para *mode*.

   If you pass in a file-like object, the wave object will not close
   it when its "close()" method is called; it is the caller's
   responsibility to close the file object.

   The "open()" function may be used in a "with" statement.  When the
   "with" block completes, the "Wave_read.close()" or
   "Wave_write.close()" method is called.

   Distinto en la versión 3.4: Se agregó soporte para archivos no
   encontrados.

exception wave.Error

   Error que se produce cuando algo es imposible porque viola la
   especificación WAV o alcanza una deficiencia de implementación.

## Los objetos *Wave_read*

class wave.Wave_read

   Read a WAV file.

   Los objetos *Wave_read*, tal como lo retorna "open()", tienen los
   siguientes métodos:

   close()

      Close the stream if it was opened by "wave", and make the
      instance unusable.  This is called automatically on object
      collection.

   getnchannels()

      Retorna el número de canales de audio ("1" para mono, "2" para
      estéreo).

   getsampwidth()

      Retorna el ancho de la muestra en bytes.

   getframerate()

      Retorna la frecuencia del muestreo.

   getnframes()

      Retorna el número de cuadros del audio.

   getcomptype()

      Retorna el tipo de compresión ("'NONE'" es el único tipo
      admitido).

   getcompname()

      Versión legible para humanos de "getcomptype()". Generalmente
      "'not compressed'" significa "'NONE'".

   getparams()

      Returns a "namedtuple()" "(nchannels, sampwidth, framerate,
      nframes, comptype, compname)", equivalent to output of the
      "get*()" methods.

   readframes(n)

      Lee y retorna como máximo *n* cuadros de audio, como un objeto
      "bytes".

   rewind()

      Rebobina el puntero del archivo hasta el principio de la
      secuencia de audio.

   The following two methods are defined for compatibility with the
   old "aifc" module, and don't do anything interesting.

   getmarkers()

      Retorna "None".

      Deprecated since version 3.13, will be removed in version 3.15:
      The method only existed for compatibility with the "aifc" module
      which has been removed in Python 3.13.

   getmark(id)

      Lanza un error.

      Deprecated since version 3.13, will be removed in version 3.15:
      The method only existed for compatibility with the "aifc" module
      which has been removed in Python 3.13.

   Los dos métodos siguientes definen un término "posición" que es
   compatible entre ellos y, es dependiente de la implementación.

   setpos(pos)

      Establece el puntero del archivo en la posición especificada.

   tell()

      Retorna la posición actual del puntero del archivo.

## Los objetos *Wave_write*

class wave.Wave_write

   Write a WAV file.

   Wave_write objects, as returned by "open()".

   For seekable output streams, the "wave" header will automatically
   be updated to reflect the number of frames actually written.  For
   unseekable streams, the *nframes* value must be accurate when the
   first frame data is written.  An accurate *nframes* value can be
   achieved either by calling "setnframes()" or "setparams()" with the
   number of frames that will be written before "close()" is called
   and then using "writeframesraw()" to write the frame data, or by
   calling "writeframes()" with all of the frame data to be written.
   In the latter case "writeframes()" will calculate the number of
   frames in the data and set *nframes* accordingly before writing the
   frame data.

   Distinto en la versión 3.4: Se agregó soporte para archivos no
   encontrados.

   Wave_write objects have the following methods:

   close()

      Make sure *nframes* is correct, and close the file if it was
      opened by "wave".  This method is called upon object collection.
      It will raise an exception if the output stream is not seekable
      and *nframes* does not match the number of frames actually
      written.

   setnchannels(n)

      Configure el número de canales.

   getnchannels()

      Return the number of channels.

   setsampwidth(n)

      Establezca el ancho de la muestra en *n* bytes.

   getsampwidth()

      Return the sample width in bytes.

   setframerate(n)

      Establezca la velocidad del cuadro en *n*.

      Distinto en la versión 3.2: Una entrada no-entera para este
      método se redondea al número entero más cercano.

   getframerate()

      Return the frame rate.

   setnframes(n)

      Establezca el número de cuadros en *n*. Esto se cambiará más
      adelante si el número de cuadros realmente escritos es diferente
      (este intento de actualización levantará un error si no se
      encuentra la secuencia de salida).

   getnframes()

      Return the number of audio frames written so far.

   setcomptype(type, name)

      Establece el tipo de compresión y la descripción. Por el
      momento, solo se admite el tipo de compresión "NONE", lo que
      significa que no hay compresión.

   getcomptype()

      Return the compression type ("'NONE'").

   getcompname()

      Return the human-readable compression type name.

   setparams(tuple)

      The *tuple* should be "(nchannels, sampwidth, framerate,
      nframes, comptype, compname)", with values valid for the
      "set*()" methods.  Sets all parameters.

   getparams()

      Return a "namedtuple()" "(nchannels, sampwidth, framerate,
      nframes, comptype, compname)" containing the current output
      parameters.

   tell()

      Retorna la posición actual en el archivo, con el mismo descargo
      para los métodos "Wave_read.tell()" y "Wave_read.setpos()".

   writeframesraw(data)

      Escribe cuadros de audio, sin corregir *nframes*.

      Distinto en la versión 3.4: Todo *bytes-like object* ahora es
      aceptado.

   writeframes(data)

      Escribe cuadros de audio y se asegura de que *nframes* sea
      correcto. Levantará un error si no se puede encontrar la
      secuencia de salida y si el número total de cuadros que se han
      escrito después de que se haya escrito *data* no coincide con el
      valor establecido previamente para *nframes*.

      Distinto en la versión 3.4: Todo *bytes-like object* ahora es
      aceptado.

      Tenga en cuenta que no es válido establecer ningún parámetro
      después de invocar a "writeframes()" o "writeframesraw()", y
      cualquier intento de hacerlo levantará "wave.Error".
