def inspect_pointer(value):
    print(f"Decimal : {value}")
    print(f"Hex     : 0x{value:08X}")

    high = (value >> 16) & 0xFFFF
    low = value & 0xFFFF

    print(f"High16  : {high} (0x{high:04X})")
    print(f"Low16   : {low} (0x{low:04X})")

    print()

    print(f"Offset / 16 : {value // 16}")
    print(f"Offset / 32 : {value // 32}")
    print(f"Offset / 48 : {value // 48}")
    print(f"Offset / 64 : {value // 64}")