import os
import json

from UM.Logger import Logger

from . import Dremel3DPlugin, Dremel3DAction


def getMetaData():
    return {}


def register(app):
    plugin_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "plugin.json"
    )
    try:
        with open(plugin_file_path) as plugin_file:
            plugin_info = json.load(plugin_file)
            Logger.log("d", "Dremel3DPlugin version: {}".format(plugin_info["version"]))
    except:
        Logger.log("w", "Dremel3DPlugin failed to get version information!")

    plugin = Dremel3DPlugin.Dremel3DPlugin()
    return {
        "extension": plugin,
        "output_device": plugin,
        "machine_action": Dremel3DAction.Dremel3DAction(),
    }
