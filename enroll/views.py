# tasks/views.py
from django.http import HttpResponse
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer 
from datetime import datetime
from django.http import JsonResponse 
import ctypes
import ctypes.wintypes  

 
now = datetime.now()


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
 
def ActiveScreen(request):
   
    def get_active_screen_id_windows():
        user32 = ctypes.windll.user32
        active_window = user32.GetForegroundWindow()
        active_screen_id = user32.MonitorFromWindow(active_window, 2)
        return active_screen_id

    active_screen_id = get_active_screen_id_windows()

    if active_screen_id:
        print(f"Active Screen ID: {active_screen_id}")
        return JsonResponse({'Active_Screen_ID': active_screen_id})
    else:
        return HttpResponse("No active screen found.")
 

def ActiveScreenId():
   
    def get_active_screen_id_windows():
        user32 = ctypes.windll.user32
        active_window = user32.GetForegroundWindow()
        active_screen_id = user32.MonitorFromWindow(active_window, 2)
        return active_screen_id

    active_screen_id = get_active_screen_id_windows()

    if active_screen_id:
        # print(f"Active Screen ID: {active_screen_id}")
        return active_screen_id
    else:
        return  "No active screen found."
   

def ActiveScreenIndex(request): 
    # Define necessary Windows API structures and constants
    class RECT(ctypes.Structure):
        _fields_ = [("left", ctypes.c_long),
                    ("top", ctypes.c_long),
                    ("right", ctypes.c_long),
                    ("bottom", ctypes.c_long)]

    class MONITORINFO(ctypes.Structure):
        _fields_ = [("cbSize", ctypes.c_uint),
                    ("rcMonitor", RECT),
                    ("rcWork", RECT),
                    ("dwFlags", ctypes.c_uint)]

    MONITOR_DEFAULTTOPRIMARY = 1
    MONITOR_ENUM_ALL = 0x0004
 

    # Load required Windows API functions
    user32 = ctypes.windll.user32
    user32.EnumDisplayMonitors.restype = ctypes.c_bool
    user32.EnumDisplayMonitors.argtypes = (ctypes.c_void_p, ctypes.POINTER(RECT), ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p), ctypes.c_void_p)

    # Callback function to collect monitor information
    def monitor_enum_proc(hMonitor, hdcMonitor, lprcMonitor):
        monitors.append(hMonitor)
        return True

    # Initialize list to store monitor handles
    monitors = []

    # Enumerate all monitors
    user32.EnumDisplayMonitors(0, None, ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(monitor_enum_proc), None)

    # Get information about each monitor

    for hMonitor in monitors:
        monitor_info = MONITORINFO()
        monitor_info.cbSize = ctypes.sizeof(MONITORINFO)
        user32.GetMonitorInfoW(hMonitor, ctypes.byref(monitor_info))

        # # Extract relevant monitor information
        # monitor_id = hMonitor
        # monitor_name = monitor_info.rcMonitor.left, monitor_info.rcMonitor.top
        # activeScreen = ActiveScreenId()
        currentDisplayIndex = monitors.index(ActiveScreenId())
  
   
    return JsonResponse({'Active_Screen_Index': currentDisplayIndex})