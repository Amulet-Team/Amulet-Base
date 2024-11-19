# Add amulet/bin to the library path.


def _patch_path():
    import os
    import sys

    path = os.path.join(os.path.dirname(__file__), "bin")
    if sys.platform == "win32":
        os.add_dll_directory(path)
    elif sys.platform == "darwin":
        os.environ["DYLD_LIBRARY_PATH"] = (
            os.environ.get("DYLD_LIBRARY_PATH", "") + os.pathsep + path
        )
    else:
        os.environ["LD_LIBRARY_PATH"] = (
            os.environ.get("LD_LIBRARY_PATH", "") + os.pathsep + path
        )


_patch_path()
