import threading, asyncio, os, bitcoin, logging, multiprocessing
from tqdm import tqdm
import ip
from sokit import *



api_key = '23c518e4-e589-46da-98cf-3b39102dda6c'



PR_ip = socket.gethostbyname(socket.gethostname())
PU_ip = ip.ip.ip_address(self=1 ,api_key=api_key)

print(PR_ip, PU_ip)
