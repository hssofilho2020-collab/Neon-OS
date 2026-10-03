[app]
title = Neon OS
package.name = neonos
package.domain = org.neon.os
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 28c
android.accept_sdk_license_agreements = True
android.ant_path = /home/runner/.buildozer/android/platform/apache-ant-1.9.4/bin/ant
p4a.branch = master
