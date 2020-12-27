#rpm_device is the name of the ported device
%define rpm_device bullhead
#rpm_vendor is used in the rpm space
%define rpm_vendor lge
#Manufacturer and device name to be shown in UI
%define vendor_pretty LG
%define device_pretty Nexus 5x
%define have_vibrator_native 1
%define have_led 1
%include droid-hal-version/droid-hal-version.inc
