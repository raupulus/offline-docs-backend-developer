"""
Troceado de un documento largo en secciones.

El manual de Bash se distribuye como una sola pieza. Guardarlo entero
lo haría inservible en el visor: una página de varios megas sin índice
y sin poder enlazar a un apartado concreto.
"""

from __future__ import annotations

import re


def split_sections(
    markdown_text: str,
    levels: tuple[int, ...] = (2,),
) -> list[tuple[str, str]]:
    """Parte por encabezados y devuelve [(título, contenido), ...].

    Si no hay encabezados del nivel pedido, devuelve el documento entero
    como una sola sección en vez de perderlo.
    """
    marks = "|".join("#" * level for level in sorted(levels))
    pattern = re.compile(rf"^({marks})\s+(.+?)\s*$", re.MULTILINE)

    matches = list(pattern.finditer(markdown_text))
    if not matches:
        return [("Manual", markdown_text.strip())]

    sections: list[tuple[str, str]] = []

    preamble = markdown_text[: matches[0].start()].strip()
    if preamble:
        sections.append(("Introducción", preamble))

    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(markdown_text)
        chunk = markdown_text[match.start():end].strip()
        if chunk:
            sections.append((match.group(2), chunk))

    return sections
