from drf_yasg.renderers import SwaggerUIRenderer


class YogiyoSwaggerUIRenderer(SwaggerUIRenderer):
    template = 'api_doc_ui/yogiyo-swagger-ui.html'
