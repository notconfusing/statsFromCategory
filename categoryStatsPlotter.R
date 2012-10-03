#plottin output from Category stats py script
library("reshape")
library("ggplot2")
setwd("~/workspace/oahack/categoryStats")

edits <- read.table('forR.txt', header = T)
#use this to get sum aggregrates by month
#edits$AllBooks <- rowSums(edits[,2:ncol(edits)])

edits.melt <- melt(edits, id = 'MonthsSinceJan2001')

tail(edits.melt)


allarticles <- ggplot(edits.melt, aes(x = MonthsSinceJan2001, y = value, colour = variable)) +
geom_line() +
ylab("Edits") + xlab("Year") +
scale_colour_discrete(name="Candidate") +
opts(legend.key.size = unit(1, "cm")) +
#facet_wrap(~ colour, ncol=4) + #comment out if you want on signle graph
#opts(legend.position = "none") +
scale_x_continuous(breaks=c(0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144),
                   labels=c("Jan 01","Jan 02","Jan 03","Jan 04","Jan 05","Jan 06","Jan 07",
                            "Jan 08","Jan 09","Jan 10","Jan 11","Jan 12","Jan 13"))

print(allarticles)




