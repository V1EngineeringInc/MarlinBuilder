## Development/Understanding these scripts.

Start with the .github/workflows/builds.yml file. That tells github when to start a build, and which
steps to take to complete a particular build.

These are the main steps:
 - Check out a fresh copy of the MarlinFirmware.
 - Call "config-for-machine", which will change the Configuration.h, Configuration_adv.h, etc. for
     that particular machine.
     - This calls a particular machine setup file, like src/configs/V1CNC_Rambo_Dual
     - This calls specific groups of configs, such as configuring it for a CNC, rambo specific
         choices, and accessories such as an LCD and dual endstops.
 - Call platformio to verify the build works (test) and produce a firmware file.
 - Collect the Marlin folder and zip it up. Also collect the firmware file.

To really take a deep look at how Marlin gets set up for a particular build configuration, take a
look at src/configs/V1CNC_Rambo_Dual, and then find each file it uses to configure Marlin, such as
src/configs/boards/rambo.

The configs are broken into different categories:
 - common:
     - v1-base-config: which changes some names to V1, and sets the Bootscreen.h.
     - cnc, 3dp, zxy: Run one of these to set the machine type.
 - boards:
     - Each board type has a file here for configuring the build for that particular board.
     - This can get a little messy, because a titan aero extruder has different steps/mm on a mini
         rambo than on a ramps.
 - accessories:
     - These are board and machine type "independent" features. For example, dual endstops, or
         aero-extruder

If you want to change any of the configurations, make the appropriate changes to the configs/
scripts, push to a new branch, and then let github actions build a .zip for you. Download the zip,
and look at the Configuration files it produced. You should then also do a runtime test by flashing
the board with the firmware file, or flash it through arduino.

Don't forget to set the version number in src/core/version. I don't have a good way to do that
automatically.

## Local builds

If you want to use these scripts to configure Marlin on your local machine, then read the instructions here:

- [Windows WSL2](UBUNTU_BUILD.md)
- [Ubuntu Linux](UBUNTU_BUILD.md)
