import xbmc
import xbmcgui
import time
import dbus

suspend_bt_listener = dbus.SystemBus() \
    .get_object('htpc.bt_power_listener', '/htpc/bt_power_listener') \
    .get_dbus_method('suspend', 'htpc.bt_power_listener')

description = 'After switching the remote can be turned off without causing ' \
              'the media center to power down. To return to Kodi press OK ' \
              'on your controller.'

# Prompt to continue HDMI switch
if not xbmcgui.Dialog().yesno("Switch to HDMI-2?", description):
    exit()

# Switch HDMI Input and set the bt-power-listener to suspend mode
xbmc.executebuiltin('LIRC.Send(SEND_ONCE LG_AKB73975711 INPUT)')
xbmc.executebuiltin('LIRC.Send(SEND_ONCE LG_AKB73975711 RIGHT)')
xbmc.executebuiltin('LIRC.Send(SEND_ONCE LG_AKB73975711 OK)')
suspend_bt_listener(True)

# Wait for input to return to kodi
xbmcgui.Dialog().ok("Return to HDMI-1", "Press OK to return to HDMI-1")

# Switch HDMI back and turn the bt-power-listener back on
xbmc.executebuiltin('LIRC.Send(SEND_ONCE LG_AKB73975711 INPUT)')
xbmc.executebuiltin('LIRC.Send(SEND_ONCE LG_AKB73975711 LEFT)')
xbmc.executebuiltin('LIRC.Send(SEND_ONCE LG_AKB73975711 OK)')
suspend_bt_listener(False)
