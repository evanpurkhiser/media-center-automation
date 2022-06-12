## Media Center Automation

I have a very small media center in my bedroom with:

- [LG 47LB5900 47-Inch LED TV](http://www.lg.com/us/tvs/lg-47LB5900-led-tv)
- 2x [Micca MB42X Bookshelf speakers](http://www.miccatron.com/micca-mb42x/)
- [SMSL Q5 Amplifier](http://amzn.com/B00NLX5NRS)
- [Gigabyte GB-BXi5-5200 Ultra Compact PC](http://www.gigabyte.us/products/product-page.aspx?pid=5323#ov)
  - Samsung 850 EVO 120 GB mSATA
  - Kingston HyperX Impact Black 8GB Kit SODIMM

The PC is running a minimal arch linux installation with [Kodi](kodi.tv). I'm
using a [8Bitdo NES30 bluetooth controller](http://www.nes30.com/) to control
this setup. I also have a [IRToy
v2](http://dangerousprototypes.com/docs/USB_Infrared_Toy) connected to the PC
allowing me to control the TV and amp.

This repository contains some small tools and configurations I use to automate
my setup, with low power usage and convenience in mind.

- LIRC remote configurations for the SMSL Q5 Amp and LG TV.
- udev rule to apply the proper attribute to the NES30 bluetooth device
- Kodi keymapping for the NES30 bluetooth remote

For detailed specifics on the PC configuration [see the ansible
playbook](https://github.com/evanpurkhiser/ansible-personal/blob/main/htpc.yml)
used to provision it.

### Bluetooth connection status automation

The included `bt-power-listener` script is used to listen for connection status
changes for the NES30 controller. The idea is that the power status of the
controller should dicate the media center being 'in use' or not.

#### Power On:

- Start the Kodi standalone service using systemd
- Power on my TV and amp with lirc

Thes two actions will only happen under the condition that Kodi isn't already
started and playing a video.

#### Power Off:

- Stop the kodi standalone service using systemd
- Power off my TV and amp with lirc

These actions will only happen if Kodi is not currently playing any media. In
that case instead a notification will be displayed on screen to alert me to
turn the controller back on if it has disconnected.

### HDMI switcher Kodi script

This simple script is used to switch HDMI inputs on my TV. It will also suspend
the bluetooth controller power listener, so that turning off the controler (or
having it go into standby) will _not_ trigger the TV and amp to turn off.

The script will bring up a dialog where pressing "OK" will switch back to the
first input, this allows the workflow of:

1. Turn on Xbox or other device connected to HDMI-2
2. Run the hdmi.switcher script (Likely from a home menu item)
3. Use the device (game on!)
4. Turn the controller back on and press "A" for OK.

### Arch Linux installation

A PKGBUILD file is provided [in my PKGBUILDs repository](https://github.com/evanpurkhiser/PKGBUILDs/tree/main/media-center-automation)
