[app]
title = Neon OS
package.name = neonos
package.domain = org.neon.os
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.2
requirements = python3,flet,google-genai,edge_tts,pyjnius
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.permissions = INTERNET,RECORD_AUDIO,QUERY_ALL_PACKAGES,READ_CONTACTS
android.api = 33
android.minapi = 21
android.ndk = 25b
