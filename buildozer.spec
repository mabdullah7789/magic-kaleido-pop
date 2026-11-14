# =============================================================================
# Buildozer Specification File for Google Play Store (.aab Release)
# Docs: https://kivy.org/doc/stable/guide/packaging-android.html
# PyPI: https://pypi.org/project/buildozer/
# Target API Policy: https://support.google.com/googleplay/android-developer/answer/11926878?hl=en
# =============================================================================

[app]

# (str) Title of your application
title = Magic Kaleido-Pop Studio

# (str) Package name
package.name = kaleidopop

# (str) Package domain (must be unique on Google Play Store, e.g. org.yourname)
package.domain = org.abdullahstudios

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy==2.3.1

# (str) Supported orientation (portrait, landscape, or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Presplash background color
android.presplash_color = #0D0D1A

# =============================================================================
# Android & Google Play Store Specific Settings
# =============================================================================

# (int) Target Android API, should be as high as possible.
# Starting August 31, 2026, Google Play requires new mobile apps to target
# Android 16 (API level 36) or higher (previously Android 15 / API level 35).
android.api = 36

# (int) Minimum API your APK / AAB will support (Android 7.0+)
android.minapi = 24

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Automatically accept SDK license agreements during automated builds
android.accept_sdk_license = True

# (list) The Android archs to build for.
# Google Play requires 64-bit support (arm64-v8a). Including both ensures wide compatibility.
android.archs = arm64-v8a, armeabi-v7a

# (str) Format of the release artifact: 'aab' is mandatory for new Google Play apps
android.release_artifact = aab

# (str) Format of the debug artifact: 'apk' for quick testing on your own phone
android.debug_artifact = apk

# (list) Permissions
# Kept empty! Apps targeting children & families under Google Play's Families Policy
# should not request unnecessary permissions or transmit Android Advertising IDs (AAID).
# See: https://support.google.com/googleplay/android-developer/answer/11043825?hl=en
android.permissions =

# (bool) Enables Android backup
android.allow_backup = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
