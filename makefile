JC = javac
LR = cmps142_hw4/LogisticRegression.java
LRB = cmps142_hw4/LogisticRegression_withBias.java
LRR = cmps142_hw4/LogisticRegression_withRegularization.java
CLASSES = cmps142_hw4/*.class

.SUFFIXES: .java .class

all:
	javac $(LR)
	javac $(LRB)
	javac $(LRR)


p1:
	javac $(LR)
	java $(CLASSES)
p2: 
	javac $(LRB)
	java $(CLASSES)
p3: 
	javac $(LRR)
	java$(CLASSES)

default: .java.class

clean:
	$(RM) *.class