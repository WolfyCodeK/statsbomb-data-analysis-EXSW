from django.shortcuts import render
import re
from django.conf import settings
import os
# Create your views here.

def main(request):
    print("hhhhhhh")
    return render(request, 'space/main.html')

def space(request):
    time = request.GET.get('time')
    print(time)  # Print the time value in the console
    print("waaaa")
    # Other actions related to the "space" view
    render_time = time
    print(render_time,"rendertime")

    pattern = r"(\d+):(\d+)"
    matchTime = re.match(pattern, render_time)
    
    matchPeriod = str(re.findall(r'[^- ]+$', render_time))
    matchPeriod = matchPeriod.removeprefix("['")
    matchPeriod = matchPeriod.removesuffix("']") 
    
    if matchTime:
        minutes = int(matchTime.group(1))
        seconds = int(matchTime.group(2))
        total_seconds = minutes * 60 + seconds

    if (int(matchPeriod) == 2):
        total_seconds -= (45 * 60)
    
    #glb_filename=f"../../../MCI/mancity/pitch/glbmodels/{time}.glb"
    glb_filename=f"space/glbmodels/{matchPeriod}_{total_seconds}.glb"
    #glb_filename='space/output.glb'

    if not os.path.exists(glb_filename):
        print("no existy")

    return render(request, 'space/main.html', {'glb_filename': glb_filename})
