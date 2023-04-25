# Android Dynamic Feature Modules : The Future
## What is Dynamic Delivery?
Google Play uses your app bundle to generate and serve optimized APKs for each user’s device configuration, so they download only the code and resources they need to run your app.

Through Dynamic Delivery, users can then download and install app’s dynamic features on demand after they’ve already installed the base APK of your app. As a result, the initial download size of your app is less and users don’t need unused code/features in their devices.

## Dynamic Delivery with split APKs
Split APKs are very similar to regular APKs. However, the Android platform is able to treat multiple installed split APKs as a single app.
- **Base APK**: this APK contains code and resources that all other split APKs can access and provides the basic functionality for your app.
- **Configuration APKs**: each of these APKs includes native libraries and resources for a specific screen density, CPU architecture, or language. When a user downloads your app, their device downloads and installs only the configuration APKs that target their device.
- **Dynamic Feature APKs**: each of these APKs contains code and resources for a feature of your app that is not required when your app is first installed.

## What are Dynamic Feature Modules?
Dynamic Feature Modules allow you to separate certain features and resources from the base module of your app and include them in your app bundle. Users can download and install these modules later on demand after they’ve already installed the base APK of the app using Dynamic Delivery.

## Downloading dynamic feature modules
With Google Play Core Library, your app can download dynamic feature modules on demand to devices running Android 5.0 (API level 21) and higher. You can also use this API to download on demand modules for your Android Instant Apps.

# Exploring Dynamic Feature Modules
## Estructura de Android App Bunde (.aab)

## Características Dynamic Feature Modules
En vez de que la aplicación dependa de la característica, la característica depende de la aplicación (_Añadir imagen del minuto 4:15_). La aplicación puede compilar sin esa característica.

### ¿Cuándo utilizar Dynamic Feature modules?
Es recomendable utilizar Dynamic Feature Modules cuando la aplicación es de un gran tamaño, es decir, para ahorrar espacio. También es recomendable utilizar Dynamic Feature Modules cuando el equipo de trabajo es muy grande, ya que permite dividir en grupos que trabajarán en las diferentes características y son fáciles de "unir" a la aplicación.

[_He dejado el vídeo en el minuto 21:54_]

## References
- Android Dynamic Feature Modules : The Future - [medium.com](https://medium.com/mindorks/dynamic-feature-modules-the-future-4bee124c0f1)
- Exploring Dynamic Feature Modules - [droidcon.com](https://www.droidcon.com/2022/09/30/exploring-dynamic-feature-modules/)
  - [github.com/AlecStrong/boxapp](https://github.com/AlecStrong/boxapp)
    - [https://github.com/AlecStrong](https://github.com/AlecStrong)

## Articles of interest
- On Demand Modules - [developer.android.com](https://developer.android.com/codelabs/on-demand-dynamic-delivery#0)
