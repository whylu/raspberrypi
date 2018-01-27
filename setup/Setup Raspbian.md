# Install OS
1. Download raspbian image from : https://www.raspberrypi.org/downloads/raspbian/
2. Download [Etcher](https://etcher.io/) and install it.
3. Open Etcher and select from your hard drive the Raspberry Pi .img or  .zip file you wish to write to the SD card.
4. Select the SD card you wish to write your image to.
5. Review your selections and click 'Flash!' to begin writing data to the SD card.

ref:
* [installation guide.](https://www.raspberrypi.org/documentation/installation/installing-images/README.md)

# SSH setup
For headless setup, SSH can be enabled by placing a file named ssh, without any extension, onto the boot partition of the SD card from another computer. When the Pi boots, it looks for the ssh file. If it is found, SSH is enabled and the file is deleted. The content of the file does not matter; it could contain text, or nothing at all.

If you have loaded Raspbian onto a blank SD card, you will have two partitions. The first one, which is the smaller one, is the boot partition. Place the file into this one.


default name: pi  
default password: baspberry

[change passowrd](https://www.raspberrypi.org/documentation/linux/usage/users.md)
```bash
passwd
```

ref: 
* [ssh](https://www.raspberrypi.org/documentation/remote-access/ssh/)
* [about user](https://www.raspberrypi.org/documentation/linux/usage/users.md)

# VNC
You can enable VNC Server at the command line using [raspi-config](https://www.raspberrypi.org/documentation/configuration/raspi-config.md):
```bash
sudo raspi-config
```
Now, enable VNC Server by doing the following:  
  \- Navigate to Interfacing Options.  
  \- Scroll down and select VNC > Yes.




# Timezone


# 
