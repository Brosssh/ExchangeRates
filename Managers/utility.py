def try_parse_float(p :str) -> float | str:
    try:
        return float(p)
    except Exception:
        return p