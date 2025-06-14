# Technical Context: RapTrainer

## Core Technologies
- **Primary Language**: Python
- **Primary Platform**: Notion. The entire system is built upon Notion's databases and API.
- **Notion Integration**: `notion-client` Python library is the key bridge for any potential automation.
- **Environment Management**: `python-dotenv` for managing environment variables (like API keys).

## Technologies for "Quick Capture" Workflow
The "quick capture" feature will likely rely on existing integrations rather than custom code initially.
- **Potential Solutions**:
  - **Native Notion Features**: Utilizing the mobile app's "Share Sheet" functionality on iOS/Android.
  - **No-Code Automation**: Services like `Zapier` or `IFTTT` to create workflows (e.g., "Email to Notion," "Telegram message to Notion").
  - **Platform-Specific Scripting**: `iOS Shortcuts` could be used to build a custom input form that talks to the Notion API.

## Future/Deprioritized Technologies
- **Hebrew Phonetics**: The `phonikud` library is no longer a priority, as rhyme grouping will be manual.
- **MIDI Interaction**: Libraries like `mido` are not needed for the core product but would be required for the "Freestyle Capture" tool in the future.
- **Audio Recording**: Libraries like `sounddevice` are also on hold until the "Freestyle Capture" tool is revisited.

## Required Technologies for "Freestyle Capture" Tool
The high-priority feature will require expanding the tech stack.

- **Desktop Application Framework (Optional but likely)**: To package the tool for easy background execution.
  - **Potential Candidates**: `PyQt`, `Tkinter`, or a lighter solution using a library like `pystray` for a system tray icon.
- **YouTube Integration (Complex Future Goal)**:
  - **Option 1 (Browser Extension)**: Requires JS, HTML, CSS and a way to communicate with the Python backend.
  - **Option 2 (In-App Player)**: Could use a library like `pytube` for getting stream data, but playing it might require a GUI framework (e.g., PyQt with a web view).

## Initial Tech Stack Decision
The initial MVP (`Freestyle Capture` audio-only) will be a Python script focusing on:
1.  **MIDI input** (`mido` is a strong first choice).
2.  **Audio recording and buffering** (`sounddevice` is a good candidate).
3.  Saving the buffer to a file (e.g., `.wav` or `.mp3` via another library like `pydub`).
4.  Optionally, integration with the `notion-client` to upload the captured file. 