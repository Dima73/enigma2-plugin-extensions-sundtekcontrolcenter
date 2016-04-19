#
#  sundtek control center
#  coded by giro77
#  support: http://www.i-have-a-dreambox.com
#
#
#  This plugin is licensed under the Creative Commons 
#  Attribution-NonCommercial-ShareAlike 3.0 Unported License.
#  To view a copy of this license, please visit
#  http://creativecommons.org/licenses/by-nc-sa/3.0/ or send a letter to Creative
#  Commons, 559 Nathan Abbott Way, Stanford, California 94305, USA.
#
#  Alternatively, this plugin may be distributed 
#  with devices from sundtek ltd. or sundtek germany.
#
#  This plugin is NOT free software. It is open source, you are allowed to
#  modify it (if you keep the license), but it may not be commercially 
#  distributed other than under the conditions noted above. 
#
#  Sundtek Control Center Plugin is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
#

from . import _
from Plugins.Plugin import PluginDescriptor
from Components.config import config
import SundtekControlCenter

####################################################################

def main(session, **kwargs):
    try:
        session.open(SundtekControlCenter.SundtekControlCenter)
    except:
        import traceback
        traceback.print_exc()

def SundtekControlCenterStart(menuid):
    if (config.plugins.SundtekControlCenter.display.value == "2" or config.plugins.SundtekControlCenter.display.value == "3") and (menuid == "scan" or menuid == "services_recordings"):
        return [(_("Sundtek Control Center"), main, "sundtek_control_enter", 50)]
    return [ ]

def Plugins(path, **kwargs):
    global plugin_path
    plugin_path = path
    list = [
        PluginDescriptor(name=_("sundtek control center plugin"), description =_("installs the sundtek driver and runs related shellscripts"), where = PluginDescriptor.WHERE_MENU, fnc=SundtekControlCenterStart),
        PluginDescriptor(name=_("sundtek control center plugin"), description =_("installs the sundtek driver and runs related shellscripts"), where = PluginDescriptor.WHERE_PLUGINMENU,icon="plugin.png", fnc=main)
        ]
    if config.plugins.SundtekControlCenter.display.value == "1" or config.plugins.SundtekControlCenter.display.value == "3":
        list.append(PluginDescriptor(name=_("sundtek control center plugin"), description =_("installs the sundtek driver and runs related shellscripts"), where = PluginDescriptor.WHERE_EXTENSIONSMENU, fnc=main))
    return list
