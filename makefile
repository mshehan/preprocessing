JC = javac
JFLAGS = -g
ALL = cmps142_hw4/*.java
LR = cmps142_hw4/LogisticRegression.java
LR_JAVA = cmps_hw4/LogisticRegression

LRB = cmps142_hw4/LogisticRegression_withBias.java
LRB_JAVA = cmps142_hw4/LogisticRegression_withBias

LRR = cmps142_hw4/LogisticRegression_withRegularization.java
LRR_JAVA = cmps142_hw4/LogisticRegression_withRegularization

CLASSES = cmps142_hw4/*.class

.SUFFIXES: .java .class

all:
	javac $(ALL) $(JFLAGS)

p1:
	javac $(LR) $(JFLAGS)
	java $(LR_JAVA)
	
p2: 
	javac $(LRB) $(JFLAGS)
	java $(LRB_JAVA)
p3: 
	javac $(LRR) $(JFLAGS)
	java $(LRR_JAVA)

default: .java.class

clean:
	$(RM) cmps142_hw4/*.class