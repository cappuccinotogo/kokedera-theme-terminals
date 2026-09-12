# Kokedera for WezTerm

Copy the desired TOML files into `~/.config/wezterm/colors/`, or add the absolute path to this folder to your existing `config.color_scheme_dirs` list. Then add this before `return config` in your existing `wezterm.lua`:

```lua
config.color_scheme = "Kokedera Dusk"
```

For another directory, append it to `config.color_scheme_dirs`; keep your other directories. Local `config.colors` settings can override a scheme. The `metadata.name` in each file defines the selectable name.

## Variants

Kokedera Dusk (dark), Kokedera Morning (light), Kokedera Night (dark), Kokedera Spring (dark), Kokedera Summer (dark), Kokedera Autumn (dark), Kokedera Winter (light), Kokedera Rain (dark), Kokedera Mist (dark).

All formats use the same shared 16-color ANSI palette, foreground and background for each variant. Application-specific cursor, selection and UI behavior may differ.

## References

- [WezTerm documentation](https://wezterm.org/config/appearance.html)
