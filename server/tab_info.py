import json


class TabInfo(json.JSONEncoder):
    id = 0
    name = ''
    sort = 0
    icons_selected = ''
    icons_unselected = ''
    tab_child_infos = list()


class TabChildInfo:
    tab_id = 0
    tab_name = ''
    source = ''
    platform = ''
    sort = 0
    show_type = ''
    show = 1


class InfoEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, TabInfo):
            return int(obj)
        elif isinstance(obj, TabChildInfo):
            return float(obj)
        else:
            return json.JSONEncoder.default(self, obj)
