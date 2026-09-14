---
title: '"winsound" --- Sound-playing interface for Windows'
source_url: https://docs.python.org/es/3
source_path: library/winsound.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4540
---

# "winsound" --- Sound-playing interface for Windows

======================================================================

The "winsound" module provides access to the basic sound-playing
machinery provided by Windows platforms.  It includes functions and
several constants.

Availability: Windows.

winsound.Beep(frequency, duration)

   Hace sonar el altavoz del PC. El parámetro *frequency* especifica
   la frecuencia, en hercio (hz), de la señal de audio y debe estar en
   el rango de 37 a 32.767 hz. El parámetro *duration* especifica el
   numero de milisegundo de duración de la señal de audio. Si el
   sistema no puede hacer sonar el altavoz, se lanza "RuntimeError".

winsound.PlaySound(sound, flags)

   Llama a la función responsable de "PlaySound()" desde el API de la
   plataforma.  El parámetro *sound* puede ser un nombre de archivo,
   un alias de sonido del sistema, datos de audio como un *bytes-like
   object* , o "None".  Su interpretación depende del valor de
   *flags*, que puede ser una combinación ORed de las constantes
   descritas a continuación. Si el parámetro de *sound* es "None",
   cualquier sonido de forma de onda que se esté reproduciendo en ese
   momento se detiene. Si el sistema indica un error, se lanza
   "RuntimeError`".

winsound.MessageBeep(type=MB_OK)

   Llama a la función responsable de "MensajeBeep()" de la API de la
   plataforma.  Esto reproduce un sonido como se especifica en el
   registro.  El argumento *type* especifica qué sonido se reproduce;
   los valores posibles son "-1", "MB_ICONASTERISK",
   "MB_ICONEXCLAMATION", "MB_ICONHAND", "MB_ICONQUESTION", y "MB_OK",
   todos descritos a continuación.  El valor "-1" produce un "simple
   pitido"; este es el último recurso si un sonido no puede ser
   reproducido de otra manera.  Si el sistema indica un error, se
   lanza "RuntimeError".

winsound.SND_FILENAME

   El parámetro *sound* es el nombre de un archivo WAV. No lo uses con
   "SND_ALIAS".

winsound.SND_ALIAS

   El parámetro *sound* es un nombre de asociación de sonido del
   registro.  Si el registro no contiene tal nombre, reproduce el
   sonido por defecto del sistema a menos que "SND_NODEFAULT" también
   se especifique. Si no se registra ningún sonido por defecto, se
   lanza "RuntimeError". No lo uses con "SND_FILENAME".

   Todos los sistemas Win32 soportan al menos lo siguiente; la mayoría
   de los sistemas soportan muchos más:

   +----------------------------+------------------------------------------+
   | "PlaySound()" *name*       | Panel de control correspondiente nombre  |
   |                            | (*name*) del sonido                      |
   |============================|==========================================|
   | "'SystemAsterisk'"         | Asterisco                                |
   +----------------------------+------------------------------------------+
   | "'SystemExclamation'"      | Exclamación                              |
   +----------------------------+------------------------------------------+
   | "'SystemExit'"             | Salir de Windows                         |
   +----------------------------+------------------------------------------+
   | "'SystemHand'"             | Parada crítica                           |
   +----------------------------+------------------------------------------+
   | "'SystemQuestion'"         | Pregunta                                 |
   +----------------------------+------------------------------------------+

   Por ejemplo:

      import winsound
      # Play Windows exit sound.
      winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

      # Probably play Windows default sound, if any is registered (because
      # "*" probably isn't the registered name of any sound).
      winsound.PlaySound("*", winsound.SND_ALIAS)

winsound.SND_LOOP

   Reproducir el sonido repetidamente.  El flag "SND_ASYNC" también
   debe ser usada para evitar el bloqueo.  No puede ser usada con
   "SND_MEMORY".

winsound.SND_MEMORY

   El parámetro *sound* de "PlaySound()" es una imagen de memoria de
   un archivo WAV, como un *bytes-like object*.

   Nota:

     Este módulo no admite la reproducción desde una imagen de memoria
     de forma sincrónica, por lo que una combinación de este indicador
     y "SND_ASYNC" se lanza "RuntimeError".

winsound.SND_PURGE

   Detiene la reproducción de todas las instancias de un sonido
   específico.

   Nota:

     Esta flag no esta soportado en las plataformas modernas de
     Windows.

winsound.SND_ASYNC

   Retorna inmediatamente, permitiendo que los sonidos se reproduzcan
   asincrónicamente.

winsound.SND_NODEFAULT

   Si no se puede encontrar el audio especificado, no reproduce el
   sonido predeterminado del sistema.

winsound.SND_NOSTOP

   No interrumpe los sonidos que se están reproduciendo.

winsound.SND_NOWAIT

   Retorna inmediatamente en caso de que  el controlador de sonido
   está ocupado.

   Nota:

     Esta flag no esta soportado en las plataformas modernas de
     Windows.

winsound.SND_APPLICATION

   The *sound* parameter is an application-specific alias in the
   registry. This flag can be combined with the "SND_ALIAS" flag to
   specify an application-defined sound alias.

winsound.SND_SENTRY

   Triggers a SoundSentry event when the sound is played.

   Added in version 3.14.

winsound.SND_SYNC

   The sound is played synchronously.  This is the default behavior.

   Added in version 3.14.

winsound.SND_SYSTEM

   Assign the sound to the audio session for system notification
   sounds.

   Added in version 3.14.

winsound.MB_ICONASTERISK

   Reproduce el sonido "SystemDefault".

winsound.MB_ICONEXCLAMATION

   Reproduce el sonido "SystemExclamation".

winsound.MB_ICONHAND

   Reproduce el sonido "SystemHand".

winsound.MB_ICONQUESTION

   Reproduce el sonido "SystemQuestion".

winsound.MB_OK

   Reproduce el sonido "SystemDefault".

winsound.MB_ICONERROR

   Reproduce el sonido "SystemHand".

   Added in version 3.14.

winsound.MB_ICONINFORMATION

   Reproduce el sonido "SystemDefault".

   Added in version 3.14.

winsound.MB_ICONSTOP

   Reproduce el sonido "SystemHand".

   Added in version 3.14.

winsound.MB_ICONWARNING

   Reproduce el sonido "SystemExclamation".

   Added in version 3.14.
