from pygal_maps_world.i18n import COUNTRIES


def get_country_code(countey_name):
    for code, name in COUNTRIES.items():
        if name == countey_name:
            return code
    return None
