from django.http import HttpResponse
from django.shortcuts import render
import socket
import ssl
import datetime
from flask import Flask
def ssl_info_view(request):
    strona = ['www.google.pl']
    def ssl_expiry_datetime(wydawca):
        ssl_dateformat = r'%b %d %H:%M:%S %Y %Z'

        context = ssl.create_default_context()
        context.check_hostname = False

        try:
            conn = context.wrap_socket(
                socket.socket(socket.AF_INET),
                server_hostname=wydawca,
            )
            conn.settimeout(5.0)

            conn.connect((wydawca, 443))
            ssl_info = conn.getpeercert()
            return datetime.datetime.strptime(ssl_info['notAfter'], ssl_dateformat)

        except Exception as j:
            raise j

    ssl_results = []

    for data in strona:
        now = datetime.datetime.now()
        try:
            koniec = ssl_expiry_datetime(data)
            diff = koniec - now
            result = {
                'nazwa_strony': data,
                'wazna_do': koniec.strftime("%Y-%m-%d"),
                'pozostalo_dni': diff.days,
            }
            ssl_results.append(result)
        except Exception as j:
            error_message = f"Błąd podczas sprawdzania SSL dla {data}: {str(j)}"
            result = {
                'nazwa_strony': data,
                'error_message': error_message,
            }
            ssl_results.append(result)

    context = {'ssl_results': ssl_results}
    return render(request, 'ssl_info.html', context)