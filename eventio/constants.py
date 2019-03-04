SYNC_MARKER_SIZE = 4
SYNC_MARKER_BIG_ENDIAN = b'\xd4\x1f\x8a\x37'
SYNC_MARKER_LITTLE_ENDIAN = SYNC_MARKER_BIG_ENDIAN[::-1]
SYNC_MARKER_UINT8_VALUE = 3558836791
SYNC_MARKER_INT8_VALUE = -736130505

OBJECT_HEADER_SIZE = 12
EXTENSION_SIZE = 4
TOPLEVEL_HEADER_SIZE = OBJECT_HEADER_SIZE + SYNC_MARKER_SIZE


TYPE_NUM_BITS = 16
TYPE_POS = 0

USER_NUM_BITS = 1
USER_POS = 16

EXTENDED_NUM_BITS = 1
EXTENDED_POS = 17

VERSION_NUM_BITS = 12
VERSION_POS = 20

ONLY_SUBOBJECTS_NUM_BITS = 1
ONLY_SUBOBJECTS_POS = 30

LENGTH_NUM_BITS = 30
LENGTH_POS = 0

EXTENSION_NUM_BITS = 12
EXTENSION_POS = 0
