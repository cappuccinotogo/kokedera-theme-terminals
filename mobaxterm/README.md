# Kokedera for MobaXterm

Exit MobaXterm so it does not rewrite settings while you edit them. Back up your active `MobaXterm.ini` (the location depends on your portable/installed configuration). In that file, merge the desired theme’s values into the existing `[Colors]` section; create the section if absent. Keep all other sections, connection definitions and settings. Restart MobaXterm. Existing sessions with their own colors may need their color customization reset to the global scheme.

These are **INI snippets**, not complete MobaXterm configuration files. The key layout follows the established MobaXterm exports in iTerm2-Color-Schemes; MobaXterm’s public documentation describes color configuration but does not formally specify every INI key. Native runtime verification is still required for your release.

## Variants

Kokedera Dusk (dark), Kokedera Morning (light), Kokedera Night (dark), Kokedera Spring (dark), Kokedera Summer (dark), Kokedera Autumn (dark), Kokedera Winter (light), Kokedera Rain (dark), Kokedera Mist (dark).

All formats use the same shared 16-color ANSI palette, foreground and background for each variant. Application-specific cursor, selection and UI behavior may differ.

## References

- [MobaXterm documentation](https://mobaxterm.mobatek.net/documentation.html)
- [Format reference](https://github.com/mbadolato/iTerm2-Color-Schemes/tree/master/mobaxterm)
