from django import template

register = template.Library()

@register.filter
def get_player_name(player_id, players_dict):
    return players_dict.get(player_id, '') if player_id else ''
