from django.http import JsonResponse
from django.conf import settings
from .utils import get_part_2, get_part_3
from .models import get_part_4
from .logic import get_part_5

def get_flag(request):
    # Проверка на внимательность
    if request.headers.get('X-Django-Identity') != 'DjangoEtoYa':
        return JsonResponse({
            "error": "Access Denied",
            "hint": "Check the headers. Who are you? 'X-Django-Identity'?"
        }, status=403)

    # Сборка флага
    flag = (
        settings.INTERNAL_ID +
        get_part_2() +         
        get_part_3() +         
        get_part_4() +         
        get_part_5()        
    )

    return JsonResponse({
        "status": "success",
        "result": flag
    })
