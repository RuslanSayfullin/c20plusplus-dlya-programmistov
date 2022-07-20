@register.simple_tag
def count_inquery_overdue(designer):
    """просроченный запрос"""
    return count_froze_overdue_new(designer=designer)
    l = []
    for a in chain(api.froze.get_overdue_froze_status_new(designer), api.froze.get_overdue_froze_status_repeat(designer), Froze.manager.overdue_think(designer)):
        if a.ko_status != 0 or a.dubl:
            continue
        l.append(a)count_froze_overdue
    return len(l)

    froze_items = (len(api.froze.get_overdue_froze_status_new(designer)),
                   len(api.froze.get_overdue_froze_status_repeat(designer)),
                   len(Froze.manager.overdue_think(designer)))
    return sum(froze_items)
