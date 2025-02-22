[app]

# (str) Title of your application
title = My ToDo App

# (str) Package name
package.name = mytodoapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
source.include_patterns =

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts =

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs =

# (list) List of exclusions using pattern matching
source.exclude_patterns =

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
version.regex =
version.filename =

# (list) Application requirements
requirements = python3,kivy

# (str) Custom source folders for requirements
#     Sets custom source for any requirements with recipes
#     sources.dirs = my_custom_sources

# (list) Garden requirements
garden_requirements =

# (str) Presplash of the application
presplash.filename = %(source.dir)s/splash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
services =

#
# OSX Specific
#

#
# author = © Copyright Info

# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
osx.kivy_version = 2.2.1

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for new android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
android.presplash_color = #FFFFFF

# (list) Permissions
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 24

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = org.kivy.android.PythonActivity

# (list) Pattern to whitelist for the whole project
android.whitelist =

# (str) Path to a custom whitelist file
# android.whitelist.src =

# (str) Path to a custom blacklist file
# android.blacklist.src =

# (list) Java classes to add to the project (can point to a .java file)
# android.add_java =

# (list) Gradle dependencies to add
# android.gradle_dependencies =

# (bool) Enable AndroidX support. Enable when 'android.useAndroidX' is yes in build.gradle
android.enable_androidx = True

# (list) Add java compile options
# android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

# (list) Gradle repositories to add
# android.gradle_repositories =

# (list) packaging options to add
# android.packaging_options =

# (list) Java system properties to set
# android.system_properties =

# (str) OUYA Console category. Should be one of GAME or APP
# android.ouya.category = GAME

# (str) Filename of OUYA Console icon
# android.ouya.icon.filename = %(source.dir)s/my-ouya-icon.png

# (str) XML file to include as an intent filters in <application> tag
# android.manifest.intent_filters =

# (list) Android additional libraries to copy into libs/armeabi
# android.add_libs_armeabi = libs/android/*.so
# android.add_libs_armeabi_v7a = libs/android-v7/*.so
# android.add_libs_arm64_v8a = libs/android-v8/*.so
# android.add_libs_x86 = libs/android-x86/*.so
# android.add_libs_mips = libs/android-mips/*.so

# (bool) Indicate whether the screen should stay on
# android.wakelock = False

# (list) Android application meta-data to set (key=value format)
# android.meta_data =

# (list) Android library project to add (will be added in the
# project.properties automatically.)
# android.library_references =

# (str) Android logcat filters to use
# android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a superjar
# android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = arm64-v8a

# (int) overrides automatic versionCode computation (used in build.gradle)
# this is not the same as version and must only contain numbers
# android.numeric_version = 1
