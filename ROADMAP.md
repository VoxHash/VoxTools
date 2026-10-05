# Roadmap — VoxTools

High-level milestones aligned with the current 0.2.x codebase (CLI/TUI/GUI shell + files/crypto/devtools/image plugins).

## Near term (0.2.x)

### Stability & DX
- [ ] Register plugin Typer sub-apps so `voxtools <plugin> --help` works end-to-end
- [ ] Finish TUI plugin panels for all shipped plugins
- [ ] Finish GUI widgets for crypto/devtools beyond basic shells
- [ ] Harden optional-dependency plugin discovery (ai/media/net stubs)

### Docs & distribution
- [ ] Publish MkDocs site to GitHub Pages under the VoxTools repo name
- [ ] Ship pip/PyPI `voxtools` package when ready
- [ ] Cross-platform release binaries via existing release workflow

## Mid term (0.3.x)

### Plugin expansion
- [ ] Media plugin (FFmpeg): convert, thumbnails, metadata
- [ ] Network plugin: ping/DNS, HTTP probe, optional speedtest extra
- [ ] AI plugin: summarize/translate/codegen behind `VOXTOOLS_OPENAI_API_KEY`

### Developer experience
- [ ] Plugin scaffold template + docs generator
- [ ] Plugin test helpers in `tests/`
- [ ] Optional plugin marketplace/registry design doc

## Later

- [ ] Custom theme packs beyond system/light/dark
- [ ] Opt-in telemetry (off by default; already modeled in settings)
- [ ] Web UI only if CLI/TUI/GUI demand justifies it

---

Items move only when they match shipped code. Feedback: [SUPPORT.md](SUPPORT.md) · contact@voxhash.dev
