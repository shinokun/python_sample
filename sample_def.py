
###fileの一覧表示　再帰的#########################################
import pathlib
import os
return_list = []

def show_recursive(path):
    path = pathlib.Path(path)
    for po in path.iterdir():
        if po.is_dir():
            #ディレクトリだったら再帰的に自分を呼び出し、最下層まで検索する
            show_recursive(po)
            #matchさせたいファイルがある場合はマッチするファイル名を指定する
        elif po.is_file() and po.match("*.*"):
            return_list.append(str(po) + "@" + str((os.path.getsize(str(po)))) + "byte")
    return(return_list)

#################################################################

###ファイルの圧縮#################################################
import zipfile
def create_zip(mode,zip_name,filelist):
    if mode == "W":
        with zipfile.ZipFile(zip_name,'w') as zf:
            for i,v in enumerate(filelist):
                print(v)
                zf.write(v)
    elif mode == "a":
        with zipfile.ZipFile(zip_name,'a') as zf:
            for i,v in enumerate(filelist):
                print(v)
                zf.write(v)
    else:
        return "モードを選択してください"
################################################################