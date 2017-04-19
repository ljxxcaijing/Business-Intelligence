#读取数据集
#data = read.delim("~data.txt", header=FALSE)
k = 4 #聚类个数
rows = nrow(data)#得到数据集的行数
cols = ncol(data)#得到数据集的列数
indexMatrix <- matrix(0,rows,2)#索引矩阵
randSeveralFloat = runif(k,min = 0.3,max = 1)#产生随机数
randSeveralInteger = as.integer(rows * randSeveralFloat)
centers = matrix(0,nrow=k,cols)  
for(i in 1:k){#得到初始聚类中心
  indexMatrix[randSeveralInteger[i],1] = i
  centers[i,]= data[randSeveralInteger[i],]
  centers = matrix(centers,k,cols)
}
plot(data)
points(centers,pch=8,cex=2)

#迭代计算
for(i in 1:rows){#对每一个样本，开始划分所在的类别
  initialDis = 1000
  previousCluster = indexMatrix[i,1]#该样本当前所在的类别
  for(j in 1:k){  			
    currentDistance = (sum((data[i,] - centers[j,])^2)) ^ 0.5
    if(currentDistance < initialDis){				
      initialDis = currentDistance
      indexMatrix[i,1] = j#该样本属于第j个类
      indexMatrix[i,2] = currentDistance#样本与该类的簇中心的距离
    }
  }		
}
a = cbind(indexMatrix,data)#构造画图用矩阵
b = 2+ncol(data)#列的数量
idx = as.integer(a[[1]])#以类作为index
plot(a[,3:b], pch = c(24, 21, 22,25)[idx], col = c("black", "red", "blue","green")[idx], panel.first = grid())
points(centers,pch=8,cex=2)

#计算中心
for(m in 1:k){
  clusterMatrix <- data[indexMatrix[,1]==m,]#得到属于第m个类的所有样本
  if(nrow(clusterMatrix) > 0){#如果属于m类的样本数大于0
    centers[m,] = colMeans(clusterMatrix)#计算样本的均值，作为新的聚类中心
  }
  else{
    centers[m,] <- centers[m,]#第m类的聚类中心未发生变化	
  }
}
a = cbind(indexMatrix,data)#构造画图用矩阵
b = 2+ncol(data)#列的数量
idx = as.integer(a[[1]])#以类作为index
plot(a[,3:b], pch = c(24, 21, 22,25)[idx], col = c("black", "red", "blue","green")[idx], panel.first = grid())
points(centers,pch=8,cex=2)

for(i in 1:k){
  clusterMatrix = data[indexMatrix[,1]==m.]
  if(nrow(clusterMatrix) > 0){
    centers[m,] = colMeans(clusterMatrix)
  }
}