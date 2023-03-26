# SC-88-Pro-Toolkit
EzoGaming's SC-88Pro Toolkit!!
This is my toolkit that I am working on to generate SysEx (System Exclusive) messages for the Roland Sound Canvas SC-88 Pro. I was originally only concerned with checksum generation.

See [Wiki](https://github.com/FlashlightET/SC-88-Pro-Toolkit/wiki) for some general info on SC-88Pro SysEx Events

## GUI
![image](https://user-images.githubusercontent.com/29938499/227798474-816ad98c-06a3-4017-8de2-1af7c46b4a20.png)
Gui getting there.

Progress:
In Progress:
- EFX Type & Parameters (~~30-40% Done)
    - Parameter Defining
    - Default Values
    - Parameter Types
- System Resets (67% Done)
    - GS Done
    - 88 Done
    - GM Not done

Not Started:
- Turn on EFX
- EQ
- Global values
- System parameters
- Reverb
- Delay
- Chorus
- Draw
    - Will be for importing files, not a drawing screen as there is already a tool for that
- Write
- Part Parameters
- Scale Tuning

## Other Useful Tools
[Mido](https://github.com/mido/mido) - Python library for working with the MIDI interface and file format. Does not use F0 F7.

[MIDI-OX](http://www.midiox.com/) - Tool that can send SysEx events manually (however I find mido more convenient). Uses F0 F7.

[Sekaiju](https://openmidiproject.osdn.jp/Sekaiju_en.html) - MIDI editor with convenient event editing. Uses F0 F7.

[TMIDI Player](https://blackmidi.fandom.com/wiki/Software:TMIDI_Player) - MIDI player with visualization of parameters (plays at a slightly off speed)

[MIDIopsy](https://jeffbourdier.github.io/midiopsy/) - Barebones (and laggy) MIDI event editor. Does not use F0 F7.

[SC-88Pro LCD SysEx Generator](http://robbi-985.homeip.net/blog/?p=1352) - Generate SysEx for graphic pages and text with checksum. Also can decode graphic/text messages and fix their checksums.

[Serval Neso](https://www.amazon.com/gp/product/B075NL6YQ6) - Helps me make my midis sound good(? debatable)

## Sources for Information
SC-88 Pro Itself

[SomethingUnreal/Robbi-985](http://robbi-985.homeip.net/88pmidi/)

[Roland](https://cdn.roland.com/assets/media/pdf/SC-88PRO_OM.pdf)

## Future Ideas?
- MIDI Optimizer
    - Quantize pitch bend and CC events to be less frequent
    - Currently a dream due to how MIDI files are delta and I'm too confused by that to be able to write it
- SC-88 Lyrics Generator
    - Similar to the Audacity method used in [Bad Canvas](https://github.com/FlashlightET/BadCanvas) but the timing is correct
    - Convert lyric tracks into sc-88 text?
