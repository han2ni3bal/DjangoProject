from django.http import JsonResponse
from django.template import TemplateDoesNotExist
from django.utils.deprecation import MiddlewareMixin


class ExceptionMiddleware(MiddlewareMixin):
  def process_exception(self, request, exception):
    if type(exception) == TemplateDoesNotExist:
      mess = "Page {} not exist".format(request.path)
      return JsonResponse({"message": mess, "error": True, "code": 500}, status=404)
    else:
      mess = "500 occured when {} {}, param is {}, error is {}".format(request.method, request.path, request.body,
                                                                       str(exception))
      return JsonResponse({"message": mess, "error": True, "code": 500}, status=500)
