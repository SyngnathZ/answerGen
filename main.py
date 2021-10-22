#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sqlite3


def main():
    conn = sqlite3.connect('information.db')
    cur = conn.cursor()

    while True:
        inputtext = input('请输入您需要查询的部分选项（标题不能复制）:\n若查询完毕，请输入td退出查询程序\n')
        if inputtext == 'td':
            break
        else:
            try:
                sql_text = "select Question, Options, Answer From quesInfo WHERE Options like (" + "'%" + str(
                    inputtext) + "%'" + ")"

                pointer = cur.execute(sql_text)
                for each in pointer:
                    optionlist = each[1].split('###')
                    answerlist = each[2].split('###')
                    print('题目是:\n')
                    print(each[0])  # 输出题目
                    print('选项是:\n')
                    print('\n'.join(optionlist))
                    print('答案是:\n')
                    print(','.join(answerlist))

            except:
                print('好像没这题，请缩小字符数目')

    cur.close()
    conn.close()


if __name__ == '__main__':
    main()
