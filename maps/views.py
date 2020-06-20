from django.shortcuts import render


def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.eyJ1IjoiemVyYWlzc2UiLCJhIjoiY2tibmUwazdxMXJvaTJycHZxZXpuajhsZSJ9.wi3tj3MLF6IaELpfmHpLzw'

    print(str(mapbox_access_token))
    return render(request, 'default.html', 
                  { 'mapbox_access_token': str(mapbox_access_token) })
    