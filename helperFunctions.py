def coerce(str):
    if(str.lower() == "true"):
        return True
    if(str.lower() == "false"):
        return False
    try:
        return int(str)
    except:
        pass
    return str.strip()
