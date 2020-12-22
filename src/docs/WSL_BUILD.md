# Local development build [Ubuntu Linux / WSL2]

Make sure you have the dependencies.
- Install Python 
```
sudo apt update
sudo apt install python3 python3-pip
```
- Add the following lines to your ~/.bashrc file: 
```
alias python=python
alias pip=pip3
```
- Checkout Marlin
```
git clone git@github.com:MarlinFirmware/Marlin.git Marlin
cd Marlin
git checkout bugfix-2.0.x
cd ..
```
- Run build steps (for each machine you want to target)
```
src/core/config-for-machine V1CNC_SkrPro_DualLR_2209
src/core/build-for-machine
```