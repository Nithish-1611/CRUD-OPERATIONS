from django.shortcuts import get_object_or_404, redirect, render
from .models import Item

def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return redirect('item_list')
