# V1 Engineering Preconfigured Marlin

This repository provides a preconfigured version of Marlin that is optimized for CNC and milling purposes.

## Getting started

TODO: Possibly links to download pre-built firmware.

## Building V1 Marlin

These scripts require the PlatformIO CLI and GNU `sed`

[Install PlatformIO](https://docs.platformio.org/en/latest/installation.html)

In order to generate the configuration you must first pull the Marlin submodule

```
git submodule update --init --recursive
```

Then generate the example configuration using the following script

```
UPSTREAM_BRANCH=2.0.x ./v1-scripts/pull-from-upstream
```

Then generate a firmware file by running

```
./v1-scripts/build-for-machine machine-name
```

Machine names are based on the folder and filename within `v1-scripts/configs`. For example, for the Archim board you would use `MPCNC/Archim1_T8_16T_LCD`.

The firmware file will be located in the `MarlinFirmware/.pio` directory.
