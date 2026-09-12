# Kokedera for Alacritty

For current TOML-based Alacritty, copy a theme into your Alacritty configuration directory, for example `themes/kokedera-dusk.toml`. Add its path to the existing `[general]` `import` array:

```toml
[general]
import = ["themes/kokedera-dusk.toml"]
```

Keep any existing imports in the array and use only one `[general]` table. Configuration locations include `~/.config/alacritty/alacritty.toml` on Unix and `%APPDATA%\alacritty\alacritty.toml` on Windows. Explicit colors in your main file override imported colors. Older YAML-based releases need an upgrade.

## Variants

Kokedera Dusk (dark), Kokedera Morning (light), Kokedera Night (dark), Kokedera Spring (dark), Kokedera Summer (dark), Kokedera Autumn (dark), Kokedera Winter (light), Kokedera Rain (dark), Kokedera Mist (dark).

All formats use the same shared 16-color ANSI palette, foreground and background for each variant. Application-specific cursor, selection and UI behavior may differ.

## References

- [Alacritty documentation](https://alacritty.org/config-alacritty.html)
