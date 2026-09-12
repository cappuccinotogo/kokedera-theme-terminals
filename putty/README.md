# Kokedera for PuTTY

The `.reg` files add color-only sessions named **Kokedera Dusk**, etc., under your own Windows user account. Inspect the file, then import it with Registry Editor (or double-click and accept Windows’ import prompt). Open PuTTY, load the new Kokedera session, enter your host and connection settings, and save it under a connection-specific name.

The import does not modify **Default Settings** or other named sessions. Reimporting a file updates colors in the matching Kokedera session, so export that key first if you customized it. Foreground/background, cursor and all 16 ANSI colors are mapped to PuTTY’s interleaved normal/bold color indices. Selection is managed by PuTTY.

## Variants

Kokedera Dusk (dark), Kokedera Morning (light), Kokedera Night (dark), Kokedera Spring (dark), Kokedera Summer (dark), Kokedera Autumn (dark), Kokedera Winter (light), Kokedera Rain (dark), Kokedera Mist (dark).

All formats use the same shared 16-color ANSI palette, foreground and background for each variant. Application-specific cursor, selection and UI behavior may differ.

## References

- [PuTTY documentation](https://www.chiark.greenend.org.uk/~sgtatham/putty/0.83/htmldoc/Chapter4.html#config-colours)
- [Format reference](https://git.tartarus.org/?p=simon/putty.git;a=blob;f=doc/pterm.but;hb=HEAD)
