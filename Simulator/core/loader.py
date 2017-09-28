import os
import bge

import logzero
from . import datatypes

log = logzero.logger

MISSING_BLEND_ERROR = "Unable to find model file at {}"
LIBLOAD_PROPERTY = 'LIBLOAD_LOADER_KNOWN'


def lib_load_unique(path):
    '''Sometimes you want to have completely seperate objects (eg materials).
    Currently this isn't possible using libnew, so we have to load the whole
    blend file by passing in the blend as a data string (otherwise BGE
    complains about loading it multiple times). Note that this will lose any
    relative paths - so you can't use things like external textures in blends
    loaded with this method.

    Returns the library name and a list of added objects. Note that the list
    of added objects includes those on hidden and visible layers'''
    if not os.path.isfile(path):
        # Raise error if the path does not exist
        log.error(MISSING_BLEND_ERROR.format(path))
        raise ValueError(MISSING_BLEND_ERROR.format(path))
    else:
        log.info("Loading Unique {}".format(path))

        scene = bge.logic.getCurrentScene()

        # Store what objects are already in existance so we can find the new
        # ones
        for obj in scene.objects + scene.objectsInactive:
            obj[LIBLOAD_PROPERTY] = True

        # Generates a unique library name by incrementing a number
        # Note that it counts up to 19 and then goes 100, 101....
        libname = 'UNIQUE_LIBLOAD0'
        while libname in bge.logic.LibList():
            libname = libname[:-1] + str(int(libname[-1]) + 1)

        # Read the blend file into a string so that blender doesn't know the
        # path it is loaded from. This means BGE won't complain when we try
        # to load the blend again
        raw_data = open(path, 'rb').read()

        # Load the blend!
        bge.logic.LibLoad(libname, 'Scene', raw_data, load_actions=True)

        # Retrieve all objects not noticed in the previous search.
        added = datatypes.NamedObjectList()
        for obj in scene.objects + scene.objectsInactive:
            if LIBLOAD_PROPERTY not in obj:
                added.append(obj)
                obj[LIBLOAD_PROPERTY] = True

        return libname, added

