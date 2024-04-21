def to_bytes(bits):
    bytes=bits/8
    return bytes

def to_kilobytes(bytes):
    kilobytes=bytes/1000
    return kilobytes

def to_kibibytes(bytes):
    kibibytes=bytes/1024
    return kibibytes

def to_megabytes(kilobytes):
    megabytes=kilobytes/1000
    return megabytes

def to_mebibytes(kibibytes):
    mebibytes=kibibytes/1024
    return mebibytes

def to_gigabytes(kilobytes):
    gigabytes=kilobytes/1000
    return gigabytes

def to_gibibytes(kibibytes):
    gibibytes=kibibytes/1024
    return gibibytes

bits=int(input('Enter an amount of bits: '))
bytes=to_bytes(bits)
kilobytes=to_kilobytes(bytes)
kibibytes=to_kibibytes(bytes)
megabytes=to_megabytes(kilobytes)
mebibytes=to_mebibytes(kibibytes)
gigabytes=to_gigabytes(kilobytes)
gibibytes=to_gibibytes(kibibytes)

types=['bytes','kilobytes','kibibytes','megabytes','mebibytes','gigabytes','gibibytes']
nums=[bytes,kilobytes,kibibytes,megabytes,mebibytes,gigabytes,gibibytes]

for i in range(0,len(types)):
    print(bits,'in',types[i],'is',nums[i])