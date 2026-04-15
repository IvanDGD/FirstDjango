from django.http import *
from django.views.decorators.csrf import *

def multiplication_table(request):
    content = """
    <!DOCTYPE html>
    <html lang="uk">
    <head>
        <meta charset="UTF-8">
        <title>Таблиця множення</title>
    </head>
    <body>
        <h2 style="text-align:center;">Таблиця множення</h2>
        <table>
            <tr>
                <th>*</th>
    """

    for i in range(1, 11):
        content += f"<th>{i}</th>"

    content += "</tr>"

    for i in range(1, 11):
        content += f"<tr><th>{i}</th>"
        for j in range(1, 11):
            content += f"<td>{i * j}</td>"
        content += "</tr>"

    content += """
        </table>
    </body>
    </html>
    """

    return HttpResponse(content)