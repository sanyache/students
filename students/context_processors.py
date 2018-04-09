from .util import get_groups, get_current_lang

def groups_processor(request):
    return {'GROUPS': get_groups(request)}
def lang_processor(request):
    return{'LANG': get_current_lang(request)}