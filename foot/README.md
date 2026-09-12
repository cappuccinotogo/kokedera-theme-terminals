# Kokedera for foot

These files target **foot 1.26 or newer**, using the current `[colors-dark]` / `[colors-light]` sections. Copy the chosen file to `~/.config/foot/themes/`, then add this in the main section at the top of your existing `foot.ini` (before any section headers):

```ini
include=~/.config/foot/themes/kokedera-dusk.ini
```

Each theme selects its corresponding `initial-color-theme` and defines that color section. Start a new foot window; if using the server, restart it when convenient. Existing color definitions after the include override the theme. For older foot, upgrade or rename the theme’s color section to `[colors]` and remove `initial-color-theme`; do not use the legacy section on foot 1.28+.

## Variants

Kokedera Dusk (dark), Kokedera Morning (light), Kokedera Night (dark), Kokedera Spring (dark), Kokedera Summer (dark), Kokedera Autumn (dark), Kokedera Winter (light), Kokedera Rain (dark), Kokedera Mist (dark).

All formats use the same shared 16-color ANSI palette, foreground and background for each variant. Application-specific cursor, selection and UI behavior may differ.

## References

- [foot documentation](https://codeberg.org/dnkl/foot/src/branch/master/doc/foot.ini.5.scd)
