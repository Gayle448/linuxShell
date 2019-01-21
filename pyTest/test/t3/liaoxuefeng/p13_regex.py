#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: p13_regex.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-19-下午5:02
# ---------------------说明--------------------------
# h正则表达式使用.主要测试py兼容的是哪种标准, 和java,和bash的异同
# ---------------------------------------------------
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143193331387014ccd1040c814dee8b2164bb4f064cff000#0

import re

# re模块
#
# 有了准备知识，我们就可以在Python中使用正则表达式了。Python提供re模块，包含所有正则表达式的功能。由于Python的字符串本身也用\转义，所以要特别注意：
#
# s = 'ABC\\-001' # Python的字符串
# # 对应的正则表达式字符串变成：
# # 'ABC\-001'
#
# 因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题了：
#
# s = r'ABC\-001' # Python的字符串
# # 对应的正则表达式字符串不变：
# # 'ABC\-001'

regex_a_3num = r'^a\d{3}'
regex_a_allnum = r'^a\d.*'
regex_num = re.compile(regex_a_3num)
# regex_num = re.compile(regex_a_allnum)
print(regex_num.match("a7772"))
print(regex_num.match("a733"))
print(regex_num.match("a7772asdf"))

if regex_num.match("a234234"):
    print("匹配成功.")
else:
    print("匹配失败.")

# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。
# <_sre.SRE_Match object; span=(0, 5), match='a7772'>
# <_sre.SRE_Match object; span=(0, 4), match='a733'>
# <_sre.SRE_Match object; span=(0, 9), match='a7772asdf'>


# 切分字符串
#
# 用正则表达式切分字符串比用固定的字符更灵活，请看正常的切分代码：


test1 = "a b c   d"
test2 = "a b c d"
testd1 = "a,b ;,c,,d"
testd2 = "a,b,c  ,d"
print("普通分割:", test1.split(" "))
print("普通分割:", test2.split(" "))
print("普通分割逗号:", testd1.split(","))
print("普通分割逗号:", testd2.split(","))
regex_space = re.compile(r'\s+')
regex_space_d = re.compile(r'\s,+')
print("正则分割:", regex_space.split(test1))
print("正则分割:", regex_space.split(test2))
print("正则逗号分割:", regex_space_d.split(testd1))
print("正则逗号分割:", regex_space_d.split(testd2))

test_html="<j1 class=adfa>asdf</h1>"

# 非打印字符
#
# 非打印字符也可以是正则表达式的组成部分。下表列出了表示非打印字符的转义序列：
# 字符 	描述
# \cx 	匹配由x指明的控制字符。例如， \cM 匹配一个 Control-M 或回车符。x 的值必须为 A-Z 或 a-z 之一。否则，将 c 视为一个原义的 'c' 字符。
# \f 	匹配一个换页符。等价于 \x0c 和 \cL。
# \n 	匹配一个换行符。等价于 \x0a 和 \cJ。
# \r 	匹配一个回车符。等价于 \x0d 和 \cM。
# \s 	匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。注意 Unicode 正则表达式会匹配全角空格符。
# \S 	匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
# \t 	匹配一个制表符。等价于 \x09 和 \cI。
# \v 	匹配一个垂直制表符。等价于 \x0b 和 \cK。
# 特殊字符
#
# 所谓特殊字符，就是一些有特殊含义的字符，如上面说的 runoo*b 中的 *，简单的说就是表示任何字符串的意思。如果要查找字符串中的 * 符号，则需要对 * 进行转义，即在其前加一个 \: runo\*ob 匹配 runo*ob。
#
# 许多元字符要求在试图匹配它们时特别对待。若要匹配这些特殊字符，必须首先使字符"转义"，即，将反斜杠字符\ 放在它们前面。下表列出了正则表达式中的特殊字符：
# 特别字符 	描述
# $ 	匹配输入字符串的结尾位置。如果设置了 RegExp 对象的 Multiline 属性，则 $ 也匹配 '\n' 或 '\r'。要匹配 $ 字符本身，请使用 \$。
# ( ) 	标记一个子表达式的开始和结束位置。子表达式可以获取供以后使用。要匹配这些字符，请使用 \( 和 \)。
# * 	匹配前面的子表达式零次或多次。要匹配 * 字符，请使用 \*。
# + 	匹配前面的子表达式一次或多次。要匹配 + 字符，请使用 \+。
# . 	匹配除换行符 \n 之外的任何单字符。要匹配 . ，请使用 \. 。
# [ 	标记一个中括号表达式的开始。要匹配 [，请使用 \[。
# ? 	匹配前面的子表达式零次或一次，或指明一个非贪婪限定符。要匹配 ? 字符，请使用 \?。
# \ 	将下一个字符标记为或特殊字符、或原义字符、或向后引用、或八进制转义符。例如， 'n' 匹配字符 'n'。'\n' 匹配换行符。序列 '\\' 匹配 "\"，而 '\(' 则匹配 "("。
# ^ 	匹配输入字符串的开始位置，除非在方括号表达式中使用，此时它表示不接受该字符集合。要匹配 ^ 字符本身，请使用 \^。
# { 	标记限定符表达式的开始。要匹配 {，请使用 \{。
# | 	指明两项之间的一个选择。要匹配 |，请使用 \|。
#
# 圆括号()是组，主要应用在限制多选结构的范围/分组/捕获文本/环视/特殊模式处理
# 示例：
# 1、(abc|bcd|cde)，表示这一段是abc、bcd、cde三者之一均可，顺序也必须一致
# 2、(abc)?，表示这一组要么一起出现，要么不出现，出现则按此组内的顺序出现
# 3、(?:abc)表示找到这样abc这样一组，但不记录，不保存到$变量中，否则可以通过$x取第几个括号所匹配到的项，比如：(aaa)(bbb)(ccc)(?:ddd)(eee)，可以用$1获取(aaa)匹配到的内容，而$3则获取到了(ccc)匹配到的内容，而$4则获取的是由(eee)匹配到的内容，因为前一对括号没有保存变量
# 4、a(?=bbb) 顺序环视 表示a后面必须紧跟3个连续的b
# 5、(?i:xxxx) 不区分大小写 (?s:.*) 跨行匹配.可以匹配回车符
#
# 方括号是单个匹配，字符集/排除字符集/命名字符集
# 示例：
# 1、[0-3]，表示找到这一个位置上的字符只能是0到3这四个数字，与(abc|bcd|cde)的作用比较类似，但圆括号可以匹配多个连续的字符，而一对方括号只能匹配单个字符
# 2、[^0-3]，表示找到这一个位置上的字符只能是除了0到3之外的所有字符
# 3、[:digit:] 0-9 [:alnum:] A-Za-z0-9

text_point_1 = "a,b c,, ,;,d;e;f;;g  gg"
text_point_2 = 'a,b;; c ,,, d'
# 分隔符以','或'空格'或';'号分割字符串
regex_split = r'[\s+\,\;]'
regex_comp_split_sdf = re.compile(r'[\s\,\;]+')
regex_comp_split_sdf2 = re.compile(r'(\s+|\,+|\;+)')
print("1:", regex_comp_split_sdf.split(text_point_1))
print("2:", re.split(regex_split, text_point_1))
print("3:", re.split(regex_comp_split_sdf, text_point_1))
print("4:", re.split(regex_comp_split_sdf2, text_point_1))

# group,提取分组.
# 分组
#
# 除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）。比如：
#
# ^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码

regex_comp_group_tel = re.compile(r'^(\d{3})-(\d{3,8})$')
testlist = ['010123123', '123-123123']
for item in testlist:
    matchResult = regex_comp_group_tel.match(item)
    if matchResult:
        group_1 = matchResult.groups()
        group_2 = matchResult.groups("1")
        print("item->(%s),group1:[%s],group2:[%s]", matchResult, )
