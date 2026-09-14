---
title: Introduction to Line Editing
source_url: https://www.gnu.org/software/bash/manual
source_path: 040-introduction-to-line-editing.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 400
---

## Introduction to Line Editing

The following paragraphs use Emacs style to describe the notation used to represent keystrokes.

The text `C-k` is read as ‘Control-K’ and describes the character produced when the k key is pressed while the Control key is depressed.

The text `M-k` is read as ‘Meta-K’ and describes the character produced when the Meta key (if you have one) is depressed, and the k key is pressed (a meta character), then both are released. The Meta key is labeled ALT or Option on many keyboards. On keyboards with two keys labeled ALT (usually to either side of the space bar), the ALT on the left side is generally set to work as a Meta key. One of the ALT keys may also be configured as some other modifier, such as a Compose key for typing accented characters.

On some keyboards, the Meta key modifier produces characters with the eighth bit (0200) set. You can use the `enable-meta-key` variable to control whether or not it does this, if the keyboard allows it. On many others, the terminal or terminal emulator converts the metafied key to a key sequence beginning with ESC as described in the next paragraph.

If you do not have a Meta or ALT key, or another key working as a Meta key, you can generally achieve the latter effect by typing ESC *first*, and then typing k. The ESC character is known as the meta prefix).

Either process is known as metafying the k key.

If your Meta key produces a key sequence with the ESC meta prefix, you can make `M-key` key bindings you specify (see `Key Bindings` in [Readline Init File Syntax](#Readline-Init-File-Syntax)) do the same thing by setting the `force-meta-prefix` variable.

The text `M-C-k` is read as ‘Meta-Control-k’ and describes the character produced by metafying `C-k`.

In addition, several keys have their own names. Specifically, DEL, ESC, LFD, SPC, RET, and TAB all stand for themselves when seen in this text, or in an init file (see [Readline Init File](#Readline-Init-File)). If your keyboard lacks a LFD key, typing C-j will output the appropriate character. The RET key may be labeled Return or Enter on some keyboards.
