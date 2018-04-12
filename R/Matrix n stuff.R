inp <- read.table("c:\\infoviz\\ehpostcode.csv",header=F, sep=",")
inp <- subset(inp,inp$V10 != "")
library(ggplot2)
m <- qplot(xlab="Longitude",ylab="Latitude",main="EH Postcode heatmap",geom="blank",x=inp$V3,y=inp$V4,data=inp)  + stat_bin2d(bins =200,aes(fill = log1p(..count..))) 
m 

head(iris)
dim(iris)
ggplot(iris,aes(x=Sepal.Length))+geom_bar()
ggplot(iris,aes(x=Petal.Length))+geom_bar()

pairs(iris
      
      ,upper.panel=panel.cor
      )

colnames(iris,)

x<- seq(1:10)
x

for(i in x)
{
   if (x[i] %% 2 == 0)   { 
                                print(x[i]*x[i])
                        }
   else {
                print("FAIL")
     }
}



##  Define a matrix;
require(MASS)
mymat=matrix(c(1:8,6), ncol=3)
class(mymat)
inv(mymat)
inv0 <- ginv(mymat)

matmult=mymat %*%  inv0

# Find Eigen value anf ERigen vector
myls<- eigen(mymat)



