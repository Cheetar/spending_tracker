from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from tracker.models import Board, Profile


@login_required
def dashboard(request):
    profile = Profile.objects.get(user=request.user)
    latest_board = Board.objects.all().filter(owner=profile).first()
    if latest_board is None:
        return redirect('create_board')
    return redirect('board', latest_board.id)


@login_required
def board(request, id):
    board = get_object_or_404(Board, id=id)
    spendings = board.spendings
    return render(request, 'analyser/board.html', {'spendings': spendings, 'board': board})


@login_required
def create_board(request):
    return render(request, 'analyser/create_board.html')
