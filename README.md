### 小六壬 起卦程序

首先运行 安装模块
```
pip3 install -r requirements.txt
```
运行程序 
```
python3 main.py 
```
 
运行成功会出现 阳历时间 阴历时间，并且会让你填写月 日 时辰 数字
如果你是报数起卦月日输入处可以直接使用随机数字即可
```qigua
现在阳历时间为：2021-09-20  12:39

辛丑年丁酉月辛未日
农历时间: 8 月 14 日 

以下是时辰对应的数字：
子时 23:00-01:00：1 
丑时 01:00-03:00：2 
寅时 03:00-05:00：3 
卯时 05:00-07:00：4 
辰时 07:00-09:00：5 
巳时 09:00-11:00：6 
午时 11:00-13:00：7 
未时 13:00-15:00：8 
申时 15:00-17:00：9 
酉时 17:00-19:00：10
戌时 19:00-21:00：11
亥时 21:00-23:00：12 

请输入月/随机数：2
请输入日/随机数：3
请输入时辰：5
+------------------------------------------------------+
|                     ☯三宫☯☯所属☯                     
+-------------+-------------+-------------+------------+
|   ☯天  时☯  |   ☯地  利☯  |   ☯人  和☯  |  ☯用  神☯ 
+-------------+-------------+-------------+------------+
| ☯留连☯(土)☯ | ☯赤口☯(金)☯ | ☯留连☯(土)☯ | ☯巳时(火)☯ 
|   ☯起 因☯   |   ☯经 过☯   |   ☯现 在☯   |  ☯未 来☯ 
+-------------+-------------+-------------+------------+

```
第1版本，只是安排了合宫取象释意 后期会根据六神的意思进行完整解释输出。

第2版已经输出，增加卦辞解释取象。

第2.1版本增加五行生克输出和时辰用神输出，并且格式化了输出文本

感谢 天衍阁·潇六 提供的天衍阁小六壬取象书籍和B站妙易居士老师的教学视频。
