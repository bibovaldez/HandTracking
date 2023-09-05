# control volume using pycaw

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Get current volume
currentVolumeDb = volume.GetMasterVolumeLevel()
print(currentVolumeDb)
# set volume

# minVolumeDb, maxVolumeDb, volumeStepDb = volume.GetVolumeRange()
# print(f"Minimum volume (dB): {minVolumeDb}")
# print(f"Maximum volume (dB): {maxVolumeDb}")
# print(f"Volume step (dB): {volumeStepDb}")



