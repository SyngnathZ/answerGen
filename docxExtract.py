#!/usr/bin/python
# -*- coding: UTF-8 -*-

from docx import Document



class seqNode:
    def __init__(self, Questions, Options, Answers):
        self.question = Questions
        self.option = Options
        self.answer = Answers


def getParaQue(doc):
    # 每一段的内容
    i = 0
    queIndex = []
    for para in doc.paragraphs:
        paralist = para.text.split('、')
        try:
            int(paralist[0])
            queIndex.append(i)
        except:
            pass
        i += 1

    return queIndex


def initializeNode(doc, Index):
    docxList = []
    for each in range(len(Index)):
        if each != len(Index) - 1:
            options = []
            for i in range(Index[each] + 1, Index[each + 1]):
                options.append(doc.paragraphs[i].text)
            docxNode = seqNode(doc.paragraphs[Index[each]].text, options,
                               doc.paragraphs[Index[each]].text.split('【')[1].split('】')[0].split(','))
            docxList.append(docxNode)

    return docxList


def main():
    doc = Document('./docx/机汽学院安全教育题库.docx')
    initializeNode(doc, getParaQue(doc))


if __name__ == '__main__':
    main()
