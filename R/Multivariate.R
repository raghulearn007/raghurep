############################# Multivariate Stats #######################
install.packages("devtools")
library(devtools)
install_github("statcourses/essexBigdata")
data("measure")

install.packages("drat")
drat::addRepo("statcourses")
install.packages("essexBigdata")
vignette("practical1", package = "essexBigdata")

install.packages("archdata") #Pottery Data is here;
library(archdata)
data("RBPottery")


cov(iris[,c("Sepal.Length","Sepal.Width","Petal.Length","Petal.Width")]) 

cor(iris[,c("Sepal.Length","Sepal.Width","Petal.Length","Petal.Width")]) 
xx<-dist(scale(iris[1:10,c("Sepal.Length","Sepal.Width","Petal.Length","Petal.Width")],center=FALSE))
ggplot(data=iris,aes(x="Sepal.Length"))+geom_density()
pairs(iris)

xx

scale(iris[1:10,c("Sepal.Length","Sepal.Width","Petal.Length","Petal.Width")],center=FALSE)

xx
dim(iris)
