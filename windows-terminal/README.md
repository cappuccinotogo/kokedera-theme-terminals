# Kokedera for Windows Terminal

Create `%LOCALAPPDATA%\Microsoft\Windows Terminal\Fragments\Kokedera\` and copy `kokedera.json` there. Restart Windows Terminal, then select a Kokedera scheme under **Settings → your profile → Appearance → Color scheme**. The fragment adds nine schemes without changing existing profiles.

Alternatively, merge individual objects from `schemes/` into the `schemes` array of your existing `settings.json`. Set `"colorScheme": "Kokedera Dusk"` on the desired profile. Do not replace your settings file with a scheme or fragment.

## Variants

Kokedera Dusk (dark), Kokedera Morning (light), Kokedera Night (dark), Kokedera Spring (dark), Kokedera Summer (dark), Kokedera Autumn (dark), Kokedera Winter (light), Kokedera Rain (dark), Kokedera Mist (dark).

All formats use the same shared 16-color ANSI palette, foreground and background for each variant. Application-specific cursor, selection and UI behavior may differ.

## References

- [Windows Terminal documentation](https://learn.microsoft.com/en-us/windows/terminal/json-fragment-extensions)
- [Format reference](https://learn.microsoft.com/en-us/windows/terminal/customize-settings/color-schemes)
