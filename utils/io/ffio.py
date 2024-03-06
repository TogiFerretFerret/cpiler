# ---------------------------------------------------------------------------- #
#                                File I/O Utils                                #
# ---------------------------------------------------------------------------- #

class FFio:
    """
    A class for fast file input/output operations.

    Attributes:
        fname (str): The name of the file.
        fcontents (str): The contents of the file.
        hasCached (bool): A flag indicating whether the file has been cached.
        fmetadata (dict): The metadata of the file.

    Methods:
        __init__(self, file): Initializes a new instance of the FFio class.
        fread(self, cache=True, usecache=False): Read the contents of the file and optionally cache it.
        fwrite(self, contents, cache=False): Write the given contents to the file.
        fappend(self, contents, cache=False, usecache=False): Append the given contents to the file.
        cacheRead(self): Reads and returns the cached file contents.
        cache(self): Caches the contents of the file and updates the metadata.
        metaRead(self): Reads and returns the metadata of the cached file.
    """

    def __init__(self, file):
        self.fname = file
        self.fcontents = ""
        self.hasCached = False
        self.fmetadata = {"fname": self.fname, "flines": 0}

    def fread(self, cache=True, usecache=False):
        """
        Read the contents of the file and optionally cache it.

        Args:
            cache (bool, optional): Whether to cache the file contents. Defaults to True.
            usecache (bool, optional): Whether to use the cached contents if available. Defaults to False.

        Returns:
            str: The contents of the file.

        Raises:
            LookupError: If the file has not been cached and usecache is True.
        """
        with open(self.fname, "rt") as freadval:
            sreadval = freadval.read()
            freadval.close()
            if cache:
                self.fcontents = sreadval
                self.fmetadata["flines"] = len(self.fcontents.splitlines())
                self.hasCached = True
            if usecache and self.hasCached:
                return self.fcontents
            elif not self.hasCached:
                raise LookupError("File has not yet been cached!")
            return sreadval

    def fwrite(self, contents, cache=False):
        """
        Write the given contents to the file.

        Parameters:
        - contents: The contents to be written to the file.
        - cache: A boolean indicating whether to update the file cache.

        Returns:
        None
        """
        with open(self.fname, "wt") as fwriteval:
            fwriteval.write(str(contents))
            if cache:
                self.fcontents = str(contents)
                self.fmetadata["flines"] = len(self.fcontents.splitlines())
            fwriteval.close()

    def fappend(self, contents, cache=False, usecache=False):
        """
        Append the given contents to the file.

        Parameters:
        - contents: The contents to be appended to the file.
        - cache: A boolean indicating whether to update the file cache. Default is False.
        - usecache: A boolean indicating whether to use the file cache. Default is False.

        Raises:
        - LookupError: If the file has not yet been cached.

        """
        with open(self.fname, "at") as fwriteval:
            fwriteval.write(str(contents))
            if cache and usecache and self.hasCached:
                self.fcontents += str(contents)
                self.fmetadata["flines"] += len(str(contents).splitlines())
            elif cache and not usecache:
                self.fread(cache=True, usecache=False)
            elif not self.hasCached:
                raise LookupError("File has not yet been cached!")
            if cache:
                self.fcontents = str()
                self.fmetadata["flines"] = len(self.fcontents.splitlines())
            fwriteval.close()

    def cacheRead(self):
        """
        Reads and returns the cached file contents.

        Raises:
            LookupError: If the file has not yet been cached.

        Returns:
            str: The contents of the cached file.
        """
        if not self.hasCached:
            raise LookupError("File has not yet been cached!")
        return self.fcontents

    def cache(self):
        """
        Caches the contents of the file and updates the metadata.

        Reads the contents of the file specified by `self.fname` and stores it in `self.fcontents`.
        Updates the metadata dictionary `self.fmetadata` with the number of lines in the file.
        Sets the `hasCached` flag to True.

        """
        with open(self.fname, "rt") as freadval:
            sreadval = freadval.read()
            freadval.close()
            self.fcontents = sreadval
            self.fmetadata["flines"] = len(self.fcontents.splitlines())
            self.hasCached = True

    def metaRead(self):
        """
        Reads and returns the metadata of the cached file.

        Raises:
            LookupError: If the file has not yet been cached.

        Returns:
            dict: The metadata of the cached file.
        """
        if not self.hasCached:
            raise LookupError("File has not yet been cached!")
        return self.fmetadata

