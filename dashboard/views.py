from django.shortcuts import render, redirect
from .forms import DataFileForm
from .models import DataFile
import pandas as pd
import plotly.express as px

def upload_file(request):
    if request.method == 'POST':
        form = DataFileForm(request.POST, request.FILES)
        if form.is_valid():
            datafile = form.save()
            return redirect('report', pk=datafile.pk)
    else:
        form = DataFileForm()
        
    return render(request, 'dashboard/upload.html', {'form': form})

def report_view(request, pk):
    datafile = DataFile.objects.get(pk=pk)
    df = pd.read_excel(datafile.file.path)

    fig = px.histogram(df, x=df.columns[0])
    chart = fig.to_html()

    stats = df.describe().to_html()

    return render(request, 'dashboard/report.html', {'chart': chart, 'stats': stats})
