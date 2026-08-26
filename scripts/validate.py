# Build: a649e0bd4a9d4b0180b53431e8bf6adb

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
