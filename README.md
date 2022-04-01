# UI_Auto_Test_Selenium

<i>本项目参考的对象为搜狗微信文章：https://weixin.sogou.com/  ---代码仅供参考、讨论、学习，如有侵权，联系删除</i>

<p>涉及技术：</p>
<li>Python3</li>
<li>Selenium</li>
<li>BeautifulSoap</li>
<li>BeautifulReport</li>
<li>Unittest</li>

## 项目结构
<li>config：统一配置相关</li>
&nbsp;&nbsp;&nbsp;&nbsp;|</br>
&nbsp;&nbsp;&nbsp;&nbsp;---browser.yml：基础信息存储，主要是存储一些url、账号密码等信息；
<li>Test_Case：测试用例相关</li>
<li>drivers：驱动相关，存放一些浏览器驱动文件</li>
<li>img：图片相关，主要是存在测试过程中的截图</li>
<li>data：主要是存放外部数据，比如csv、Excel、txt等</li>
<li>logs：操作日志相关</li>
<li>utils：基础操作相关</li>
&nbsp;&nbsp;&nbsp;&nbsp;|</br>
&nbsp;&nbsp;&nbsp;&nbsp;---browser_driver.py：处理浏览器的启动/关闭、最大化、GUI/NO GUI等；</br>
&nbsp;&nbsp;&nbsp;&nbsp;|</br>
&nbsp;&nbsp;&nbsp;&nbsp;---config.py：设置路径、读取yaml/Excel等文件；</br>
&nbsp;&nbsp;&nbsp;&nbsp;|</br>
&nbsp;&nbsp;&nbsp;&nbsp;---file_read.py：操作文件；
<li>Test_Result：测试报告相关</li>
<li>Run_Test.py：用例执行脚本</li>
<li>common：公共方法相关：页面滚动、鼠标点击、保存截图等公共方法</li>

## 项目描述
<p>主要是模拟用户在页面操作的一些行为：</p>
<li>文本关键词搜索；</li>
<li>二次筛选(筛选项、时间选择、时间输入等)；</li>
<li>页面切换(句柄)、详情查看；</li>
<li>页面滚动；</li>
<li>鼠标点击、悬停；</li>
