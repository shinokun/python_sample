

import sample_def

###fileの一覧表示　再帰的##################################################
##特定のファイルを指定する場合は、def内部で絞り込みを行う###
#出力用のリスト
filelist = []

#pathを指定して実行する
path = "d:\\rep"
filelist = sample_def.show_recursive(path)

import pprint
for i,v in enumerate(filelist):
    print(v)
#########################################################################


###ファイル圧縮###########################################################
#filelist = []
#import os
##圧縮ファイルを作成するディレクトリに移動する
#os.chdir("D:\\cc")
##圧縮後のファイル名を指定する
#zip_name = "test.zip"
##圧縮対象のファイルを指定する
#filelist = ["D:\\cc\\aa.bmp","D:\\aa\\bb\\旧.txt"]

#modeを指定して実行する
#mode = "w"  #書き込み用に開く(通常圧縮)
#mode = "a"  #書き込み用に開き、すでにファイルがあった場合末尾に追加する
            #展開する際に１つに統合を聞かれる
#sample_def.create_zip(mode,zip_name,filelist)
#########################################################################




