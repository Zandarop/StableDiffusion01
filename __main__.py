import glob
import os
import sys
from pathlib import Path
import logging
import importlib
from spambot import diffusion, OWNER_ID

#logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


def load_module(diffusion_module):
    path = Path(f"stablediffusion/modules/{diffusion_module}.py")
    modlinks = "stablediffusion.modules.{}".format(diffusion_module)
    spec = importlib.util.spec_from_file_location(modlinks, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(diffusion_module)
    spec.loader.exec_module(load)
    sys.modules["stablediffusion.modules." + diffusion_module] = load
    print("Successfully loaded " + diffusion_module + " module.")


def get_readable_time(seconds: int) -> str:
    count = 0
    pingtime = ""
    timearray = []
    timedetail = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        timearray.append(int(result))
        seconds = int(remainder)

    for i in range(len(timearray)):
        timearray[i] = str(timearray[i]) + timedetail[i]
    if len(time_list) == 4:
        pingtime += timearray.pop() + ", "

    timearray.reverse()
    pingtime += ":".join(timearray)

    return pingtime




path = "stablediffussion/modules/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_module(plugin_name.replace(".py", ""))

print("Deployed Stable Diffusion Bot succesfully!!")

if __name__ == "__main__":
    if BotClient:
        BotClient.run_until_disconnected()
    else:
        pass
