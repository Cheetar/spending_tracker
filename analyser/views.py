import os

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from tracker.models import Board, Profile

from .export import export_spendings_to_excel
from .forms import BoardForm, SpendingForm


def download(path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


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
    owner = board.owner
    all_boards = Board.objects.all().filter(owner=owner)
    board_form = BoardForm()
    if request.method == "POST":
        spending_form = SpendingForm(request.POST)
        if spending_form.is_valid():
            # New speding object is created but not saved into database
            new_spending = spending_form.save(commit=False)
            new_spending.board = board
            new_spending.save()
            return render(request, 'analyser/board.html', {'spendings': spendings,
                                                           'board': board,
                                                           'spending_form': spending_form,
                                                           'all_boards': all_boards,
                                                           'board_form': board_form})
    else:
        spending_form = SpendingForm()

    return render(request, 'analyser/board.html', {'spendings': spendings,
                                                   'board': board,
                                                   'spending_form': spending_form,
                                                   'all_boards': all_boards,
                                                   'board_form': board_form})


@login_required
def create_board(request):
    return render(request, 'analyser/create_board.html')


@login_required
def export(request, id):
    board = get_object_or_404(Board, id=id)
    path = export_spendings_to_excel(board)
    return download(path)
