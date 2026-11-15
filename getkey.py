import ctypes

security = ctypes.CDLL('/System/Library/Frameworks/Security.framework/Security')
security.SecKeychainSetUserInteractionAllowed.argtypes = [ctypes.c_bool]
security.SecKeychainSetUserInteractionAllowed(False)
security.SecKeychainFindGenericPassword.argtypes = [
    ctypes.c_void_p,
    ctypes.c_uint32,
    ctypes.c_char_p,
    ctypes.c_uint32,
    ctypes.c_char_p,
    ctypes.POINTER(ctypes.c_uint32),
    ctypes.POINTER(ctypes.c_void_p),
    ctypes.c_void_p,
]
security.SecKeychainFindGenericPassword.restype = ctypes.c_int32
security.SecKeychainItemFreeContent.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

service = b'Horse Announcer'
account = b'ELEVENLABS_API_KEY'
size = ctypes.c_uint32()
data = ctypes.c_void_p()
status = security.SecKeychainFindGenericPassword(
    None, len(service), service, len(account), account, ctypes.byref(size), ctypes.byref(data), None
)
if status != 0:
    raise SystemExit(1)
try:
    value = ctypes.string_at(data, size.value).decode().strip()
finally:
    security.SecKeychainItemFreeContent(None, data)
print(value)
