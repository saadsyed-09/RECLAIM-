# RECLAIM Android Home Screen Widgets (GitHub patch)

Adds 3 launcher widgets (nominal 4x2): XP/Level, Streak, and Daily Missions. XP and Streak open Progress; Missions opens Quest. App identity stays RECLAIM / com.reclaim.app. Uses the root-level reclaim.png for launcher icon asset generation.

## Apply on GitHub (mobile)
- Upload/replace `index.html` at repo root.
- Upload the entire `android-widget/` directory preserving nested folders.
- Upload `scripts/install-android-widgets.py`.
- Replace `.github/workflows/android-apk.yml` with the version in this patch.
- Keep `reclaim.png` in the repo root.
- Commit, then Actions → Build RECLAIM Android APK → Run workflow.
- Install the downloaded debug APK. Long press home screen → Widgets → RECLAIM.

Widgets sync their cached values when the app saves/opens. Android launchers can slightly adjust widget dimensions. This patch has not been run against your actual GitHub repo or Nothing Phone; build/runtime verification is still needed. If the workflow fails, share the exact log.
