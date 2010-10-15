from struct import *

if "Struct" not in locals():
    class Struct(object):
        
        def __init__(self, format):
            self.format = format
            
        def pack(self, *args):
            """Identical to the pack() function, using the compiled format. (len(result) will equal self.size.)"""
            return pack(self.format, *args)
        
        def pack_into(self, buffer, offset, *args):
            """Identical to the pack_into() function, using the compiled format."""
            return pack_into(self.format, buffer, offset, *args)
        
        def unpack(self, string):
            """Identical to the unpack() function, using the compiled format. (len(string) must equal self.size)."""
            return unpack(self.format, string)
        
        def unpack_from(self, buffer, offset=0):
            """Identical to the unpack_from() function, using the compiled format. (len(buffer[offset:]) must be at least self.size)."""
            unpack_from(self.format, buffer, offset)
        
        @property
        def size(self):
            """The calculated size of the struct (and hence of the string) corresponding to format."""
            return calcsize(self.format)
