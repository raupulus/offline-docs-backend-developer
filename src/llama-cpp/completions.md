---
title: Completions
source_repo: ggml-org/llama.cpp
source_ref: master
source_commit: 4c9233c03
source_path: completions.md
technology: llama-cpp
version: master
license: MIT
retrieved_at: '2026-09-15'
order: 230
---

# Completions

Command-line completion is available for some environments.

## Bash Completion

```bash
$ build/bin/llama-cli --completion-bash > ~/.llama-completion.bash
$ source ~/.llama-completion.bash
```

Optionally this can be added to your `.bashrc` or `.bash_profile` to load it
automatically. For example:

```console
$ echo "source ~/.llama-completion.bash" >> ~/.bashrc
```
