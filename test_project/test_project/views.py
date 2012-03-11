from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        return self.render_to_response({
            'my_route': [
                {'lat': 50.07758, 'lng': 14.42114},
                {'lat': 50.07350, 'lng': 14.41996},
                {'lat': 50.07376, 'lng': 14.42400},
                {'lat': 50.07230, 'lng': 14.42258},
                {'lat': 50.07095, 'lng': 14.41906},
            ]})
