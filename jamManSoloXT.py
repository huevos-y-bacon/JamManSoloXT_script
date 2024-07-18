#!/usr/bin/env python3

import os

path = 'JamManSoloXT'

# Get a list of all the Patch## Folders
patchFolders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
patchFolders.sort()

# For each Patch## Folder:
for patchFolder in patchFolders:
    # Get a list of all the Phrase folders
    phraseFolders = [f for f in os.listdir(os.path.join(path, patchFolder)) if os.path.isdir(os.path.join(path, patchFolder, f))]
    phraseFolders.sort()
    
    # Delete patch.xml if it exists
    if os.path.exists(os.path.join(path, patchFolder, 'patch.xml')):
        try:
            print("Deleting", os.path.join(path, patchFolder, 'patch.xml'))
            os.remove(os.path.join(path, patchFolder, 'patch.xml'))
        except Exception:
            pass

    try:
        # Delete .DS_Store files
        os.remove(os.path.join(path, patchFolder, '.DS_Store'))
    except Exception:
        pass

    # For each Phrase folder:
    for phraseFolder in phraseFolders:
        # Rename phrase.xml to Patch##_phrase.xml
        try:
            print("Renaming", os.path.join(path, patchFolder, phraseFolder, 'phrase.xml'), "to", os.path.join(path, patchFolder + '_phrase.xml'))
            os.rename(os.path.join(path, patchFolder, phraseFolder, 'phrase.xml'), os.path.join(path, patchFolder + '_phrase.xml'))
        except Exception:
            pass

        # Rename phrase.wav to Patch##_phrase.wav
        try:
            print("Renaming", os.path.join(path, patchFolder, phraseFolder, 'phrase.wav'), "to", os.path.join(path, patchFolder + '_phrase.wav'))
            os.rename(os.path.join(path, patchFolder, phraseFolder, 'phrase.wav'), os.path.join(path, patchFolder + '_phrase.wav'))
        except Exception:
            pass

        # If the Phrase folder is empty, delete it
        if not os.listdir(os.path.join(path, patchFolder, phraseFolder)):
            print("Deleting", os.path.join(path, patchFolder, phraseFolder))
            os.rmdir(os.path.join(path, patchFolder, phraseFolder))

    # If the Patch## folder is empty, delete it
    if not os.listdir(os.path.join(path, patchFolder)):
        print("Deleting", os.path.join(path, patchFolder))
        os.rmdir(os.path.join(path, patchFolder))


# Get a list of all the Patch##_phrase.xml files
phraseFiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.endswith('_phrase.xml')]
phraseFiles.sort()

# For each Patch##_phrase.xml file:
for phraseFile in phraseFiles:
    # Read the file
    with open(os.path.join(path, phraseFile), 'r') as f:
        data = f.read()

    # Find the <BeatsPerMinute> tag
    bpm = data[data.find('<BeatsPerMinute>') + 16:data.find('</BeatsPerMinute>')]
    # Round bpm to 3 decimal places
    bpm = "{:.3f}".format(float(bpm))
    bpm = bpm.replace('.', '_')

    # Rename the file to Patch##_phrase_BPM###.###.xml
    try:
        print("Renaming", os.path.join(path, phraseFile), "to", os.path.join(path, phraseFile[:-4] + '_BPM' + bpm + '.xml'))
        os.rename(os.path.join(path, phraseFile), os.path.join(path, phraseFile[:-4] + '_BPM' + bpm + '.xml'))
    except Exception:
        pass

    # Rename the corresponding .wav file to Patch##_phrase_BPM###.###.wav
    try:
        print("Renaming", os.path.join(path, phraseFile[:-4] + '.wav'), "to", os.path.join(path, phraseFile[:-4] + '_BPM' + bpm + '.wav'))
        os.rename(os.path.join(path, phraseFile[:-4] + '.wav'), os.path.join(path, phraseFile[:-4] + '_BPM' + bpm + '.wav'))
    except Exception:
        pass

print("Done!")
