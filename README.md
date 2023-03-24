# SC-88-Pro-Toolkit
EzoGaming's SC-88Pro Toolkit!!
This is my toolkit that I am working on to generate SysEx (System Exclusive) messages for the Roland Sound Canvas SC-88 Pro. I was originally only concerned with checksum generation.

See [Wiki](https://github.com/FlashlightET/SC-88-Pro-Toolkit/wiki) for some general info on SC-88Pro SysEx Events

## GUI
![image](https://user-images.githubusercontent.com/29938499/227429444-89ab70a9-d616-461d-88e7-f0eaa94371e8.png)
Gui is nowhere near complete but I'm trying to prototype it out. I have no experience with tkinter.

## Other Useful Tools
[Mido](https://github.com/mido/mido) - Python library for working with the MIDI interface and file format. Does not use F0 F7.

[MIDI-OX](http://www.midiox.com/) - Tool that can send SysEx events manually (however I find mido more convenient). Uses F0 F7.

[Sekaiju](https://openmidiproject.osdn.jp/Sekaiju_en.html) - MIDI editor with convenient event editing. Uses F0 F7.

[TMIDI Player](https://blackmidi.fandom.com/wiki/Software:TMIDI_Player) - MIDI player with visualization of parameters (plays at a slightly off speed)

[MIDIopsy](https://jeffbourdier.github.io/midiopsy/) - Barebones (and laggy) MIDI event editor. Does not use F0 F7.

[SC-88Pro LCD SysEx Generator](http://robbi-985.homeip.net/blog/?p=1352) - Generate SysEx for graphic pages and text with checksum. Also can decode graphic/text messages and fix their checksums.

## Sources for Information
SC-88 Pro Itself

[SomethingUnreal/Robbi-985](http://robbi-985.homeip.net/88pmidi/)

[Roland](https://cdn.roland.com/assets/media/pdf/SC-88PRO_OM.pdf)
