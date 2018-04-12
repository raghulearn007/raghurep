 n = 25
 theta = seq(0, 2*pi, length=n+1)[1:n]
 x = sin(theta)
 y = cos(theta)
 plot.new()
 plot.window(xlim = c(-1,1),
              ylim = c(-1,1),
              asp = 1)
 for(i in 2:n)
  for(j in 1:(i-1))
    segments(x[i], y[i], x[j], y[j])
 title(main="A 17 Rosette")
 
 plot.new()
 plot.window(xlim=c(0, 100), ylim = c(-10, 1000))
 x<-seq(1,10,0.00001)
 y=exp(sqrt(x))
 z=exp(x)
 plot(x,y,type="l")
 lines(x,z,type="l")
 
 ################ Data.Table Exercise ##################
 dim(iris)
 install.packages("data.table")
 library(data.table)
 ir<- as.data.table(iris)
 class(ir)
 
 ir1<- ir[Sepal.Length>=5,c("Species","Sepal.Length"),Species,with=FALSE]
 
 ir1<- ir[Sepal.Length>=5,.(Species ,Sepal.Length),Species,]
 
 ir1<- ir[Sepal.Length>=5,.(.N,mean(Sepal.Length)) ,Species,]
 ir1[setorder(Species)]
 
 ir[,.(.N),Species]
 break1<-c(-2,5,7,Inf)
 ir$sep_break=cut(ir$Sepal.Length,break1)
 ir[]
 ir[,.(.N),sep_break]
 
 seto
 View(ir)
 
 
 ##Orderring;
 
 ir2<- ir1[order(Species)]
 
 
 
"Length" %in% colnames(iris)