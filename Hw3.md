
<p align="center"><font size="8">2017BIHomework2</font></p>
<p align="center"><font size="4">Cai Jing</font></p>

### 1. Line chart
```{r}
data(USPersonalExpenditure) # 导入数据
data = USPersonalExpenditure
View(data)
plot(data[1,],ylim=c(0,100), xaxt="n",
     type="o",lwd=2,col="red",pch=24,cex=1.5,
     xlab="1940~1960",ylab="Food and Tobacco & Household Operation",
     main="‘Food and Tobacco’ and ‘House- hold Opertion’ 
     from 1940 to 1960")
# 画图取“Food”的数据，画出“Food”随年份变化的红色三角(pch=24)曲线，并将x轴置空
axis(side=1,at=1:5,tck=-0.05,
	 labels=c("1940","1945","1950","1955","1960"))
# 自定义x轴，1940～1960年
lines(data[2,],col = "blue",type = "o",lwd = 2,pch=5)
# 画“Household”的蓝色方形(pch=5)曲线
legend("bottomright",legend=c("Food and Tobacco","Household
Operation"),col=c("blue","red"),pch=c(5,24),lty=1) # 在右下角做注释
``` 
<center>
<img src="screenshoot/Hw3/1.png" width="60%"/>

Figure 1. ‘Food and Tobacco’ and ‘House- hold Opertion’ 
     from 1940 to 1960"
</center>



### 2. Pie chart
```{r}
par(mfrow = c(2,2)) # 把plot区域划分成2*2的四部分便于比较
#画1945年的饼图
lbls <- c("Food and Tobacco", "Household Operation", 
		"Medical and Health","Personal Care", "Private Education")
pct <- round(data[,2]/sum(data[,2])*100) # 计算每一部分占总数的百分比
lbls <- paste(lbls, pct) # 加上每一部分所占的百分比 
lbls <- paste(lbls,"%",sep="") # 算出的百分比加上“％”
pie(data[,2],labels = lbls, 
    main="Pie Chart of 1945") #画1945年饼图

#画1950年的饼图
lbls <- c("Food and Tobacco", "Household Operation", 
		"Medical and Health","Personal Care", "Private Education")
pct <- round(data[,3]/sum(data[,3])*100) # 计算每一部分占总数的百分比
lbls <- paste(lbls, pct) # 加上每一部分所占的百分比 
lbls <- paste(lbls,"%",sep="") # 算出的百分比加上“％”
pie(data[,3],labels = lbls, 
    main="Pie Chart of 1950") #画1950年饼图

#画1955年的饼图
lbls <- c("Food and Tobacco", "Household Operation", 
		"Medical and Health","Personal Care", "Private Education")
pct <- round(data[,4]/sum(data[,4])*100) # 计算每一部分占总数的百分比
lbls <- paste(lbls, pct) # 加上每一部分所占的百分比 
lbls <- paste(lbls,"%",sep="") # 算出的百分比加上“％”
pie(data[,4],labels = lbls, 
    main="Pie Chart of 1955") #画1955年饼图

#画1960年的饼图
lbls <- c("Food and Tobacco", "Household Operation", 
		"Medical and Health","Personal Care", "Private Education")
pct <- round(data[,5]/sum(data[,5])*100) # 计算每一部分占总数的百分比
lbls <- paste(lbls, pct) # 加上每一部分所占的百分比 
lbls <- paste(lbls,"%",sep="") # 算出的百分比加上“％”
pie(data[,5],labels = lbls, 
    main="Pie Chart of 1960") #画饼图
```
<center>
<img src="screenshoot/Hw3/2.png" width = "90%" />

Figure 2. Pie plot from 1940 to 1960
</center>


### 3. Bar chart
```{r}
barplot(data,col=rainbow(5),
        main="Bar plot from 1940 to 1960") #用rainbow上色，beside＝T表示竖着构图
legend("topleft", legend=rownames(data), pch=15, col=rainbow(5)) #在左上角注释
```
<center>
<img src="screenshoot/Hw3/3.png" width = "60%" />

Figure 3. Bar plot from 1940 to 1960
</center>


### 4. Boxplot chart
```{r}
data(ChickWeight)# 导入数据
data = ChickWeight
View(data)

install.packages("ggplot2")# 安装ggplot包
library(ggplot2)
ggplot(data,aes(x=factor(data$Time),y=data$weight)) + geom_boxplot()
#  
# 横坐标时Time指标
```
<center>
<img src="screenshoot/Hw3/4.1.png" width = "80%" />

Figure 4. Weight under different ‘Time’
</center>


```{r}
ggplot(data,aes(x=interaction(data$Time, data$Diet),
y=data$weight))+geom_boxplot() 
# weight under different ‘Time’ and ‘Diet’
# 横坐标时Time和Diet的笛卡尔积的组合
```
<center>
<img src="screenshoot/Hw3/4.2.png" width = "80%" />

Figure 5. Weight under different ‘Time’ and ‘Diet’
</center>
