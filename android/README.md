# Android app

Kotlin + Jetpack Compose, MVVM. Fully on-device — **no server component**.

**Target device:** Flip 7 (Snapdragon 8 Elite) — expected to run whisper.cpp
`small`/`medium` comfortably on-device.

## Flow
1. BLE scan/connect to the recorder (GATT client)
2. Pull file list, then pull WAV files (chunked over BLE)
3. Queue files for on-device transcription via whisper.cpp Android bindings
4. Store transcripts in Room DB with FTS search
5. Notes screen: list, search, tap to read, export via share sheet

## Screens
- **Home** — device status / connect
- **Record** — recording list on the device
- **Sync & Transcribe** — pull + transcription queue/progress
- **Notes** — transcript list / search / export

> Android Studio project scaffolding not yet added. Generate the Gradle project
> into this directory (the `.gitignore` already excludes `build/`, `.gradle/`, etc.).
