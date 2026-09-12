# Kokedera for Termux

In Termux, create `~/.termux/` if needed. Back up your current `~/.termux/colors.properties`, then merge the chosen `.properties` file’s `foreground`, `background`, `cursor` and `color0`–`color15` entries into it, keeping any other settings. If the file does not exist, copy the chosen file there as `colors.properties`. Run:

```sh
termux-reload-settings
```

The colors are local configuration and do not require the Termux:Styling add-on. The Android UI and selection handles follow Termux/Android settings.

## Variants

Kokedera Dusk (dark), Kokedera Morning (light), Kokedera Night (dark), Kokedera Spring (dark), Kokedera Summer (dark), Kokedera Autumn (dark), Kokedera Winter (light), Kokedera Rain (dark), Kokedera Mist (dark).

All formats use the same shared 16-color ANSI palette, foreground and background for each variant. Application-specific cursor, selection and UI behavior may differ.

## References

- [Termux documentation](https://github.com/termux/termux-app/blob/master/terminal-emulator/src/main/java/com/termux/terminal/TerminalColorScheme.java)
- [Format reference](https://github.com/termux/termux-styling)
