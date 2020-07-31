from apps.media.models import Media


class AddMediaMixin:

    def get_context_data(self, **kwargs):
            context = super(AddMediaMixin, self).get_context_data(**kwargs)
            context["medias"] = Media.objects.all()
            return context
