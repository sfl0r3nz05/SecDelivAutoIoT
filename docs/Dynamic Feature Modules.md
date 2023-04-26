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
<img src="https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/images/Captura%20estructura%20aab.PNG" alt="Estructura .abb" width="75%" height="75%">

## Características Dynamic Feature Modules
En vez de que la aplicación dependa de la característica, la característica depende de la aplicación. La aplicación puede compilar sin esa característica.

<img src="https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/images/Captura%20feature%20depende%20de%20app.PNG" alt="Feature depende de app">

### ¿Cuándo utilizar Dynamic Feature modules?
Es recomendable utilizar Dynamic Feature Modules cuando la aplicación es de un gran tamaño, es decir, para ahorrar espacio. También es recomendable utilizar Dynamic Feature Modules cuando el equipo de trabajo es muy grande, ya que permite dividir en grupos que trabajarán en las diferentes características y son fáciles de "unir" a la aplicación.

Dynamic feature Modules introduce una nueva forma de tener dependencias entre módulos. Antes tenía que estar todo en el módulo de la aplicación, ahora es posible tener dos módulos desaclopados. No puedes separar dos features que dependan de la misma librería.

<img src="https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/images/Captura%20diferentes%20modulos.PNG" alt="Diferentes módulos">

# Dynamic Feature Modules (características importantes)
- Los módulos dinámicos sólo se descargan a medida que el usuario lo vaya necesitando.
- Se pueden desintalar los Dynamic feature Modules. Manualmente (como una aplicación, en ajustes) o eliminados automáticamente por el sistema operativo.
- Por defecto, la descarga del Dynamic Feature Module se muestra en la barra de notificaciones.
- En Dynamic Feature Modules, sólo se actualizan los módulos instalados que tengan una actualización, si no tiene actualización no se actualiza. Sin Dynamic Feature Modules, se tiene que actualizar la aplicación al completo.
- Con Dynamic Feature Modules, se puede utilizar la aplicación base mientras que se descargan los módulos dinámicos.
- La idea es que cada módulo funcionan como APK diferentes sólo que se hace referencia desde la aplicación base.

# References
- Android Dynamic Feature Modules : The Future - [medium.com](https://medium.com/mindorks/dynamic-feature-modules-the-future-4bee124c0f1)
- Exploring Dynamic Feature Modules - [droidcon.com](https://www.droidcon.com/2022/09/30/exploring-dynamic-feature-modules/)
  - [github.com/AlecStrong/boxapp](https://github.com/AlecStrong/boxapp)
    - [https://github.com/AlecStrong](https://github.com/AlecStrong)
- Descripción general de la entrega de funciones en Play - [developer.android.com](https://developer.android.com/guide/playcore/feature-delivery?hl=es-419)

# Articles of interest
- On Demand Modules - [developer.android.com](https://developer.android.com/codelabs/on-demand-dynamic-delivery#0)
- Navigation in feature modules - MAD Skills - [youtube.com](https://www.youtube.com/watch?v=iURWvHxTM3k&ab_channel=AndroidDevelopers)
- How to Implement Dynamic Feature Module / Play Feature Module - Android Java and Kotlin - [youtube.com](https://www.youtube.com/watch?v=1-lf13pRLNo&t=225s&ab_channel=BiLalZurmati)
