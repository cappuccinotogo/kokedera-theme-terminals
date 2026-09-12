# Kokedera for Terminator

Close Terminator before editing `~/.config/terminator/config`. Make a backup, then insert the chosen file’s `[[Kokedera Dusk]]` block inside your existing `[profiles]` section. If no `[profiles]` section exists, create it once. Keep existing profiles and all other sections. Restart Terminator and choose the new profile from its context menu or Preferences.

These fragments use current `cursor_bg_color` / `cursor_fg_color` keys. They disable inherited system colors for the new profile. Selection colors are controlled by VTE/Terminator.

## Variants

Kokedera Dusk (dark), Kokedera Morning (light), Kokedera Night (dark), Kokedera Spring (dark), Kokedera Summer (dark), Kokedera Autumn (dark), Kokedera Winter (light), Kokedera Rain (dark), Kokedera Mist (dark).

All formats use the same shared 16-color ANSI palette, foreground and background for each variant. Application-specific cursor, selection and UI behavior may differ.

## References

- [Terminator documentation](https://gnome-terminator.readthedocs.io/en/latest/config.html)
- [Format reference](https://github.com/gnome-terminator/terminator/blob/master/terminatorlib/config.py)
