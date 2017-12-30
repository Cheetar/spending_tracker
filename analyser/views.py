from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from tracker.models import Board, Profile


@login_required
def dashboard(request):
    # add try except if user have no boards then redirect to create_board view
    profile = Profile.objects.get(user=request.user)
    latest_board = Board.objects.get(owner=profile)
    return redirect('board', latest_board.id)


@login_required
def board(request, id):
    board = Board.objects.get(id=id)
    spendings = board.spendings
    return render(request, 'analyser/board.html', {'spendings': spendings})
