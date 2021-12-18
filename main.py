import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # 步驟一（替換Microsoft JhengHei字型）
plt.rcParams['axes.unicode_minus'] = False  # 步驟二（解決座標軸負數的負號顯示問題）
background = '#363636'
plt.rcParams['savefig.facecolor'] = background
plt.rcParams['axes.facecolor'] = background


def filter_ByClassName(class_name,data):
    temp = pd.DataFrame(data)
    for i in temp.index:
        if temp.at[i, '班級'] not in class_name:
            temp = temp.drop(index=[i])

    return temp


def q1(temp, qusetion, choose):
    width = 0.1
    total = len(temp.index)
    plt.figure(figsize=(15, 10))
    plt.title(qusetion,fontsize=20,color='w')
    plt.grid(True,axis='y')
    boy = np.zeros((5), dtype=float)
    girl = np.zeros((5), dtype=float)
    if choose == 0:
        arr = ['完全不熟悉', '不熟悉', '有點熟悉', '很熟悉', '非常熟悉']
    elif choose == 1:
        arr = ['完全不重要', '不重要', '有點重要', '很重要', '非常重要']
    elif choose == 2:
        arr = ['完全不同意', '不同意', '有點同意', '很同意', '非常同意']

    for i in temp.iloc:
        if i['性別'] == '男':
            boy[i[qusetion]-1] += 1
        if i['性別'] == '女':
            girl[i[qusetion]-1] += 1

    x = np.arange(len(arr))



    plt.bar(x - width-0.05, boy, width, label='男',edgecolor='cornflowerblue',linewidth=2,color= background)
    plt.bar(x, boy/total*100, width, label='男比例',edgecolor='lightsteelblue',linewidth=2,color= background)
    plt.bar(x + width+0.05, girl, width, label='女',edgecolor='peachpuff',linewidth=2,color= background)
    plt.bar(x + 2*width +0.1, girl / total*100, width, label='男比例',edgecolor='sandybrown',linewidth=2,color=background)

    num = max(np.max(girl), np.max(girl),np.max(girl / total*100),np.max(boy / total*100))
    plt.tick_params(axis='both', labelsize=18)
    plt.xticks(x, arr, color='w')
    if num >= 200:
        y = np.arange(0, num * 1.5, 50)
    elif num < 100:
        y = np.arange(0, num * 1.5, 10)
    else:
        y = np.arange(0, num * 1.5, 20)
    plt.yticks(y, color='w')

    for x, y in enumerate(boy):
        if y != 0:
            plt.text(x - width-0.05, y+0.5, '%s' % int(y), ha='center',color='w')
    for x, y in enumerate(boy/total*100):
        if y != 0:
            plt.text(x, y+0.5, '%s' % round(y, 2) + '%', ha='center',color='w')
    for x, y in enumerate(girl):
        if y != 0:
            plt.text(x + width+0.05, y+0.5, '%s' % int(y), ha='center',color='w')
    for x, y in enumerate(girl / total*100):
        if y != 0:
            plt.text(x + 2*width+0.1, y+0.5, '%s' % round(y, 2) + '%', ha='center',color='w')
    # plt.show()
    # return plt,boy/total*100,girl / total*100
    plt.setp(plt.legend(loc='best',fontsize=18).get_texts(), color='w')
    return plt

def q2(temp,qusetion,choose):
    width = 0.2
    total = len(temp.index)
    plt.figure(figsize=(15, 10))
    plt.title(qusetion,fontsize=20,color='w')
    plt.grid(True, axis='y')

    true_list = np.zeros((4), dtype=float)
    false_list = np.zeros((4), dtype=float)
    none_list = np.zeros((4), dtype=float)
    plt.tick_params(axis='both',labelsize=18)

    arr = ['男', '男比例', '女', '女比例']
    x = np.arange(len(arr))
    plt.xticks(x, arr, color='w')
    plt.yticks(color='w')
    if choose == 0:
        for i in temp.iloc:
            # print(i[qusetion])
            if i[qusetion] == '是' or i[qusetion] == '願意' or i[qusetion] == '會' or i[qusetion] == '可以':
                if i['性別'] == '男':
                    true_list[0] += 1
                else:
                    true_list[2] += 1
            else :
                if i['性別'] == '男':
                    false_list[0] += 1
                else:
                    false_list[2] += 1
    elif choose == 1:
        temp = temp.fillna('不會')
        for i in temp.iloc:
            # print(i[qusetion])
            if i[qusetion] == '不可以' or '答對' in i[qusetion]:
                if i['性別'] == '男':
                    true_list[0] += 1
                else:
                    true_list[2] += 1
            elif i[qusetion] == '不會':
                if i['性別'] == '男':
                    none_list[0] += 1
                else:
                    none_list[2] += 1
            else:
                if i['性別'] == '男':
                    false_list[0] += 1
                else:
                    false_list[2] += 1

    true_list[1] = true_list[0]/total*100
    true_list[3] = true_list[2]/total*100

    false_list[1] = false_list[0] / total*100
    false_list[3] = false_list[2] / total*100

    none_list[1] = none_list[0] / total * 100
    none_list[3] = none_list[2] / total * 100
    # print(true_list)
    if choose == 0:
        plt.bar(x-width-0.05, true_list, width, label='是', edgecolor='cornflowerblue', linewidth=2, color=background)
        plt.bar(x, false_list, width, label='否', edgecolor='sandybrown', linewidth=2, color=background)
    elif choose == 1 or choose == 2:
        plt.bar(x - width-0.05, true_list, width, label='是', edgecolor='cornflowerblue', linewidth=2, color=background)
        plt.bar(x, false_list, width, label='否', edgecolor='sandybrown', linewidth=2, color=background)
        plt.bar(x + width+0.05, none_list, width, label='不會', color=background, edgecolor='peachpuff', linewidth=2)
    plt.legend(loc='center', fontsize=24)
    count = 0
    for x, y in enumerate(true_list):
        count+=1
        if y != 0 :
            if count == 2 or count == 4:
                plt.text(x-width-0.05, y+0.5, '%s' % round(y, 2) + '%', ha='center',color='w')
            else:
                plt.text(x-width-0.05, y+0.5, '%s' % int(y), ha='center',color='w')
    count = 0
    for x, y in enumerate(false_list):
        count += 1
        if y != 0:
            if count == 2 or count == 4:
                plt.text(x, y+0.5, '%s' % round(y, 2) + '%', ha='center',color='w')
            else:
                plt.text(x, y+0.5, '%s' % int(y), ha='center',color='w')
    count = 0
    if choose == 1:
        for x, y in enumerate(none_list):
            count += 1
            if y != 0:
                if count == 2 or count == 4:
                    plt.text(x + width+0.05, y+0.5, '%s' % round(y, 2) + '%', ha='center',color='w')
                else:
                    plt.text(x + width+0.05, y+0.5, '%s' % int(y), ha='center',color='w')

    num = max(np.max(true_list), np.max(false_list), np.max(none_list))
    if num >= 200:
        y = np.arange(0, num * 1.5, 50)
    elif num < 100:
        y = np.arange(0, num * 1.5, 10)
    else:
        y = np.arange(0, num * 1.5, 20)
    plt.yticks(y, color='w')
    plt.text(-0.3,(num*1.5)*0.8, f'\n男比例 :{round(true_list[1],2)}% \n女比例 :{round(true_list[3],2)}%',fontsize=18,color='w')

    plt.setp(plt.legend(loc='best',fontsize=18).get_texts(), color='w')

    return plt


if __name__ == '__main__':
    name = []
    data = pd.read_excel('20211213各學院普測(各班分析).xlsx')
    class_name_data = pd.read_excel('20211213各學院普測(各班分析).xlsx',sheet_name='工作表2')
    question = data.columns[2:]

    calss_name = input('class name')
    lenght = len(calss_name)
    a = calss_name[lenght - 1]
    b = calss_name[:2]
    for i in class_name_data.iloc:
        if a in i['班級'] and b in i['班級']:
            if i['班級'] not in name:
                name.append(i['班級'])
    class_data = pd.DataFrame()
    for i in name:
        class_data = class_data.append(filter_ByClassName(name,data))

    print(class_data)
    if not os.path.exists(calss_name):
        os.mkdir(calss_name)
    for i in range(0,len(question)):

        if i < 3:
            data = q1(class_data, question[i], i)
        elif i == 3:
            data = q1(class_data, question[i], 2)
        elif i <12 or i == 13 or i == 16 or i == 18:
            data = q2(class_data, question[i], 0)
        elif i == 12 or i <= 15 or i == 17 or i == 19:
            data = q2(class_data, question[i], 1)

        # data.show()
        data.savefig(calss_name +"\\" + str(i+1) + str(question[i]) + '.png')
        data.clf()