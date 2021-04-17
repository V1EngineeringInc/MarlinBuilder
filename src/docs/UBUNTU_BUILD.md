# Local development build [Ubuntu Linux / Windows WSL2]

__Ensure you have the dependencies.__

## For windows install WSL2
https://docs.microsoft.com/en-us/windows/wsl/install-win10

## _Install Python_ 
```
sudo apt update
sudo apt install python3 python3-pip python3-virtualenv
```

## _Setup Python virtual environment and Install PlatformIO_
```
virtualenv -p python3 .venv
source .venv/bin/activate
pip install platformio
```

## _Checkout Marlin_
```
git clone git@github.com:MarlinFirmware/Marlin.git Marlin -b bugfix-2.0.x --depth 1
```

## _Run build steps_
For each machine you want to target, replace V1CNC_ConfigName with the machine config. (eg. V1CNC_SkrPro_DualLR_2209)
```
source .venv/bin/activate
src/core/config-for-machine V1CNC_ConfigName
src/core/build-for-machine
```

## _Post build cleanup_
Optional but helps when getting build errors between different configurations
```
cd Marlin
git checkout .
git reset --hard
git clean -f
cd ..
```
