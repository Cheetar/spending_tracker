from django import template

from tracker.models import Board, Profile

register = template.Library()


@register.simple_tag
def users_boards(request):
    owner = Profile.objects.get(user=request.user)
    boards = Board.objects.all().filter(owner=owner)
    return boards
