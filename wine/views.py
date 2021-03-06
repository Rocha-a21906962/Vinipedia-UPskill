from django.http import request
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from wine.forms import EvaluationForm
from wine.models import Wine, Evaluation
from wine.models import Tag
from django.db.models import Q, Avg

def search(request):
    query = request.GET.get("query")
    wine_query = Wine.objects.filter(
        (Q(name__icontains=query) | Q(types__name__icontains=query) | Q(producer__name__icontains=query))
    )
    context = {'wines': wine_query}

    return render(request, 'wine/search.html',
                  context)


class WineList(ListView):  # (Substitui o view abaixo!)
    template_name = 'wine/list.html'
    context_object_name = 'wines'  # (Alterar nome do contexto para ser usado no template)
    model = Wine
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(WineList, self).get_context_data(**kwargs)

        num_visitas = self.request.session.get("visitas_wine_list", 0)
        num_visitas += 1

        self.request.session["visitas_wine_list"] = num_visitas

        return context

    def get_queryset(self):
        try:
            tag = get_object_or_404(Tag, slug=self.kwargs.get('tag_slug'))

            if tag:
                # Filtrar tag ou lista
                return get_list_or_404(Wine, types__in=[tag])
        except:
            return get_list_or_404(Wine)


class WineDetail(DetailView):
    template_name = 'wine/detail.html'
    context_object_name = 'wine'
    model = Wine


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = EvaluationForm()
        self.wine_pageview()

        return context

    def post(self, request, pk):
        evaluation_form = EvaluationForm(data=request.POST)
        if evaluation_form.is_valid():
            new_evaluation = evaluation_form.save(commit=False)
            new_evaluation.wine = self.get_object()
            new_evaluation.user = request.user
            evaluation_form.save()
            return redirect(self.get_object())
        else:

            context = {'wine': self.get_object(), 'form': evaluation_form}
            return render(request, self.template_name, context)

    def wine_pageview(self):
        wine = self.get_object()
        wine.pageviews += 1
        wine.save()
        pass


# TODO mudar para a homepage
class EvaluationList(ListView):
    model = Evaluation
    template_name = 'homepage.html'
    context_object_name = 'evaluations'

class Homepage(ListView):
    model = Evaluation
    template_name = 'homepage.html'
    context_object_name = 'evaluations'
