from fastapi import FastAPI
from typing import List
from starlette.requests import Request
from starlette.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse 
import pathlib


app = FastAPI()

app.mount("/templates", StaticFiles(directory="templates", html=True), name="templates")
# app.mount("/predict_v2", StaticFiles(directory="predict_v2"), name="predict_v2")
# mount test image
# app.mount("/templates", StaticFiles(directory="templates", html=True), name="templates")


@app.get('/')
async def read_index():
    return FileResponse('templates/index.html')


@app.get("/result")
async def get(path: str, start: int = 0, end: int = 100):
    return FileResponse('templates/list.html')

def renderNewDict(raw_path):
    file_read = open(raw_path, "r")
    output_dict = []
    for line in file_read:
        elements = line.split("\t")
        if (elements[0] == "\\right"):
            elements.append("")
        elif (elements[0] == "\\left"):
            elements.append("")
        elif (elements[0] == "\\gt"):
            elements.append(">")
        elif (elements[0] == "\\lt"):
            elements.append("<")
        elif (elements[0] == "COMMA"):
            elements.append(".")
        else:
            elements.append(elements[0])
        output_dict.append(elements)
    return output_dict



def spaceParsev(inp):
    # remove $ and space
    # inp = inp[1:]
    # inp = inp[:-2]
    inp = inp.replace("$", "").strip()
    inp = inp.replace(" ", "")
    # get list dictionary
    # dic = []
    # file = open("/mlcv/WorkingSpace/Personals/thinhvq/CROHME/ABM/dictionary.txt")
    # for line in file:
    #     dic.append(line.split("\t")[0])
    dict_map = renderNewDict("/mlcv/WorkingSpace/Personals/thinhvq/CROHME/data/dictionary.txt")
    # dict_map = renderNewDict("/mlcv/WorkingSpace/Personals/thinhvq/CROHME/ABM/dict.txt")
    # sort with length
    dict_map.sort(reverse=True, key = lambda x: len(x[0]))
    # print(dict_map)
    # handle char
    ch = 0
    temp = ""
    while (ch < len(inp)):
        # print(ch)
        flag = False
        for child in dict_map:
            if (inp[ch: ch + len(child[0])] == child[0]):
                # print(child)
                flag = True
                # temp = temp + inp[ch: ch + len(child[0]) + " "
                temp = temp + child[2] + " "
                ch = ch + len(child[0]) 
                break
        # print(inp[ch: ch + 1])
        if ( inp[ch: ch + 1] == " "):
            ch = ch + 1
            break
        if (flag == False):
            # print(inp[ch: ch + 1])
            temp = temp +  inp[ch: ch + 1] + " "
            ch = ch + 1
    return temp.strip()
@app.get("/list")
async def listLatex(path:str, start: int, end: int):
    file = open(path, "r")
    folderPath = pathlib.Path(path).stem
    app.mount("/" + folderPath, StaticFiles(directory=folderPath), name=folderPath)
    output = []
    couter = 0
    for line in file:
        couter += 1
        if (couter >= start) and (couter <= end):
            output.append(line.split("\t"))
    return output
    
