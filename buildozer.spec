[app]
title = Neon Bixby
package.name = neonbixby
package.domain = com.neon.bixby
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1
requirements = python3==3.11.6,kivy==2.3.0
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
android.ant = auto
