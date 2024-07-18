# JamManSoloXT

## Purpose

Process each folder in the JamManSoloXT folder, move files, delete files, read files, move/rename files into a flat folder, with each filename reflecting the tempo and length of the file.

## Overview of script functionality

The folder JamManSoloXT contains a structure like this:
- `Patch##/patch.xml` # i.e. Patch01 thru Patch30
- `Patch##/PhraseA/phrase.xml`
- `Patch##/PhraseA/phrase.wav`

### Part 1:

For each `Patch##` folder:
- `patch.xml` can be discarded
- `phrase.xml` should be renamed to `Patch##_phrase.xml`
- `phrase.wav` should be renamed to `Patch##_phrase.wav`

For each `Patch##` folder:
- delete `patch.xml`

For each Phrase folder:
- Rename `phrase.xml` to `Patch##_phrase.xml`
- Rename `phrase.wav` to `Patch##_phrase.wav`

### Part 2:

For each `Patch##_phrase.xml` file:
- Read the file
- Find the `<JamManPhrase>/<BeatsPerMinute>` tag
- Round the value to 3 decimal places
- Rename the file to `Patch##_phrase_BPM###.###.xml`
- Rename the corresponding .wav file to `Patch##_phrase_BPM###.###.wav`

## Example output

```bash
❯ ./jamManSoloXT.py
Deleting JamManSoloXT/Patch01/patch.xml
Renaming JamManSoloXT/Patch01/PhraseA/phrase.xml to JamManSoloXT/Patch01_phrase.xml
Renaming JamManSoloXT/Patch01/PhraseA/phrase.wav to JamManSoloXT/Patch01_phrase.wav
Deleting JamManSoloXT/Patch01/PhraseA
Deleting JamManSoloXT/Patch01
Deleting JamManSoloXT/Patch02/patch.xml
Renaming JamManSoloXT/Patch02/PhraseA/phrase.xml to JamManSoloXT/Patch02_phrase.xml
Renaming JamManSoloXT/Patch02/PhraseA/phrase.wav to JamManSoloXT/Patch02_phrase.wav
Deleting JamManSoloXT/Patch02/PhraseA
Deleting JamManSoloXT/Patch02
Deleting JamManSoloXT/Patch03/patch.xml
Renaming JamManSoloXT/Patch03/PhraseA/phrase.xml to JamManSoloXT/Patch03_phrase.xml
Renaming JamManSoloXT/Patch03/PhraseA/phrase.wav to JamManSoloXT/Patch03_phrase.wav
Deleting JamManSoloXT/Patch03/PhraseA
Deleting JamManSoloXT/Patch03
Deleting JamManSoloXT/Patch04/patch.xml
Renaming JamManSoloXT/Patch04/PhraseA/phrase.xml to JamManSoloXT/Patch04_phrase.xml
Renaming JamManSoloXT/Patch04/PhraseA/phrase.wav to JamManSoloXT/Patch04_phrase.wav
Deleting JamManSoloXT/Patch04/PhraseA
Deleting JamManSoloXT/Patch04
Deleting JamManSoloXT/Patch05/patch.xml
Renaming JamManSoloXT/Patch05/PhraseA/phrase.xml to JamManSoloXT/Patch05_phrase.xml
Renaming JamManSoloXT/Patch05/PhraseA/phrase.wav to JamManSoloXT/Patch05_phrase.wav
Deleting JamManSoloXT/Patch05/PhraseA
Deleting JamManSoloXT/Patch05
Renaming JamManSoloXT/Patch01_phrase.xml to JamManSoloXT/Patch01_phrase_BPM104_530.xml
Renaming JamManSoloXT/Patch01_phrase.wav to JamManSoloXT/Patch01_phrase_BPM104_530.wav
Renaming JamManSoloXT/Patch02_phrase.xml to JamManSoloXT/Patch02_phrase_BPM104_530.xml
Renaming JamManSoloXT/Patch02_phrase.wav to JamManSoloXT/Patch02_phrase_BPM104_530.wav
Renaming JamManSoloXT/Patch03_phrase.xml to JamManSoloXT/Patch03_phrase_BPM104_895.xml
Renaming JamManSoloXT/Patch03_phrase.wav to JamManSoloXT/Patch03_phrase_BPM104_895.wav
Renaming JamManSoloXT/Patch04_phrase.xml to JamManSoloXT/Patch04_phrase_BPM104_895.xml
Renaming JamManSoloXT/Patch04_phrase.wav to JamManSoloXT/Patch04_phrase_BPM104_895.wav
Renaming JamManSoloXT/Patch05_phrase.xml to JamManSoloXT/Patch05_phrase_BPM104_895.xml
Renaming JamManSoloXT/Patch05_phrase.wav to JamManSoloXT/Patch05_phrase_BPM104_895.wav
Done!
```
