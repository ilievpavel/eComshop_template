from django.views.generic import CreateView

from store.form_mixin import BootstrapFormMixin


class CreateForm(BootstrapFormMixin, CreateView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_fields__()
