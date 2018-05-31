JC = javac
JFLAGS = -g
ALL = cmps142_hw4/*.java
LR = cmps142_hw4/LogisticRegression.java
LR_JAVA = cmps142_hw4/LogisticRegression

LRB = cmps142_hw4/LogisticRegression_withBias.java
LRB_JAVA = cmps142_hw4/LogisticRegression_withBias

LRR = cmps142_hw4/LogisticRegression_withRegularization.java
LRR_JAVA = cmps142_hw4/LogisticRegression_withRegularization

CLASSES = cmps142_hw4/*.class

.SUFFIXES: .java .class

all:
	javac $(ALL) $(JFLAGS)

.java.class:
	$(JC) $(JFLAGS) $*.java

p1: $(LR_JAVA).class
	java $(LR_JAVA)

$(LR_JAVA).class: $(LR)
	javac $(LR) $(JFLAGS)

p2: $(LRB_JAVA).class
	java $(LRB_JAVA)
$(LRB_JAVA):
	javac $(LRB) $(JFLAGS)

p3: $(LRR_JAVA).class
	java $(LRR_JAVA)
$(LRR_JAVA).class: 
	javac $(LRR) $(JFLAGS)

default: .java.class

clean:
	$(RM) cmps142_hw4/*.class