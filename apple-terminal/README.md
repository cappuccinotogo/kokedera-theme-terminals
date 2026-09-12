# Kokedera for Apple Terminal

Open **Terminal → Settings → Profiles**, open the action menu below the profile list, choose **Import**, and select a `.terminal` file. Choose the new Kokedera profile for a window or make it your default. Importing adds a profile.

The files contain the 16 ANSI colors, text, background, selection and cursor as native archived `NSColor` values. Apple Terminal controls selected-text foreground itself; that field cannot be kept identical to terminals that expose a separate selection foreground. Colors use Terminal’s native device-RGB archive representation, so display color management can differ slightly from sRGB-aware applications.

## Variants

Kokedera Dusk (dark), Kokedera Morning (light), Kokedera Night (dark), Kokedera Spring (dark), Kokedera Summer (dark), Kokedera Autumn (dark), Kokedera Winter (light), Kokedera Rain (dark), Kokedera Mist (dark).

All formats use the same shared 16-color ANSI palette, foreground and background for each variant. Application-specific cursor, selection and UI behavior may differ.

## References

- [Apple Terminal documentation](https://support.apple.com/guide/terminal/import-and-export-terminal-profiles-trml4299c696/mac)
- [Format reference](https://github.com/mbadolato/iTerm2-Color-Schemes/tree/master/terminal)
