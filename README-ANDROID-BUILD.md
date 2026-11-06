# RECLAIM v0.9 Android build

This is the polished web project prepared for Capacitor. It is not an APK yet.

## Build APK
1. Install Node.js and Android Studio (Android SDK).
2. Extract this folder and open a terminal inside it.
3. Run `npm install`
4. Run `npx cap add android`
5. Run `npx cap sync android`
6. Run `npx cap open android`
7. In Android Studio: Build > Build Bundle(s) / APK(s) > Build APK(s)

App ID: `com.reclaim.app`
App name: `RECLAIM`

Before publishing, test on the target Android phone. This package has not been built or device-tested as an APK in this environment.


## Phone-only APK build (cloud builder)

This project is a Capacitor web app. A cloud ZIP-to-APK builder may package it as a WebView app, but check whether it supports Capacitor projects and whether it includes the required app files. Do not upload source to a service unless you are comfortable with its privacy policy. Keep your app signing key private and backed up.

For a simple personal APK, use a reputable builder that supports uploading a ZIP and custom launcher icon. Set app name to RECLAIM and package ID to `com.reclaim.app`. Upload the project ZIP, select the new RECLAIM icon, build, download the APK, then scan it with Play Protect before installing.
