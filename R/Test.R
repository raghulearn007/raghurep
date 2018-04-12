library(knitr)
print("Hello World")
render_markdown()
knit("Test.r")

x<- "  abcde"

x1<- substr(trim(x),5,5)
x1

s1="James"
s2="Bond"

s=paste(s1,s2)

paste0(s1,s2)

sub("Bond","Rhodes",s)

my_list=c("a1","b1","c1")
class(my_list)

my_list[4]=+"h1"

#Generate Random normal data;

test=rnorm(2000000)
my_ds=as.data.frame(test)
library(ggplot2)
ggplot(my_ds,aes(x=test))+geom_histogram(bins=1000)

ggplot(my_ds, aes(x=test) )+stat_qq()
qqline(x=test)

p <- 0.2
log(p/(1-p))

log(1)



