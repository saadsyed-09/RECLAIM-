# RECLAIM — GitHub Actions APK build (phone-friendly)

This ZIP contains the RECLAIM web app and a GitHub Actions workflow to build a debug APK in GitHub's cloud runner. No Android Studio or laptop is needed for the build itself.

## Build from your phone

1. Extract this ZIP on your phone if needed, or upload the ZIP contents to a new GitHub repository (the files must be at the repository root; do not upload the ZIP as a single file).
2. Create a repository named `RECLAIM` and upload all files/folders from this project. Ensure `.github/workflows/android-apk.yml` is included.
3. In GitHub, open **Actions**. If prompted, enable Actions for the repository.
4. Select **Build RECLAIM Android APK** in the left panel, tap **Run workflow**, choose `main`, then run it.
5. Wait for the workflow to finish. Open the completed run and scroll to **Artifacts**. Download `RECLAIM-debug-APK`.
6. Extract the artifact ZIP and install `app-debug.apk` on your Nothing Phone 3a. Android may ask you to allow installing apps from that browser/file manager.

## Important
- This produces a **debug APK for personal testing**, not a Play Store release.
- The APK is not signed with a private release key.
- GitHub Actions build must complete successfully; no APK is included in this source ZIP.
- Keep the repository private if you want your source code private. Never commit passwords, API keys, or signing keystores.
- If build fails, open the failed workflow run and share the error log/screenshot.
